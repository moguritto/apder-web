#!/usr/bin/env python3
"""«Investigación terapéutica» (docs/investigacion-terapeutica/index.html): la página entera.

  python3 scripts/investigacion/generar.py

El TEXTO vive en scripts/investigacion/texto.html, en HTML llano (h2, h3, p, listas, las dos tablas, las preguntas
y las referencias): ahí se corrige. Este guion le pone el diseño y no cambia ni una palabra. Sustituye a apertura.py.

Seña de la puerta «Terapia»: fondo claro, manchas e ilustración. Estilos y guion propios, sin depender de las hojas
de las guías de terapia (que cambian a su ritmo): docs/investigacion-terapeutica/investigacion.css (todo bajo .iv,
prefijo iv-) e investigacion.js (barra de lectura, apartado en curso y gráfico que se dibuja al llegar).
  · portada con la escalera de la evidencia (semilla, brote y flor: preliminar, prometedora y sólida);
  · «De un vistazo»: la pirámide de la evidencia, con cada línea de investigación en su piso;
  · cuatro partes con índice lateral: Entender · Problema a problema · Participar · Dudas y fuentes;
  · las fases de un ensayo como camino, los límites de la evidencia como ideas numeradas y un gráfico con el número
    de participantes de los estudios que cita la página (ESTUDIOS);
  · la tabla de la evidencia con un trazo por fase, y esa misma ficha (sustancias, fase y nivel) bajo el título de
    cada problema de salud.

Todo lo que se dibuja sale del texto: la pirámide, las fichas y los trazos se leen de la tabla «Cómo va la
investigación en cada problema de salud»; los niveles, de la columna «Nivel de evidencia»; las fases, de la tabla
de fases. Lo único que se escribe aquí son los rótulos de la página, los nombres cortos del índice (INDICE) y la
lista de estudios del gráfico (ESTUDIOS), que el guion comprueba contra el texto: si un número cambia, se para.
El <head>, la cabecera y el pie se conservan de la página publicada (los pone scripts/cabecera.py).
"""
import html
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from cabecera import aplicar  # noqa: E402

DOCS = RAIZ / "docs"
PAG = DOCS / "investigacion-terapeutica" / "index.html"
TEXTO = Path(__file__).with_name("texto.html")
VERSION = "20261127a"

ENTRADA = "Qué se sabe, qué falta por saber y cómo participar en un ensayo clínico con garantías."
NIVELES = {1: ("Preliminar", "Estudios pequeños"), 2: ("Prometedora", "Al menos un ensayo aleatorizado favorable"),
           3: ("Sólida", "Varios ensayos de fase 3 y aprobación como medicamento")}
