#!/usr/bin/env python3
"""«Medicinas por familias» (docs/medicinas/index.html): la página entera.

  python3 scripts/medicinas/generar.py            escribe la página
  python3 scripts/medicinas/generar.py --fotos    rehace además los recortes de docs/medicinas/img/

El TEXTO vive en scripts/medicinas/texto.html, en HTML llano (h2, h3, p, listas, la tabla, las preguntas y las
referencias): ahí se corrige. Este guion le pone el diseño y no cambia ni una palabra. Sustituye a apertura.py.

Seña de la puerta «Guías de medicinas»: papel cuadriculado, símbolo y molécula, y un color por grupo
(teja, azul, verde). La página es un atlas:
  · portada de cuaderno con la tabla de las nueve familias;
  · «De un vistazo»: la tabla del texto, vuelta libro de cuentas;
  · una lámina por familia (número, acción principal y la molécula de una de sus guías) y, debajo, sus entradas.
    Cada entrada lleva una casilla con su símbolo: rellena si tiene guía, punteada si no. Las que tienen guía
    enseñan además su molécula. Al pie de cada entrada, sus fichas de la Enciclopedia y, si no hay guía, su página
    de Psiconáutica (los nombres de esos enlaces se leen del <h1> de cada página de destino);
  · fotos, solo de cuando en cuando: una figura numerada en seis de las familias (FOTOS). Créditos en /creditos/.

Qué va en este guion y no en el texto: el color y la molécula de cada familia (FAMILIAS), el símbolo y los enlaces
de cada entrada (ENTRADAS, por el título de su <h3>), las fotos (FOTOS) y los rótulos de la página.
Si se añade una entrada al texto, hay que darle su línea en ENTRADAS: el guion se para y lo dice.
El <head>, la cabecera y el pie se conservan de la página publicada (los pone scripts/cabecera.py).
"""
import html
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
from cabecera import MEDICINAS, aplicar  # noqa: E402

DOCS = RAIZ / "docs"
PAG = DOCS / "medicinas" / "index.html"
TEXTO = Path(__file__).with_name("texto.html")
VERSION = "20261127a"

ENTRADILLA = ("Un mapa de las plantas, hongos y moléculas que cambian la conciencia, agrupados por su química y por "
              "cómo actúan. Para ver de un vistazo qué comparten, en qué se diferencian y qué riesgos tiene cada familia.")
GRUPOS = [("f1", "Activan el receptor 5-HT2A"), ("f2", "Otros mecanismos"), ("f3", "Plantas y hongos")]

# ancla del <h2>: (nombre corto para la tabla y el índice, grupo de color, guía cuya molécula abre la lámina)
FAMILIAS = {
    "triptaminas": ("Triptaminas", "f1", "psilocibina"),
    "ergolinas": ("Ergolinas", "f1", "lsd"),
    "fenetilaminas": ("Fenetilaminas", "f1", "mescalina"),
    "empatogenos": ("Empatógenos", "f2", "mdma"),
    "disociativos": ("Disociativos", "f2", "ketamina"),
    "oneirogenos": ("Oneirógenos", "f2", "ibogaina"),
    "plantas-diversas": ("Plantas y hongos", "f3", "salvia-divinorum"),
    "delirantes": ("Delirantes", "f3", "datura"),
    "nuevas-moleculas": ("Nuevas moléculas", "f2", None),
}

