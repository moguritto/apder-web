#!/usr/bin/env python3
"""Recortes de las fotos de la portada (docs/index.html).

Parte de fotos que ya están en docs/enciclopedia/img/ (autoría y licencia en CREDITOS.md)
y escribe versiones recortadas y ligeras en docs/img/inicio/*.webp.

Uso (desde la raíz del repositorio):  python3 scripts/fotos_portada.py
Necesita Pillow (pip install pillow).

Cada línea de RECORTES: salida, origen, caja (x0, y0, x1, y1 en fracciones del original), ancho final y calidad WebP.
Si se cambia una foto, hay que cambiar también su línea en los créditos de la portada y en CREDITOS.md.
"""
from pathlib import Path
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "docs" / "enciclopedia" / "img"
SALIDA = RAIZ / "docs" / "img" / "inicio"

RECORTES = [
    # portada: retablo de tres arcos
    ("peyote.webp",     "pey-flor.jpg",      (0.292, 0.000, 0.751, 1.000), 600, 74),
    ("mongui.webp",     "idx-psilocybe.jpg", (0.050, 0.000, 0.945, 1.000), 400, 80),
    ("gloria.webp",     "idx-ipomoea.jpg",   (0.130, 0.000, 0.670, 1.000), 340, 80),
    # tarjetas de la Enciclopedia
    ("ayahuasca.webp",  "aya-liana.jpg",     (0.080, 0.000, 0.915, 1.000), 1100, 78),
    ("matamoscas.webp", "ama-joven.jpg",     (0.230, 0.000, 0.808, 1.000), 560, 76),
    ("cacao.webp",      "idx-cacao.jpg",     (0.100, 0.000, 0.900, 1.000), 560, 80),
    # fondos de «Buscar» y de la página no encontrada (docs/buscar/buscar.css)
    ("bosque.webp",     "ama-bosque.jpg",    (0.000, 0.300, 1.000, 0.880), 1600, 62),
    ("rio.webp",        "aya-rio.jpg",       (0.000, 0.180, 1.000, 0.900), 1600, 62),
]


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)
    for salida, origen, (x0, y0, x1, y1), ancho, calidad in RECORTES:
        im = Image.open(ORIGEN / origen).convert("RGB")
        w, h = im.size
        im = im.crop((round(x0 * w), round(y0 * h), round(x1 * w), round(y1 * h)))
        if im.width > ancho:
            im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
        destino = SALIDA / salida
        im.save(destino, "WEBP", quality=calidad, method=6)
        print(f"{salida:18s} {im.width}x{im.height}  {destino.stat().st_size // 1024} KB  <- {origen}")


if __name__ == "__main__":
    main()