PARTES = [  # (ancla, título, entradilla, primera sección, dibujo)
    ("parte-entender", "Entender", "Qué se investiga, cómo es un ensayo y por qué conviene leer los resultados con calma.", "introduccion",
     '<circle class="m-salvia" cx="206" cy="92" r="76"/><rect class="m-crema" x="158" y="40" width="96" height="116" rx="12"/>'
     '<path class="t-salvia" d="M176 70h60M176 90h60M176 110h30"/><circle class="m-blanco" cx="232" cy="120" r="27"/>'
     '<circle class="t-tierra" cx="232" cy="120" r="27"/><path class="t-tierra" d="M252 140l22 22"/>'
     '<circle class="m-tierra" cx="92" cy="50" r="20"/><circle class="m-arena" cx="72" cy="130" r="28"/>'),
    ("parte-problemas", "Problema a problema", "En qué punto está la investigación en cada problema de salud, con sus resultados y sus límites.",
     "estado-evidencia",
     '<circle class="m-tierra" cx="212" cy="92" r="76"/><rect class="m-crema" x="144" y="44" width="136" height="26" rx="13"/>'
     '<rect class="m-crema" x="144" y="78" width="136" height="26" rx="13"/><rect class="m-crema" x="144" y="112" width="136" height="26" rx="13"/>'
     '<path class="t-bosque" d="M160 57h76M160 91h48M160 125h22"/><circle class="m-salvia" cx="88" cy="56" r="22"/>'
     '<circle class="m-crema" cx="70" cy="132" r="26"/>'),
    ("parte-participar", "Participar", "Dónde buscar un ensayo, qué preguntar, qué derechos tienes y qué señales invitan a desconfiar.", "participar",
     '<circle class="m-arena2" cx="208" cy="92" r="78"/><rect class="m-blanco" x="164" y="40" width="88" height="112" rx="12"/>'
     '<rect class="m-bosque" x="189" y="31" width="38" height="18" rx="8"/><path class="t-salvia" d="M180 80l8 8 14-16M180 116l8 8 14-16"/>'
     '<path class="t-tierra" d="M214 82h22M214 118h22"/><circle class="m-tierra" cx="92" cy="52" r="20"/><circle class="m-salvia" cx="76" cy="130" r="26"/>'),
    ("parte-dudas", "Dudas y fuentes", "Las preguntas más frecuentes y los estudios en los que se apoya esta página.", "preguntas-frecuentes",
     '<circle class="m-salvia" cx="208" cy="94" r="76"/><path class="m-crema" d="M148 60c20-8 42-8 60 2v84c-18-10-40-10-60-2z"/>'
     '<path class="m-blanco" d="M268 60c-20-8-42-8-60 2v84c18-10 40-10 60-2z"/>'
     '<path class="t-bosque" d="M164 84c10-3 20-3 30 0M164 106c10-3 20-3 30 0M222 84c10-3 20-3 30 0M222 106c10-3 20-3 30 0"/>'
     '<circle class="m-tierra" cx="94" cy="54" r="22"/><circle class="m-arena" cx="74" cy="132" r="26"/>'),
]
INDICE = {  # nombres cortos para el índice lateral (si no, el título del apartado)
    "introduccion": "Qué se investiga y por qué", "estado-evidencia": "La tabla completa",
    "depresion-resistente": "Depresión resistente", "tept": "Estrés postraumático (TEPT)",
    "final-de-vida": "Enfermedad grave y final de la vida", "toc": "Obsesivo-compulsivo (TOC)", "otras": "Otras líneas",
    "participar": "Participar en un ensayo",
}
# Gráfico «cuántas personas»: (apartado, rótulo, participantes, frase del texto que lo dice)
ESTUDIOS = [
    ("depresion-resistente", "Depresión resistente · psilocibina", 233, "233 personas"),
    ("depresion-resistente", "Depresión resistente · ayahuasca", 29, "29 pacientes"),
    ("depresion-mayor", "Depresión mayor · psilocibina", 59, "59 personas"),
    ("depresion-mayor", "Depresión mayor · psilocibina", 24, "24 personas"),
    ("depresion-mayor", "Depresión mayor · psilocibina", 104, "104 personas"),
    ("depresion-mayor", "Depresión mayor · psilocibina", 52, "52 personas"),
    ("adicciones", "Alcohol · psilocibina", 95, "95 personas"),
    ("adicciones", "Tabaco · psilocibina", 15, "15 fumadores"),
    ("final-de-vida", "Ansiedad · LSD", 42, "42 personas"),
    ("toc", "TOC · psilocibina", 9, "9 personas"),
    ("anorexia", "Anorexia · psilocibina", 10, "10 mujeres"),
    ("bipolar", "Trastorno bipolar · psilocibina", 15, "15 personas"),
    ("otras", "Lesión cerebral · ibogaína", 30, "30 veteranos"),
]
ANCLA_ESTUDIO = {"Alcohol · psilocibina": "alcohol", "Tabaco · psilocibina": "tabaco"}

ICO_NIVEL = {
    1: '<path d="M24 40V29"/><path d="M24 31c0-6-4-9-10-9 0 6 4 9 10 9z"/><path d="M14 40h20"/>',
    2: '<path d="M24 40V19"/><path d="M24 30c0-6-4-9-10-9 0 6 4 9 10 9z"/><path d="M24 23c0-5 4-8 9-8 0 5-4 8-9 8z"/><path d="M14 40h20"/>',
    3: '<path d="M24 40V21"/><path d="M24 33c0-5-4-8-9-8 0 5 4 8 9 8z"/><path d="M24 30c0-4 3-7 8-7 0 4-3 7-8 7z"/><circle cx="24" cy="13" r="3.2"/>'
       '<path d="M24 5.5v2M24 18.500v2M16.500 13h2M29.500 13h2M18.700 7.700l1.400 1.400M27.900 16.900l1.400 1.400M29.300 7.700l-1.400 1.400M20.100 16.900l-1.400 1.400"/><path d="M14 40h20"/>',
}

