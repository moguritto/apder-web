# -*- coding: utf-8 -*-
"""Convierte el wikitexto traducido de PsychonautWiki en HTML para Psiconáutica.

A diferencia del conversor provisional, no tira las piezas de la wiki ({{...}}): las convierte.
- Listas de efectos ({{effects/physical|…}} y demás), avisos, listas de interacciones peligrosas
  (las compartidas vienen de plantillas_es.py), «Artículo principal», «Véase también», citas.
- Páginas incrustadas ({{:Título}}): se insertan desde su propia traducción.
- Tablas ({| … |}), referencias numeradas (<ref>, {{cite …}}, {{sfn}}) y notas ({{efn}}).
- Las fichas con dosis (SubstanceBox) y lo que no aporta en la web (galerías, vídeos, esbozos) se quitan.

Uso: Conversor(paginas, nombres).html(titulo_original, wikitexto) -> (html, datos)
  paginas: {título original: wikitexto traducido}, para las páginas incrustadas
  nombres: {título original: título en español}, para los textos de los enlaces «Artículo principal»
Solo biblioteca estándar."""
import html
import re
from urllib.parse import quote

try:
    from . import plantillas_es as P
except ImportError:          # ejecutado como script desde la carpeta
    import plantillas_es as P

PW = "https://psychonautwiki.org/wiki/"
WP = "https://en.wikipedia.org/wiki/"
NUL = "\x00"

EFECTOS = {
    "physical": "Efectos físicos", "visual": "Efectos visuales", "cognitive": "Efectos cognitivos",
    "auditory": "Efectos auditivos", "multisensory": "Efectos multisensoriales", "transpersonal": "Efectos transpersonales",
    "disconnective": "Efectos de desconexión", "aftereffects": "Efectos posteriores", "paradoxical": "Efectos paradójicos",
    "tactile": "Efectos táctiles", "olfactory": "Efectos olfativos", "gustatory": "Efectos gustativos",
    "spiritual": "Efectos espirituales", "emotional": "Efectos emocionales", "uncomfortable": "Efectos incómodos",
    "physical/uncomfortable": "Efectos físicos incómodos",
}
# Plantillas que no se muestran en la web (fichas con dosis, avisos de esbozo, navegación, multimedia, metadatos).
FUERA = re.compile(
    r"^(substancebox|botanybox|mycologybox|summarysheet|stub|\w*stub|approval|decree|disclaimer|for|gallery|"
    r"#set|#widget|#ev|#if|#switch|experience reports|responsible use2|template:responsible use2|clarify|dead link|"
    r"submissionpanel|headerpanel/?.*?/end|navbox|reflist-talk|pp-.*|tocright|toc|notoc|clear|anchor|"
    r"effects/seealso|effects/content|list/effects|-|bots|wip|update|cleanup|merge.*|copyedit|translation|legend|empty|bookbox|list|opinion|verify source)$", re.I)
CITA = re.compile(r"^(cite[ _]\w+|citation)$", re.I)
SIN_ENLACE = re.compile(r"^(file|image|archivo|imagen|category|categoría|media|special|user|user talk|talk|template|help):", re.I)
CLASE = re.compile(r"\[\[\s*(psychoactive|chemical) class::([^\]|]+)(?:\|([^\]]*))?\]\]", re.I)
DESTINO_CLASE = {   # destino de los enlaces de clase escritos en español por el traductor
    "estimulante": "Stimulants", "estimulantes": "Stimulants", "depresora": "Depressant", "depresor": "Depressant",
    "depresoras": "Depressant", "psicodélica": "Psychedelics", "psicodélico": "Psychedelics", "entactógena": "Entactogens",
    "entactógeno": "Entactogens", "opioide": "Opioids", "cannabinoide": "Cannabinoid", "disociativa": "Dissociatives",
    "disociativo": "Dissociatives", "delirante": "Deliriant", "nootrópica": "Nootropic", "nootrópico": "Nootropic",
    "catinonas": "Substituted cathinones", "fenetilaminas": "Substituted phenethylamines", "anfetaminas": "Substituted amphetamines",
    "triptaminas": "Substituted tryptamines", "lisergamidas": "Lysergamides", "benzodiazepinas": "Benzodiazepines",
    "benzodiacepinas": "Benzodiazepines", "tienodiazepinas": "Thienodiazepines", "gabapentinoides": "Gabapentinoids",
    "fenidatos": "Phenidates", "benzofuranos": "Benzofurans", "morfinanos": "Morphinans", "alcohol": "Alcohol",
    "alcoholes": "Alcohol", "pirrolidinofenonas": "Pyrrolidinophenones", "fenilpropilaminas": "Phenylpropylamines",
}
ESTILO_OK = re.compile(r"^\s*(background(?:-color)?|color|text-align)\s*:\s*[#a-z0-9 ,.%()-]+$", re.I)
WP_RUTA = re.compile(r"wp-(content|includes)", re.I)
TAGS_OK = ("b", "i", "u", "s", "sub", "sup", "small", "code", "em", "strong", "br")


