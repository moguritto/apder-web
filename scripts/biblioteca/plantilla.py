#!/usr/bin/env python3
"""Plantilla de las fichas de libro (docs/biblioteca/<libro>/index.html).

  python3 scripts/biblioteca/plantilla.py            pone al día todas las fichas
  python3 scripts/biblioteca/plantilla.py --mira     dice cuántas cambiaría, sin escribir

No toca los textos: solo recoloca las piezas de cada ficha y cambia de dónde salen los estilos.
- Quita el bloque <style> copiado dentro de cada página y enlaza docs/biblioteca/biblioteca.css.
- Apertura en verde pino (`section.lb-cab`): migas, cubierta, título, subtítulo, autoría, año e idioma y etiquetas.
- Debajo (`div.lb-bajo`): a la izquierda, descripción y datos de edición (`div.lb-datos`); a la derecha, dónde encontrarlo (`aside.lb-caja`).
- Al final (`div.lb-resto`): lecturas relacionadas y aviso.

Se puede lanzar las veces que haga falta: una ficha ya puesta al día (`lb2`) no se toca.
Ficha nueva: se copia una ya publicada, se cambian sus datos y se añade su <li> en la portada de la Biblioteca.
Comprueba que no se pierde texto: si las palabras de una ficha cambian al recolocarla, no la escribe y lo dice.
"""
import html
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
BIB = RAIZ / "docs" / "biblioteca"
VERSION = "20261125b"
CSS = f'<link rel="stylesheet" href="../biblioteca.css?v={VERSION}">'


def palabras(trozo):
    t = re.sub(r"<style.*?</style>", " ", trozo, flags=re.S)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    return sorted(t.split())


def poner_al_dia(s):
    """Devuelve (página nueva, motivo) — motivo no vacío si no se ha podido."""
    i0 = s.index('<main id="contenido" class="guia-cuerpo">')
    i1 = s.index("</main>", i0)
    main = s[i0:i1]
    if 'class="lb lb2"' in main:
        s = re.sub(r'<link rel="stylesheet" href="\.\./biblioteca\.css[^>]*>', CSS, s)
        return con_pie(s), ""
    sin_estilo = re.sub(r"<style.*?</style>", "", main, count=1, flags=re.S)
    m = re.search(r'<div class="s-ancho lb">\s*(<p class="s-antetitulo">.*?</p>)\s*<div class="lb-top">\s*'
                  r'(<div class="lb-col-portada">.*?</div>(?:\s*<p class="lb-aviso">[^<]*</p>)?</div>)\s*<div class="lb-info">(.*?)</div>\s*'
                  r'(<aside class="lb-caja".*?</aside>)\s*</div>(.*)</div>\s*$', sin_estilo, re.S)
    if not m:
        return s, "no reconozco la estructura"
    migas, portada, info, caja, resto = m.groups()
    corte = re.search(r"<h2|<h3 class=\"lb-h3\"|<p class=\"lb-desc\"|<p class=\"lb-aviso\"", info)
    arriba, abajo = (info[:corte.start()], info[corte.start():]) if corte else (info, "")
    arriba = re.sub(r'\s*<p class="lb-meta"></p>', "", arriba)
    datos = f'<div class="lb-datos">\n{abajo.strip()}\n</div>\n' if abajo.strip() else ""
    nuevo = f"""<main id="contenido" class="guia-cuerpo">
<div class="lb lb2">
<section class="lb-cab"><div class="s-ancho">
{migas}
<div class="lb-top">
{portada}
<div class="lb-info">
{arriba.strip()}
</div>
</div>
</div></section>
<div class="s-ancho lb-bajo{'' if datos else ' sin-datos'}">
{datos}{caja}
</div>
<div class="s-ancho lb-resto">
{resto.strip()}
</div>
</div>
"""
    antes = palabras(sin_estilo)
    antes_sin_meta = antes  # un <p class="lb-meta"> vacío no tiene palabras
    if palabras(nuevo) != antes_sin_meta:
        return s, "cambian las palabras"
    pagina = s[:i0] + nuevo + s[i1:]
    if "../biblioteca.css" not in pagina:
        pagina = re.sub(r'(<link rel="stylesheet" href="\.\./\.\./tierra\.css[^>]*>)', r"\1\n" + CSS, pagina, count=1)
    return con_pie(pagina), ""


def con_pie(pagina):
    """marca la columna de la cubierta cuando lleva una línea debajo (de qué edición es la portada)"""
    return re.sub(r'<div class="lb-col-portada">(<div class="bx-portada[^>]*>.*?</div>\s*<p class="lb-aviso">)',
                  r'<div class="lb-col-portada lb-con-pie">\1', pagina, flags=re.S)


def main():
    mira = "--mira" in sys.argv
    hechas = fallos = 0
    for f in sorted(BIB.glob("*/index.html")):
        s = f.read_text(encoding="utf-8")
        if 'class="s-ancho lb' not in s and 'class="lb lb2"' not in s:
            continue
        nueva, motivo = poner_al_dia(s)
        if motivo:
            fallos += 1
            print(f"sin tocar ({motivo}): {f.parent.name}")
        elif nueva != s:
            hechas += 1
            if not mira:
                f.write_text(nueva, encoding="utf-8")
    print(f"fichas {'que cambiarían' if mira else 'puestas al día'}: {hechas} · sin tocar por dudas: {fallos}")


if __name__ == "__main__":
    main()
