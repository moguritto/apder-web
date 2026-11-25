#!/usr/bin/env python3
"""Apertura de «Investigación terapéutica» (docs/investigacion-terapeutica/index.html).

  python3 scripts/investigacion/apertura.py

La página se escribe a mano. Este guion solo rehace su apertura, entre las marcas
<!-- apertura:inicio --> y <!-- apertura:fin -->:
- portada con la seña de Terapia (fondo claro, manchas y dibujo), y
- «De un vistazo»: una tarjeta por problema de salud con su nivel de evidencia.

Las tarjetas se leen de la tabla «Cómo va la investigación en cada problema de salud» de la propia página:
si se cambia la tabla, se vuelve a lanzar y las tarjetas cambian con ella. Aquí no se escribe ningún dato.
"""
import html
import re
from pathlib import Path

PAG = Path(__file__).resolve().parent.parent.parent / "docs" / "investigacion-terapeutica" / "index.html"
VERSION = "20261125a"
NIVELES = [("sólida", 3), ("prometedora", 2), ("preliminar", 1)]


def texto(t):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t))).strip()


def main():
    s = PAG.read_text(encoding="utf-8")
    i = s.index('id="estado-evidencia"')
    tabla = s[i:s.index("</table>", i)]
    tarjetas = []
    for fila in re.findall(r"<tr>(.*?)</tr>", tabla, re.S)[1:]:
        celdas = re.findall(r"<td[^>]*>(.*?)</td>", fila, re.S)
        ancla = re.search(r'href="(#[^"]+)"', celdas[0])
        nombre, sust, fase, nivel = (texto(c) for c in celdas)
        n = next((v for k, v in NIVELES if nivel.lower().startswith(k)), 1)
        e = html.escape
        cab = f'<a href="{ancla.group(1)}">{e(nombre)}</a>' if ancla else e(nombre)
        tarjetas.append(f'<li class="n{n}"><h3>{cab}</h3><p class="iv-sust">{e(sust)}</p>'
                        f'<p class="iv-nivel"><span class="iv-medidor" aria-hidden="true"><i></i><i></i><i></i></span>{e(nivel)}</p>'
                        f'<p class="iv-fase">{e(fase)}</p></li>')
    apertura = f"""<!-- apertura:inicio (la escribe scripts/investigacion/apertura.py) -->
<section class="art-portada iv-portada">
  <div class="ancho">
    <div>
      <span class="mini"><a href="../terapia/">Terapia</a> · Investigación</span>
      <h1>Investigación <i>terapéutica</i></h1>
      <p class="entrada">Qué se sabe, qué falta por saber y cómo participar en un ensayo clínico con garantías.</p>
      <p class="iv-atajos"><a href="#estado-evidencia">La tabla completa</a><a href="#participar">Participar en un ensayo</a><a href="#senales-alarma">Señales de alarma</a><a href="#profesionales">Para profesionales</a></p>
    </div>
    <div class="art-dibujo" aria-hidden="true">
      <div class="mancha"></div><div class="mancha2"></div>
      <svg viewBox="0 0 100 100" focusable="false">
        <circle cx="50" cy="50" r="37" fill="rgba(255,255,255,.16)" stroke="#fff" stroke-width="2.2"/>
        <path d="M32 66V54M44 66V46M56 66V38M68 66V30" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
        <path d="M28 72h44" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>
      </svg>
      <div class="chip" style="left:-2%;top:10%">{len(tarjetas)} líneas<small>de investigación, una a una</small></div>
      <div class="chip" style="right:-2%;bottom:8%">Tres niveles<small>preliminar, prometedora y sólida</small></div>
    </div>
  </div>
</section>
<section class="s-ancho iv-vistazo" aria-labelledby="iv-t">
  <div class="iv-cab"><h2 id="iv-t">De un vistazo</h2><p>En qué punto está cada línea. <b>Preliminar:</b> estudios pequeños. <b>Prometedora:</b> al menos un ensayo aleatorizado favorable. <b>Sólida:</b> varios ensayos de fase 3 y aprobación como medicamento. Los criterios y los matices, <a href="#estado-evidencia">más abajo</a>.</p></div>
  <ul class="iv-mapa">
{chr(10).join(tarjetas)}
  </ul>
</section>
<!-- apertura:fin -->"""
    if "<!-- apertura:inicio" in s:
        s = re.sub(r"<!-- apertura:inicio.*?<!-- apertura:fin -->", lambda m: apertura, s, flags=re.S)
    else:
        s = re.sub(r'<section class="s-cabeza s-cabeza-sola">.*?</section>', lambda m: apertura, s, count=1, flags=re.S)
    s = re.sub(r'\n<link rel="stylesheet" href="investigacion\.css[^>]*>', "", s)
    s = re.sub(r'(<link rel="stylesheet" href="\.\./tierra\.css[^>]*>)', rf'\1\n<link rel="stylesheet" href="investigacion.css?v={VERSION}">', s, count=1)
    PAG.write_text(s, encoding="utf-8")
    print(f"apertura escrita · {len(tarjetas)} tarjetas")


if __name__ == "__main__":
    main()
