#!/usr/bin/env python3
"""Página «Todas las guías» (docs/sustancias/index.html).

  python3 scripts/guias/generar.py            escribe la página
  python3 scripts/guias/generar.py --fotos    además rehace los recortes de docs/sustancias/img/ (necesita Pillow)

De dónde sale cada cosa:
- Las guías y sus familias: MEDICINAS, en scripts/cabecera.py (las mismas del menú).
- Familia, vía y duración de cada tarjeta: se leen de la ficha de cada guía publicada
  (docs/sustancias/<guía>/index.html, caja `s-ficha-mol`). Aquí no se escribe ninguna cifra.
- El esquema «Cuánto dura cada una» necesita la duración en minutos: está en DURA, copiada a mano
  de esa misma ficha. Si cambia la duración de una guía, hay que cambiarla también ahí.
- El texto largo (qué son, cómo se usan, tipos, riesgos, si algo va mal, preguntas): scripts/guias/texto.html.
- Cabecera, pie y <head>: se conservan los de la página publicada (la cabecera la escribe scripts/cabecera.py).
- Las tarjetas no llevan fotos: la seña de las guías es la molécula y su símbolo (SIMBOLOS). Fotos, solo de cuando en cuando
  (FOTOS y FRANJA): una franja en esta página y una foto dentro del texto de algunas guías. Créditos en /creditos/.
"""
import html
import math
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from cabecera import MEDICINAS  # noqa: E402

DOCS = RAIZ / "docs"
PAG = DOCS / "sustancias" / "index.html"
VERSION = "20261125c"

ANCLAS = ["clasicos", "otras", "plantas"]
ENTRADILLAS = [
    "Los que dieron nombre a la palabra: las setas, el LSD, los cactus con mescalina, la DMT y sus parientes.",
    "Empatógenos, disociativos, la ibogaína y dos moléculas de laboratorio emparentadas con los clásicos.",
    "Plantas y hongos de acción muy distinta entre sí. Varias no son psicodélicos: cada guía explica qué es y qué cuidados pide.",
]

# símbolo de cada guía, para la tabla de la apertura y la esquina de su ficha (como en una tabla de elementos)
SIMBOLOS = {
    "psilocibina": "Ps", "lsd": "LSD", "mescalina": "Me", "dmt": "DMT", "ayahuasca": "Ay", "5-meo-dmt": "5-MeO",
    "mdma": "MDMA", "ketamina": "K", "ibogaina": "Ib", "2c-b": "2C-B", "4-aco-dmt": "4-AcO",
    "amanita-muscaria": "Am", "salvia-divinorum": "Sa", "cannabis": "Ca", "kanna": "Kn", "kratom": "Kr",
    "datura": "Da", "cacao": "Cc", "tabaco": "Tb", "microdosis": "μ",
}
# Fotos, de cuando en cuando (25-11-2026): una dentro del texto de la guía cuando la medicina es una planta, un hongo
# o un animal, y una franja en «Todas las guías». Nunca en las tarjetas (ahí, solo molécula).
# guía: (origen en docs/enciclopedia/img, caja x0,y0,x1,y1 en fracciones, pie de foto)
FOTOS = {
    "psilocibina":      ("idx-psilocybe.jpg", (0.00, 0.03, 1.00, 0.47), "Monguis (<em>Psilocybe semilanceata</em>), una de las setas de psilocibina de los prados europeos."),
    "mescalina":        ("idx-peyote.jpg",    (0.00, 0.10, 1.00, 0.86), "Peyote (<em>Lophophora williamsii</em>) en flor."),
    "dmt":              ("aya-chacruna.jpg",  (0.00, 0.12, 1.00, 0.88), "Hojas de chacruna (<em>Psychotria viridis</em>), una de las plantas que contienen DMT."),
    "ayahuasca":        ("aya-liana.jpg",     (0.00, 0.08, 1.00, 0.92), "Tallo de la liana de la ayahuasca (<em>Banisteriopsis caapi</em>)."),
    "5-meo-dmt":        ("idx-sapo.jpg",      (0.00, 0.08, 1.00, 0.92), "Sapo del desierto de Sonora (<em>Incilius alvarius</em>)."),
    "ibogaina":         ("idx-iboga.jpg",     (0.00, 0.30, 1.00, 0.68), "Arbusto de iboga (<em>Tabernanthe iboga</em>) con frutos."),
    "amanita-muscaria": ("ama-hero.jpg",      (0.00, 0.10, 1.00, 0.94), "Matamoscas (<em>Amanita muscaria</em>) en el bosque."),
    "salvia-divinorum": ("idx-salvia.jpg",    (0.00, 0.08, 1.00, 0.93), "Flor de <em>Salvia divinorum</em>."),
    "datura":           ("idx-datura.jpg",    (0.00, 0.20, 1.00, 0.76), "Flor de <em>Datura inoxia</em>."),
    "cacao":            ("idx-cacao.jpg",     (0.00, 0.20, 1.00, 0.76), "Fruto de cacao (<em>Theobroma cacao</em>) abierto."),
    "tabaco":           ("idx-tabaco.jpg",    (0.00, 0.08, 1.00, 0.92), "Tabaco rústico o mapacho (<em>Nicotiana rustica</em>) en flor."),
}
# franja de «Todas las guías»: (ficha de la Enciclopedia, origen, caja, nombre)
FRANJA = [
    ("mongui", "idx-psilocybe.jpg", (0.00, 0.00, 1.00, 0.88), "Mongui"),
    ("peyote", "pey-flor.jpg", (0.26, 0.00, 0.80, 1.00), "Peyote"),
    ("ayahuasca", "aya-flores.jpg", (0.00, 0.00, 1.00, 1.00), "Ayahuasca"),
    ("iboga", "idx-iboga.jpg", (0.00, 0.10, 1.00, 0.95), "Iboga"),
    ("hierba-de-la-pastora", "sal-hero.jpg", (0.20, 0.00, 0.80, 1.00), "Hierba de la pastora"),
    ("cacao", "idx-cacao.jpg", (0.10, 0.00, 0.90, 1.00), "Cacao"),
]

