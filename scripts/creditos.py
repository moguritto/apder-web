#!/usr/bin/env python3
"""Página «Créditos de las fotografías» (docs/creditos/index.html).

  python3 scripts/creditos.py

Las licencias de las fotos piden citar al autor. Para no llenar de créditos las páginas, van todos juntos aquí,
y el pie de todas las páginas enlaza a esta. Se leen de CREDITOS.md: cada fila con enlace a Wikimedia Commons
es una foto (los recortes de una misma foto salen una sola vez). Al añadir una foto: su fila en CREDITOS.md y relanzar.
El marco (cabecera, pie y <head>) se copia de la página de aviso legal.
"""
import html
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
TITULO = "Créditos de las fotografías"
DESC = ("Autoría y licencia de las fotografías de apder.org. Proceden de Wikimedia Commons y se usan reducidas o "
        "recortadas, con la licencia de cada original.")
LIC = {"public domain": "Dominio público", "cc0": "CC0 (dominio público)"}


def main():
    fotos = {}
    for fila in (RAIZ / "CREDITOS.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| `([^`]+)` \| ([^|]*) \| (.*?) · \[Wikimedia Commons\]\((.*?)\) \| ([^|]+) \|", fila)
        if not m:
            continue
        archivo, que, autor, url, lic = (x.strip() for x in m.groups())
        titulo = re.sub(r"_", " ", re.sub(r"^.*File:", "", url))
        titulo = re.sub(r"%([0-9A-Fa-f]{2})", lambda k: bytes.fromhex(k.group(1)).decode("latin-1"), titulo)
        titulo = titulo.encode("latin-1", "ignore").decode("utf-8", "ignore") or titulo
        fotos.setdefault(url, (re.sub(r"\.(jpe?g|png|webp|JPG)$", "", titulo), re.sub(r"\[\d+\]", "", autor), LIC.get(lic.lower(), lic)))
    lista = "\n".join(f'<li><a href="{html.escape(u)}" rel="noopener">{html.escape(t)}</a> · {html.escape(a)} · {html.escape(l)}</li>'
                      for u, (t, a, l) in sorted(fotos.items(), key=lambda x: x[1][0].lower()))
    assert 120 <= len(DESC) <= 160, len(DESC)

    s = (DOCS / "aviso-legal" / "index.html").read_text(encoding="utf-8")
    cabeza = s[:s.index("</head>")]
    cabeza = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + DESC, cabeza)
    cabeza = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + DESC, cabeza)
    cabeza = re.sub(r"<title>.*?</title>", f"<title>{TITULO} | APDER</title>", cabeza)
    cabeza = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + TITULO + " · APDER", cabeza)
    cabeza = cabeza.replace("https://apder.org/aviso-legal/", "https://apder.org/creditos/")
    if "rel=\"canonical\"" not in cabeza:
        cabeza += '<link rel="canonical" href="https://apder.org/creditos/">\n'
    cab = re.search(r'<header class="cabecera".*?</header>', s, re.S).group(0)
    # El menú necesita menu.js; en el aviso legal va entre </main> y el pie, así que se copia aparte.
    menu = re.search(r'<script src="[^"]*menu\.js[^"]*" defer></script>', s).group(0)
    pie = menu + "\n" + s[s.index("<footer"):]
    pagina = f"""{cabeza}</head>
<body class="guia">
<a class="saltar" href="#contenido">Saltar al contenido</a>
{cab}

<main id="contenido" class="guia-cuerpo legal-cuerpo">
<section class="bloque legal">
<div class="ancho">
<h1 class="como-h2">{TITULO}</h1>
<div class="legal-texto">
<p>Las fotografías de esta web proceden de <a href="https://commons.wikimedia.org/" rel="noopener">Wikimedia Commons</a>. Las usamos reducidas o recortadas. Cada una conserva la licencia de su original, y los recortes se comparten con esa misma licencia. Gracias a quienes las hicieron y las compartieron.</p>
<p>Las {len(fotos)} fotografías, por orden alfabético. El enlace lleva a la ficha de cada una, donde están el original y el texto de su licencia.</p>
<ul class="creditos-lista">
{lista}
</ul>
<p>Los dibujos de las moléculas, los mapas de la Enciclopedia y las ilustraciones se han hecho para APDER. Las cubiertas de los libros pertenecen a sus editoriales y se muestran para identificar cada obra.</p>
<p>Si eres autor de una imagen y ves un error en su crédito, escríbenos a <a href="mailto:info@apder.org">info@apder.org</a> y lo corregimos.</p>
</div>
</div>
</section>
</main>
{pie}"""
    import sys
    sys.path.insert(0, str(RAIZ / "scripts"))
    from cabecera import aplicar           # cabecera y pie con las rutas y marcas de esta página
    pagina = aplicar(pagina, "creditos/index.html")[0]
    destino = DOCS / "creditos"
    destino.mkdir(exist_ok=True)
    (destino / "index.html").write_text(pagina, encoding="utf-8")
    print(f"docs/creditos/index.html · {len(fotos)} fotografías")


if __name__ == "__main__":
    main()
