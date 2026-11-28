#!/usr/bin/env python3
"""Ficha bibliográfica con iconos de cada libro (docs/biblioteca/<libro>/index.html).

  python3 scripts/biblioteca/ficha.py            pone la ficha en todas las páginas que aún no la tienen
  python3 scripts/biblioteca/ficha.py --mira     dice cuántas cambiaría, sin escribir

Qué hace en cada página (una ya hecha no se vuelve a tocar):
- Cambia la tabla de datos antigua (`dl.lb-dl`) por una lista de filas finas (`dl.lb-det`), una por dato, con un icono
  pequeño junto a la etiqueta y los nombres de campo que usan las librerías: Editorial, Fecha de publicación, Idioma,
  Longitud de impresión, ISBN-10, ISBN-13…
- El año y el idioma de la apertura pasan también a la lista. Si el año de la obra y el de la edición no coinciden,
  salen los dos («Año de la obra» y «Fecha de publicación»).
- El ISBN-10 se calcula a partir del ISBN-13 (solo los que empiezan por 978 y tienen bien el dígito de control).
- Pone un icono pequeño en las etiquetas de temática y de medicina de la apertura.

No inventa datos: solo recoloca los que ya están en la página. Comprueba que el resto del texto no cambia y que
ningún dato de la tabla se pierde; si no, no escribe la página y lo dice.
Iconos: docs/biblioteca/iconos.svg (un <symbol> por icono). Estilos: bloque «Ficha bibliográfica con iconos», al
final de docs/biblioteca/biblioteca.css.
"""
import html
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
BIB = RAIZ / "docs" / "biblioteca"
VERSION = "20261128b"
CSS = f'<link rel="stylesheet" href="../biblioteca.css?v={VERSION}">'

TEMATICAS = {
    "Historia": "c-historia",
    "Otras lecturas": "c-otras",
    "Plantas y sustancias": "c-plantas",
    "Antropología, etnobotánica y chamanismo": "c-antropologia",
    "Divulgación y ciencia": "c-ciencia",
    "Terapia y clínica": "c-terapia",
    "Espiritualidad y filosofía": "c-espiritualidad",
    "Académico y obras de referencia": "c-academico",
    "Memorias y testimonios": "c-memorias",
    "Literatura y ficción": "c-literatura",
    "Política y sociedad": "c-politica",
    "Química y farmacología": "c-quimica",
    "Reducción de riesgos e integración": "c-riesgos",
}

# etiqueta de la tabla antigua -> (etiqueta nueva, icono, orden)
CAMPOS = {
    "Editorial": ("Editorial", "editorial", 10),
    "Editorial en el repertorio": ("Editorial", "editorial", 10),
    "Año": ("Fecha de publicación", "fecha", 20),
    "Año consignado": ("Fecha de publicación", "fecha", 20),
    "Edición": ("Edición", "edicion", 40),
    "Idioma": ("Idioma", "idioma", 50),
    "Páginas": ("Longitud de impresión", "paginas", 60),
    "Colección": ("Colección", "coleccion", 90),
    "Volumen": ("Volumen", "volumen", 100),
    "Sustancias": ("Sustancias", "sustancia", 110),
    "Título de la edición": ("Título de la edición", "titulo", 200),
    "Otros títulos documentados": ("Otros títulos", "otros", 210),
}


def icono(nombre):
    return f'<svg class="lb-i" aria-hidden="true" focusable="false"><use href="../iconos.svg#{nombre}"/></svg>'


def texto(trozo):
    return html.unescape(re.sub(r"<[^>]+>", " ", trozo))


def palabras(trozo):
    return sorted(texto(trozo).split())


def liso(t):
    return re.sub(r"[^0-9a-záéíóúüñ]", "", texto(t).casefold())


def isbn10(isbn13):
    """ISBN-10 que corresponde a un ISBN-13 de prefijo 978 con el dígito de control correcto; si no, ''."""
    d = [int(c) for c in isbn13]
    if len(d) != 13 or isbn13[:3] != "978":
        return ""
    if (10 - sum(n * (1 if i % 2 == 0 else 3) for i, n in enumerate(d[:12])) % 10) % 10 != d[12]:
        return ""
    nueve = d[3:12]
    control = sum((i + 1) * n for i, n in enumerate(nueve)) % 11
    return "".join(map(str, nueve)) + ("X" if control == 10 else str(control))


def fila(etiqueta, ico, valor):
    return f'<div class="lb-d"><dt>{icono(ico)}{etiqueta}</dt><dd>{valor}</dd></div>'