def esc(s):
    return html.escape(s, quote=True)


def bloques_plantilla(t, i):
    """Devuelve el final (exclusivo) del bloque {{ … }} que empieza en i, respetando anidamiento."""
    n, j = 0, i
    while j < len(t):
        if t.startswith("{{", j):
            n += 1
            j += 2
        elif t.startswith("}}", j):
            n -= 1
            j += 2
            if n == 0:
                return j
        else:
            j += 1
    return len(t)


def partir(cuerpo):
    """Parte «nombre|a|b=c» por las barras de primer nivel (no dentro de {{}} ni de [[]])."""
    partes, nivel_l, nivel_t, actual, i = [], 0, 0, [], 0
    while i < len(cuerpo):
        if cuerpo.startswith("{{", i):
            nivel_t += 1; actual.append("{{"); i += 2; continue
        if cuerpo.startswith("}}", i) and nivel_t:
            nivel_t -= 1; actual.append("}}"); i += 2; continue
        if cuerpo.startswith("[[", i):
            nivel_l += 1; actual.append("[["); i += 2; continue
        if cuerpo.startswith("]]", i) and nivel_l:
            nivel_l -= 1; actual.append("]]"); i += 2; continue
        c = cuerpo[i]
        if c == "|" and not nivel_l and not nivel_t:
            partes.append("".join(actual)); actual = []
        else:
            actual.append(c)
        i += 1
    partes.append("".join(actual))
    nombre = partes[0].strip()
    pos, nom = [], {}
    for p in partes[1:]:
        m = re.match(r"^\s*([\w\- ]+?)\s*=(.*)$", p, re.S)
        if m and "[[" not in m.group(1) and "{{" not in m.group(1):
            nom[m.group(1).strip().lower()] = m.group(2).strip()
        else:
            pos.append(p)
    return nombre, pos, nom


def incluir(t, incrustada=False):
    """Aplica <noinclude>, <onlyinclude> e <includeonly> como MediaWiki."""
    if incrustada:
        if "<onlyinclude>" in t:
            t = "\n".join(re.findall(r"<onlyinclude>(.*?)</onlyinclude>", t, re.S))
        t = re.sub(r"<noinclude>.*?</noinclude>", "", t, flags=re.S)
        t = re.sub(r"</?includeonly>", "", t)
    else:
        t = re.sub(r"<includeonly>.*?</includeonly>", "", t, flags=re.S)
        t = re.sub(r"</?(noinclude|onlyinclude)>", "", t)
    return t


def quitar_ficheros(t):
    """Quita las imágenes [[File:…]] aunque su pie lleve enlaces dentro (las imágenes no se publican)."""
    salida, i = [], 0
    patron = re.compile(r"\[\[\s*:?(file|image|archivo|imagen|media)\s*:", re.I)
    while True:
        m = patron.search(t, i)
        if not m:
            salida.append(t[i:])
            return "".join(salida)
        salida.append(t[i:m.start()])
        n, j = 0, m.start()
        while j < len(t):
            if t.startswith("[[", j):
                n += 1; j += 2
            elif t.startswith("]]", j):
                n -= 1; j += 2
                if n == 0:
                    break
            else:
                j += 1
        i = j


def limpiar_fuente(t):
    t = quitar_ficheros(t)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"^''Traducción al español de la página .*$\n?", "", t, count=1, flags=re.M)
    t = re.sub(r"(?<![{\w])\w+=https?://[^\s}]*\}\}", "", t)          # restos de plantillas rotas en el propio original
    t = re.sub(r"^''La información de dosis no se traduce:.*?''\s*$", "", t, flags=re.M)
    t = re.sub(r"__[A-Z]+__", "", t)
    t = re.sub(r"<gallery.*?</gallery>", "", t, flags=re.S | re.I)
    t = t.replace("\r", "")
    return t