# título del <h3>: (símbolo, guía o None, fichas de la Enciclopedia, página de Psiconáutica o None)
ENTRADAS = {
    "Psilocibina y setas psilocibes": ("Ps", "psilocibina", ["psilocibina", "mongui", "san-isidro"], None),
    "DMT": ("DMT", "dmt", ["dmt", "chacruna", "jurema"], None),
    "Ayahuasca": ("Ay", "ayahuasca", ["ayahuasca", "harmina-y-harmalina"], None),
    "5-MeO-DMT": ("5-MeO", "5-meo-dmt", ["5-meo-dmt", "sapo-de-sonora"], None),
    "4-AcO-DMT": ("4-AcO", "4-aco-dmt", ["4-aco-dmt"], None),
    "Bufotenina, yopo y cebil": ("Bu", None, ["bufotenina", "yopo", "cebil"], "bufotenin"),
    "Virola": ("Vi", None, ["epena"], None),
    "LSD": ("LSD", "lsd", ["lsd"], None),
    "LSA: semillas de Ipomoea y Argyreia": ("LSA", None, ["lsa", "gloria-de-la-manana", "rosa-lisergica"], "lsa"),
    "Cornezuelo": ("Co", None, ["cornezuelo"], "ergot"),
    "Mescalina: peyote y San Pedro": ("Me", "mescalina", ["mescalina", "peyote", "san-pedro"], None),
    "2C-B": ("2C-B", "2c-b", ["2c-b"], None),
    "La familia 2C": ("2C-x", None, [], "2c-x"),
    "DOx": ("DOx", None, [], "dox"),
    "MDMA": ("MDMA", "mdma", ["mdma"], None),
    "MDA": ("MDA", None, [], "mda"),
    "Nuevas moléculas en investigación": ("Nv", None, [], None),
    "Ketamina y esketamina": ("K", "ketamina", ["ketamina"], None),
    "Óxido nitroso": ("N₂O", None, [], "nitrous"),
    "DXM": ("DXM", None, [], "dextromethorphan"),
    "PCP (mención histórica)": ("PCP", None, [], "pcp"),
    "Ibogaína": ("Ib", "ibogaina", ["ibogaina", "iboga"], None),
    "Calea zacatechichi": ("Cl", None, ["hierba-de-los-suenos"], "calea-ternifolia"),
    "Silene capensis": ("Si", None, ["raiz-africana-de-los-suenos"], None),
    "Salvia divinorum": ("Sa", "salvia-divinorum", ["hierba-de-la-pastora", "salvinorina-a"], None),
    "Amanita muscaria": ("Am", "amanita-muscaria", ["amanita-muscaria", "muscimol"], None),
    "Cannabis": ("Ca", "cannabis", ["cannabis", "thc"], None),
    "Kanna": ("Kn", "kanna", ["kanna"], None),
    "Kratom": ("Kr", "kratom", ["kratom", "mitraginina"], None),
    "Kava": ("Kv", None, ["kava"], "kava"),
    "Cacao": ("Cc", "cacao", ["cacao"], None),
    "Tabaco, rapé y mapacho": ("Tb", "tabaco", ["tabaco", "mapacho", "rape"], None),
    "Sananga": ("Sn", None, ["sananga"], None),
    "Kambó": ("Kb", None, ["kambo"], None),
    "Ruda siria (harmala)": ("Rs", None, ["ruda-siria", "harmina-y-harmalina"], "peganum-harmala"),
    "Nenúfar azul": ("Nz", None, ["loto-azul"], "nymphaea-caerulea"),
    "Damiana": ("Dm", None, ["damiana"], None),
    "Datura": ("Da", "datura", ["estramonio", "toloache", "escopolamina"], None),
    "Brugmansia": ("Br", None, ["floripondio"], None),
    "Belladona": ("Be", None, ["belladona"], "atropa-belladonna"),
    "Mandrágora": ("Mn", None, ["mandragora"], "mandragora"),
    "Psicoplastógenos": ("Pp", None, [], None),
    "Análogos no alucinógenos": ("An", None, [], None),
    "Formulaciones de acción corta y nuevas vías": ("Fo", None, [], None),
}

