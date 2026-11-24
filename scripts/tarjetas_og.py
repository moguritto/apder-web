"""Genera las imágenes para compartir (Open Graph) de apder.org: una tarjeta
de 1200×630 por página, sencilla: el título, el dibujo de la molécula o el
logo y la marca APDER, con la paleta Tierra y las letras de la web. Pesan menos de 100 KB, por debajo del límite de
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

# nombre de archivo, título, dibujo
TARJETAS = [
    ("../og-apder", "APDER", "logo"),
    ("medicinas-guias", "Medicinas", "logo"),
    ("medicinas-familias", "Medicinas por familias", "mol:ayahuasca"),
    ("terapia-mdma", "Terapia con MDMA", "mol:mdma"),
    ("investigacion", "Investigación", "mol:5-meo-dmt"),
    ("biblioteca", "Biblioteca", "logo"),
    ("formaciones", "Formaciones en el mundo", "svg:formaciones"),
    ("quien-es-quien", "Quién es quién", "logo"),
    ("persona-albert-hofmann", "Albert Hofmann", "mol:lsd"),
    ("persona-stanislav-grof", "Stanislav Grof", "logo"),
    ("persona-maria-sabina", "María Sabina", "logo"),
    ("persona-aldous-huxley", "Aldous Huxley", "mol:mescalina"),
    ("persona-humphry-osmond", "Humphry Osmond", "logo"),
    ("persona-valentina-y-gordon-wasson", "Valentina y Gordon Wasson", "logo"),
    ("persona-richard-evans-schultes", "Richard Evans Schultes", "logo"),
    ("persona-timothy-leary", "Timothy Leary", "logo"),
    ("persona-ram-dass", "Ram Dass", "logo"),
    ("persona-alan-watts", "Alan Watts", "logo"),
    ("persona-ann-y-alexander-shulgin", "Los Shulgin", "mol:2c-b"),
    ("persona-leo-zeff", "Leo Zeff", "logo"),
    ("guia-microdosis-setas", "Microdosis de setas", "mol:psilocibina"),
    ("guia-microdosis-lsd", "Microdosis de LSD", "mol:lsd"),
    ("guia-microdosis-ayahuasca", "Microdosis de ayahuasca", "mol:ayahuasca"),
    ("guia-microdosis-dmt", "Microdosis de DMT", "mol:dmt"),
    ("guia-microdosis-ibogaina", "Microdosis de ibogaína", "mol:ibogaina"),
    ("guia-microdosis-mescalina", "Microdosis de mescalina", "mol:mescalina"),
]
GUIAS = {
    "psilocibina": "Psilocibina", "lsd": "LSD", "mescalina": "Mescalina", "dmt": "DMT",
    "ayahuasca": "Ayahuasca", "5-meo-dmt": "5-MeO-DMT", "mdma": "MDMA", "ketamina": "Ketamina",
    "ibogaina": "Ibogaína", "2c-b": "2C-B", "4-aco-dmt": "4-AcO-DMT", "amanita-muscaria": "Amanita",
    "salvia-divinorum": "Salvia", "cannabis": "Cannabis", "kanna": "Kanna", "kratom": "Kratom",
    "datura": "Datura", "cacao": "Cacao", "tabaco": "Tabaco", "microdosis": "Microdosis",
}
MOLECULA = {"amanita-muscaria": "amanita", "salvia-divinorum": "salvia"}
for slug, nombre in GUIAS.items():
    TARJETAS.append((f"guia-{slug}", nombre, "mol:" + MOLECULA.get(slug, slug)))


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
    if len(lineas) > max_lineas or any(draw.textlength(l, font=f) > ancho for l in lineas):
        return None
    return lineas


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


def tarjeta(nombre, titulo, tipo):
    """Tarjeta sencilla: solo el título y el dibujo (y la marca APDER abajo)."""
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
    for tam in (150, 136, 124, 112, 100, 90, 80):
        f_tit = fuente("dm-serif-display-latin-400-normal", tam)
        lineas = partir(d, titulo, f_tit, ancho, 2)
        if lineas:
            break
    paso = int(tam * 1.02)
    alto = paso * len(lineas)
    y = (H - alto) // 2 - int(tam * 0.12)
    for l in lineas:
        d.text((x, y), l, font=f_tit, fill=TIERRA)
        y += paso
    if titulo != "APDER":
        f_marca = fuente("nunito-sans-latin-700-normal", 26)
        d.text((x, H - 76), "APDER", font=f_marca, fill=BOSQUE)

    os.makedirs(SALIDA, exist_ok=True)
    ruta = os.path.normpath(os.path.join(SALIDA, nombre + ".png"))
    base.quantize(colors=64, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(ruta, optimize=True)
    return ruta, os.path.getsize(ruta)


if __name__ == "__main__":
    solo = set(sys.argv[1:])
    for t in TARJETAS:
        if solo and t[0] not in solo:
            continue
        ruta, peso = tarjeta(*t)
        print(f"{os.path.relpath(ruta, RAIZ)}  {peso // 1024} KB")
