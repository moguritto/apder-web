#!/usr/bin/env python3
"""Plantilla de las guías de medicinas (docs/sustancias/<guía>/index.html): cabecera y «En pocas palabras».

  python3 scripts/guias/plantilla.py

Las guías se escriben a mano. Este guion solo pone al día el marcado de dos piezas, sin tocar el texto,
y se puede lanzar las veces que haga falta (no cambia lo que ya está al día):

- Apertura (`section.s-cabeza` → añade `s-cab-guia`): cada dato de la ficha en su línea
  (`<p class="s-ficha-dato"><strong>Familia:</strong> <span>…</span></p>`) y, si la guía tiene foto
  (FOTOS, en scripts/guias/generar.py), la foto y su crédito, leído de CREDITOS.md.
- «En pocas palabras» (`ul.s-claves` → añade `s-resumen`): el texto de cada punto va en un `<span>`.
- Enlaza `docs/sustancias/guia.css`, donde están los estilos de las dos piezas.

Guía nueva: se copia una carpeta, se cambia el texto y se lanza este guion.
"""
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generar import DOCS, FOTOS, creditos  # noqa: E402

VERSION = "20261125a"
CSS = f'<link rel="stylesheet" href="../guia.css?v={VERSION}">'


def ficha(aside, slug, cred):
    lineas = []
    for linea in aside.split("\n"):
        m = re.fullmatch(r'<p(?: class="s-ficha-dato")?>(<strong>.*)</p>', linea)
        if not m:
            lineas.append(linea)
            continue
        for trozo in re.split(r"\s+·\s+(?=<strong>)", m.group(1)):
            k = re.fullmatch(r"(<strong>[^<]*</strong>)\s*(.*)", trozo, re.S)
            valor = k.group(2)
            if not valor.startswith("<span>"):
                valor = f"<span>{valor}</span>"
            lineas.append(f'<p class="s-ficha-dato">{k.group(1)} {valor}</p>')
    aside = "\n".join(lineas)
    aside = re.sub(r'\n<img class="s-foto"[^>]*>', "", aside)
    aside = re.sub(r'\n<p class="s-foto-cred">.*?</p>', "", aside)
    if slug in FOTOS:
        fuente, _, que = FOTOS[slug]
        autor, url, lic = cred[fuente]
        lic = "dominio público" if lic.lower() in ("public domain", "cc0") else lic
        aside = aside.replace('<aside class="s-ficha-mol">',
                              f'<aside class="s-ficha-mol">\n<img class="s-foto" src="../img/{slug}.webp" alt="{html.escape(que)}" width="520" height="390">', 1)
        aside = aside.replace("</aside>", f'<p class="s-foto-cred">Foto: <a href="{html.escape(url)}" rel="noopener">{html.escape(autor)}</a>, {lic}</p>\n</aside>')
    return aside


def claves(ul):
    def li(m):
        cuerpo = m.group(2)
        if cuerpo.startswith("<span>"):
            return m.group(0)
        return f"<li>{m.group(1)} <span>{cuerpo}</span></li>"
    return re.sub(r"<li>(<strong>[^<]+</strong>)\s*(.*?)</li>", li, ul, flags=re.S)


def main():
    cred = creditos()
    n = 0
    for f in sorted((DOCS / "sustancias").glob("*/index.html")):
        slug = f.parent.name
        s = antes = f.read_text(encoding="utf-8")
        s = s.replace('<section class="s-cabeza">', '<section class="s-cabeza s-cab-guia">', 1)
        s = re.sub(r'<aside class="s-ficha-mol">.*?</aside>', lambda m: ficha(m.group(0), slug, cred), s, count=1, flags=re.S)
        s = s.replace('<ul class="s-claves">', '<ul class="s-claves s-resumen">', 1)
        s = re.sub(r'<ul class="s-claves s-resumen">.*?</ul>', lambda m: claves(m.group(0)), s, count=1, flags=re.S)
        s = re.sub(r'<link rel="stylesheet" href="\.\./guia\.css[^>]*>\n?', "", s)
        s = re.sub(r'(<link rel="stylesheet" href="\.\./\.\./tierra\.css[^>]*>)', r"\1\n" + CSS, s, count=1)
        if s != antes:
            f.write_text(s, encoding="utf-8")
            n += 1
    print(f"guías puestas al día: {n}")


if __name__ == "__main__":
    main()