def comillas(s):
    """Negrita y cursiva de MediaWiki (''' y ''), con etiquetas bien anidadas aunque se crucen."""
    trozos = re.split(r"('{2,})", s)
    abiertas, out = [], []

    def alternar(tag):
        if tag in abiertas:
            dentro = abiertas[abiertas.index(tag) + 1:]
            for t in reversed(dentro):
                out.append("</%s>" % t)
            out.append("</%s>" % tag)
            abiertas.remove(tag)
            for t in dentro:
                out.append("<%s>" % t)
        else:
            out.append("<%s>" % tag)
            abiertas.append(tag)
    for i, tr in enumerate(trozos):
        if i % 2 == 0:
            out.append(tr)
            continue
        n = len(tr)
        if n == 4:
            out.append("'"); n = 3
        elif n > 5:
            out.append("'" * (n - 5)); n = 5
        if n == 2:
            alternar("em")
        elif n == 3:
            alternar("strong")
        else:
            if "em" in abiertas and "strong" in abiertas and abiertas.index("em") > abiertas.index("strong"):
                alternar("em"); alternar("strong")
            elif "em" in abiertas or "strong" in abiertas:
                alternar("strong"); alternar("em")
            else:
                alternar("strong"); alternar("em")
    for t in reversed(abiertas):
        out.append("</%s>" % t)
    return "".join(out)


