#!/usr/bin/env python3
"""Apertura de «Medicinas por familias» (docs/medicinas/index.html).

  python3 scripts/medicinas/apertura.py

La página se escribe a mano. Este guion solo rehace su apertura, entre las marcas
<!-- apertura:inicio --> y <!-- apertura:fin -->: portada de cuaderno (la seña de las guías de medicinas)
y una casilla por familia, con su número, sus ejemplos y cómo actúa.

Las casillas se leen de la propia página: los títulos numerados (`<h2 id="…">1. Triptaminas</h2>`) y la tabla
«Las familias de un vistazo». Si cambian, se vuelve a lanzar. Aquí no se escribe ningún dato.
"""
import html
import re
from pathlib import Path

PAG = Path(__file__).resolve().parent.parent.parent / "docs" / "medicinas" / "index.html"
VERSION = "20261125a"


def main():
    s = PAG.read_text(encoding="utf-8")
    familias = re.findall(r'<h2 id="([^"]+)">(\d+)\. ([^<]+)</h2>', s)
    i = s.index('id="resumen"')
    filas = re.findall(r"<tr>(.*?)</tr>", s[i:s.index("</table>", i)], re.S)[1:]
    assert len(filas) == len(familias), (len(filas), len(familias))
    casillas = []
    for (ancla, num, nombre), fila in zip(familias, filas):
        _, ejemplos, accion = re.findall(r"<td[^>]*>(.*?)</td>", fila, re.S)
        casillas.append(f'<li><a href="#{ancla}"><b>{num}</b><span class="mf-nombre">{html.escape(html.unescape(nombre))}</span>'
                        f'<span class="mf-ej">{ejemplos.strip()}</span><span class="mf-accion">{accion.strip()}</span></a></li>')
    apertura = f"""<!-- apertura:inicio (la escribe scripts/medicinas/apertura.py) -->
<section class="mf-portada">
<div class="s-ancho">
<div class="mf-texto">
<p class="s-antetitulo"><a href="../sustancias/">Medicinas</a> · Por familias</p>
<h1>Medicinas <em>por familias</em></h1>
<p class="mf-entrada">Un mapa de las plantas, hongos y moléculas que cambian la conciencia, agrupados por su química y por cómo actúan. Para ver de un vistazo qué comparten, en qué se diferencian y qué riesgos tiene cada familia.</p>
<p class="mf-atajos"><a href="#introduccion">Qué entendemos por medicina</a><a href="#reduccion-de-riesgos">Reducción de riesgos</a><a href="../sustancias/">Las 19 guías, una a una</a></p>
</div>
<ol class="mf-familias" aria-label="Las {len(casillas)} familias">
{chr(10).join(casillas)}
</ol>
</div>
</section>
<!-- apertura:fin -->"""
    if "<!-- apertura:inicio" in s:
        s = re.sub(r"<!-- apertura:inicio.*?<!-- apertura:fin -->", lambda m: apertura, s, flags=re.S)
    else:
        s = re.sub(r'<section class="s-cabeza s-cabeza-sola">.*?</section>', lambda m: apertura, s, count=1, flags=re.S)
    s = re.sub(r'\n<link rel="stylesheet" href="medicinas\.css[^>]*>', "", s)
    s = re.sub(r'\n<link rel="preload" href="\.\./fuentes/dm-serif-display-latin-400-italic\.woff2"[^>]*>', "", s)
    s = re.sub(r'(<link rel="stylesheet" href="\.\./tierra\.css[^>]*>)',
               r'<link rel="preload" href="../fuentes/dm-serif-display-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>\n'
               rf'\1\n<link rel="stylesheet" href="medicinas.css?v={VERSION}">', s, count=1)
    PAG.write_text(s, encoding="utf-8")
    print(f"apertura escrita · {len(casillas)} familias")


if __name__ == "__main__":
    main()
