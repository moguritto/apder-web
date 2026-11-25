#!/usr/bin/env python3
"""Portada de la Biblioteca (docs/biblioteca/index.html).

  python3 scripts/biblioteca/portada.py

Rehace la portada alrededor del catálogo que ya está publicado, sin tocar los libros:
- Se conservan tal cual la lista de libros (`ul#b-lista`) y el árbol de filtros (`aside#b-filtros`).
  Los libros no se editan aquí: cada uno tiene su `<li>` en esta página y su ficha en `docs/biblioteca/<libro>/`.
- Se escriben de nuevo la apertura, «Por dónde empezar» (RUTAS), las entradas por tema, medicina e idioma
  (con recuentos contados sobre la lista) y el marco del catálogo.
- Estilos en `docs/biblioteca/biblioteca.css` y código en `docs/biblioteca/biblioteca.js` (compartidos con las fichas).

Se puede lanzar las veces que haga falta: parte siempre de la lista y los filtros de la página publicada.
"""
import html
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parent.parent.parent
DOCS = RAIZ / "docs"
PAG = DOCS / "biblioteca" / "index.html"
VERSION = "20261125b"

# abanico de portadas de la apertura (deben tener imagen de portada)
ABANICO = ["vida-de-maria-sabina", "the-psychedelic-explorer-s-guide", "how-to-change-your-mind",
           "historia-general-de-las-drogas", "psicodelicos-y-salud-mental"]

# rutas de lectura: (título, entradilla, [(libro, por qué)])
RUTAS = [
    ("Para empezar", "Tres puertas de entrada, dos de ellas en español.", [
        ("how-to-change-your-mind", "Una introducción periodística a la investigación y las experiencias psicodélicas."),
        ("psicodelicos-y-salud-mental", "Una revisión divulgativa de las bases cerebrales y las aplicaciones terapéuticas."),
        ("tu-cerebro-con-psicodelicos", "Una aproximación a la farmacología y la neurociencia."),
    ]),
    ("Ciencia y clínica", "De los primeros estudios a la investigación de hoy.", [
        ("the-varieties-of-psychedelic-experience", "Una obra histórica sobre las experiencias psicodélicas."),
        ("lsd-psychotherapy", "Una obra de Stanislav Grof sobre psicoterapia e investigación."),
        ("psicodelicos-y-salud-mental", "Una mirada actual a la investigación en salud mental."),
    ]),
    ("Integración y acompañamiento", "Para quien prepara, acompaña o integra.", [
        ("integracion-psiquedelica", "Una guía sobre la integración en psicoterapia."),
        ("the-psychedelic-explorer-s-guide", "Una introducción a la preparación y el acompañamiento."),
        ("the-psychedelic-experience", "Una obra histórica inspirada en el Bardo Thödol."),
    ]),
    ("Historia y tradiciones", "De Eleusis a la Amazonía.", [
        ("the-road-to-eleusis", "Una propuesta sobre los misterios de Eleusis."),
        ("how-to-change-your-mind", "Un recorrido por la historia reciente de la investigación."),
        ("the-yage-letters", "Correspondencia sobre los viajes amazónicos de sus autores."),
    ]),
]

LUPA = '<svg class="ico peq" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"></circle><path d="M16 16l4 4"></path></svg>'


def libros(lista):
    out = {}
    for li in re.findall(r'<li class="b-libro.*?</li>', lista, re.S):
        d = dict(re.findall(r'data-(\w+)="([^"]*)"', li))
        d = {k: html.unescape(v) for k, v in d.items()}
        d["slug"] = re.search(r'href="([^"/]+)/"', li).group(1)
        m = re.search(r'<a class="bx-portada" href="[^"]+"[^>]*?(style="[^"]*")>(.*?)</a>', li, re.S)
        d["estilo"], d["dentro"] = m.group(1), m.group(2)
        d["img"] = "<img" in d["dentro"]
        d["tit"] = html.unescape(re.sub(r"<[^>]+>", "", re.search(r'<p class="b-tit">(.*?)</p>', li, re.S).group(1)))
        d["meta"] = html.unescape(re.sub(r"<[^>]+>", "", re.search(r'<p class="b-meta">(.*?)</p>', li, re.S).group(1)))
        out[d["slug"]] = d
    return out


def cubierta(b, clase, perezosa=True):
    dentro = b["dentro"]
    if not perezosa:
        dentro = dentro.replace(' loading="lazy"', "")
    return f'<span class="bx-portada {clase}{" con-img" if b["img"] else ""}" {b["estilo"]} aria-hidden="true">{dentro}</span>'