NOMBRES_CORTOS = {"psilocibina": "Psilocibina", "mescalina": "Mescalina", "amanita-muscaria": "Amanita", "salvia-divinorum": "Salvia"}

# duración en minutos para el esquema: (mínimo, máximo, «hasta» o None, abierta por arriba)
DURA = {
    "dmt": (5, 20, None, False), "salvia-divinorum": (5, 15, 60, False), "5-meo-dmt": (15, 45, None, False),
    "ketamina": (60, 120, None, False), "kanna": (60, 180, None, False), "cacao": (120, 240, None, False),
    "kratom": (120, 300, None, False), "cannabis": (120, 480, None, False), "mdma": (180, 360, None, False),
    "4-aco-dmt": (240, 360, None, False), "psilocibina": (240, 360, 480, False), "ayahuasca": (240, 360, None, True),
    "2c-b": (240, 480, None, False), "amanita-muscaria": (360, 600, None, True), "lsd": (480, 720, None, False),
    "mescalina": (480, 720, 840, False), "ibogaina": (1440, 2160, None, False), "datura": (1440, 2880, None, True),
}
T0, T1 = 4, 3600            # el eje va de 4 minutos a 60 horas, en escala logarítmica
MARCAS = [(5, "5 min"), (15, "15 min"), (60, "1 h"), (240, "4 h"), (720, "12 h"), (1440, "24 h"), (2880, "48 h")]


def x(minutos):
    return round(100 * math.log(minutos / T0) / math.log(T1 / T0), 2)


