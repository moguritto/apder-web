# -*- coding: utf-8 -*-
"""Ficha de sustancia de Psiconáutica: la «SubstanceBox» de PsychonautWiki, en español.

Convierte un diccionario ya normalizado (ver EJEMPLO) en HTML sin JavaScript.
El estilo está en docs/psiconautica/wiki.css, bloque «ficha de sustancia» (.wk-fs).

Reglas que no se tocan:
 1. Las cifras se pintan tal cual llegan: no se calculan, convierten ni redondean.
    La unidad acompaña a cada cifra de dosis.
 2. La curva es un esquema: usa los valores medios solo para dibujar y no escribe cifras.
 3. Si falta un dato, su fila no sale. Nunca se rellena con nada.

Formato de los datos:
 - dosis:    {"umbral": (min, max), "ligera": ..., "comun": ..., "fuerte": ..., "alta": ...}
             min y max son TEXTO tal cual la fuente; max vacío si solo hay una cifra.
 - duracion: {"total": (min, max, unidad), "inicio": ..., "subida": ..., "pico": ..., "bajada": ..., "posteriores": ...}
             unidad en inglés y plural: seconds, minutes, hours, days, weeks.
"""
import html
import os
import re


def esc(s):
    return html.escape(str(s), quote=True)


VIAS = {"oral": "Oral", "sublingual": "Sublingual", "buccal": "Bucal", "insufflated": "Esnifada", "intranasal": "Intranasal",
        "smoked": "Fumada", "inhaled": "Inhalada", "vaporized": "Vaporizada", "intravenous": "Intravenosa",
        "intramuscular": "Intramuscular", "subcutaneous": "Subcutánea", "rectal": "Rectal", "transdermal": "Transdérmica"}
NIVELES = (("umbral", "Umbral"), ("ligera", "Ligera"), ("comun", "Común"), ("fuerte", "Fuerte"), ("alta", "Muy fuerte"))
FASES = (("total", "Total"), ("inicio", "Inicio"), ("subida", "Subida"), ("pico", "Pico"), ("bajada", "Bajada"),
         ("posteriores", "Efectos posteriores"))
TIEMPO = {"seconds": ("segundo", "segundos", 1 / 60.0), "minutes": ("minuto", "minutos", 1.0), "hours": ("hora", "horas", 60.0),
          "days": ("día", "días", 1440.0), "weeks": ("semana", "semanas", 10080.0)}
MICRO = ("µg", "μg", "ug", "mcg")
INTERACCIONES = (("peligrosa", "Peligrosas"), ("insegura", "Inseguras"), ("incierta", "Inciertas"))
SECCION = {"guia": "Guía", "micro": "Microdosis", "terapia": "Terapia", "enciclopedia": "Enciclopedia de medicinas",
           "biblioteca": "Biblioteca", "persona": "Quién es quién"}
LICENCIA = "https://creativecommons.org/licenses/by-sa/4.0/deed.es"

# Los datos de la captura que mandó Mannu (2C-B, vía oral). Sirve de muestra del formato.
EJEMPLO = {
    "nombre": "2C-B",
    "imagen": "",                                   # ruta de la imagen de la molécula, o vacío
    "comunes": ["2C-B", "Nexus", "Bromo Mescaline", "BDMPEA", "Venus"],
    "sustitutivo": "4-Bromo-2,5-dimethoxyphenethylamine",
    "sistematico": "",
    "clase_psicoactiva": [("Psicodélico", "../psychedelic/")],      # (texto, enlace o vacío)
    "clase_quimica": [("Feniletilamina", "")],
    "vias": [{
        "via": "oral", "unidad": "mg", "biodisponibilidad": "",
        "dosis": {"umbral": ("5", ""), "ligera": ("10", "15"), "comun": ("15", "25"), "fuerte": ("25", "45"), "alta": ("45", "")},
        "duracion": {"total": ("5", "7", "hours"), "inicio": ("20", "40", "minutes"), "subida": ("60", "90", "minutes"),
                     "pico": ("60", "90", "minutes")},
        "notas": [],                                # frases ya en HTML (por ejemplo, la leyenda de la vía)
    }],
    "interacciones": {},                            # {"peligrosa": [(texto, enlace)], "insegura": [...], "incierta": [...]}
    "otras": [],                                    # [(título de sección, [(etiqueta, valor en HTML)])] para lo que tenga la original
    "original": "https://psychonautwiki.org/wiki/2C-B",
    "fecha": "26-11-2026",                          # día en que se descargaron los datos
}


