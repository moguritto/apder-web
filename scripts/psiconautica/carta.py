#!/usr/bin/env python3
"""Dibuja docs/psiconautica/carta.svg: curvas de nivel como las de una carta náutica.
Es el fondo de la portada y de la cabecera de cada página de Psiconáutica.

    python3 scripts/psiconautica/carta.py      (necesita numpy y matplotlib; solo hace falta si se quiere otro dibujo)

El dibujo sale siempre igual (semilla fija)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.normpath(os.path.join(AQUI, "..", "..", "docs", "psiconautica", "carta.svg"))
W, H = 1200, 640
rng = np.random.default_rng(7)

x = np.linspace(0, W, 480)
y = np.linspace(0, H, 256)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)
# montes y fosas del fondo
montes = [(820, 250, 190, 150, 1.0), (1040, 470, 150, 120, .75), (560, 470, 170, 110, .55),
          (300, 170, 200, 130, .45), (1130, 120, 120, 100, .5), (120, 520, 160, 120, -.35), (640, 90, 150, 90, -.3)]
for cx, cy, sx, sy, a in montes:
    Z += a * np.exp(-(((X - cx) / sx) ** 2 + ((Y - cy) / sy) ** 2))
for _ in range(9):   # ondulación suave
    kx, ky, f = rng.uniform(.003, .012), rng.uniform(.003, .012), rng.uniform(0, 6.28)
    Z += .05 * np.sin(kx * X + ky * Y + f)

niveles = np.linspace(Z.min() + .04, Z.max() - .03, 17)
cs = plt.contour(X, Y, Z, levels=niveles)
trozos = []
for i, segs in enumerate(cs.allsegs):
    d = []
    for s in segs:
        if len(s) < 8:
            continue
        s = np.vstack([s[::4], s[-1:]]) if len(s) > 40 else s
        d.append("M" + "L".join("%.1f %.1f" % (px, H - py) for px, py in s).replace(".0", ""))
    if d:
        cls = ' class="m"' if i % 4 == 0 else ""     # una de cada cuatro, más marcada (curva maestra)
        trozos.append('<path%s d="%s"/>' % (cls, "".join(d)))
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" fill="none" stroke="#a6dccb" stroke-width="1" '
       'stroke-linejoin="round"><style>path{opacity:.5}.m{opacity:.95;stroke-width:1.4}</style>%s</svg>\n' % (W, H, "".join(trozos)))
os.makedirs(os.path.dirname(SALIDA), exist_ok=True)
with open(SALIDA, "w", encoding="utf-8") as f:
    f.write(svg)
print(SALIDA, len(svg) // 1024, "KB")