ILUSTRACION = """<svg viewBox="0 0 640 520" focusable="false">
        <path fill="#7d9a7a" d="M82 118C132 38 270 2 384 30c114 28 214 122 210 236s-116 206-240 220S96 446 54 340 38 188 82 118z"/>
        <path fill="#c2643c" d="M262 164c84-44 212-22 268 58s40 200-40 256-208 50-274-18-56-174-20-236c18-30 38-46 66-60z"/>
        <ellipse cx="334" cy="456" rx="272" ry="34" fill="#efe4d0"/>
        <path fill="#f7f1e6" d="M92 456v-74a16 16 0 0 1 16-16h152v90z"/>
        <path fill="#fbf7ef" d="M260 456V298a16 16 0 0 1 16-16h152v174z"/>
        <path fill="#f7f1e6" d="M428 456V226a16 16 0 0 1 16-16h118a16 16 0 0 1 16 16v230z"/>
        <path d="M260 372v84M428 290v166" stroke="#e5d6bb" stroke-width="3" stroke-linecap="round"/>
        <g fill="#ddd0b8"><rect x="139" y="408" width="22" height="8" rx="4" fill="#2f3e33"/><rect x="166" y="408" width="22" height="8" rx="4"/><rect x="193" y="408" width="22" height="8" rx="4"/>
        <rect x="305" y="364" width="22" height="8" rx="4" fill="#2f3e33"/><rect x="332" y="364" width="22" height="8" rx="4" fill="#2f3e33"/><rect x="359" y="364" width="22" height="8" rx="4"/>
        <rect x="464" y="322" width="22" height="8" rx="4" fill="#2f3e33"/><rect x="491" y="322" width="22" height="8" rx="4" fill="#2f3e33"/><rect x="518" y="322" width="22" height="8" rx="4" fill="#2f3e33"/></g>
        <path fill="#7a3519" d="M148 366a29 15 0 0 1 58 0z"/>
        <path d="M177 354v-20" stroke="#2f3e33" stroke-width="5" stroke-linecap="round"/>
        <path fill="#2f3e33" d="M177 340c-15 2-24-7-24-18 14-2 24 5 24 18z"/><path fill="#48614b" d="M177 334c2-13 12-20 23-18 0 12-9 20-23 18z"/>
        <path fill="#7a3519" d="M311 282a33 16 0 0 1 66 0z"/>
        <path d="M344 270v-70" stroke="#2f3e33" stroke-width="5" stroke-linecap="round"/>
        <path fill="#2f3e33" d="M344 252c-21 2-34-10-34-26 19-2 34 9 34 26zM344 218c-15 2-25-7-25-19 14-2 25 6 25 19z"/>
        <path fill="#48614b" d="M344 242c2-19 17-30 34-28 0 17-13 30-34 28zM344 208c2-13 12-21 25-19 0 12-10 21-25 19z"/>
        <path fill="#7a3519" d="M467 210a36 17 0 0 1 72 0z"/>
        <path d="M503 198V96" stroke="#2f3e33" stroke-width="5" stroke-linecap="round"/>
        <path fill="#2f3e33" d="M503 180c-22 2-36-11-36-28 20-2 36 10 36 28zM503 142c-17 2-28-8-28-22 16-2 28 8 28 22z"/>
        <path fill="#48614b" d="M503 168c2-20 18-32 36-30 0 18-14 32-36 30zM503 132c2-15 14-24 28-22 0 14-11 24-28 22z"/>
        <g fill="#f7f1e6"><circle cx="503" cy="72" r="12"/><circle cx="523" cy="84" r="12"/><circle cx="523" cy="106" r="12"/><circle cx="503" cy="118" r="12"/><circle cx="483" cy="106" r="12"/><circle cx="483" cy="84" r="12"/></g>
        <circle cx="503" cy="95" r="11" fill="#e9b98f"/>
      </svg>"""


