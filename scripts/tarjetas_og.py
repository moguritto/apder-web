"""Genera las imágenes para compartir (Open Graph) de apder.org: una tarjeta
de 1200×630 por página, con la paleta Tierra, las letras de la web y el dibujo
de la molécula o el logo. Pesan menos de 100 KB, por debajo del límite de
WhatsApp (300 KB).

Uso:  python3 scripts/tarjetas_og.py          (desde la raíz del repositorio)
Necesita: pip install pillow cairosvg fonttools brotli

Para añadir una página: añade una línea a TARJETAS y pon en su <head>
og:image = https://apder.org/img/og/<nombre>.png (y twitter:image igual).
"""
import io
import os
import re
import sys

import cairosvg
from fontTools.ttLib import TTFont
from PIL import Image, ImageChops, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RAIZ, "docs")
SALIDA = os.path.join(DOCS, "img", "og")
TMP = os.path.join(RAIZ, ".tmp-fuentes")

CREMA, ARENA, SALVIA = "#f7f1e6", "#efe4d0", "#cdd3c1"
TIERRA, BOSQUE, SUAVE = "#9c4a26", "#2f3e33", "#6c6257"
W, H = 1200, 630

GUIA = "Qué es, cómo actúa, qué dice la ciencia, riesgos y legalidad"

# nombre de archivo, antetítulo, título, subtítulo, dibujo
TARJETAS = [
    ("medicinas-guias", "APDER · Guías", "Medicinas psicodélicas", "19 guías en español, con fuentes y reducción de riesgos", "logo"),
    ("medicinas-familias", "APDER · Artículo", "Las medicinas, por familias", "Triptaminas, fenetilaminas, empatógenos, plantas y más", "mol:ayahuasca"),
    ("terapia-mdma", "APDER · MDMA", "Terapia asistida con MDMA", "Qué es, cómo se vive, qué dice la investigación y dónde es legal", "mol:mdma"),
    ("investigacion", "APDER · Investigación", "Investigación terapéutica", "Qué se sabe, qué falta por saber y cómo participar en ensayos", "mol:5-meo-dmt"),
    ("biblioteca", "APDER · Recursos", "Biblioteca", "425 libros sobre psicodélicos y enteógenos, con buscador", "logo"),
    ("guia-sesion", "Guía para participantes", "Guía para tu sesión", "Antes, durante y después: cómo prepararte e integrar lo vivido", "svg:corazon"),
    ("protocolo-taller", "Guía para participantes", "Meditación de corazón", "Preparación, acompañamiento, música e integración", "svg:corazon"),
]
GUIAS = {
    "psilocibina": "Setas de psilocibina", "lsd": "LSD", "mescalina": "Mescalina, peyote y San Pedro",
    "dmt": "DMT", "ayahuasca": "Ayahuasca", "5-meo-dmt": "5-MeO-DMT", "mdma": "MDMA",
    "ketamina": "Ketamina", "ibogaina": "Ibogaína", "2c-b": "2C-B", "4-aco-dmt": "4-AcO-DMT",
    "amanita-muscaria": "Amanita muscaria", "salvia-divinorum": "Salvia divinorum",
    "cannabis": "Cannabis", "kanna": "Kanna", "kratom": "Kratom", "datura": "Datura",
    "cacao": "Cacao ceremonial", "tabaco": "Tabaco sagrado",
}
MOLECULA = {"amanita-muscaria": "amanita", "salvia-divinorum": "salvia"}
for slug, nombre in GUIAS.items():
    TARJETAS.append((f"guia-{slug}", "APDER · Guía", nombre, GUIA, "mol:" + MOLECULA.get(slug, slug)))


def fuente(nombre, tam):
    os.makedirs(TMP, exist_ok=True)
    ttf = os.path.join(TMP, nombre + ".ttf")
    if not os.path.exists(ttf):
        t = TTFont(os.path.join(DOCS, "fuentes", nombre + ".woff2"))
        t.flavor = None
        t.save(ttf)
    return ImageFont.truetype(ttf, tam)


def partir(draw, texto, f, ancho, max_lineas):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if draw.textlength(prueba, font=f) <= ancho or not actual:
            actual = prueba
        else:
            lineas.append(actual)
            actual = p
    lineas.append(actual)
    return lineas if len(lineas) <= max_lineas else None