class Conversor:
    def __init__(self, paginas, nombres):
        self.paginas = {k.lower(): v for k, v in paginas.items()}
        self.nombres = {k.lower(): v for k, v in nombres.items()}
        self.sin_plantilla = {}

    # ------------------------------------------------------------ entrada
    def html(self, titulo, texto, titulo_es=None):
        self.titulo, self.titulo_es = titulo, (titulo_es or titulo)
        self.refs, self.ref_nombre, self.notas, self.bloques = [], {}, [], []
        self.hay_lista_refs = False
        texto = limpiar_fuente(incluir(texto))
        clases = self.clases(texto)
        cuerpo = self.fragmento(texto, 0)
        cuerpo = self.poner_listas(cuerpo)
        return cuerpo, {"clases": clases}

    def clases(self, t):
        """Clase psicoactiva y química, tal como las marca la wiki ([[psychoactive class::…]])."""
        out = {}
        for m in CLASE.finditer(t[:4000]):
            tipo = "psicoactiva" if m.group(1).lower() == "psychoactive" else "quimica"
            txt = (m.group(3) or m.group(2)).strip()
            if re.fullmatch(r"[a-z \-]+", txt) and txt.lower() not in DESTINO_CLASE:   # destino en inglés sin texto
                continue
            out.setdefault(tipo, txt)
        return out

    # ------------------------------------------------------------ fragmento: plantillas, refs, tablas, bloques
    def fragmento(self, t, prof):
        t = self.sacar_refs(t)
        t = self.plantillas(t, prof)
        t = re.sub(r"<blockquote>(.*?)</blockquote>", lambda m: self.bloque('<blockquote>%s</blockquote>' % self.fragmento(m.group(1), prof + 1)), t, flags=re.S | re.I)
        t = self.tablas(t)
        return self.lineas(t)

    def bloque(self, h):
        self.bloques.append(h)
        return "\n%sB%d%s\n" % (NUL, len(self.bloques) - 1, NUL)

    # ------------------------------------------------------------ referencias
    def sacar_refs(self, t):
        def con(m):
            attrs, dentro = m.group(1) or "", m.group(2)
            return self.ref(attrs, dentro)

        def sola(m):
            return self.ref(m.group(1) or "", None)
        # primero las que se cierran solas (<ref name=x />): si no, se leerían como abiertas y se tragarían el texto hasta el siguiente </ref>.
        # El número se reserva en el orden en que aparecen, como en la wiki.
        t = re.sub(r"<ref(\s[^>]*?)?(?<!/)>(.*?)</ref>|<ref(\s[^>]*?)?/>",
                   lambda m: con(m) if m.group(2) is not None else self.ref(m.group(3) or "", None), t, flags=re.S | re.I)
        if re.search(r"<references\s*/?>|<references>", t, re.I):
            self.hay_lista_refs = True
        t = re.sub(r"<references\s*/?>(?:.*?</references>)?", "\n%sREFS%s\n" % (NUL, NUL), t, flags=re.S | re.I)
        return t

    def ref(self, attrs, dentro):
        nombre = re.search(r'name\s*=\s*"?([^"/>]+?)"?\s*(?:$|group|/)', attrs.strip() + " ")
        nombre = nombre.group(1).strip() if nombre else None
        grupo = re.search(r'group\s*=\s*"?([^"/>\s]+)', attrs)
        if grupo:                                  # notas con grupo: van a «Notas»
            if dentro is None:
                return ""
            return self.nota(dentro)
        if nombre and nombre in self.ref_nombre:
            n = self.ref_nombre[nombre]
            if dentro and not self.refs[n - 1]:
                self.refs[n - 1] = self.cita_html(dentro)
            return "%sR%d%s" % (NUL, n, NUL)
        if dentro is None and not nombre:
            return ""
        self.refs.append(self.cita_html(dentro) if dentro else "")
        n = len(self.refs)
        if nombre:
            self.ref_nombre[nombre] = n
        return "%sR%d%s" % (NUL, n, NUL)

    def nota(self, dentro):
        self.notas.append(self.en_linea(self.plantillas(dentro, 3)))
        return "%sN%d%s" % (NUL, len(self.notas), NUL)

    def cita_html(self, dentro):
        """Una referencia: las plantillas {{cite …}} se escriben como cita; el resto, como texto."""
        def cita(m):
            nombre, pos, nom = partir(m.group(0)[2:-2])
            if not CITA.match(nombre):
                return ""
            return self.formatear_cita(nom)
        partes, i, salida = dentro, 0, []
        while True:
            j = partes.find("{{", i)
            if j < 0:
                salida.append(partes[i:]); break
            salida.append(partes[i:j])
            k = bloques_plantilla(partes, j)
            bloque = partes[j:k]
            nombre = partir(bloque[2:-2])[0]
            if CITA.match(nombre):
                salida.append(self.formatear_cita(partir(bloque[2:-2])[2]))
            elif nombre.lower() == "!":
                salida.append("|")
            i = k
        return self.en_linea("".join(salida).strip())

    def formatear_cita(self, nom):
        g = lambda *ks: next((nom[k] for k in ks if nom.get(k)), "")
        autores = g("vauthors", "authors", "author")
        if autores:
            autores = ", ".join(re.findall(r"\(\(([^)]*)\)\)", autores)) or autores
        else:
            nombres = []
            for i in range(1, 9):
                ap = nom.get("last%d" % i) or (nom.get("last") if i == 1 else "")
                no = nom.get("first%d" % i) or (nom.get("first") if i == 1 else "")
                if ap:
                    nombres.append("%s, %s" % (ap, no) if no else ap)
            autores = "; ".join(nombres)
        anio = g("year")
        if not anio:
            m = re.search(r"(1[89]\d\d|20\d\d)", g("date"))
            anio = m.group(1) if m else ""
        titulo = g("title", "chapter")
        fuente = g("journal", "work", "website", "publisher", "newspaper", "magazine", "periodical")
        vol, num, pags = g("volume"), g("issue"), g("pages", "page")
        url, doi, pmid = g("url"), g("doi"), g("pmid")
        if WP_RUTA.search(url):
            url = ""
        out = []
        if autores:
            out.append(autores.strip().rstrip(".") + ".")
        if anio:
            out.append("(%s)." % anio)
        if titulo:
            titulo = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", titulo)
            out.append(("[%s %s]." % (url, titulo.replace("]", ")"))) if url and not doi else titulo.rstrip(".") + ".")
        if fuente:
            f = "''%s''" % fuente
            if vol:
                f += ", %s" % vol + ("(%s)" % num if num else "")
            if pags:
                f += ", %s" % pags
            out.append(f + ".")
        if doi:
            out.append("[https://doi.org/%s doi:%s]" % (doi.strip(), doi.strip()))
        elif pmid:
            out.append("[https://pubmed.ncbi.nlm.nih.gov/%s/ PMID %s]" % (pmid.strip(), pmid.strip()))
        elif url and not titulo:
            out.append("[%s %s]" % (url, url))
        return " ".join(out)

    # ------------------------------------------------------------ plantillas
    def plantillas(self, t, prof):
        salida, i = [], 0
        while True:
            j = t.find("{{", i)
            if j < 0:
                salida.append(t[i:]); break
            if t.startswith("{{{", j):        # parámetro sin rellenar
                k = t.find("}}}", j)
                salida.append(t[i:j]); i = len(t) if k < 0 else k + 3; continue
            salida.append(t[i:j])
            k = bloques_plantilla(t, j)
            salida.append(self.plantilla(t[j + 2:k - 2], prof))
            i = k
        return "".join(salida)

    def plantilla(self, cuerpo, prof):
        nombre, pos, nom = partir(cuerpo)
        n = re.sub(r"\s+", " ", nombre.replace("_", " ")).strip()
        n = re.sub(r"^template:", "", n, flags=re.I)
        nl = n.lower()
        clave = nl + ("|" + "|".join("%s=%s" % (k, v) for k, v in sorted(nom.items())) if nom else "")
        if n.startswith(":"):                                   # página incrustada
            return self.incrustar(n[1:].strip(), prof)
        if nl == "!":
            return "|"
        if CITA.match(n):
            return self.ref("", "{{%s}}" % cuerpo)
        if nl in ("citation needed", "cn", "fact"):
            return '<sup class="w-falta">[cita requerida]</sup>'
        if nl in ("efn", "notetag", "efn-ua", "efn-lr", "note"):
            return self.nota(pos[0] if pos else nom.get("1", ""))
        if nl == "sfn":
            txt = "%s (%s)" % (pos[0].strip() if pos else "", pos[1].strip() if len(pos) > 1 else "")
            if nom.get("p") or nom.get("pp"):
                txt += ", p. %s" % (nom.get("p") or nom.get("pp"))
            return self.ref("", txt + ".")
        if nl == "r":
            return "".join(self.ref('name="%s"' % p.strip(), None) for p in pos if p.strip())
        if nl in ("notelist", "notes", "notelist-ua"):
            return "\n%sNOTAS%s\n" % (NUL, NUL)
        if nl in ("reflist", "references"):
            self.hay_lista_refs = True
            return "\n%sREFS%s\n" % (NUL, NUL)
        if nl == "linear-gradient":
            direccion = {"left": "to right", "right": "to left", "top": "to bottom", "bottom": "to top"}.get(pos[0].strip() if pos else "", "to right")
            colores = pos[1] if len(pos) > 1 else ""
            return "background:linear-gradient(%s,%s)" % (direccion, colores)
        if nl.startswith("effects/"):
            sub = nl[len("effects/"):]
            if sub == "base":
                return "".join(self.plantillas(p, prof) for p in pos)
            titulo = EFECTOS.get(sub, "Otros efectos")
            contenido = "\n".join(pos) if pos else nom.get("1", "")
            return self.bloque('<div class="w-efectos"><h4>%s</h4>%s</div>' % (titulo, self.fragmento(contenido, prof + 1)))
        if nl == "preamble/subjectiveeffects":
            return self.bloque('<div class="w-aviso w-nota">%s</div>' % self.fragmento(P.PREAMBULO_EFECTOS, prof + 1))
        if nl == "preamble/spiritualeffects":
            return "\n" + P.PREAMBULO_ESPIRITUAL + "\n"
        if nl == "dangerousinteractions/intro":
            return self.bloque('<div class="w-aviso w-nota">%s</div>' % self.fragmento(P.INTERACCIONES_INTRO, prof + 1))
        if nl.startswith("dangerousinteractions/"):
            base = "dangerousinteractions/stimulants" if nl.startswith("dangerousinteractions/stimulants") else clave
            texto = P.INTERACCIONES.get(base) or P.INTERACCIONES.get(nl)
            if texto is None:
                self.sin_plantilla[n] = self.sin_plantilla.get(n, 0) + 1
                return ""
            return "\n" + texto.replace("{pagina}", self.titulo_es) + "\n"
        if nl in P.ESBOZO or nl.replace(" ", "") in P.ESBOZO:
            return self.bloque('<div class="w-aviso w-esbozo">%s</div>' % self.fragmento(P.ESBOZO.get(nl) or P.ESBOZO[nl.replace(" ", "")], prof + 1))
        if nl == "depressantod":
            return self.bloque('<div class="w-aviso w-peligro">%s</div>' % self.fragmento(P.depresor_od(pos[0] if pos else ""), prof + 1))
        if nl.startswith("warning/"):
            texto = P.AVISOS.get(nl.split("|")[0]) or P.AVISOS.get(nl)
            if not texto:
                self.sin_plantilla[n] = self.sin_plantilla.get(n, 0) + 1
                return ""
            return self.bloque('<div class="w-aviso w-peligro">%s</div>' % self.fragmento(texto, prof + 1))
        if nl == "headerpanel":
            return "".join(self.plantillas(p, prof) for p in pos)
        if nl in ("genericpanel/warning", "mbox", "warning"):
            texto = nom.get("title") or nom.get("text") or (pos[0] if pos else "")
            return self.bloque('<div class="w-aviso w-peligro">%s</div>' % self.fragmento(texto, prof + 1)) if texto.strip() else ""
        if nl in ("main", "main article"):
            return self.bloque('<p class="w-principal">Artículo principal: %s</p>' % self.lista_enlaces(pos))
        if nl in ("further", "see also", "further information"):
            pos = [p for p in pos if p.strip()]
            return self.bloque('<p class="w-principal">Véase también: %s</p>' % self.lista_enlaces(pos)) if pos else ""
        if nl in ("distinguish", "distinguish2"):
            return self.bloque('<p class="w-principal">No confundir con %s.</p>' % self.lista_enlaces(pos, " ni "))
        if nl in ("quote", "quote2", "quote3", "quotation", "cquote", "blockquote"):
            texto = pos[0] if pos else nom.get("text", nom.get("quote", ""))
            autor = pos[1] if len(pos) > 1 else nom.get("author", nom.get("sign", ""))
            pie = "<footer>%s</footer>" % self.en_linea(autor) if autor.strip() else ""
            return self.bloque("<blockquote>%s%s</blockquote>" % (self.fragmento(texto, prof + 1), pie))
        if nl == "cc-notice":
            url, autores = nom.get("url", ""), nom.get("author(s)", nom.get("author", ""))
            txt = "Parte de este texto procede de [%s esta fuente]%s, con licencia Creative Commons." % (url, (", de " + autores) if autores else "")
            return self.bloque('<p class="w-principal">%s</p>' % self.en_linea(txt)) if url else ""
        if nl == "nowrap":
            return pos[0] if pos else ""
        if FUERA.match(nl) or FUERA.match(nl.split("/")[0]) or nl.startswith("#"):
            return ""
        self.sin_plantilla[n.split("|")[0]] = self.sin_plantilla.get(n.split("|")[0], 0) + 1
        return ""

    def lista_enlaces(self, destinos, union=", "):
        enl = []
        for d in destinos:
            d = d.strip()
            if not d:
                continue
            base, _, sec = d.partition("#")
            texto = self.nombres.get(base.strip().lower(), base.strip())
            enl.append('<a href="%s">%s</a>' % (PW + quote(d.replace(" ", "_"), safe="#/:(),"), esc(texto)))
        return union.join(enl)

    def incrustar(self, titulo, prof):
        if prof > 2:
            return ""
        t = self.paginas.get(titulo.replace("_", " ").strip().lower())
        if not t:
            return ""
        t = limpiar_fuente(incluir(t, incrustada=True))
        return self.bloque(self.fragmento(t, prof + 1))

    # ------------------------------------------------------------ tablas
    def tablas(self, t):
        while True:
            m = re.search(r"^\s*\{\|", t, re.M)
            if not m:
                return t
            ini = m.start()
            nivel, pos, fin = 0, ini, len(t)
            for ln in re.finditer(r"^.*$", t[ini:], re.M):
                s = ln.group(0).strip()
                if s.startswith("{|"):
                    nivel += 1
                elif s.startswith("|}"):
                    nivel -= 1
                    if nivel == 0:
                        fin = ini + ln.end()
                        break
            bruto = t[ini:fin]
            t = t[:ini] + self.bloque(self.tabla(bruto)) + t[fin:]

    def celda_attrs(self, attrs):
        est = re.search(r'style\s*=\s*"([^"]*)"', attrs)
        span = "".join(' %s="%s"' % (k, v) for k, v in re.findall(r'(colspan|rowspan)\s*=\s*"?(\d+)', attrs))
        if not est:
            return span
        bueno = ";".join(d.strip() for d in est.group(1).split(";") if ESTILO_OK.match(d) or d.strip().startswith("background:linear-gradient"))
        bueno = re.sub(r"[^#a-zA-Z0-9 ,.%():;\-]", "", bueno)
        return span + (' style="%s"' % bueno if bueno else "")

    def tabla(self, bruto):
        filas, fila, celda, caption = [], [], None, ""
        lineas = bruto.strip().split("\n")[1:]
        for ln in lineas:
            s = ln.strip()
            if s.startswith("{|"):
                continue
            if s.startswith("|}"):
                break
            if s.startswith("|+"):
                caption = s[2:].strip(); continue
            if s.startswith("|-"):
                if fila:
                    filas.append(fila)
                fila = []; celda = None; continue
            if s.startswith("!") or s.startswith("|"):
                tag = "th" if s.startswith("!") else "td"
                sep = r"\s*!!\s*|\s*\|\|\s*" if tag == "th" else r"\s*\|\|\s*"
                for trozo in re.split(sep, s[1:]):
                    attrs, contenido = "", trozo
                    m = re.match(r'^([^|\[{]*=[^|\[{]*)\|(?!\|)(.*)$', trozo)
                    if m:
                        attrs, contenido = m.group(1), m.group(2)
                    celda = [tag, self.celda_attrs(attrs), [contenido]]
                    fila.append(celda)
                continue
            if celda is not None:
                celda[2].append(ln)
        if fila:
            filas.append(fila)
        h = ['<table class="w-tabla">']
        if caption:
            h.append("<caption>%s</caption>" % self.en_linea(caption))
        for f in filas:
            h.append("<tr>" + "".join("<%s%s>%s</%s>" % (tg, at, self.celda(c), tg) for tg, at, c in f) + "</tr>")
        h.append("</table>")
        return "".join(h)

    def celda(self, partes):
        txt = "\n".join(partes).strip()
        if re.search(r"^[*#]", txt, re.M):
            return self.lineas(txt)
        return self.en_linea(re.sub(r"\n+", "<br>", txt))

    # ------------------------------------------------------------ líneas
    def lineas(self, t):
        salida, parrafo, pila = [], [], []

        def cerrar_parrafo():
            if parrafo:
                x = self.en_linea(" ".join(parrafo))
                if x.strip():
                    salida.append("<p>%s</p>" % x)
                parrafo.clear()

        def cerrar_listas(hasta=0):
            while len(pila) > hasta:
                tipo = pila.pop()
                salida.append("</li></%s>" % tipo if tipo in ("ul", "ol") else "</dd></dl>")

        for linea in t.split("\n"):
            s = linea.rstrip()
            if re.fullmatch(r"\s*%sB\d+%s\s*" % (NUL, NUL), s) or s.strip() in ("%sREFS%s" % (NUL, NUL), "%sNOTAS%s" % (NUL, NUL)):
                cerrar_parrafo(); cerrar_listas()
                salida.append(s.strip()); continue
            m = re.match(r"^(={1,6})\s*(.+?)\s*\1\s*$", s)
            if m:
                cerrar_parrafo(); cerrar_listas()
                nivel = max(2, min(len(m.group(1)), 4))
                salida.append("<h%d>%s</h%d>" % (nivel, self.en_linea(m.group(2)), nivel)); continue
            if re.match(r"^-{4,}\s*$", s):
                cerrar_parrafo(); cerrar_listas(); salida.append("<hr>"); continue
            m = re.match(r"^([*#:;]+)\s*(.*)$", s)
            if m:
                cerrar_parrafo()
                marcas, contenido = m.group(1), m.group(2)
                tipos = ["ul" if c == "*" else "ol" if c == "#" else "dl" for c in marcas]
                comun = 0
                while comun < min(len(pila), len(tipos)) and pila[comun] == tipos[comun]:
                    comun += 1
                if comun == len(tipos) and comun == len(pila) and comun:
                    salida.append("</li>" if tipos[-1] != "dl" else "</dd>")
                    salida.append("<li>" if tipos[-1] != "dl" else "<dd>")
                else:
                    if comun == len(tipos) and comun < len(pila):
                        cerrar_listas(comun)
                        salida.append("</li><li>" if tipos[-1] != "dl" else "</dd><dd>")
                    else:
                        cerrar_listas(comun)
                        for tp in tipos[comun:]:
                            salida.append("<%s><li>" % tp if tp != "dl" else "<dl><dd>")
                            pila.append(tp)
                if marcas.endswith(";") and ":" in contenido:
                    term, _, defi = contenido.partition(":")
                    contenido = "<strong>%s</strong>: %s" % (term.strip(), defi.strip())
                elif marcas.endswith(";"):
                    contenido = "<strong>%s</strong>" % contenido
                contenido = re.sub(r"</?p>", "<br>", contenido)
                salida.append(self.en_linea(contenido))
                continue
            if not s.strip():
                cerrar_parrafo(); cerrar_listas(); continue
            cerrar_listas()
            parrafo.append(s.strip())
        cerrar_parrafo(); cerrar_listas()
        h = "\n".join(salida)
        h = re.sub(r"<li>\s*(<br>\s*)*</li>|<dd>\s*</dd>", "", h)
        h = re.sub(r"<(ul|ol)>\s*</\1>|<dl>\s*</dl>", "", h)
        h = re.sub(r"(<li>)(\s*<br>)+", r"\1", h)
        h = re.sub(r"<p>\s*(<br>\s*)*</p>", "", h)
        return h

    # ------------------------------------------------------------ en línea
    def enlace(self, m):
        destino, texto, cola = m.group(1).strip(), m.group(2), m.group(3) or ""
        if SIN_ENLACE.match(destino.lstrip(":")):
            return ""
        prop = re.match(r"^([\w ]+)::(.*)$", destino)
        if prop:
            destino = prop.group(2).strip()
            es_clase = "class" in prop.group(1).lower()
            if es_clase and texto is None and re.fullmatch(r"[a-z \-]+", destino) and destino.lower() not in DESTINO_CLASE:
                return cola                     # clase en inglés sin texto: el traductor ya la dijo con sus palabras
            if es_clase and destino.lower() in DESTINO_CLASE:
                texto = texto if texto is not None else destino
                destino = DESTINO_CLASE[destino.lower()]
        destino = destino.lstrip(":")
        if texto is None:
            texto = destino.split("#")[0] if not destino.startswith("#") else destino[1:]
        texto = texto + cola
        if re.match(r"^(wikipedia|w|wp):", destino, re.I):
            url = WP + quote(destino.split(":", 1)[1].strip().replace(" ", "_"), safe="#/:(),")
            return '<a class="ext" href="%s" rel="noopener">%s</a>' % (url, texto)
        if destino.startswith("#"):
            return texto
        return '<a href="%s">%s</a>' % (PW + quote(destino.replace(" ", "_"), safe="#/:(),"), texto)

    def en_linea(self, s):
        if not s:
            return ""
        s = html.unescape(s)
        s = esc(s).replace("&quot;", '"').replace("&#x27;", "'")
        for tag in TAGS_OK:
            s = re.sub(r"&lt;(/?)%s(\s[^&]*?)?\s*/?&gt;" % tag, lambda m: "<%s%s>" % (m.group(1), tag), s, flags=re.I)
        s = re.sub(r"&lt;(/?)p(\s[^&]*?)?&gt;", lambda m: "" if m.group(1) else "<br>", s, flags=re.I)
        s = re.sub(r"&lt;/?[a-zA-Z][^&]*?&gt;", "", s)
        s = s.replace("<br></br>", "<br>")
        # enlaces internos (con «cola» de letras pegada: [[barbiturate]]s)
        s = re.sub(r"\[\[([^\[\]|]+)(?:\|([^\[\]]*))?\]\]([a-záéíóúñü]*)", self.enlace, s)
        s = re.sub(r"\[\[[^\]]*\]\]", "", s)
        # externos
        # (los PDF alojados en «wp-content» de otras webs van sin enlace: el comprobador del sitio los veta)
        s = re.sub(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]", lambda m: m.group(2) if WP_RUTA.search(m.group(1)) else
                   '<a class="ext" href="%s" rel="noopener">%s</a>' % (m.group(1), m.group(2)), s)
        s = re.sub(r"\[(https?://[^\s\]]+)\]", lambda m: "" if WP_RUTA.search(m.group(1)) else
                   '<a class="ext" href="%s" rel="noopener">enlace</a>' % m.group(1), s)
        s = comillas(s)
        s = re.sub(r"\s+", " ", s)
        s = re.sub(r"%sR(\d+)%s" % (NUL, NUL), lambda m: '<sup class="w-ref"><a href="#ref-%s">[%s]</a></sup>' % (m.group(1), m.group(1)), s)
        s = re.sub(r"%sN(\d+)%s" % (NUL, NUL), lambda m: '<sup class="w-ref"><a href="#nota-%s">[nota %s]</a></sup>' % (m.group(1), m.group(1)), s)
        return s.strip()

    # ------------------------------------------------------------ montaje final
    def poner_listas(self, h):
        for _ in range(4):                    # bloques dentro de bloques
            h = re.sub(r"%sB(\d+)%s" % (NUL, NUL), lambda m: self.bloques[int(m.group(1))], h)
        notas = ""
        if self.notas:
            notas = '<ol class="w-notas">%s</ol>' % "".join(
                '<li id="nota-%d">%s</li>' % (i + 1, n) for i, n in enumerate(self.notas))
        refs = ""
        if self.refs:
            refs = '<ol class="w-refs">%s</ol>' % "".join(
                '<li id="ref-%d">%s</li>' % (i + 1, r or "Referencia sin datos en el original.") for i, r in enumerate(self.refs))
        mref, mnot = "%sREFS%s" % (NUL, NUL), "%sNOTAS%s" % (NUL, NUL)
        if notas and mnot in h:
            h = h.replace(mnot, notas, 1)
        elif notas:
            refs = "<h3>Notas</h3>" + notas + ("<h3>Referencias</h3>" + refs if refs else "")
        h = h.replace(mnot, "")
        if mref in h:
            h = h.replace(mref, refs, 1).replace(mref, "")
        elif refs:
            h += "<h2>Referencias</h2>" + refs
        # resolver marcas que hayan quedado dentro de bloques ya montados
        h = re.sub(r"%sR(\d+)%s" % (NUL, NUL), lambda m: '<sup class="w-ref"><a href="#ref-%s">[%s]</a></sup>' % (m.group(1), m.group(1)), h)
        h = re.sub(r"%sN(\d+)%s" % (NUL, NUL), lambda m: '<sup class="w-ref"><a href="#nota-%s">[nota %s]</a></sup>' % (m.group(1), m.group(1)), h)
        h = h.replace(NUL, "")
        # apartados que se quedan sin contenido (p. ej. «Referencias» sin lista)
        for _ in range(3):
            h = re.sub(r"<h([2-4])>[^<]*</h\1>\s*(?=<h([2-4])>|$)",
                       lambda m: "" if m.group(2) is None or int(m.group(2)) <= int(m.group(1)) else m.group(0), h)
        return h.strip()