def slug(t):
    t = unicodedata.normalize("NFKD", html.unescape(re.sub(r"<[^>]+>", "", t)))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def plano(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def medidor(n):
    return f'<span class="iv-medidor n{n}" aria-hidden="true"><i></i><i></i><i></i></span>'


def niveles_de(txt):
    """«Sólida (esketamina); prometedora (psilocibina)» -> [[3, 'esketamina'], [2, 'psilocibina']]"""
    out = []
    for parte in plano(txt).split(";"):
        p = parte.strip()
        n = next((k for k, (nom, _) in NIVELES.items() if p.lower().startswith(nom.lower())), 0)
        if n:
            out.append([n, p[len(NIVELES[n][0]):].strip(" ,()")])
        elif out:
            out[-1][1] = (out[-1][1] + "; " if out[-1][1] else "") + p
    assert out, f"nivel de evidencia sin reconocer: {txt}"
    return out


def pista(txt):
    """Trazo de cuatro tramos (fase 1, fase 2, fase 3, aprobación) a partir de la columna «Fase más avanzada»."""
    v, marcha = None, False
    for parte in plano(txt).lower().split(";"):
        if "en marcha" in parte:
            marcha = True
            parte = parte[:parte.index("(")] if "(" in parte else parte
        x = (4 if "aprobad" in parte else 3 if "fase 3" in parte else 1.5 if re.search(r"fase 1\s*[–-]\s*2", parte)
             else 2 if "fase 2" in parte else 1 if "fase 1" in parte else .5 if "piloto" in parte else None)
        if x is not None:
            v = x if v is None else max(v, x)
    if v is None:
        return '<span class="iv-pista sin" aria-hidden="true"><i></i><i></i><i></i><i></i></span>'
    celdas = []
    for k in range(4):
        lleno = max(0, min(1, v - k))
        cl = ' class="m"' if marcha and lleno == 0 and k < v + 1 else ' class="ap"' if k == 3 and lleno else ""
        celdas.append(f'<i{cl} style="--l:{lleno:g}"></i>')
    return f'<span class="iv-pista" aria-hidden="true">{"".join(celdas)}</span>'


def listas(t):
    """Listas del texto: con rótulo en negrita, filas con el rótulo a la izquierda; sin él, puntos."""
    def una(m):
        lis = re.findall(r"<li>(.*?)</li>", m.group(1), re.S)
        partes = [re.match(r"<strong>([^<]+?)[.:]</strong>\s*(.+)$", li.strip(), re.S) for li in lis]
        if all(partes):
            filas = "\n".join(f"<li><b>{p.group(1)}</b><p>{p.group(2)}</p></li>" for p in partes)
            return f'<ul class="iv-filas">\n{filas}\n</ul>'
        return '<ul class="iv-puntos">' + m.group(1) + "</ul>"
    return re.sub(r"<ul>(.*?)</ul>", una, t, flags=re.S)


def prosa(t):
    t = re.sub(r'<div class="s-destacado">(.*?)</div>', r'<aside class="iv-apunte" role="note">\1</aside>', t, flags=re.S)
    t = re.sub(r"<p>(<strong>Estado[^<]*:</strong>)", r'<p class="iv-estado">\1', t)
    t = re.sub(r"<p>(<strong>Límites[^<]*:</strong>)", r'<p class="iv-limites">\1', t)
    return listas(t)


def main():
    texto = TEXTO.read_text(encoding="utf-8")
    ms = list(re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', texto, re.S))
    antes_h2 = texto[:ms[0].start()]
    secs = {}
    for i, m in enumerate(ms):
        fin = ms[i + 1].start() if i + 1 < len(ms) else len(texto)
        secs[m.group(1)] = (m.group(2).strip(), texto[m.end():fin].strip())
    aviso = re.search(r'<div class="s-destacado">(.*?)</div>', antes_h2, re.S).group(1).strip()

    # --- la tabla de la evidencia: de aquí salen la pirámide, las fichas y los trazos
    cuerpo_ev = secs["estado-evidencia"][1]
    tabla = re.search(r"<table>(.*?)</table>", cuerpo_ev, re.S).group(1)
    cab = [plano(x) for x in re.findall(r"<th>(.*?)</th>", tabla, re.S)]
    lineas = []
    for fila in re.findall(r"<tr>(.*?)</tr>", tabla, re.S)[1:]:
        ind, sus, fase, niv = [c.strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", fila, re.S)]
        a = re.match(r'<a href="#([^"]+)">(.*?)</a>$', ind, re.S)
        lineas.append({"id": a.group(1), "nombre": a.group(2), "sus": sus, "fase": fase, "nivel": niv, "niveles": niveles_de(niv)})
    por_id = {l["id"]: l for l in lineas}

    def ficha(ancla):
        l = por_id[ancla]
        n = max(x[0] for x in l["niveles"])
        return (f'<dl class="iv-ficha"><div><dt>{cab[1]}</dt><dd>{l["sus"]}</dd></div>'
                f'<div><dt>{cab[2]}</dt><dd>{pista(l["fase"])}{l["fase"]}</dd></div>'
                f'<div><dt>{cab[3]}</dt><dd>{medidor(n)}{l["nivel"]}</dd></div></dl>')

    # --- portada
    n_refs = len(re.findall(r'<li id="ref-\d+">', secs["referencias"][1]))
    revisado = plano(re.search(r'<p class="s-revisado">(.*?)</p>', secs["referencias"][1], re.S).group(1)).rstrip(".")
    minutos = round(len(plano(texto).split()) / 210)
    portada = f"""<section class="iv-hero">
  <div class="ancho iv-hero-in">
    <div class="iv-hero-txt">
      <p class="mini iv-miga"><a href="../terapia/">Terapia</a> · Investigación</p>
      <h1>Investigación <i>terapéutica</i></h1>
      <p class="iv-entrada">{ENTRADA}</p>
      <dl class="iv-datos">
        <div><dt>Qué recoge</dt><dd>{len(lineas)} líneas de investigación, una a una</dd></div>
        <div><dt>Cómo se mide</dt><dd>Tres niveles de evidencia</dd></div>
        <div><dt>De dónde sale</dt><dd>{n_refs} estudios y documentos citados</dd></div>
      </dl>
      <p class="iv-fecha">{revisado} · Unos {minutos} minutos de lectura</p>
    </div>
    <div class="iv-hero-ilu" aria-hidden="true">
      {ILUSTRACION}
      <span class="iv-rotulo r1">{NIVELES[1][0]}</span>
      <span class="iv-rotulo r2">{NIVELES[2][0]}</span>
      <span class="iv-rotulo r3">{NIVELES[3][0]}</span>
    </div>
  </div>
</section>"""

    # --- de un vistazo: la pirámide de la evidencia
    pisos = {3: [], 2: [], 1: []}
    for l in lineas:
        for n, nota in l["niveles"]:
            pisos[n].append(f'<li><a href="#{l["id"]}">{l["nombre"]}' + (f"<small>{nota}</small>" if nota else "") + "</a></li>")
    assert len(pisos[1]) > len(pisos[2]) > len(pisos[3]), "la pirámide ya no es una pirámide: revisa la frase de «De un vistazo»"
    bloques = "\n".join(
        f'<div class="iv-piso n{n}"><div class="iv-piso-t"><svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">{ICO_NIVEL[n]}</svg>'
        f'<p><b>{NIVELES[n][0]}</b>{medidor(n)}<span>{NIVELES[n][1]}</span></p></div>\n<ul>{"".join(pisos[n])}</ul></div>' for n in (3, 2, 1))
    vistazo = f"""<section class="iv-vistazo">
  <div class="iv-vistazo-cab">
    <h2 id="de-un-vistazo">De un vistazo</h2>
    <p>En qué punto está cada línea de investigación. La mayoría sigue en la base de la pirámide. Los criterios y los matices, <a href="#estado-evidencia">más abajo</a>.</p>
  </div>
  <div class="iv-piramide">
{bloques}
  </div>
</section>"""

    # --- apartados
    def h3s(cuerpo):
        """[(título o None, html)] por cada <h3> (los que ya traen id lo conservan)."""
        tr = re.split(r"<h3(?: id=\"([^\"]+)\")?>(.*?)</h3>", cuerpo, flags=re.S)
        out = [(None, None, tr[0])]
        for i in range(1, len(tr), 3):
            out.append((tr[i] or slug(tr[i + 1]), tr[i + 1], tr[i + 2]))
        return out

    def intro(cuerpo):
        out = []
        for ancla, tit, cu in h3s(cuerpo):
            if tit is None:
                out.append(prosa(cu.strip()))
                continue
            cab3 = f'<h3 id="{ancla}">{tit}</h3>'
            if "terapia-asistida" in ancla:
                lis = [re.match(r"<strong>([^<]+?)\.</strong>\s*(.+)$", x.strip(), re.S) for x in re.findall(r"<li>(.*?)</li>", cu, re.S)]
                assert len(lis) == 3 and all(lis)
                pasos = "\n".join(f'<li><span class="num">{i}</span><b>{m.group(1)}</b><p>{m.group(2)}</p></li>' for i, m in enumerate(lis, 1))
                out.append(cab3 + "\n" + cu[:cu.index("<ul>")].strip() + f'\n<ol class="iv-pasos">\n{pasos}\n</ol>\n' + cu[cu.index("</ul>") + 5:].strip())
            elif "fases" in ancla:
                filas = [[c.strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", f, re.S)] for f in re.findall(r"<tr>(.*?)</tr>", cu, re.S)[1:]]
                # Los rótulos de las columnas siguen ahí para quien lee con lector de pantalla.
                rot = [plano(c) for c in re.findall(r"<th[^>]*>(.*?)</th>", cu, re.S)]
                assert len(rot) == 3, "cambia la tabla de fases: revisa los rótulos"
                puntos = [3, 8, 16, 0, 32]
                assert len(filas) == len(puntos), "cambia la tabla de fases: revisa «puntos»"
                etapas = []
                for (fase, pregunta, gente), k in zip(filas, puntos):
                    m = re.match(r"Fase (\d)", fase)
                    num = m.group(1) if m else '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M5 10.500l3.200 3.200L15 6.800"/></svg>'
                    quien = "" if plano(gente) in ("—", "-", "") else (
                        f'<p class="iv-gente"><span class="iv-puntitos" aria-hidden="true">{"<i></i>" * k}</span>'
                        f'<span class="solo-lectores">{rot[2]}: </span>{gente}</p>')
                    clase = "" if m else ' class="ap"'
                    etapas.append(f'<li{clase}><span class="num">{num}</span><b>{fase}</b>'
                                  f'<p><span class="solo-lectores">{rot[1]}: </span>{pregunta}</p>{quien}</li>')
                ini, fin = cu.index('<div class="s-tabla'), cu.index("</table></div>") + len("</table></div>")
                out.append(cab3 + "\n" + cu[:ini].strip() + f'\n<ol class="iv-fases">\n{chr(10).join(etapas)}\n</ol>\n' + cu[fin:].strip())
            elif "evidencia-todavia" in ancla:
                lis = [re.match(r"<strong>([^<]+?)\.</strong>\s*(.+)$", x.strip(), re.S) for x in re.findall(r"<li>(.*?)</li>", cu, re.S)]
                assert all(lis)
                ideas = "\n".join(f'<li><span class="n">{i}</span><b>{m.group(1)}</b><p>{m.group(2)}</p></li>' for i, m in enumerate(lis, 1))
                out.append(cab3 + f'\n<ol class="iv-ideas dos">\n{ideas}\n</ol>\n' + grafico() + cu[cu.index("</ul>") + 5:].strip())
            else:
                out.append(cab3 + "\n" + prosa(cu.strip()))
        return "\n\n".join(out)

    def grafico():
        for ancla, _, n, frase in ESTUDIOS:
            assert frase in plano(secs[ancla][1]), f"el texto de «{ancla}» ya no dice «{frase}»: revisa ESTUDIOS"
        tope = max(e[2] for e in ESTUDIOS)
        filas = "\n".join(
            f'<div class="fila"><a class="et" href="#{ANCLA_ESTUDIO.get(rot, ancla)}">{rot}</a><span class="barra"><i class="a" style="--v:{n / tope * 100:.1f}%"></i></span>'
            f'<span class="val">{n}</span></div>' for ancla, rot, n, _ in sorted(ESTUDIOS, key=lambda e: -e[2]))
        menos = sum(1 for e in ESTUDIOS if e[2] < 60)
        return (f'<figure class="iv-grafico iv-muestras">\n<figcaption>Cuántas personas participaron en {len(ESTUDIOS)} de los estudios que cita esta página</figcaption>\n'
                f'{filas}\n<p class="pie">Cada barra es un estudio. {menos} de los {len(ESTUDIOS)} tienen menos de 60 participantes.</p>\n</figure>\n')

    def evidencia(cuerpo):
        ini, fin = cuerpo.index("<ul>"), cuerpo.index("</ul>") + 5
        defs = [re.match(r"<strong>([^<]+?):</strong>\s*(.+)$", x.strip(), re.S) for x in re.findall(r"<li>(.*?)</li>", cuerpo[ini:fin], re.S)]
        assert len(defs) == 3 and all(defs)
        tarjetas = []
        for d in defs:
            n = next(k for k, (nom, _) in NIVELES.items() if nom == d.group(1))
            tarjetas.append(f'<li class="n{n}"><svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">{ICO_NIVEL[n]}</svg>'
                            f'<b>{d.group(1)}</b>{medidor(n)}<p>{d.group(2)}</p></li>')
        filas = "\n".join(
            f'<tr><th scope="row"><a href="#{l["id"]}">{l["nombre"]}</a></th><td data-label="{cab[1]}">{l["sus"]}</td>'
            f'<td data-label="{cab[2]}">{pista(l["fase"])}{l["fase"]}</td>'
            f'<td data-label="{cab[3]}">{medidor(max(x[0] for x in l["niveles"]))}{l["nivel"]}</td></tr>' for l in lineas)
        t_fin = cuerpo.index("</table></div>") + len("</table></div>")
        cabecera_tabla = "".join(f'<th scope="col">{c}</th>' for c in cab)
        return (cuerpo[:ini].strip() + f'\n<ul class="iv-niveles">\n{chr(10).join(tarjetas)}\n</ul>\n'
                '<p class="iv-leyenda"><span class="iv-pista" aria-hidden="true"><i style="--l:1"></i><i style="--l:1"></i><i style="--l:0"></i><i style="--l:0"></i></span>'
                "El trazo de cada fila tiene cuatro tramos: fase 1, fase 2, fase 3 y aprobación.</p>\n"
                f'<table class="iv-tabla">\n<thead><tr>{cabecera_tabla}</tr></thead>\n<tbody>\n{filas}\n</tbody>\n</table>\n'
                + re.sub(r"^<p>", '<p class="iv-nota">', cuerpo[t_fin:].strip()))

    def problema(ancla, cuerpo):
        out = []
        for a3, tit, cu in h3s(cuerpo):
            if tit is None:
                out.append((ficha(ancla) + "\n" if ancla in por_id else "") + prosa(cu.strip()))
            else:
                out.append(f'<h3 id="{a3}">{tit}</h3>\n' + (ficha(a3) + "\n" if a3 in por_id else "") + prosa(cu.strip()))
        return "\n\n".join(out)

    def participar(cuerpo):
        out = []
        for a3, tit, cu in h3s(cuerpo):
            if tit is None:
                out.append(prosa(cu.strip()))
            elif "donde-buscar" in a3:
                out.append(f'<h3 id="{a3}">{tit}</h3>\n' + prosa(cu.strip().replace("<ul>", '<ul class="iv-registros">', 1)))
            elif "criterios" in a3:
                lis = [re.match(r"<strong>([^<]+?):</strong>\s*(.+)$", x.strip(), re.S) for x in re.findall(r"<li>(.*?)</li>", cu, re.S)]
                assert len(lis) == 2 and all(lis)
                cajas = "".join(f'<div class="{c}"><b>{m.group(1)}</b><p>{m.group(2)}</p></div>' for c, m in zip(("si", "no"), lis))
                out.append(f'<h3 id="{a3}">{tit}</h3>\n' + cu[:cu.index("<ul>")].strip() + f'\n<div class="iv-compara iv-criterios">{cajas}</div>\n'
                           + prosa(cu[cu.index("</ul>") + 5:].strip()))
            elif "que-preguntar" in a3:
                out.append(f'<div class="iv-cuidado iv-preguntas">\n<h3 id="{a3}">{tit}</h3>\n' + cu.strip() + "\n</div>")
            else:
                out.append(f'<h3 id="{a3}">{tit}</h3>\n' + prosa(cu.strip()))
        return "\n\n".join(out)

    def senales(cuerpo):
        ini, fin = cuerpo.index("<ul>"), cuerpo.index("</ul>") + 5
        cola = cuerpo[fin:].strip()
        cola = re.sub(r"\b(112|024)\b", r'<a href="tel:\1">\1</a>', cola)
        cola = re.sub(r"^<p>", '<p class="iv-ayuda">', cola)
        return cuerpo[:ini].strip() + "\n" + cuerpo[ini:fin].replace("<ul>", '<ul class="iv-senales">', 1) + "\n" + cola

    partes_por_seccion = {p[3]: i for i, p in enumerate(PARTES)}
    bloques, grupos = [], []
    for ancla, (titulo, cuerpo) in secs.items():
        if ancla in partes_por_seccion:
            i = partes_por_seccion[ancla]
            pa, pt, pe, _, dib = PARTES[i]
            bloques.append(f'<div class="iv-parte p{i + 1}" id="{pa}">\n<div class="txt"><span class="num">Parte {i + 1}</span><p class="tit">{pt}</p><p>{pe}</p></div>\n'
                           f'<div class="ilu"><svg viewBox="0 0 320 180" aria-hidden="true" focusable="false">{dib}</svg></div>\n</div>')
            grupos.append((pa, pt, []))
        grupos[-1][2].append((ancla, INDICE.get(ancla, plano(titulo))))
        if ancla == "introduccion":
            dentro = intro(cuerpo)
        elif ancla == "estado-evidencia":
            dentro = evidencia(cuerpo)
        elif ancla == "participar":
            dentro = participar(cuerpo)
        elif ancla == "senales-alarma":
            dentro = senales(cuerpo)
        elif ancla == "preguntas-frecuentes":
            dentro = cuerpo.replace('class="s-faq"', 'class="iv-faq"')
        elif ancla == "referencias":
            dentro = (cuerpo.replace('class="s-refs"', 'class="iv-refs"').replace('class="s-revisado"', 'class="iv-nota"')
                      .replace('class="s-nota s-descargo"', 'class="iv-descargo"'))
        else:
            dentro = problema(ancla, cuerpo)
        cierre = " iv-cierre" if ancla == "referencias" else ""
        if ancla == "referencias":
            bloques.append("""<section class="iv-sec">
<h2 id="sigue-por-aqui">Sigue por aquí</h2>
<ul class="iv-sigue">
<li><a href="../terapia/"><b>Guías de terapia</b><span>Cómo se trabaja con cada medicina en un proceso terapéutico.</span></a></li>
<li><a href="../formaciones/"><b>Dónde formarse</b><span>Formaciones en terapia con psicodélicos de todo el mundo.</span></a></li>
<li><a href="../medicinas/"><b>Medicinas por familias</b><span>Un mapa de las plantas, hongos y moléculas, por su química y por cómo actúan.</span></a></li>
<li><a href="../biblioteca/"><b>Biblioteca</b><span>Más de 800 libros para leer a fondo.</span></a></li>
</ul>
</section>""")
        bloques.append(f'<section class="iv-sec{cierre}">\n<h2 id="{ancla}">{titulo}</h2>\n{dentro}\n</section>')

    items = ['<li><a href="#de-un-vistazo">De un vistazo</a></li>']
    for i, (pa, pt, hijos) in enumerate(grupos, 1):
        sub = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in hijos)
        items.append(f'<li class="grupo"><span class="num">{i}</span><a href="#{pa}">{pt}</a>\n<ol>{sub}</ol></li>')
    lista = "\n".join(items)

    principal = f"""<main id="contenido" class="iv">
<div class="iv-progreso" aria-hidden="true"><span></span></div>

{portada}

<div class="ancho">
  <aside class="iv-aviso" aria-label="Aviso">
    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 7.6v.2"/></svg>
    {aviso}
  </aside>

{vistazo}
</div>

<div class="ancho iv-guia">
<nav class="iv-indice" aria-label="Contenido de la página">
<strong>Contenido</strong>
<ol>
{lista}
</ol>
</nav>
<div class="iv-cuerpo">
<details class="iv-indice-movil s-toc-movil">
<summary>Contenido</summary>
<ol>
{lista}
</ol>
</details>

{(chr(10) * 2).join(bloques)}
</div>
</div>
</main>"""

    # --- marco de la página publicada: <head>, cabecera, pie y guiones
    s = PAG.read_text(encoding="utf-8")
    antes = s[:s.index("<main")]
    despues = s[s.index("</main>") + 7:]
    antes = re.sub(r'\n<link rel="stylesheet" href="\.\./terapia/[^>]*>', "", antes)
    antes = re.sub(r'<link rel="stylesheet" href="investigacion\.css[^>]*>', f'<link rel="stylesheet" href="investigacion.css?v={VERSION}">', antes)
    cursiva = '<link rel="preload" href="../fuentes/dm-serif-display-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>'
    if cursiva not in antes:
        antes = antes.replace('<link rel="stylesheet" href="../tierra.css', cursiva + '\n<link rel="stylesheet" href="../tierra.css', 1)
    assert f"investigacion.css?v={VERSION}" in antes
    despues = re.sub(r"\s*<script>(?:(?!</script>).)*?\.s-toc a(?:(?!</script>).)*?</script>", "", despues, count=1, flags=re.S)
    despues = re.sub(r'\n<script src="(?:\.\./terapia/terapia|investigacion)\.js[^>]*></script>', "", despues)
    despues = re.sub(r'(<script src="\.\./menu\.js[^>]*></script>)',
                     lambda m: m.group(1) + f'\n<script src="investigacion.js?v={VERSION}" defer></script>', despues, count=1)
    assert "investigacion.js" in despues
    pagina = aplicar(antes + principal + despues, "investigacion-terapeutica/index.html")[0]
    PAG.write_text(pagina, encoding="utf-8")
    print(f"docs/investigacion-terapeutica/index.html · {len(lineas)} líneas · {len(secs)} apartados · {n_refs} referencias · {len(pagina) // 1024} KB")


if __name__ == "__main__":
    main()