def dibujo(tipo, caja):
    """Devuelve una imagen RGBA del dibujo ajustada a la caja (ancho, alto)."""
    if tipo == "logo":
        im = Image.open(os.path.join(DOCS, "img", "apder-icono.webp")).convert("RGBA")
        alfa = im.split()[3]
        # líneas en verde bosque, como en og-apder.png
        gris = im.convert("L").point(lambda v: 255 - v)
        alfa = ImageChops.multiply(alfa, gris.point(lambda v: min(255, v * 2)))
        im = Image.new("RGBA", im.size, BOSQUE)
        im.putalpha(alfa)
    elif tipo.startswith("svg:"):
        png = cairosvg.svg2png(url=os.path.join(DOCS, "img", tipo[4:] + ".svg"), output_width=caja[0] * 2)
        im = Image.open(io.BytesIO(png)).convert("RGBA")
        im = im.crop(im.getbbox())
    else:
        svg = open(os.path.join(DOCS, "sustancias", "moleculas", tipo[4:] + ".svg"), encoding="utf-8").read()
        svg = svg.replace("#000000", BOSQUE).replace("#FFFFFF", "none")
        svg = re.sub(r"stroke-width:2\.0px", "stroke-width:2.4px", svg)
        svg = re.sub(r"<rect[^>]*style='opacity:1\.0;fill:#FFFFFF[^>]*/>", "", svg)
        png = cairosvg.svg2png(bytestring=svg.encode(), output_width=caja[0] * 2)
        im = Image.open(io.BytesIO(png)).convert("RGBA")
        im = im.crop(im.getbbox())
    im.thumbnail(caja, Image.LANCZOS)
    return im


def tarjeta(nombre, ante, titulo, sub, tipo):
    base = Image.new("RGB", (W, H), CREMA)
    d = ImageDraw.Draw(base)
    d.ellipse((720, -60, 1300, 500), fill=ARENA)
    capa = Image.new("RGB", (W, H), "white")
    ImageDraw.Draw(capa).ellipse((660, 400, 1080, 820), fill=SALVIA)
    base = ImageChops.multiply(base, capa)
    d = ImageDraw.Draw(base)

    im = dibujo(tipo, {"logo": (400, 330), "svg:corazon": (330, 300)}.get(tipo, (420, 330)))
    cx, cy = 910, 300
    base.paste(im, (cx - im.width // 2, cy - im.height // 2), im)

    x, ancho = 80, 560
    f_ante = fuente("nunito-sans-latin-700-normal", 24)
    # elige tamaños para que el bloque quepa entre el margen de arriba y «apder.org»
    for tam, tam_s in ((112, 40), (100, 40), (92, 38), (84, 36), (76, 34), (68, 32)):
        f_tit = fuente("dm-serif-display-latin-400-normal", tam)
        f_sub = fuente("dm-serif-display-latin-400-normal", tam_s)
        lineas = partir(d, titulo, f_tit, ancho, 2)
        ls = partir(d, sub, f_sub, ancho - 10, 3)
        if not lineas or not ls:
            continue
        alto = 24 + 30 + len(lineas) * int(tam * 1.04) + 26 + len(ls) * int(tam_s * 1.28) + 26 + 6
        if alto <= 440:
            break
    y = max(64, (H - 40 - alto) // 2)
    d.text((x, y), ante.upper(), font=f_ante, fill=BOSQUE)
    y += 24 + 30 - int(tam * 0.2)
    for l in lineas:
        d.text((x, y), l, font=f_tit, fill=TIERRA)
        y += int(tam * 1.04)
    y += 26 + int(tam * 0.2) - int(tam_s * 0.2)
    for l in ls:
        d.text((x, y), l, font=f_sub, fill=BOSQUE)
        y += int(tam_s * 1.28)
    y += 26 + int(tam_s * 0.2)
    d.rounded_rectangle((x, y, x + 96, y + 6), radius=3, fill=TIERRA)
    f_web = fuente("nunito-sans-latin-700-normal", 24)
    d.text((x, H - 62), "apder.org", font=f_web, fill=SUAVE)
    if y > H - 80:
        print(f"  aviso: el texto de {nombre} llega muy abajo ({y}px)")

    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.join(SALIDA, nombre + ".png")
    base.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(ruta, optimize=True)
    return ruta, os.path.getsize(ruta)


if __name__ == "__main__":
    solo = set(sys.argv[1:])
    for t in TARJETAS:
        if solo and t[0] not in solo:
            continue
        ruta, peso = tarjeta(*t)
        print(f"{os.path.relpath(ruta, RAIZ)}  {peso // 1024} KB")