# Fotos, de cuando en cuando: una figura en las familias que tienen plantas, hongos o animales con foto en la Enciclopedia.
# familia: (pie, [(archivo de docs/enciclopedia/img, caja x0,y0,x1,y1 en fracciones, nombre del recorte, rótulo,
#                  ficha de la Enciclopedia, texto alternativo)])
FOTOS = {
    "triptaminas": ("Un hongo, una planta y un animal: las triptaminas están repartidas por toda la naturaleza.", [
        ("idx-psilocybe.jpg", (0, .02, 1, .544), "mongui", "Mongui", "mongui",
         "Tres monguis de sombrero puntiagudo entre la hierba"),
        ("aya-chacruna.jpg", (0, 0, 1, 1), "chacruna", "Chacruna", "chacruna", "Hojas verdes y brillantes de chacruna"),
        ("idx-sapo.jpg", (.055, 0, .945, 1), "sapo", "Sapo de Sonora", "sapo-de-sonora", "Un sapo de Sonora visto de frente"),
    ]),
    "ergolinas": ("Gloria de la mañana (<em>Ipomoea tricolor</em>). Sus semillas contienen LSA.", [
        ("idx-ipomoea.jpg", (0, .17, 1, .75), "gloria", "Gloria de la mañana", "gloria-de-la-manana",
         "Flor azul de gloria de la mañana, en forma de campana"),
    ]),
    "fenetilaminas": ("Los dos cactus con mescalina más conocidos: el peyote y el San Pedro.", [
        ("pey-wirikuta.jpg", (0, 0, 1, 1), "peyote", "Peyote", "peyote", "Un grupo de peyotes redondos y grises a ras de suelo"),
        ("idx-sanpedro.jpg", (0, .05, 1, .6125), "san-pedro", "San Pedro", "san-pedro", "Columnas verdes de cactus San Pedro"),
    ]),
    "oneirogenos": ("Iboga (<em>Tabernanthe iboga</em>), el arbusto de África central de cuya raíz procede la ibogaína.", [
        ("idx-iboga.jpg", (0, .36, 1, .718), "iboga", "Iboga", "iboga", "Ramas de iboga con frutos alargados de color naranja"),
    ]),
    "plantas-diversas": ("Cuatro de las plantas y hongos de este grupo. Cada uno actúa a su manera.", [
        ("sal-flor.jpg", (0, 0, 1, 1), "salvia", "Salvia divinorum", "hierba-de-la-pastora",
         "Flor blanca y aterciopelada de Salvia divinorum, con el cáliz morado"),
        ("ama-hero.jpg", (.055, 0, .945, 1), "amanita", "Amanita muscaria", "amanita-muscaria",
         "Tres setas rojas con motas blancas en el suelo del bosque"),
        ("idx-cacao.jpg", (0, .125, 1, .875), "cacao", "Cacao", "cacao", "Fruto de cacao abierto, con la pulpa blanca a la vista"),
        ("idx-loto.jpg", (0, 0, 1, 1), "nenufar", "Nenúfar azul", "loto-azul", "Flor azul de nenúfar sobre hojas flotantes"),
    ]),
    "delirantes": ("Una datura en flor y una mandrágora en un grabado antiguo.", [
        ("idx-datura.jpg", (0, .1, 1, .85), "datura", "Datura", "toloache", "Flor blanca de datura, grande y en forma de trompeta"),
        ("idx-mandragora.jpg", (.04, .16, .96, .85), "mandragora", "Mandrágora", "mandragora",
         "Grabado antiguo de dos mandrágoras con la raíz en forma de cuerpo"),
    ]),
}
IMG = DOCS / "medicinas" / "img"

ICONOS = [  # reducción de riesgos, por orden
    '<circle cx="18" cy="24" r="10"/><circle cx="30" cy="24" r="10"/>',
    '<path d="M24 40c-9 0-15-6-15-15S15 9 24 9s15 6 15 15"/><path d="M24 31c-4 0-7-3-7-7s3-6 6-6 5 2 5 5-2 4-4 4"/>',
    '<path d="M24 39S9 30 9 19a8 8 0 0 1 15-4 8 8 0 0 1 15 4c0 11-15 20-15 20z"/>',
    '<path d="M19 8h10M21 8v11L11 36a3 3 0 0 0 3 4h20a3 3 0 0 0 3-4L27 19V8"/><path d="M16 30h16"/>',
    '<circle cx="17" cy="17" r="5"/><circle cx="32" cy="19" r="4"/><path d="M7 38c0-6 4-10 10-10s10 4 10 10M30 28c6 0 10 4 10 9"/>',
    '<path d="M11 37c0-16 8-26 26-26 0 16-8 26-26 26z"/><path d="M11 37l16-16"/>',
]
MOL_VACIA = ('<svg viewBox="0 0 260 200" aria-hidden="true" focusable="false"><g fill="none" stroke="currentColor" '
             'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="3 8">'
             '<path d="M70 62l40-23 40 23v46l-40 23-40-23z"/><path d="M150 62l44 14 0 46-44-14"/>'
             '<path d="M194 76l32-18M110 131v34M70 62L40 45"/></g></svg>')