def limpio(t):
    t = re.sub(r"<sup>.*?</sup>", "", t, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def sin_acentos(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def leer_guia(slug):
    s = (DOCS / "sustancias" / slug / "index.html").read_text(encoding="utf-8")
    caja = re.search(r'<aside class="s-ficha-mol">.*?</aside>', s, re.S).group(0)
    datos = {limpio(a).rstrip(":"): limpio(b) for a, b in re.findall(r"<strong>([^<]*:)</strong>\s*(?:<span>)?([^<·]*)", caja)}
    alias = limpio(re.search(r'<p class="s-alias[^"]*">(.*?)</p>', s, re.S).group(1)).strip("()")
    familia = datos.get("Familia") or datos.get("Tipo") or ""
    corta = re.split(r"[(;]", familia)[0].strip()
    corta = corta[:1].upper() + corta[1:]
    dur = datos.get("Duración", "")
    m = re.match(r"[\d\s–-]+(?:min|h)\b", dur)
    dur_corta = m.group(0).strip() if m else re.split(r"[,(;]", dur)[0].strip()
    return {"alias": alias, "familia": corta, "familia_larga": familia, "dur": dur, "dur_corta": dur_corta,
            "via": datos.get("Vía habitual", ""), "inicio": datos.get("Inicio", "")}


def creditos():
    """autor (con enlace) y licencia de cada foto de origen, leídos de CREDITOS.md"""
    out = {}
    for fila in (RAIZ / "CREDITOS.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| `docs/enciclopedia/img/([^`]+)` \|[^|]*\| (.*?) · \[Wikimedia Commons\]\((.*?)\) \| ([^|]+) \|", fila)
        if m:
            out[m.group(1)] = (re.sub(r"\[\d+\]", "", m.group(2)).strip(), m.group(3), m.group(4).strip())
    return out


def hacer_fotos():
    """recortes de docs/sustancias/img/ (necesita Pillow): 16:9 para el texto de las guías y 4:5 para la franja"""
    from PIL import Image
    origen = DOCS / "enciclopedia" / "img"
    salida = DOCS / "sustancias" / "img"
    salida.mkdir(exist_ok=True)

    def recorte(nombre, fuente, caja, ancho, proporcion, calidad=74):
        im = Image.open(origen / fuente).convert("RGB")
        w, h = im.size
        x0, y0, x1, y1 = caja
        im = im.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)))
        w, h = im.size
        if w / h > proporcion:
            n = round(h * proporcion); im = im.crop(((w - n) // 2, 0, (w - n) // 2 + n, h))
        else:
            n = round(w / proporcion); im = im.crop((0, (h - n) // 2, w, (h - n) // 2 + n))
        if im.width > ancho:
            im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
        im.save(salida / nombre, "WEBP", quality=calidad, method=6)
        print(f"{nombre:30s} {im.width}x{im.height} {(salida / nombre).stat().st_size // 1024} KB")

    for slug, (fuente, caja, _) in FOTOS.items():
        recorte(slug + ".webp", fuente, caja, 880, 16 / 9)
    for slug, fuente, caja, _ in FRANJA:
        recorte(f"franja-{slug}.webp", fuente, caja, 400, 4 / 5)


RELOJ = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"></circle><path d="M12 7.5V12l3 2"></path></svg>'
LUPA = '<svg class="ico peq" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg>'


def tarjeta(slug, mol, nombre, g):
    e = html.escape
    busca = sin_acentos(" ".join([nombre, g["alias"], g["familia_larga"], slug]))
    fig = f'<span class="g-fig"><img class="g-mol" src="moleculas/{mol}.svg" alt="" width="260" height="200" loading="lazy" decoding="async"><i class="g-sim" aria-hidden="true">{SIMBOLOS[slug]}</i></span>'
    dur = f'<span class="g-dur">{RELOJ}{e(g["dur_corta"])}</span>' if g["dur_corta"] else ""
    return (f'<li><a class="g-guia" href="{slug}/" data-b="{e(busca)}">{fig}'
            f'<span class="g-txt"><b>{e(nombre)}</b><small>{e(g["alias"])}</small></span>'
            f'<span class="g-datos"><span>{e(g["familia"])}</span>{dur}</span></a></li>')


def construir():
    actual = PAG.read_text(encoding="utf-8")
    cab = re.search(r'<header class="cabecera".*?</header>', actual, re.S).group(0)
    pie = re.search(r'<footer class="pie.*?</footer>', actual, re.S).group(0)
    cabeza = actual[:actual.index("</head>")]
    cabeza = re.sub(r'\n<link rel="stylesheet" href="(\.\./enciclopedia/enciclopedia\.css|guias\.css)[^>]*>', "", cabeza)
    cabeza = re.sub(r'\n<link rel="preload" href="(img/orb-1\.webp|\.\./fuentes/dm-serif-display-latin-400-italic\.woff2)"[^>]*>', "", cabeza)
    css_enc = re.search(r'enciclopedia\.css\?v=[0-9a-z]+', (DOCS / "enciclopedia" / "index.html").read_text(encoding="utf-8"))
    cabeza = cabeza.replace('<link rel="stylesheet" href="../tierra.css',
                            '<link rel="preload" href="../fuentes/dm-serif-display-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>\n'
                            '<link rel="stylesheet" href="../tierra.css')
    cabeza += (f'<link rel="stylesheet" href="../enciclopedia/{css_enc.group(0) if css_enc else "enciclopedia.css"}">\n'
               f'<link rel="stylesheet" href="guias.css?v={VERSION}">\n')

    guias, familias = {}, []
    for i, (titulo, lista) in enumerate(MEDICINAS):
        tarjetas = []
        for slug, mol, nombre in lista:
            guias[slug] = dict(leer_guia(slug), nombre=nombre, mol=mol, fam=i)
            tarjetas.append(tarjeta(slug, mol, nombre, guias[slug]))
        familias.append(f'<div class="g-familia f{i + 1}" id="{ANCLAS[i]}"><div class="g-fam-cab"><h3>{titulo}</h3>'
                        f'<p>{ENTRADILLAS[i]}</p></div>\n<ul class="g-rejilla">\n' + "\n".join(tarjetas) + "\n</ul></div>")
    n = len(guias)

    # esquema de duraciones, de la más breve a la más larga
    filas = []
    for slug in sorted(DURA, key=lambda s: (DURA[s][1], DURA[s][0])):
        a, b, hasta, abierta = DURA[slug]
        g = guias[slug]
        extra = ""
        if hasta:
            extra = f'<i class="hasta" style="--a:{x(b)};--b:{x(hasta)}"></i>'
        elif abierta:
            extra = f'<i class="mas" style="--a:{x(b)}"></i>'
        filas.append(f'<li class="f{g["fam"] + 1}"><a href="{slug}/">{html.escape(g["nombre"])}</a>'
                     f'<span class="g-pista"><i style="--a:{x(a)};--b:{x(b)}"></i>{extra}</span>'
                     f'<span class="g-cuanto">{html.escape(g["dur"])}</span></li>')
    vars_marcas = ";".join(f"--t{i}:{x(m)}" for i, (m, _) in enumerate(MARCAS, 1))
    marcas = "".join(f'<span style="--a:{x(m)}">{t}</span>' for m, t in MARCAS)
    sin_dato = [g["nombre"] for s, g in guias.items() if s not in DURA]

    # tabla de la apertura: una celda por guía, una fila por familia
    celdas = []
    for i, (_, lista) in enumerate(MEDICINAS):
        for j, (slug, _, nombre) in enumerate(lista):
            g = guias[slug]
            sim = SIMBOLOS[slug]
            corto = NOMBRES_CORTOS.get(slug, nombre)
            nueva = " g-fila" if j == 0 else ""
            celdas.append(f'<a class="f{i + 1} l{min(len(sim), 4)}{nueva}" href="{slug}/" aria-label="{html.escape(nombre)}">'
                          f'<small>{html.escape(g["dur_corta"])}</small><b>{sim}</b><span>{html.escape(corto)}</span></a>')
    tabla = "".join(celdas)

    franja = "".join(f'<a href="../enciclopedia/{slug}/"><img src="img/franja-{slug}.webp" alt="" width="400" height="500" loading="lazy" decoding="async"><b>{nombre}</b></a>'
                     for slug, _, _, nombre in FRANJA)

    texto = (RAIZ / "scripts" / "guias" / "texto.html").read_text(encoding="utf-8").strip()

    principal = f"""<main id="contenido">
<div class="enc gui">
<section class="e-portada"><div class="ancho e-portada-in">
<div><p class="etq oro">Medicinas · Guías</p><h1>Medicinas psicodélicas, <em>guía a guía</em></h1>
<p class="e-intro">Qué son, cómo actúan, qué dice la investigación y cómo reducir riesgos. En español, sin alarmismo y sin idealizarlas.</p>
<label class="e-busca">{LUPA}<input type="search" id="g-busca" aria-label="Buscar una guía por nombre" placeholder="Setas, ácido, yagé, MDMA…" autocomplete="off"></label>
<p class="e-atajos">Ir a <a href="#clasicos">Psicodélicos clásicos</a><a href="#otras">Otras medicinas</a><a href="#plantas">Plantas y hongos</a><a href="#duracion">Cuánto dura cada una</a></p></div>
<nav class="g-tabla" aria-label="Las guías, de un vistazo">{tabla}<p class="g-tabla-pie"><span class="f1">Psicodélicos clásicos</span><span class="f2">Otras medicinas</span><span class="f3">Plantas y hongos</span></p></nav>
</div></section>

<section class="e-sec ancho" id="guias">
<div class="e-cab"><div><h2>Las {n} guías</h2></div><p class="nota">Todas siguen el mismo orden: qué es, cómo actúa, la experiencia, interacciones, quién no debería, cómo reducir riesgos, investigación e historia.</p></div>
<p class="g-vacio" id="g-vacio" hidden>Ninguna guía se llama así. Prueba en el <a id="g-general" href="../buscar/">buscador de toda la web</a>.</p>
{chr(10).join(familias)}
</section>

<section class="e-sec ancho g-duracion" id="duracion">
<div class="e-cab"><div><h2>Cuánto dura cada una</h2></div><p class="nota">De los minutos de la DMT a los dos días de la datura. Son tiempos orientativos, tomados de cada guía: cambian con la dosis, la vía y la persona.</p></div>
<div class="g-esquema" style="{vars_marcas}">
<p class="g-leyenda"><span class="f1">Psicodélicos clásicos</span><span class="f2">Otras medicinas</span><span class="f3">Plantas y hongos</span></p>
<div class="g-eje" aria-hidden="true">{marcas}</div>
<ol class="g-filas">
{chr(10).join(filas)}
</ol>
<p class="g-nota-esquema">El eje no es regular: cada marca vale varias veces la anterior, para que quepan en la misma línea cinco minutos y dos días. La barra clara indica hasta dónde puede alargarse.{" Sin duración en su guía: " + ", ".join(sin_dato) + "." if sin_dato else ""}</p>
</div>
</section>

<section class="e-sec ancho" id="plantas-de-cerca">
<div class="e-cab"><div><h2>Las plantas, de cerca</h2></div><p class="nota">Varias de estas medicinas son una planta, un hongo o un animal antes que una molécula. Su retrato, su territorio y su historia están en la <a href="../enciclopedia/">Enciclopedia</a>.</p></div>
<div class="g-franja">{franja}</div>
</section>

<section class="e-sec ancho" id="mas">
<div class="e-cab"><div><h2>Otras maneras de entrar</h2></div></div>
<div class="g-puertas">
<a href="microdosis/"><b>Microdosis</b><span>Qué es, qué se sabe y qué no. Sin cifras ni pautas.</span></a>
<a href="../medicinas/"><b>Medicinas por familias</b><span>Triptaminas, fenetilaminas, disociativos y el resto, en un solo artículo.</span></a>
<a href="../terapia/"><b>Guías de terapia</b><span>Cómo es un proceso terapéutico con cada medicina, según la investigación.</span></a>
</div>
<nav class="g-indice" aria-label="En esta página"><b>Y debajo, para situarse</b><a href="#que-son">¿Qué son?</a><a href="#usos">¿Cómo se usan?</a><a href="#tipos">Tipos</a><a href="#riesgos">Riesgos</a><a href="#si-algo-va-mal">Si algo va mal</a><a href="#preguntas">Preguntas frecuentes</a></nav>
</section>
</div>

<div class="guia-cuerpo g-leer">
<section class="s-intro">
<div class="s-col">
{texto}
<p class="s-solo-impresion">Dirección canónica: https://apder.org/sustancias/</p>
</div>
<div class="s-espacio"></div>
</section>
</div>
</main>
<script>
(function(){{var c=document.getElementById('g-busca');if(!c)return;
var t=[].slice.call(document.querySelectorAll('.g-guia')),f=[].slice.call(document.querySelectorAll('.g-familia')),v=document.getElementById('g-vacio'),g=document.getElementById('g-general');
function n(s){{return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').trim()}}
function filtra(){{var q=n(c.value),hay=0;
t.forEach(function(a){{var ok=!q||a.getAttribute('data-b').indexOf(q)>-1;a.parentNode.hidden=!ok;if(ok)hay++}});
f.forEach(function(d){{d.hidden=!d.querySelector('li:not([hidden])')}});
v.hidden=hay>0;if(g)g.href='../buscar/'+(q?'?q='+encodeURIComponent(c.value.trim()):'')}}
c.addEventListener('input',filtra);
c.addEventListener('keydown',function(e){{if(e.key==='Enter'){{var p=document.querySelector('.g-rejilla li:not([hidden]) .g-guia');if(p&&c.value.trim()){{e.preventDefault();p.focus()}}}}}});
filtra()}})();
</script>
<script src="../menu.js?v=20261123a" defer></script>
"""
    PAG.write_text(cabeza + "</head>\n<body class=\"guia\">\n<a class=\"saltar\" href=\"#contenido\">Saltar al contenido</a>\n"
                   + cab + "\n\n" + principal + "\n" + pie + "\n<script src=\"../tierra.js\" defer></script>\n</body>\n</html>\n",
                   encoding="utf-8")
    print(f"docs/sustancias/index.html · {n} guías · {len(filas)} en el esquema de duración")


if __name__ == "__main__":
    if "--fotos" in sys.argv:
        hacer_fotos()
    construir()
