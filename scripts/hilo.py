"""Hilo de cada medicina: enlaces entre las páginas que APDER tiene de una misma medicina.

Una medicina puede tener en apder.org su guía, su ficha en la Enciclopedia, su guía de microdosis, su entrada en
«Medicinas por familias», su página en Psiconáutica, su guía de terapia y sus libros en la Biblioteca. Este guion
pone en cada una de esas páginas, justo debajo de la cabecera, una línea fina con las demás: el hilo
(<nav class="hilo">). Cada cuenta lleva el color de la puerta del menú a la que lleva; la de la página en la que
se está va rellena.

  python3 scripts/hilo.py            pone el hilo en todas las páginas
  python3 scripts/hilo.py --mira     dice cuántas páginas cambiarían y lo que no encuentra, sin escribir
  python3 scripts/hilo.py --lista    escribe, medicina a medicina, qué enlaza cada hilo

scripts/cabecera.py también lo pone (llama a poner() en cada página), así que basta con lanzar ese guion después
de cualquier generador. Los generadores de la Enciclopedia y de Psiconáutica reescriben sus páginas enteras y les
quitan el hilo hasta que se lanza otra vez.

Los datos van en MEDICINAS. En cada medicina, la primera página de cada lista es la principal: a ella lleva el hilo
desde las demás secciones. Psiconáutica va por el título original de la página (data-original), como en
scripts/psiconautica/puentes.py. GEMELAS une una ficha de la Enciclopedia con la página de Psiconáutica del mismo
ser (el peyote con Lophophora williamsii): desde una se va a la otra y no a la principal.
Una página pertenece a la primera medicina que la nombra. Lo que no existe en docs/ no se enlaza (--mira lo dice).
Los libros se cuentan en la portada de la Biblioteca (data-sust): una etiqueta sin libros no sale, y el número se
rehace cada vez que se lanza el guion.
Estilos: docs/hilo.css, enlazada solo en las páginas con hilo, justo después de tierra.css. Si se cambia, subir VERSION.
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
VERSION = "20261128a"   # va en el ?v= de hilo.css: se sube cuando cambia la hoja


def M(nombre, guia=None, enc=(), micro=None, familia=None, psi=(), terapia=None, libros=None, gemelas=None):
    return {"nombre": nombre, "guia": guia, "enc": list(enc), "micro": micro, "familia": familia,
            "psi": list(psi), "terapia": terapia, "libros": libros, "gemelas": gemelas or {}}


# Orden de las medicinas: decide a cuál pertenece una página que nombran dos (la primera).
MEDICINAS = [
    # --- Con guía ---
    M("Psilocibina", guia="sustancias/psilocibina/", micro="sustancias/microdosis/setas/", terapia="terapia/psilocibina/",
      enc=["psilocibina", "mongui", "san-isidro", "psilocibe-azulado", "pajaritos", "derrumbe", "copelandia"],
      psi=["Psilocybin mushrooms", "Psilocin", "Psilocybe cubensis", "Psilocybe cyanescens", "Psilocybe mexicana",
           "Panaeolus cyanescens"],
      gemelas={"san-isidro": "Psilocybe cubensis", "psilocibe-azulado": "Psilocybe cyanescens",
               "pajaritos": "Psilocybe mexicana", "copelandia": "Panaeolus cyanescens"},
      familia="psilocibina-y-setas-psilocibes", libros="psilocibina"),
    M("LSD", guia="sustancias/lsd/", micro="sustancias/microdosis/lsd/", terapia="terapia/lsd/",
      enc=["lsd"], psi=["LSD"], familia="lsd", libros="LSD"),
    M("Mescalina", guia="sustancias/mescalina/", micro="sustancias/microdosis/mescalina/", terapia="terapia/mescalina/",
      enc=["mescalina", "peyote", "san-pedro", "antorcha-peruana"],
      psi=["Mescaline", "Lophophora williamsii", "Echinopsis pachanoi", "Echinopsis peruviana"],
      gemelas={"peyote": "Lophophora williamsii", "san-pedro": "Echinopsis pachanoi",
               "antorcha-peruana": "Echinopsis peruviana"},
      familia="mescalina-peyote-y-san-pedro", libros="mescalina"),
    M("DMT", guia="sustancias/dmt/", micro="sustancias/microdosis/dmt/",
      enc=["dmt", "chacruna", "chaliponga", "jurema", "vino-de-jurema", "changa"],
      psi=["DMT", "Psychotria viridis", "Mimosa tenuiflora", "Changa"],
      gemelas={"chacruna": "Psychotria viridis", "jurema": "Mimosa tenuiflora", "vino-de-jurema": "Mimosa tenuiflora",
               "changa": "Changa"},
      familia="dmt", libros="DMT"),
    M("Ayahuasca", guia="sustancias/ayahuasca/", micro="sustancias/microdosis/ayahuasca/", terapia="terapia/ayahuasca/",
      enc=["ayahuasca", "harmina-y-harmalina"], psi=["Ayahuasca", "Banisteriopsis caapi", "Harmala alkaloid"],
      gemelas={"harmina-y-harmalina": "Harmala alkaloid"}, familia="ayahuasca", libros="ayahuasca"),
    M("5-MeO-DMT", guia="sustancias/5-meo-dmt/", terapia="terapia/5-meo-dmt/",
      enc=["5-meo-dmt", "sapo-de-sonora"], psi=["5-MeO-DMT"], familia="5-meo-dmt", libros="5-MeO-DMT"),
    M("MDMA", guia="sustancias/mdma/", terapia="terapia-asistida-mdma/",
      enc=["mdma"], psi=["MDMA"], familia="mdma", libros="MDMA"),
    M("Ketamina", guia="sustancias/ketamina/", terapia="terapia/ketamina/",
      enc=["ketamina"], psi=["Ketamine"], familia="ketamina-y-esketamina", libros="ketamina"),
    M("Ibogaína", guia="sustancias/ibogaina/", micro="sustancias/microdosis/ibogaina/", terapia="terapia/ibogaina/",
      enc=["ibogaina", "iboga"], psi=["Ibogaine"], familia="ibogaina", libros="ibogaína"),
    M("2C-B", guia="sustancias/2c-b/", enc=["2c-b"], psi=["2C-B"], familia="2c-b"),
    M("4-AcO-DMT", guia="sustancias/4-aco-dmt/", enc=["4-aco-dmt"], psi=["4-AcO-DMT"], familia="4-aco-dmt"),
    M("Amanita muscaria", guia="sustancias/amanita-muscaria/",
      enc=["amanita-muscaria", "muscimol", "acido-ibotenico"], psi=["Amanita muscaria", "Ibotenic acid"],
      gemelas={"acido-ibotenico": "Ibotenic acid"}, familia="amanita-muscaria", libros="amanita"),
    M("Salvia divinorum", guia="sustancias/salvia-divinorum/",
      enc=["hierba-de-la-pastora", "salvinorina-a"], psi=["Salvia divinorum", "Salvinorin A"],
      gemelas={"salvinorina-a": "Salvinorin A"}, familia="salvia-divinorum", libros="salvia"),
    M("Cannabis", guia="sustancias/cannabis/", enc=["cannabis", "thc"], psi=["Cannabis"], familia="cannabis",
      libros="cannabis"),
    M("Kanna", guia="sustancias/kanna/", enc=["kanna"], familia="kanna"),
    M("Kratom", guia="sustancias/kratom/", enc=["kratom", "mitraginina"], psi=["Kratom"], familia="kratom",
      libros="kratom"),
    M("Datura", guia="sustancias/datura/", enc=["estramonio", "toloache", "escopolamina"], psi=["Datura"],
      familia="datura", libros="datura"),
    M("Cacao", guia="sustancias/cacao/", enc=["cacao"], psi=["Cocoa"], familia="cacao", libros="cacao"),
    M("Tabaco", guia="sustancias/tabaco/", enc=["tabaco", "mapacho", "rape"], psi=["Nicotine"],
      familia="tabaco-rape-y-mapacho", libros="tabaco"),
    # --- Sin guía, con entrada en «Medicinas por familias» ---
    M("Bufotenina", enc=["bufotenina", "yopo", "cebil", "cohoba"], psi=["Bufotenin", "Anadenanthera peregrina"],
      gemelas={"yopo": "Anadenanthera peregrina", "cohoba": "Anadenanthera peregrina"},
      familia="bufotenina-yopo-y-cebil", libros="yopo"),
    M("Virola", enc=["epena"], familia="virola"),
    M("LSA", enc=["lsa", "gloria-de-la-manana", "rosa-lisergica", "ololiuqui"],
      psi=["LSA", "Morning glory", "Ipomoea tricolor", "Argyreia nervosa"],
      gemelas={"gloria-de-la-manana": "Ipomoea tricolor", "rosa-lisergica": "Argyreia nervosa"},
      familia="lsa-semillas-de-ipomoea-y-argyreia"),
    M("Cornezuelo", enc=["cornezuelo"], psi=["Ergot"], familia="cornezuelo"),
    M("2C-x", psi=["2C-x"], familia="la-familia-2c"),
    M("DOx", psi=["DOx"], familia="dox"),
    M("MDA", psi=["MDA"], familia="mda"),
    M("Óxido nitroso", psi=["Nitrous"], familia="oxido-nitroso"),
    M("DXM", psi=["Dextromethorphan"], familia="dxm"),
    M("PCP", psi=["PCP"], familia="pcp-mencion-historica"),
    M("Hierba de los sueños", enc=["hierba-de-los-suenos"], psi=["Calea ternifolia"], familia="calea-zacatechichi"),
    M("Silene capensis", enc=["raiz-africana-de-los-suenos"], familia="silene-capensis"),
    M("Kava", enc=["kava"], psi=["Kava"], familia="kava", libros="kava"),
    M("Sananga", enc=["sananga"], familia="sananga"),
    M("Kambó", enc=["kambo"], psi=["Kambo"], familia="kambo"),
    M("Ruda siria", enc=["ruda-siria"], psi=["Peganum harmala"], familia="ruda-siria-harmala"),
    M("Loto azul", enc=["loto-azul"], psi=["Blue lotus", "Nymphaea caerulea"], familia="nenufar-azul"),
    M("Damiana", enc=["damiana"], familia="damiana"),
    # La Enciclopedia manda el floripondio y la mandrágora a la guía de la datura («Para la práctica»).
    M("Floripondio", guia="sustancias/datura/", enc=["floripondio"], familia="brugmansia"),
    M("Belladona", enc=["belladona"], psi=["Atropa belladonna"], familia="belladona"),
    M("Mandrágora", guia="sustancias/datura/", enc=["mandragora"], psi=["Mandragora"], familia="mandragora"),
    # --- Solo en la Enciclopedia y en Psiconáutica ---
    M("Coca", enc=["coca"], psi=["Coca", "Cocaine"], libros="coca"),
    M("Khat", enc=["khat"], psi=["Cathinone"]),
    M("Adormidera", enc=["adormidera"], psi=["Papaver somniferum", "Opium"], libros="opio"),
    M("Efedra", enc=["efedra"], psi=["Ephedrine"]),
    M("Nuez moscada", enc=["nuez-moscada"], psi=["Myristicin"]),
    M("Amanita pantera", enc=["amanita-pantera"], psi=["Amanita pantherina"]),
    M("Beleño negro", enc=["beleno-negro"], psi=["Hyoscyamus niger (botany)"]),
]

# Secciones del hilo, en el orden del menú (Medicinas · La experiencia · Terapia · Biblioteca).
SECCIONES = [("guia", "Guía"), ("enc", "Enciclopedia"), ("micro", "Microdosis"), ("familia", "Familia"),
             ("psi", "Psiconáutica"), ("terapia", "Terapia"), ("libros", "Libros")]

# Nombre corto de cada familia de «Medicinas por familias» (ancla de su <h2>).
FAMILIAS = {"triptaminas": "triptaminas", "ergolinas": "ergolinas", "fenetilaminas": "fenetilaminas",
            "empatogenos": "empatógenos", "disociativos": "disociativos", "oneirogenos": "oneirógenos",
            "plantas-diversas": "plantas y hongos", "delirantes": "delirantes", "nuevas-moleculas": "nuevas moléculas"}

RE_HILO = re.compile(r'\n?<nav class="hilo"[^>]*>.*?</nav>', re.S)
RE_HOJA = re.compile(r'\n?<link rel="stylesheet" href="[^"]*hilo\.css(?:\?v=[^"]*)?">')
RE_TIERRA = re.compile(r'<link rel="stylesheet" href="[^"]*tierra\.css[^"]*">')
RE_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
BINOMIO = re.compile(r"[A-Z][a-z]+ [a-z]+")


def plano(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


class Datos:
    """Lo que el hilo necesita saber de la web publicada. Se lee una vez."""

    def __init__(self, docs=DOCS):
        self.docs = Path(docs)
        self.avisos = []
        self.psi = {}           # título original -> (ruta de la página, título en español)
        for f in sorted((self.docs / "psiconautica").glob("*/index.html")):
            t = f.read_text(encoding="utf-8")
            m = re.search(r'<main[^>]*\bdata-original="([^"]*)"', t)
            if m:
                h1 = RE_H1.search(t)
                self.psi[html.unescape(m.group(1))] = (f"psiconautica/{f.parent.name}/", plano(h1.group(1)) if h1 else "")
        fam = self.docs / "medicinas" / "index.html"
        self.familias = {}      # ancla de la entrada -> nombre corto de su familia
        if fam.is_file():
            t = fam.read_text(encoding="utf-8")
            actual = None
            for m in re.finditer(r'<h([23]) id="([^"]+)"', t):
                if m.group(1) == "2":
                    actual = m.group(2) if m.group(2) in FAMILIAS else None
                elif actual:
                    self.familias[m.group(2)] = FAMILIAS[actual]
        bib = self.docs / "biblioteca" / "index.html"
        self.libros = {}        # etiqueta data-sust -> número de libros
        if bib.is_file():
            for v in re.findall(r'data-sust="([^"]*)"', bib.read_text(encoding="utf-8")):
                for s in set(v.split()):
                    self.libros[s] = self.libros.get(s, 0) + 1
        self.medicinas = [self._resolver(m) for m in MEDICINAS]
        self.duenas = {}        # ruta de la página -> (medicina, sección)
        for med in self.medicinas:
            for sec, _ in SECCIONES:
                for ruta in med["rutas"].get(sec, []):
                    if ruta not in self.duenas:
                        self.duenas[ruta] = (med, sec)

    def existe(self, ruta):
        return (self.docs / ruta / "index.html").is_file()

    def nombre(self, ruta):
        f = self.docs / ruta / "index.html"
        m = RE_H1.search(f.read_text(encoding="utf-8")) if f.is_file() else None
        return plano(m.group(1)) if m else ""

    def _resolver(self, m):
        """Pasa los datos de una medicina a rutas de docs/ y deja fuera (con aviso) lo que no existe."""
        rutas, nombres, italica = {}, {}, set()

        def pagina(sec, ruta):
            if self.existe(ruta):
                rutas.setdefault(sec, []).append(ruta)
                return ruta
            self.avisos.append(f"{m['nombre']}: no existe {ruta}")
            return None

        for sec in ("guia", "micro", "terapia"):
            if m[sec]:
                pagina(sec, m[sec])
        for slug in m["enc"]:
            r = pagina("enc", f"enciclopedia/{slug}/")
            if r:
                nombres[r] = self.nombre(r)
        psi_de = {}
        for tit in m["psi"]:
            if tit in self.psi:
                r, nom = self.psi[tit]
                rutas.setdefault("psi", []).append(r)
                nombres[r] = nom
                psi_de[tit] = r
                if nom == tit and BINOMIO.fullmatch(nom):
                    italica.add(r)
            else:
                self.avisos.append(f"{m['nombre']}: Psiconáutica no tiene «{tit}»")
        gemelas = {}
        for slug, tit in m["gemelas"].items():
            e, p = f"enciclopedia/{slug}/", psi_de.get(tit)
            if e in nombres and p:
                gemelas.setdefault(e, p)
                gemelas.setdefault(p, e)
        familia = None
        if m["familia"]:
            if m["familia"] in self.familias:
                familia = m["familia"]
            else:
                self.avisos.append(f"{m['nombre']}: «Medicinas por familias» no tiene #{m['familia']}")
        libros = self.libros.get(m["libros"], 0) if m["libros"] else 0
        return dict(m, rutas=rutas, nombres=nombres, italica=italica, gemelas_r=gemelas, familia_ok=familia,
                    n_libros=libros)

    def hilo(self, ruta_pagina):
        """HTML del hilo de una página (ruta relativa a docs/, p. ej. 'sustancias/lsd/index.html'), o ''."""
        propia = ruta_pagina[:-len("index.html")] if ruta_pagina.endswith("index.html") else ruta_pagina
        if propia not in self.duenas:
            return ""
        med, sec_propia = self.duenas[propia]
        r = "../" * ruta_pagina.count("/")
        cuentas = []
        for sec, rotulo in SECCIONES:
            detalle, italica = "", False
            if sec == "familia":
                if not med["familia_ok"]:
                    continue
                destino = f"medicinas/#{med['familia_ok']}"
                detalle = self.familias[med["familia_ok"]]
            elif sec == "libros":
                if not med["n_libros"]:
                    continue
                destino = "biblioteca/?sust=" + quote(med["libros"], safe="")
                detalle = str(med["n_libros"])
            else:
                rutas = med["rutas"].get(sec, [])
                if not rutas:
                    continue
                if sec == sec_propia:
                    cuentas.append(f'<li class="hilo-{sec}"><span class="hilo-aqui" aria-current="page">'
                                   f'<span class="hilo-t">{rotulo}</span><span class="hilo-vh"> (esta página)</span>'
                                   f'</span></li>')
                    continue
                gemela = med["gemelas_r"].get(propia)
                if gemela and gemela in rutas:
                    destino = gemela
                    detalle, italica = med["nombres"][gemela], gemela in med["italica"]
                else:
                    destino = rutas[0]
                    duena = self.duenas.get(destino, (med,))[0]
                    if duena is not med:          # la guía es de otra medicina (floripondio → datura)
                        detalle = duena["nombre"]
            det = ""
            if detalle:
                txt = html.escape(detalle)
                det = f'<span class="hilo-d"><span class="hilo-vh">: </span>{f"<i>{txt}</i>" if italica else txt}</span>'
            cuentas.append(f'<li class="hilo-{sec}"><a href="{r}{destino}"><span class="hilo-t">{rotulo}</span>{det}</a></li>')
        if len(cuentas) < 2:
            return ""
        nombre = html.escape(med["nombre"])
        return (f'<nav class="hilo" aria-labelledby="hilo-nombre">\n<div class="ancho hilo-in">'
                f'<p class="hilo-nombre" id="hilo-nombre">{nombre}<span class="hilo-vh"> en APDER</span></p>\n'
                f'<ul class="hilo-l">\n' + "\n".join(cuentas) + "\n</ul>\n</div>\n</nav>")


_DATOS = None


def datos():
    global _DATOS
    if _DATOS is None:
        _DATOS = Datos()
    return _DATOS


def poner(texto, ruta):
    """Quita el hilo que hubiera (y su hoja) y pone el que toca, justo después de la cabecera.
    Da lo mismo si se lanza dos veces."""
    limpio = RE_HOJA.sub("", RE_HILO.sub("", texto))
    nuevo = datos().hilo(ruta)
    if not nuevo:
        return limpio
    i = limpio.find('<header class="cabecera"')
    j = limpio.find("</header>", i) if i >= 0 else -1
    t = RE_TIERRA.search(limpio)
    if j < 0 or not t:
        return limpio
    j += len("</header>")
    hoja = f'\n<link rel="stylesheet" href="{"../" * ruta.count("/")}hilo.css?v={VERSION}">'
    con = limpio[:j] + "\n" + nuevo + limpio[j:]
    return con[:t.end()] + hoja + con[t.end():]


def main():
    mira = "--mira" in sys.argv
    d = datos()
    if "--lista" in sys.argv:
        for med in d.medicinas:
            print(f"\n{med['nombre']}")
            for sec, rotulo in SECCIONES:
                if sec == "familia" and med["familia_ok"]:
                    print(f"  {rotulo}: #{med['familia_ok']} ({d.familias[med['familia_ok']]})")
                elif sec == "libros" and med["n_libros"]:
                    print(f"  {rotulo}: ?sust={med['libros']} ({med['n_libros']})")
                elif med["rutas"].get(sec):
                    print(f"  {rotulo}: " + ", ".join(med["rutas"][sec]))
        return
    cambiadas = con_hilo = 0
    for f in sorted(DOCS.rglob("*.html")):
        antes = f.read_text(encoding="utf-8")
        if '<header class="cabecera"' not in antes:
            continue
        despues = poner(antes, f.relative_to(DOCS).as_posix())
        con_hilo += '<nav class="hilo"' in despues
        if despues != antes:
            cambiadas += 1
            if not mira:
                f.write_text(despues, encoding="utf-8")
    for a in d.avisos:
        print("aviso:", a)
    print(f"páginas con hilo: {con_hilo} · {'cambiarían' if mira else 'cambiadas'}: {cambiadas}")


if __name__ == "__main__":
    main()