def lista(pares, anno_obra, idioma):
    """HTML de la lista de datos a partir de los pares de la tabla y de la apertura ('' si no hay nada)."""
    filas = []  # (orden, html)
    anno_edicion = ""
    tiene_idioma = False
    for etiqueta, valor in pares:
        limpio = texto(valor).strip()
        if not re.search(r"\w", limpio):
            continue
        if etiqueta in ("ISBN", "ISBN de ediciones registradas"):
            if re.fullmatch(r"\d{13}", limpio):
                diez = isbn10(limpio)
                if diez:
                    filas.append((70, fila("ISBN-10", "isbn", diez)))
                filas.append((80, fila("ISBN-13", "isbn", f"{limpio[:3]}-{limpio[3:]}")))
            else:
                filas.append((80, fila("ISBN", "isbn", valor)))
            continue
        if etiqueta not in CAMPOS:
            filas.append((300, fila(etiqueta, "dato", valor)))
            continue
        nueva, ico, orden = CAMPOS[etiqueta]
        if nueva == "Fecha de publicación":
            anno_edicion = limpio
        if nueva == "Idioma":
            tiene_idioma = True
            valor = valor[:1].upper() + valor[1:]
        if nueva == "Longitud de impresión" and limpio.isdigit():
            valor = f"{limpio} páginas" if limpio != "1" else "1 página"
        filas.append((orden, fila(nueva, ico, valor)))
    if anno_obra and anno_obra != anno_edicion:
        filas.append((30, fila("Año de la obra", "obra", anno_obra)))
    if idioma and not tiene_idioma:
        filas.append((50, fila("Idioma", "idioma", idioma[:1].upper() + idioma[1:])))
    if not filas:
        return ""
    return '<dl class="lb-det">' + "".join(h for _, h in sorted(filas, key=lambda f: f[0])) + "</dl>"


def poner_ficha(s):
    """Devuelve (página nueva, motivo) — motivo no vacío si no se ha podido."""
    i0 = s.index('<main id="contenido" class="guia-cuerpo">')
    i1 = s.index("</main>", i0)
    main = s[i0:i1]
    if 'class="lb lb2"' not in main:
        return s, "no es una ficha puesta al día (lanza antes plantilla.py)"
    if 'class="lb-det"' in main:
        return re.sub(r'<link rel="stylesheet" href="\.\./biblioteca\.css[^>]*>', CSS, s), ""
    nuevo = main

    # apertura: año e idioma
    anno_obra = idioma = ""
    meta = re.search(r'<p class="lb-meta">(.*?)</p>', main, re.S)
    if meta:
        for parte in (p.strip() for p in texto(meta.group(1)).split("·")):
            if re.fullmatch(r"\d{3,4}", parte):
                anno_obra = parte
            elif parte and not idioma:
                idioma = parte

    # etiquetas de la apertura: icono de temática y de medicina
    etiquetas = re.search(r'<p class="lb-tags">(.*?)</p>', nuevo, re.S)
    if etiquetas:
        def con_icono(m):
            href, nombre = m.group(1), m.group(2)
            if "?cat=" in href:
                ico = TEMATICAS.get(html.unescape(nombre).strip())
                return f'<a href="{href}">{icono(ico)}{nombre}</a>' if ico else m.group(0)
            if "?sust=" in href:
                return f'<a href="{href}">{icono("sustancia")}{nombre}</a>'
            return m.group(0)
        dentro = re.sub(r'<a href="([^"]*)">([^<]*)</a>', con_icono, etiquetas.group(1))
        nuevo = nuevo[:etiquetas.start(1)] + dentro + nuevo[etiquetas.end(1):]

    # tabla de datos -> lista
    tablas = re.findall(r'<dl class="lb-dl">.*?</dl>', nuevo, re.S)
    if len(tablas) > 1:
        return s, "más de una tabla de datos"
    pares = []
    if tablas:
        dentro = tablas[0][len('<dl class="lb-dl">'):-len("</dl>")]
        pares = re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", dentro, re.S)
        if "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in pares) != dentro.strip():
            return s, "no reconozco la tabla de datos"
    bloque = lista(pares, anno_obra, idioma)
    titular = ""
    if tablas:
        if not bloque:
            return s, "la tabla de datos queda vacía"
        nuevo = nuevo.replace(tablas[0], bloque, 1)
    elif bloque:
        titular = "<h2>Ficha bibliográfica</h2>"
        descripciones = list(re.finditer(r'<p class="lb-desc">.*?</p>', nuevo, re.S))
        if descripciones:
            corte = descripciones[-1].end()
        else:
            datos = re.search(r'<div class="lb-datos">\n?', nuevo)
            if not datos:
                return s, "no encuentro dónde poner la ficha"
            corte = datos.end()
        nuevo = nuevo[:corte] + "\n" + titular + bloque + "\n" + nuevo[corte:].lstrip("\n")

    # comprobaciones: el resto del texto no cambia y ningún dato se pierde
    resto_antes = main.replace(tablas[0], " ", 1) if tablas else main
    resto_despues = nuevo.replace(bloque, " ", 1) if bloque else nuevo
    if titular:
        resto_despues = resto_despues.replace(titular, " ", 1)
    if palabras(resto_antes) != palabras(resto_despues):
        return s, "cambiaría el texto"
    en_bloque = liso(bloque)
    for etiqueta, valor in pares:
        if re.search(r"\w", texto(valor)) and liso(valor) not in en_bloque:
            return s, f"se perdería el dato «{etiqueta}»"

    s = s[:i0] + nuevo + s[i1:]
    return re.sub(r'<link rel="stylesheet" href="\.\./biblioteca\.css[^>]*>', CSS, s), ""


def main():
    mira = "--mira" in sys.argv
    hechas = fallos = 0
    for f in sorted(BIB.glob("*/index.html")):
        s = f.read_text(encoding="utf-8")
        if 'class="lb lb2"' not in s:
            continue
        nueva, motivo = poner_ficha(s)
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