def _t(x):
    return str(x if x is not None else "").strip()


def rango(a, b=""):
    a, b = _t(a), _t(b)
    return esc(a) + ("–" + esc(b) if b and b != a else "")


def unidad(u):
    u = _t(u)
    return "µg" if u in MICRO else u


def dosis_txt(clave, v, u):
    v = (list(v or ()) + ["", ""])[:2]
    if not _t(v[0]) or not unidad(u):
        return ""
    t = "%s %s" % (rango(v[0], v[1]), esc(unidad(u)))
    return t + " +" if clave == "alta" and not _t(v[1]) else t


def tiempo_txt(v):
    if not v or len(v) < 3 or not _t(v[0]) or v[2] not in TIEMPO:
        return ""
    a, b = _t(v[0]), _t(v[1])
    uno = a == "1" and b in ("", "1")
    return "%s %s" % (rango(a, b), TIEMPO[v[2]][0 if uno else 1])


def minutos(v):
    """Valor medio en minutos. Solo para dibujar la curva."""
    try:
        a = float(_t(v[0]))
        b = float(_t(v[1]) or a)
        return (a + b) / 2.0 * TIEMPO[v[2]][2]
    except (TypeError, ValueError, KeyError, IndexError):
        return None


def curva(dur, via):
    m = {k: minutos(dur.get(k)) for k in ("inicio", "subida", "pico", "bajada", "total")}
    if not (m["subida"] or m["pico"]) or not (m["bajada"] or m["total"]):
        return ""
    on, up, pk = m["inicio"] or 0.0, m["subida"] or 0.0, m["pico"] or 0.0
    off = m["bajada"] or max((m["total"] or 0.0) - (on + up + pk), 0.0)
    if up <= 0:
        up = 0.12 * (on + pk + off)
    if off <= 0:
        off = 0.4 * (on + up + pk)
    cola = bool(tiempo_txt(dur.get("posteriores")))
    x0, x4, arriba, base = 8.0, (236.0 if cola else 272.0), 9.0, 50.0
    k = (x4 - x0) / (on + up + pk + off)
    x1 = x0 + on * k
    x2 = x1 + up * k
    x3 = x2 + pk * k

    def f(n):
        return ("%.1f" % n).rstrip("0").rstrip(".")

    d = "M%s,%s L%s,%s C%s,%s %s,%s %s,%s L%s,%s C%s,%s %s,%s %s,%s" % tuple(f(n) for n in (
        x0, base, x1, base, (x1 + x2) / 2, base, (x1 + x2) / 2, arriba, x2, arriba, x3, arriba,
        x3 + (x4 - x3) * .4, arriba, x3 + (x4 - x3) * .6, base, x4, base))
    p = ['<svg viewBox="0 0 280 70" role="img" aria-label="%s">' % esc("Esquema de la duración por vía " + via.lower()),
         '<path class="area" d="%s Z"/>' % d,
         '<line class="eje" x1="8" y1="%s" x2="272" y2="%s"/>' % (f(base), f(base))]
    for x in (x1, x2, x3):
        if x0 + 1 < x < x4 - 1:
            p.append('<line class="sep" x1="%s" y1="%s" x2="%s" y2="%s"/>' % (f(x), f(arriba - 3), f(x), f(base)))
    p.append('<path class="linea" d="%s"/>' % d)
    tramos = [("Inicio", x0, x1, m["inicio"]), ("Subida", x1, x2, m["subida"]), ("Pico", x2, x3, m["pico"]), ("Bajada", x3, x4, True)]
    if cola:
        p.append('<line class="cola" x1="%s" y1="%s" x2="272" y2="%s"/>' % (f(x4), f(base), f(base)))
        tramos.append(("Después", x4, 272.0, True))
    for nombre, a, b, hay in tramos:
        if hay and b - a >= len(nombre) * 5.6 + 2:
            p.append('<text x="%s" y="64">%s</text>' % (f((a + b) / 2), nombre))
    p.append("</svg>")
    return ('<figure class="wk-fs-curva">%s<figcaption>Esquema con los valores medios de la tabla. '
            "Cada experiencia es distinta.</figcaption></figure>" % "".join(p))