def slug(t):
    t = unicodedata.normalize("NFKD", html.unescape(re.sub(r"<[^>]+>", "", t)))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def plano(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def h1_de(ruta):
    """Título (<h1>) de una página del sitio: da nombre a los enlaces de «más»."""
    f = DOCS / ruta / "index.html"
    assert f.is_file(), f"no existe {ruta}"
    m = re.search(r"<h1[^>]*>(.*?)</h1>", f.read_text(encoding="utf-8"), re.S)
    assert m, f"sin <h1>: {ruta}"
    return html.escape(plano(m.group(1)))


def notas(t):
    """Los avisos del texto (<div class="s-destacado">) pasan a nota de cuaderno."""
    return re.sub(r'<div class="s-destacado">(.*?)</div>', r'<aside class="mf-nota" role="note">\1</aside>', t, flags=re.S)


def secciones(texto):
    ms = list(re.finditer(r'<h2 id="([^"]+)">(.*?)</h2>', texto, re.S))
    out = {}
    for i, m in enumerate(ms):
        fin = ms[i + 1].start() if i + 1 < len(ms) else len(texto)
        out[m.group(1)] = (m.group(2).strip(), texto[m.end():fin].strip())
    return out


def recortes():
    from PIL import Image
    IMG.mkdir(exist_ok=True)
    for _, fotos in FOTOS.values():
        una = len(fotos) == 1
        for origen, (x0, y0, x1, y1), nombre, *_ in fotos:
            im = Image.open(DOCS / "enciclopedia" / "img" / origen).convert("RGB")
            w, h = im.size
            im = im.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)))
            ancho = min(im.width, 1280 if una else 720)
            im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
            im.save(IMG / f"{nombre}.webp", "WEBP", quality=80, method=6)
            print(f"  img/{nombre}.webp · {im.width}×{im.height} · {(IMG / (nombre + '.webp')).stat().st_size // 1024} KB")


def figura(fam, n):
    if fam not in FOTOS:
        return ""
    from PIL import Image
    pie, fotos = FOTOS[fam]
    celdas = []
    for _, _, nombre, rotulo, ficha, alt in fotos:
        w, h = Image.open(IMG / f"{nombre}.webp").size
        assert (DOCS / "enciclopedia" / ficha / "index.html").is_file(), ficha
        celdas.append(f'<a href="../enciclopedia/{ficha}/"><img src="img/{nombre}.webp" alt="{html.escape(alt)}" width="{w}" '
                      f'height="{h}" loading="lazy" decoding="async"><b>{rotulo}</b></a>')
    clase = {1: " una", 2: " dos", 3: " tres", 4: " cuatro"}[len(fotos)]
    return (f'<figure class="mf-fig{clase}">\n<div class="mf-fig-fotos">{"".join(celdas)}</div>\n'
            f'<figcaption><b>Fig. {n}</b>{pie} <a href="../creditos/">Créditos de las fotos</a></figcaption>\n</figure>\n')