def enlace_filtro(f, v, texto, n=None, clase=""):
    cuenta = f"<small>{n}</small>" if n is not None else ""
    c = f' class="{clase}"' if clase else ""
    return (f'<a{c} href="?{f}={quote(v)}#catalogo-libros" data-f="{f}" data-v="{html.escape(v)}">'
            f'<span>{html.escape(texto)}</span>{cuenta}</a>')


def construir():
    s = PAG.read_text(encoding="utf-8")
    cab = re.search(r'<header class="cabecera".*?</header>', s, re.S).group(0)
    pie = re.search(r'<footer class="pie.*?</footer>', s, re.S).group(0)
    filtros = re.search(r'<aside class="bx-lado" id="b-filtros".*?</aside>', s, re.S).group(0)
    lista = re.search(r'<ul class="b-lista bx-rejilla" id="b-lista">.*?</ul>', s, re.S).group(0)
    L = libros(lista)
    n = len(L)

    cabeza = s[:s.index("</head>")]
    cabeza = re.sub(r'\n<link rel="stylesheet" href="(\.\./enciclopedia/enciclopedia\.css|biblioteca\.css)[^>]*>', "", cabeza)
    cabeza = re.sub(r'\n<link rel="preload" href="\.\./fuentes/dm-serif-display-latin-400-italic\.woff2"[^>]*>', "", cabeza)
    cabeza = re.sub(r"\d+ fichas de libros", f"{n} fichas de libros", cabeza)
    css_enc = re.search(r'enciclopedia\.css\?v=[0-9a-z]+', (DOCS / "enciclopedia" / "index.html").read_text(encoding="utf-8")).group(0)
    cabeza = cabeza.replace('<link rel="stylesheet" href="../tierra.css',
                            '<link rel="preload" href="../fuentes/dm-serif-display-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>\n'
                            '<link rel="stylesheet" href="../tierra.css')
    cabeza += (f'<link rel="stylesheet" href="../enciclopedia/{css_enc}">\n'
               f'<link rel="stylesheet" href="biblioteca.css?v={VERSION}">\n')

    # recuentos, en el orden del árbol de filtros
    orden = {f: [html.unescape(v) for v in re.findall(rf'data-f="{f}" value="([^"]*)"', filtros)] for f in ("cat", "sust", "idioma")}
    etiquetas = {html.unescape(v): html.unescape(t) for v, t in
                 re.findall(r'value="([^"]*)"[^>]*>\s*<span class="bx-et">([^<]*)</span>', filtros)}
    cuenta_cat = Counter(b["cat"] for b in L.values())
    cuenta_sust = Counter(x for b in L.values() for x in b["sust"].split())
    cuenta_idi = Counter(b["idioma"] for b in L.values() if b["idioma"])
    temas = "".join(enlace_filtro("cat", v, etiquetas.get(v, v), cuenta_cat[v]) for v in orden["cat"] if cuenta_cat[v])
    medicinas = "".join(enlace_filtro("sust", v, etiquetas.get(v, v), cuenta_sust[v]) for v in orden["sust"] if cuenta_sust[v] and v != "general")
    idiomas = "".join(enlace_filtro("idioma", v, etiquetas.get(v, v), cuenta_idi[v]) for v in orden["idioma"] if cuenta_idi[v])
    con_idioma = sum(cuenta_idi.values())

    abanico = "".join(f'<a href="{sl}/" class="a{i}" aria-label="{html.escape(L[sl]["tit"])}">{cubierta(L[sl], "bh-cub", False)}</a>'
                      for i, sl in enumerate(ABANICO, 1))

    rutas = []
    for titulo, entradilla, items in RUTAS:
        lis = "".join(f'<li><a href="{sl}/">{cubierta(L[sl], "bh-mini")}<span><b>{html.escape(L[sl]["tit"].split(":")[0])}</b>'
                      f'<small>{html.escape(por)}</small></span></a></li>' for sl, por in items)
        rutas.append(f'<section class="bh-ruta"><h3>{titulo}</h3><p>{entradilla}</p><ul>{lis}</ul></section>')

    principal = f"""<main id="contenido">
<div class="enc bib">
<section class="e-portada"><div class="ancho e-portada-in">
<div><p class="etq oro">Biblioteca</p><h1>Libros para <em>leer a fondo</em></h1>
<p class="e-intro">{n} fichas de libros sobre medicinas psicodélicas: ciencia, terapia, historia, antropología y testimonios. Cada una con sus datos de edición y enlaces para encontrar el libro.</p>
<form class="e-busca" id="bh-form" role="search" action="./">{LUPA}<input type="search" id="bh-q" name="q" aria-label="Buscar en la biblioteca" placeholder="Título, autor o tema" autocomplete="off"><button class="btn o" type="submit">Buscar</button></form>
<p class="e-atajos">Entrar por {enlace_filtro("idioma", "español", "En español")}{enlace_filtro("cat", "Terapia y clínica", "Terapia y clínica")}{enlace_filtro("sust", "ayahuasca", "Ayahuasca")}{enlace_filtro("sust", "psilocibina", "Psilocibina")}<a href="?orden=new#catalogo-libros" data-orden="new"><span>Los más recientes</span></a></p></div>
<div class="bh-abanico">{abanico}</div>
</div></section>

<section class="e-sec ancho" id="empezar">
<div class="e-cab"><div><h2>Por dónde empezar</h2></div><p class="nota">Cuatro rutas cortas, de tres libros cada una, según lo que busques.</p></div>
<div class="bh-rutas">
{chr(10).join(rutas)}
</div>
</section>

<section class="e-sec ancho" id="entradas">
<div class="e-cab"><div><h2>Entrar por tema, medicina o idioma</h2></div><p class="nota">Cada entrada abre el catálogo ya filtrado. Después puedes combinar filtros.</p></div>
<div class="bh-entradas">
<div class="bh-grupo bh-temas"><h3>Por tema</h3><p class="bh-lista">{temas}</p></div>
<div class="bh-grupo"><h3>Por medicina</h3><p class="bh-lista bh-corta">{medicinas}</p>
<h3>Por idioma</h3><p class="bh-lista bh-corta">{idiomas}</p><p class="bh-nota">El idioma está anotado en {con_idioma} de las {n} fichas; el resto se irá completando.</p></div>
</div>
</section>

<section class="e-sec ancho bh-catalogo">
<div class="e-cab"><div><h2>El catálogo completo</h2></div><p class="nota">Busca por título, autor o tema y afina con los filtros. Las fichas con datos pendientes se irán completando.</p></div>
</section>
</div>

<div class="guia-cuerpo bib-cat">
<div class="s-ancho bx" id="catalogo-libros"><button type="button" id="b-filtros-toggle" class="bx-filtro-toggle" aria-controls="b-filtros" aria-expanded="false">Mostrar filtros</button>
{filtros}
<div class="bx-main">
<div class="bx-barra" role="search">
<label class="bx-oculto" for="b-q">Buscar por título, autor o tema</label>
<input type="search" id="b-q" placeholder="Busca por título, autor o tema…">
<div class="bx-orden"><label for="b-orden">Ordenar por</label>
<select id="b-orden"><option value="rel">Recomendados</option><option value="new">Más recientes</option><option value="old">Más antiguos</option><option value="az">Título (A–Z)</option><option value="autor">Autor (A–Z)</option></select></div>
</div>
<p id="b-n" class="bx-n-res" aria-live="polite">{n} libros</p>
<button type="button" class="bx-limpiar" id="b-compartir">Copiar enlace a estos resultados</button> <span id="b-compartir-estado" role="status" aria-live="polite"></span>
<div id="b-chips" class="bx-chips"></div>
<div id="b-vacio" class="bx-vacio" hidden><p class="bx-vacio-t">Ningún libro coincide con estos filtros.</p><p>Prueba a quitar alguno o a buscar con otras palabras.</p></div>
{lista}
<p class="bx-mas-w"><button type="button" class="bx-mas" id="b-mas" hidden>Ver más libros</button></p>
</div>
</div>
</div>

<div class="enc bib bib-fin">
<section class="ancho"><a class="bh-personas" href="../quien-es-quien/"><span><b>Las personas detrás de los libros</b><small>Hofmann, María Sabina, Grof, Naranjo, los Shulgin y otras: quién es quién, con sus obras en esta biblioteca.</small></span><i aria-hidden="true"></i></a></section>
</div>
</main>
<script src="biblioteca.js?v={VERSION}" defer></script>
<script src="../menu.js?v=20261123a" defer></script>
"""
    PAG.write_text(cabeza + "</head>\n<body class=\"guia\">\n<a class=\"saltar\" href=\"#contenido\">Saltar al contenido</a>\n"
                   + cab + "\n\n" + principal + "\n" + pie + "\n<script src=\"../tierra.js\" defer></script>\n</body>\n</html>\n",
                   encoding="utf-8")
    print(f"docs/biblioteca/index.html · {n} libros · {sum(b['img'] for b in L.values())} con portada")


if __name__ == "__main__":
    construir()