def via_html(v, grupo, abierta):
    nombre = VIAS.get(_t(v.get("via")).lower(), _t(v.get("via")).capitalize())
    u = v.get("unidad") or ""
    dos, dur = v.get("dosis") or {}, v.get("duracion") or {}
    filas_d = [(i + 1, et, dosis_txt(k, dos.get(k), u)) for i, (k, et) in enumerate(NIVELES)]
    filas_d = [x for x in filas_d if x[2]]
    filas_t = [(et, tiempo_txt(dur.get(k))) for k, et in FASES]
    filas_t = [x for x in filas_t if x[1]]
    comun = dosis_txt("comun", dos.get("comun"), u)
    resumen = ", ".join(x for x in ("común " + comun if comun else "", tiempo_txt(dur.get("total"))) if x)
    p = ['<details class="wk-fs-via" name="%s"%s>' % (esc(grupo), " open" if abierta else ""),
         "<summary><b>%s</b>%s</summary>" % (esc(nombre), "<span>%s</span>" % resumen if resumen else "")]
    bio = _t(v.get("biodisponibilidad"))
    if filas_d or bio:
        p.append('<p class="wk-fs-cap">Dosis</p><table class="wk-fs-dosis" aria-label="%s">' % esc("Dosis por vía " + nombre.lower()))
        p += ['<tr class="n%d"><th scope="row">%s</th><td>%s</td></tr>' % x for x in filas_d]
        if bio:
            p.append('<tr><th scope="row">Biodisponibilidad</th><td>%s</td></tr>' % esc(bio))
        p.append("</table>")
        if unidad(u) == "µg":
            p.append('<p class="wk-fs-ug">µg son microgramos: 1 mg equivale a 1000 µg.</p>')
    if filas_t:
        p.append('<p class="wk-fs-cap">Duración</p>' + curva(dur, nombre))
        p.append('<table class="wk-fs-dur" aria-label="%s">' % esc("Duración por vía " + nombre.lower()))
        p += ['<tr><th scope="row">%s</th><td>%s</td></tr>' % x for x in filas_t]
        p.append("</table>")
    p += ['<p class="wk-fs-ug">%s</p>' % n for n in v.get("notas") or []]
    p.append("</details>")
    return "".join(p)


def _enlaces(lista):
    return ", ".join('<a href="%s">%s</a>' % (esc(h), esc(t)) if h else esc(t) for t, h in lista or [])


def _tabla(titulo, filas, clase=""):
    """filas: (etiqueta, valor en HTML, atributos de la fila)."""
    filas = [x for x in filas if x[1]]
    if not filas:
        return ""
    return '<p class="wk-fs-sec">%s</p><table%s>%s</table>' % (
        esc(titulo), ' class="%s"' % clase if clase else "",
        "".join('<tr%s><th scope="row">%s</th><td>%s</td></tr>' % (x[2] if len(x) > 2 else "", esc(x[0]), x[1]) for x in filas))