def main():
    if "--fotos" in sys.argv or not IMG.is_dir():
        recortes()
    texto = TEXTO.read_text(encoding="utf-8")
    secs = secciones(texto)
    guias = {d: (m, n) for _, g in MEDICINAS for d, m, n in g}
    n_guias = len(guias)

    # --- la tabla «de un vistazo»: una fila por familia, en el mismo orden que los capítulos
    filas = re.findall(r"<tr>(.*?)</tr>", secs["resumen"][1], re.S)[1:]
    filas = [re.findall(r"<td[^>]*>(.*?)</td>", f, re.S) for f in filas]
    fams = []
    for ancla, (titulo, cuerpo) in secs.items():
        m = re.match(r"(\d+)\.\s*(.+)$", titulo, re.S)
        if not m:
            continue
        assert ancla in FAMILIAS, f"familia nueva sin datos en FAMILIAS: {ancla}"
        fams.append({"id": ancla, "num": int(m.group(1)), "nombre": m.group(2), "cuerpo": cuerpo,
                     "corto": FAMILIAS[ancla][0], "grupo": FAMILIAS[ancla][1], "mol": FAMILIAS[ancla][2]})
    assert len(fams) == len(filas) == len(FAMILIAS), (len(fams), len(filas))
    for f, (cat, ej, acc) in zip(fams, filas):
        f["fila"], f["ejemplos"], f["accion"] = cat.strip(), ej.strip(), acc.strip()

    # --- portada
    celdas = "".join(f'<a class="{f["grupo"]}" href="#{f["id"]}"><b>{f["num"]}</b><span>{f["corto"]}</span></a>' for f in fams)
    leyenda = "".join(f'<span class="{c}">{t}</span>' for c, t in GRUPOS)
    portada = f"""<section class="mf-portada">
<div class="ancho mf-portada-in">
<div class="mf-portada-txt">
<p class="mini mf-miga"><a href="../sustancias/">Medicinas</a> · Por familias</p>
<h1>Medicinas <em>por familias</em></h1>
<p class="mf-entradilla">{ENTRADILLA}</p>
<p class="mf-atajos"><a href="#resumen">Las familias de un vistazo</a><a href="#reduccion-de-riesgos">Reducción de riesgos</a><a href="../sustancias/">Las {n_guias} guías, una a una</a></p>
</div>
<div class="mf-tabla-caja">
<nav class="mf-tabla" aria-label="Las {len(fams)} familias">{celdas}</nav>
<p class="mf-leyenda">{leyenda}</p>
</div>
</div>
</section>"""

    # --- índice
    items = ['<li><a href="#introduccion">Qué entendemos por medicina</a></li>', '<li><a href="#resumen">De un vistazo</a></li>']
    items += [f'<li class="{f["grupo"]}{" sep" if i == 0 else ""}"><a href="#{f["id"]}"><b>{f["num"]}</b>{f["corto"]}</a></li>'
              for i, f in enumerate(fams)]
    items += ['<li class="sep"><a href="#reduccion-de-riesgos">Reducción de riesgos</a></li>',
              '<li><a href="#preguntas-frecuentes">Preguntas frecuentes</a></li>', '<li><a href="#referencias">Referencias</a></li>']
    lista = "\n".join(items)
    indice = f'<nav class="mf-indice" aria-label="Contenido de la página">\n<strong>Contenido</strong>\n<ol>\n{lista}\n</ol>\n</nav>'
    indice_movil = f'<details class="mf-indice-movil s-toc-movil">\n<summary>Contenido</summary>\n<ol>\n{lista}\n</ol>\n</details>'

    # --- qué entendemos por medicina: las dos primeras definiciones, como voces de diccionario
    titulo, cuerpo = secs["introduccion"]
    ps = re.findall(r"<p>.*?</p>", cuerpo, re.S)
    voces = [re.search(r"<strong>(.*?)</strong>", p) for p in ps[:2]]
    if len(ps) >= 3 and all(voces):
        defs = "".join(f'<div class="mf-voz"><span class="mf-voz-t" aria-hidden="true">{v.group(1)}</span>{p}</div>'
                       for v, p in zip(voces, ps[:2]))
        cuerpo = f'<div class="mf-voces">{defs}</div>\n' + "\n".join(ps[2:])
    intro = f'<section class="mf-sec mf-intro">\n<h2 id="introduccion">{titulo}</h2>\n{cuerpo}\n</section>'

    # --- de un vistazo (los rótulos de las columnas salen del texto, no de aquí)
    rot = [plano(c) for c in re.findall(r"<th[^>]*>(.*?)</th>", secs["resumen"][1], re.S)]
    if len(rot) != 3:
        sys.exit("La tabla «de un vistazo» ya no tiene tres columnas: revisa generar.py")
    lineas = "\n".join(
        f'<li class="{f["grupo"]}"><a href="#{f["id"]}"><b>{f["num"]}</b><span class="mf-v-nom">{f["fila"]}</span>'
        f'<span class="mf-v-ej"><small>{rot[1]}</small>{f["ejemplos"]}</span>'
        f'<span class="mf-v-acc"><small>{rot[2]}</small>{f["accion"]}</span></a></li>' for f in fams)
    vistazo = f"""<section class="mf-sec">
<h2 id="resumen">{secs["resumen"][0]}</h2>
<div class="mf-vistazo">
<p class="mf-v-cab" aria-hidden="true"><span>{rot[0]}</span><span>{rot[1]}</span><span>{rot[2]}</span></p>
<ol>
{lineas}
</ol>
</div>
<p class="mf-leyenda">{leyenda}</p>
</section>"""

    # --- las familias
    vistas, laminas, nfig = set(), [], 0
    for f in fams:
        trozos = re.split(r"<h3>(.*?)</h3>", f["cuerpo"], flags=re.S)
        entradas = []
        for tit, cu in zip(trozos[1::2], trozos[2::2]):
            clave = plano(tit)
            assert clave in ENTRADAS, f"entrada sin datos en ENTRADAS: «{clave}»"
            vistas.add(clave)
            sim, guia, enc, psi = ENTRADAS[clave]
            largo = len(sim)
            cl = " l3" if largo == 3 else " l4" if largo >= 4 else ""
            mas = []
            if enc:
                mas.append('<span class="mf-mas-g"><b>Enciclopedia</b>' + "".join(
                    f'<a href="../enciclopedia/{e}/">{h1_de("enciclopedia/" + e)}</a>' for e in enc) + "</span>")
            if psi and not guia:
                mas.append(f'<span class="mf-mas-g"><b>Psiconáutica</b><a href="../psiconautica/{psi}/">{h1_de("psiconautica/" + psi)}</a></span>')
            mas = f'\n<p class="mf-mas">{"".join(mas)}</p>' if mas else ""
            tarjeta = ""
            if guia:
                mol, nombre = guias[guia]
                tarjeta = (f'\n<a class="mf-e-guia" href="../sustancias/{guia}/"><span class="mf-e-fig"><img src="../sustancias/moleculas/{mol}.svg" '
                           f'alt="" width="260" height="200" loading="lazy" decoding="async"></span>'
                           f'<b>Guía completa<span class="mf-oculto"> de {html.escape(nombre)}</span></b></a>')
            entradas.append(f'<article class="mf-entrada{" con-guia" if guia else ""}">\n<span class="mf-sim{cl}" aria-hidden="true">{sim}</span>\n'
                            f'<div class="mf-e-txt">\n<h3 id="{slug(tit)}">{tit}</h3>\n{notas(cu.strip())}{mas}\n</div>{tarjeta}\n</article>')
        if f["mol"]:
            mol, nombre = guias[f["mol"]]
            lam = (f'<a class="mf-lamina-mol" href="../sustancias/{f["mol"]}/"><img src="../sustancias/moleculas/{mol}.svg" alt="" width="260" '
                   f'height="200" loading="lazy" decoding="async"><span><span class="mf-oculto">Guía de </span>{html.escape(nombre)}</span></a>')
        else:
            lam = f'<div class="mf-lamina-mol vacia">{MOL_VACIA}<span>En desarrollo</span></div>'
        fig = ""
        if f["id"] in FOTOS:
            nfig += 1
            fig = figura(f["id"], nfig)
        laminas.append(f"""<section class="mf-familia {f["grupo"]}">
<header class="mf-lamina">
<div class="mf-lamina-txt">
<p class="mf-lamina-n">Familia {f["num"]} de {len(fams)}</p>
<h2 id="{f["id"]}"><span class="mf-h-num">{f["num"]}<span class="mf-oculto">.</span></span> {f["nombre"]}</h2>
<p class="mf-accion"><span>Acción principal</span>{f["accion"]}</p>
</div>
{lam}
</header>
<div class="mf-fam-intro">
{notas(trozos[0].strip())}
</div>
{fig}<div class="mf-entradas">
{chr(10).join(entradas)}
</div>
</section>""")
    sobran = set(ENTRADAS) - vistas
    assert not sobran, f"en ENTRADAS hay títulos que ya no están en el texto: {sobran}"

    # --- reducción de riesgos
    titulo, cuerpo = secs["reduccion-de-riesgos"]
    lis = re.findall(r"<li>(.*?)</li>", cuerpo, re.S)
    assert len(lis) == len(ICONOS), "cambian las pautas de reducción de riesgos: revisa ICONOS"
    pautas = "\n".join(f'<li><svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">{ico}</svg><p>{li.strip()}</p></li>'
                       for ico, li in zip(ICONOS, lis))
    antes = cuerpo[:cuerpo.index("<ul>")].strip()
    despues = notas(cuerpo[cuerpo.index("</ul>") + 5:].strip())
    riesgos = (f'<section class="mf-sec mf-riesgos">\n<h2 id="reduccion-de-riesgos">{titulo}</h2>\n{antes}\n'
               f'<ul class="mf-pautas">\n{pautas}\n</ul>\n{despues}\n</section>')

    # --- preguntas, puertas y referencias
    titulo, cuerpo = secs["preguntas-frecuentes"]
    faq = f'<section class="mf-sec">\n<h2 id="preguntas-frecuentes">{titulo}</h2>\n{cuerpo.replace("s-faq", "mf-faq")}\n</section>'
    sigue = f"""<section class="mf-sec">
<h2 id="sigue-por-aqui">Sigue por aquí</h2>
<div class="mf-puertas">
<a class="p-guias" href="../sustancias/"><b>Todas las guías</b><span>Las {n_guias} medicinas, una a una: efectos, duración, riesgos y cuidados.</span></a>
<a class="p-enci" href="../enciclopedia/"><b>Enciclopedia de medicinas</b><span>Plantas, hongos y preparados: origen, territorio y cultura.</span></a>
<a class="p-inv" href="../investigacion-terapeutica/"><b>Investigación terapéutica</b><span>Qué se sabe de su uso en terapia y qué falta todavía por saber.</span></a>
</div>
</section>"""
    titulo, cuerpo = secs["referencias"]
    cuerpo = (cuerpo.replace('class="s-refs"', 'class="mf-refs"').replace('class="s-revisado"', 'class="mf-revisado"')
              .replace('class="s-nota s-descargo"', 'class="mf-descargo"'))
    refs = f'<section class="mf-sec">\n<h2 id="referencias">{titulo}</h2>\n{cuerpo}\n</section>'

    principal = f"""<main id="contenido" class="mf">
{portada}

<div class="ancho mf-guia">
{indice}
<div class="mf-cuerpo">
{indice_movil}
{intro}

{vistazo}

{chr(10).join(laminas)}

{riesgos}

{faq}

{sigue}

{refs}
</div>
</div>
</main>
<script>/* índice: marca la familia que se está leyendo */
(function(){{var l=document.querySelectorAll('.mf-indice a');if(!l.length||!('IntersectionObserver' in window))return;
var m={{}};l.forEach(function(a){{m[a.getAttribute('href').slice(1)]=a}});
var o=new IntersectionObserver(function(es){{es.forEach(function(e){{if(!e.isIntersecting)return;var a=m[e.target.id];if(!a)return;l.forEach(function(x){{x.classList.remove('activo');x.removeAttribute('aria-current')}});a.classList.add('activo');a.setAttribute('aria-current','location')}})}},{{rootMargin:'-150px 0px -66% 0px'}});
Object.keys(m).forEach(function(id){{var h=document.getElementById(id);if(h)o.observe(h)}});
var d=document.querySelector('.mf-indice-movil');if(d)d.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{d.open=false}})}});}})();
</script>"""

    # --- marco de la página publicada: <head>, cabecera, pie y guiones
    s = PAG.read_text(encoding="utf-8")
    antes = s[:s.index("<main")]
    despues = s[s.index("</main>") + 7:]
    despues = re.sub(r"\s*<script>(?:(?!</script>).)*?(?:\.s-toc a|\.mf-indice a)(?:(?!</script>).)*?</script>", "", despues, count=1, flags=re.S)
    antes = re.sub(r'<link rel="stylesheet" href="medicinas\.css[^>]*>', f'<link rel="stylesheet" href="medicinas.css?v={VERSION}">', antes)
    assert f"medicinas.css?v={VERSION}" in antes
    pagina = aplicar(antes + principal + despues, "medicinas/index.html")[0]
    PAG.write_text(pagina, encoding="utf-8")
    print(f"docs/medicinas/index.html · {len(fams)} familias · {len(vistas)} entradas · {nfig} figuras · {len(pagina) // 1024} KB")


if __name__ == "__main__":
    main()