def ficha(d, uso_responsable="../responsible-drug-use/"):
    nombre = d["nombre"]
    p = ['<aside class="wk-fs" aria-label="%s">' % esc("Ficha de " + nombre), '<p class="wk-fs-tit">%s</p>' % esc(nombre)]
    if d.get("imagen"):
        p.append('<figure class="wk-fs-mol"><img src="%s" alt="%s" loading="lazy" decoding="async"></figure>'
                 % (esc(d["imagen"]), esc("Estructura química de " + nombre)))
    en = lambda s: '<span lang="en">%s</span>' % esc(s) if _t(s) else ""
    p.append(_tabla("Nomenclatura", [("Nombres comunes", esc(", ".join(d.get("comunes") or []))),
                                     ("Nombre sustitutivo", en(d.get("sustitutivo"))),
                                     ("Nombre sistemático", en(d.get("sistematico")))]))
    p.append(_tabla("Clasificación", [("Clase psicoactiva", _enlaces(d.get("clase_psicoactiva"))),
                                      ("Clase química", _enlaces(d.get("clase_quimica")))]))
    vias = [v for v in d.get("vias") or [] if v.get("dosis") or v.get("duracion")]
    if vias:
        p.append('<p class="wk-fs-sec">Vías de administración</p>')
        p.append('<p class="wk-fs-aviso"><strong>Empieza siempre por dosis bajas.</strong> El peso, la tolerancia, el metabolismo '
                 'y la sensibilidad cambian de una persona a otra. <a href="%s">Consumo responsable</a>.</p>' % esc(uso_responsable))
        grupo = "via-" + re.sub(r"[^a-z0-9]+", "-", nombre.lower()).strip("-")
        p += [via_html(v, grupo, i == 0) for i, v in enumerate(vias)]
        p.append('<p class="wk-fs-nota">PsychonautWiki recoge estas dosis de usuarios y de otras fuentes, con fines educativos. '
                 "No son una recomendación: contrástalas con otras fuentes.</p>")
    inter = d.get("interacciones") or {}
    p.append(_tabla("Interacciones", [(et, _enlaces(inter.get(k)), ' class="%s"' % k) for k, et in INTERACCIONES], "wk-fs-int"))
    for titulo, filas in d.get("otras") or []:
        p.append(_tabla(titulo, filas))
    fuente = [("Original", '<a class="ext" href="%s" rel="noopener" lang="en">%s</a>, en PsychonautWiki' % (esc(d["original"]), esc(nombre))),
              ("Datos", "descargados el %s" % esc(d["fecha"]) if d.get("fecha") else ""),
              ("Licencia", '<a class="ext" href="%s" rel="license noopener">CC BY-SA 4.0</a>' % LICENCIA)]
    p.append(_tabla("Fuente", fuente))
    p.append("</aside>")
    return "".join(x for x in p if x)


# ---------- puentes con el resto de apder.org ----------

def leer_destino(docs, ruta):
    """Título y descripción de una página de la web, para su tarjeta. ruta: «sustancias/lsd/»."""
    try:
        with open(os.path.join(docs, ruta, "index.html"), encoding="utf-8") as fh:
            h = fh.read()
    except OSError:
        return None
    t = re.search(r"<title>(.*?)</title>", h, re.S)
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    titulo = re.sub(r"\s*[|·]\s*APDER\s*$", "", html.unescape(t.group(1)).strip()) if t else ""
    corto = re.split(r":| \(| \| ", titulo)[0].strip()         # «LSD: guía completa» -> «LSD»
    return {"titulo": titulo, "corto": corto, "desc": html.unescape(m.group(1)).strip() if m else ""}


def _frase(x):
    t = x["tipo"]
    if t == "guia":
        return "guía completa"
    if t == "micro":
        return "guía de microdosis"
    if t == "terapia":
        return "guía de terapia"
    if t == "enciclopedia":
        return "«%s» en la Enciclopedia de medicinas" % (x.get("corto") or x["titulo"])
    if t == "biblioteca":
        return "%s en la Biblioteca" % x["titulo"]          # el título es «82 libros»
    return "%s, en Quién es quién" % (x.get("corto") or x["titulo"])


def tambien(puentes):
    """Nota de cabecera, al estilo de las de la wiki. puentes: [{"tipo", "titulo", "desc", "href"}]."""
    if not puentes:
        return ""
    partes = ['<a href="%s">%s</a>' % (esc(x["href"]), esc(_frase(x))) for x in puentes]
    lista = partes[0] if len(partes) == 1 else ", ".join(partes[:-1]) + " y " + partes[-1]
    return '<p class="wk-tambien">Esta página es la ficha traducida de PsychonautWiki. APDER tiene además: %s.</p>' % lista


def sigue(puentes, nombre):
    """Tarjetas al final del artículo."""
    if not puentes:
        return ""
    li = "".join('<li><a href="%s"><span>%s</span><b>%s</b>%s</a></li>' % (
        esc(x["href"]), SECCION[x["tipo"]], esc(x.get("corto") if x["tipo"] in ("enciclopedia", "persona") and x.get("corto") else x["titulo"]),
        "<small>%s</small>" % esc(x["desc"]) if x.get("desc") else "")
        for x in puentes)
    return ('<nav class="wk-puentes" aria-label="%s"><h2>Sigue en APDER</h2>'
            "<p>Contenido propio de APDER, aparte de la traducción de la wiki.</p><ul>%s</ul></nav>"
            % (esc("Más sobre %s en APDER" % nombre), li))
