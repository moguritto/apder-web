#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera Psiconáutica (docs/psiconautica/): la portada con buscador e índice A–Z y una página por artículo.

    python3 scripts/psiconautica/generar.py                      rehace todo con lo ya publicado en docs/psiconautica/
    python3 scripts/psiconautica/generar.py --json CARPETA       añade o sustituye páginas desde archivos .json
    python3 scripts/psiconautica/generar.py --excluidas ARCHIVO  no publica esos títulos (uno por línea: título original o slug)

Formato de cada .json (lo escribe el traductor, en el Mac):
    {"slug": "lsd", "titulo": "LSD", "original": "LSD", "cuerpo": "<p>…</p><h2>…</h2>…",
     "tipo": "sustancia|efecto|cuidado|concepto" (opcional: si falta, se deduce),
     "nota": "frase de presentación" (opcional), "alias": ["ácido", "lisérgida"] (opcional)}

Qué hace con cada cuerpo, siempre (reglas del sitio):
- quita los apartados y enlaces de legalidad, los apartados vacíos y los avisos sueltos de dosis;
- convierte en enlaces internos los que apuntan a páginas de PsychonautWiki ya traducidas;
- marca los enlaces externos, pone anclas a los apartados y prepara el índice de la página.
La cabecera y el pie se copian de docs/sustancias/, así siguen al resto del sitio. Solo biblioteca estándar.
El resultado es estable: volver a generar una página ya generada la deja igual."""
import argparse
import glob
import html
import json
import os
import re
import sys
import unicodedata
from urllib.parse import unquote

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(AQUI, "..", "..", "docs"))
SALIDA = os.path.join(DOCS, "psiconautica")
VERSION = "20261125c"          # cambia al tocar psiconautica.css o psiconautica.js
WIKI = "https://psychonautwiki.org/wiki/"
LICENCIA = "https://creativecommons.org/licenses/by-sa/4.0/deed.es"

TIPOS = {            # clave: (singular, plural, letra del índice)
    "sustancia": ("Sustancia", "Sustancias", "s"),
    "efecto": ("Efecto", "Efectos", "e"),
    "cuidado": ("Cuidado", "Cuidado", "c"),
    "concepto": ("Concepto", "Conceptos", "o"),
}
TIPO_ANTIGUO = {"medicina": "sustancia", "cuidado": "cuidado", "efecto subjetivo": "efecto"}
# Páginas de cuidado y reducción de riesgos (por título original). El resto se deduce del texto.
CUIDADO = {"responsible use", "set and setting", "trip sitter", "bad trip", "harm reduction", "integration",
           "psychedelic integration", "safer drug use", "recovery position", "overdose", "first aid",
           "testing kits", "reagent testing kits", "drug checking", "tripsitting", "grounding", "aftercare",
           "preparation", "psychedelic first aid", "dangerous combinations", "drug combinations", "combinations"}
# Nunca se publican (regla del sitio): discusión, elaboración, extracción, síntesis, cultivo, dosificación y legalidad.
FUERA = re.compile(r"^(talk|user|user talk|template|category|file|help|psychonautwiki)\s*:|"
                   r"\b(extraction|synthesis|synthesizing|cultivation|cultivating|growing|grow guide|tek|dosage|dosing|"
                   r"volumetric|routes? of administration|preparation methods?|recipe|legal(ity| status)?)\b", re.I)
# Orden de los atajos de la portada y del bloque «Antes de una experiencia» (por título original).
PREFERIDAS = ["Psilocybin mushrooms", "LSD", "MDMA", "Ayahuasca", "Ego death", "Unity and interconnectedness", "Ketamine", "DMT"]
ANTES = ["Responsible use", "Set and setting", "Trip sitter", "Bad trip", "Harm reduction", "Integration"]
# Apartados que no se publican: dosis y administración (en cualquier página) y elaboración (en las de sustancias,
# donde «Preparación» es cómo se hace; en las de cuidado es prepararse para la experiencia y sí se publica).
AP_DOSIS = re.compile(r"\b(dosis|dosificaci[oó]n|posolog[ií]a|v[ií]as? de administraci[oó]n|pharmahuasca|redosificaci[oó]n)\b", re.I)
AP_ELABORA = re.compile(r"\b(preparaci[oó]n|elaboraci[oó]n|extracci[oó]n|s[ií]ntesis|cultivo|recetas?)\b", re.I)
# Cantidades sueltas («50 mg», «3,5 g», «100 µg»): se quita la frase entera.
CANTIDAD = re.compile(r"\d(?:\s|&nbsp;|\u00a0)*(?:mg|µg|μg|mcg|ug|ml|miligramos?|microgramos?|mililitros?|gramos?|g)\b", re.I)
LEGAL = re.compile(r"\b(legal|legalidad|ilegal|leyes|fiscalizaci[oó]n)\b|\blegal status\b", re.I)


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def esc(s):
    return html.escape(s, quote=True)


def texto(s):
    """HTML -> texto plano en una línea."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def slugificar(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def clave_wiki(t):
    """Título de PsychonautWiki normalizado para comparar: sin ancla, sin guiones bajos y en minúsculas."""
    t = unquote(t).split("#")[0].replace("_", " ").strip()
    return re.sub(r"\s+", " ", t).lower()


def orden(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


# ------------------------------------------------------------------ LECTURA
def de_json(ruta):
    d = json.loads(leer(ruta))
    d.setdefault("slug", os.path.splitext(os.path.basename(ruta))[0])
    d.setdefault("original", d.get("titulo", ""))
    return d


def de_html(ruta):
    """Lee una página ya publicada: la de esta plantilla (data-*) o la provisional del 23-11-2026."""
    s = leer(ruta)
    slug = os.path.basename(os.path.dirname(ruta))
    m = re.search(r'<main id="contenido" class="psi"([^>]*)>', s)
    if m:                                                    # plantilla nueva
        a = dict(re.findall(r'data-([a-z-]+)="([^"]*)"', m.group(1)))
        cuerpo = s[s.find("<!--cuerpo-->") + 13:s.find("<!--/cuerpo-->")]
        return {"slug": slug, "titulo": html.unescape(re.search(r"<h1>(.*?)</h1>", s, re.S).group(1)),
                "original": html.unescape(a.get("original", "")), "tipo": a.get("tipo", ""),
                "nota": html.unescape(a.get("nota", "")), "alias": [x for x in html.unescape(a.get("alias", "")).split("|") if x],
                "cuerpo": cuerpo}
    if 'class="s-cabeza"' not in s:
        return None
    ante = texto(re.search(r'<p class="s-antetitulo">(.*?)</p>', s, re.S).group(1)).split("·")[-1].strip().lower()
    nota = re.search(r'<p class="s-nota">(.*?)</p>', s, re.S)
    orig = re.search(r'<p class="e-atrib">.*?href="' + re.escape(WIKI) + r'([^"]+)"[^>]*>(.*?)</a>', s, re.S)
    art = s[s.find('<article class="s-cuerpo">') + 26:s.find("</article>")]
    return {"slug": slug, "titulo": texto(re.search(r"<h1>(.*?)</h1>", s, re.S).group(1)),
            "original": texto(orig.group(2)) if orig else "", "tipo": TIPO_ANTIGUO.get(ante, ""),
            "nota": texto(nota.group(1)) if nota else "", "alias": [], "cuerpo": art}


# ------------------------------------------------------------------ CUERPO
CAB = re.compile(r"<h([2-4])\b[^>]*>(.*?)</h\1>", re.S)


def quitar_apartados(c, prueba, hijos=True):
    """Quita cada apartado cuyo título cumple `prueba`: con todo lo que cuelga de él o, con hijos=False,
    solo con su texto propio (los subapartados se quedan y se juzgan por su título)."""
    while True:
        for m in CAB.finditer(c):
            if not prueba(texto(m.group(2))):
                continue
            nivel = int(m.group(1))
            fin = len(c)
            for n in CAB.finditer(c, m.end()):
                if not hijos or int(n.group(1)) <= nivel:
                    fin = n.start()
                    break
            c = c[:m.start()] + c[fin:]
            break
        else:
            return c


def sin_cantidades(c, cuenta):
    """Quita las frases con cantidades de sustancia de párrafos y elementos de lista. Suma en cuenta[0] las quitadas."""
    def bloque(m):
        abre, dentro, cierra = m.group(1), m.group(2), m.group(3)
        if not CANTIDAD.search(dentro) or re.search(r"<(ul|ol|p|table)\b", dentro):
            return m.group(0)
        frases = re.split(r"(?<=[.!?…»])\s+(?=(?:<[a-z][^>]*>)*[A-ZÁÉÍÓÚÑ¿¡«])", dentro.strip())
        quedan = [f for f in frases if not CANTIDAD.search(f)]
        cuenta[0] += len(frases) - len(quedan)
        resto = " ".join(quedan)
        cojo = any(len(re.findall(r"<%s\b" % t, resto)) != len(re.findall(r"</%s>" % t, resto)) for t in ("a", "strong", "em", "b", "i", "sup", "span"))
        if not quedan or cojo or len(texto(resto)) < 12:
            return ""
        return abre + resto + cierra
    c = re.sub(r"(<p>)((?:(?!</p>).)*)(</p>)", bloque, c, flags=re.S)
    return re.sub(r"(<li>)((?:(?!</?li>).)*)(</li>)", bloque, c, flags=re.S)


def preparar_cuerpo(c, mapa, slug, tipo="", cuenta=None):
    """Devuelve (cuerpo limpio, [(id, título)] de los h2)."""
    cuenta = cuenta if cuenta is not None else [0]
    c = re.sub(r'<p class="e-atrib">.*?</p>', "", c, flags=re.S)
    c = re.sub(r"<p><em>La información de dosis no se traduce.*?</em></p>", "", c, flags=re.S)
    c = re.sub(r'<div class="p-tabla">(.*?)</div>', r"\1", c, flags=re.S)              # se vuelve a poner abajo
    c = quitar_apartados(c, lambda t: bool(LEGAL.search(t) or AP_DOSIS.search(t)))
    if tipo == "sustancia":
        c = quitar_apartados(c, lambda t: bool(AP_ELABORA.search(t)), hijos=False)
    c = sin_cantidades(c, cuenta)
    c = re.sub(r"<li>(?:(?!</li>).)*?(?:Legal status|[Ee]statu[st] legal|[Ss]ituación legal|[Ll]egalidad)(?:(?!</li>).)*?</li>\s*", "", c, flags=re.S)
    c = re.sub(r"</ul>\s*<ul>", "\n", c)
    c = re.sub(r"<(ul|ol)>\s*</\1>", "", c)
    # párrafos que anuncian una lista que no vino («…incluyen:») y apartados que se quedan vacíos
    antes = None
    while antes != c:
        antes = c
        c = re.sub(r"<p>((?:(?!</p>).)*?:)\s*</p>\s*(?=<h[2-4]\b|$)", _sin_anuncio, c, flags=re.S)
        c = re.sub(r"<h([2-4])\b[^>]*>(?:(?!</h\1>).)*</h\1>\s*(?=<h[2-4]\b|$)",
                   lambda m: "" if _vacio(m, c) else m.group(0), c, flags=re.S)
    # enlaces
    def enlace(m):
        attrs, dentro = m.group(1), m.group(2)
        h = re.search(r'href="([^"]*)"', attrs)
        href = html.unescape(h.group(1)) if h else ""
        if href.startswith(WIKI):
            dest = mapa.get(clave_wiki(href[len(WIKI):]))
            if dest and dest != slug:
                return '<a href="../%s/">%s</a>' % (dest, dentro)
            if dest == slug:
                return dentro
        if href.startswith(("http://", "https://")):
            return '<a class="ext" href="%s" rel="noopener">%s</a>' % (esc(href), dentro)
        if re.fullmatch(r"\.\./[a-z0-9-]+/", href):
            if href == "../%s/" % slug:
                return dentro
            return '<a href="%s">%s</a>' % (href, dentro)
        return m.group(0)
    c = re.sub(r"<a\b([^>]*)>(.*?)</a>", enlace, c, flags=re.S)
    # anclas e índice
    indice, usados = [], set()

    def cab(m):
        nivel, dentro = m.group(1), m.group(2)
        dentro = re.sub(r'^<span class="n">\d+</span>', lambda x: re.sub(r"<[^>]+>", "", x.group(0)) + ". ", dentro)
        t = texto(dentro)
        if nivel == "4":
            n = re.match(r"(\d+)\.\s+(.*)", dentro, re.S)
            if n:
                return '<h4 class="p-nivel"><span class="n">%s</span>%s</h4>' % (n.group(1), n.group(2))
            return "<h4>%s</h4>" % dentro
        ident = base = slugificar(t) or "apartado"
        k = 2
        while ident in usados:
            ident = "%s-%d" % (base, k)
            k += 1
        usados.add(ident)
        if nivel == "2":
            indice.append((ident, t))
        return '<h%s id="%s">%s</h%s>' % (nivel, ident, dentro, nivel)
    c = CAB.sub(cab, c)
    c = re.sub(r"(<table\b.*?</table>)", r'<div class="p-tabla">\1</div>', c, flags=re.S)
    c = re.sub(r"\n{2,}", "\n", c).strip()
    return c, indice


def _sin_anuncio(m):
    """De un párrafo que anuncia una lista que no vino, quita solo la frase del anuncio."""
    frases = re.split(r"(?<=[.!?…»])\s+(?=(?:<[a-z][^>]*>)*[A-ZÁÉÍÓÚÑ¿¡«])", m.group(1).strip())
    resto = " ".join(frases[:-1])
    return "<p>%s</p>\n" % resto if len(texto(resto)) > 30 else ""


def _vacio(m, c):
    """Un encabezado está vacío si lo siguiente es un encabezado de su nivel o superior (o el final)."""
    resto = c[m.end():].lstrip()
    if not resto:
        return True
    n = re.match(r"<h([2-4])\b", resto)
    return bool(n) and int(n.group(1)) <= int(m.group(1))


def deducir_tipo(d, cuerpo):
    if d.get("tipo") in TIPOS:
        return d["tipo"]
    if clave_wiki(d.get("original", "")) in CUIDADO:
        return "cuidado"
    cabs = " | ".join(texto(m.group(2)).lower() for m in CAB.finditer(cuerpo))
    if "sustancias psicoactivas" in cabs or "informes de experiencias" in cabs or "sustancias que pueden causar este efecto" in cuerpo:
        return "efecto"
    if re.search(r"\b(química|farmacología|toxicidad|efectos subjetivos)\b", cabs):
        return "sustancia"
    return "concepto"


def primera_frase(cuerpo, tope=230):
    m = re.search(r"<p>(.*?)</p>", cuerpo, re.S)
    t = texto(m.group(1)) if m else ""
    f = re.match(r"(.{40,}?[.!?])(\s|$)", t)
    t = f.group(1) if f else t
    if len(t) > tope:
        t = t[:tope].rsplit(" ", 1)[0].rstrip(" ,;:") + "…"
    return t


def descripcion(d, cuerpo):
    """Meta description de 120 a 160 caracteres (lo exige el comprobador)."""
    base = d.get("nota") or primera_frase(cuerpo, 400)
    cola = " Página de Psiconáutica, traducida de PsychonautWiki y sin información de dosis."
    t = base
    if len(t) < 120:
        t = (base.rstrip(".") + ".") + cola if base else "%s:%s" % (d["titulo"], cola.lower())
    if len(t) < 120:
        t = "%s. %s" % (d["titulo"], t)
    if len(t) > 160:
        t = t[:159].rsplit(" ", 1)[0].rstrip(" ,;:.") + "…"
    while len(t) < 120:
        t = t.rstrip("….") + ", en español."
    return t


# ------------------------------------------------------------------ MARCO
def marco(origen):
    s = leer(os.path.join(DOCS, origen))
    cab = s[s.find('<header class="cabecera"'):s.find("</header>") + 9].replace(' aria-current="page"', "")
    cab = cab.replace("menu-abre actual", "menu-abre").replace(
        'menu-abre" aria-expanded="false" aria-controls="panel-experiencia"',
        'menu-abre actual" aria-expanded="false" aria-controls="panel-experiencia"')          # Psiconáutica va en «La experiencia» (menú del 25-11-2026)
    pie = s[s.find("<footer"):s.find("</footer>") + 9]
    css = re.search(r'tierra\.css\?v=[^"]+', s)
    menu = re.search(r'menu\.js\?v=[^"]+', s)
    return cab, pie, (css.group(0) if css else "tierra.css"), (menu.group(0) if menu else "menu.js")


def documento(ruta_rel, titulo, desc, cuerpo, pre, origen, tipo_og="article"):
    cab, pie, css, menu = marco(origen)
    url = "https://apder.org/" + ruta_rel
    assert 120 <= len(desc) <= 160, "descripción de %d caracteres en %s" % (len(desc), ruta_rel)
    assert 'href="#"' not in cuerpo, "enlace vacío en " + ruta_rel
    doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)} | APDER</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{tipo_og}">
<meta property="og:site_name" content="APDER">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://apder.org/img/og-apder.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(titulo)} · APDER">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://apder.org/img/og-apder.png">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{pre}favicon.ico" sizes="32x32">
<link rel="icon" href="{pre}img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}img/apple-touch-icon.png">
<link rel="preload" href="{pre}fuentes/dm-serif-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{pre}fuentes/nunito-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}{css}">
<link rel="stylesheet" href="{pre}psiconautica/psiconautica.css?v={VERSION}">
</head>
<body class="psiconautica">
<a class="saltar" href="#contenido">Saltar al contenido</a>
{cab}
{cuerpo}
{pie}
<script src="{pre}{menu}" defer></script>
<script src="{pre}tierra.js" defer></script>
<script src="{pre}psiconautica/psiconautica.js?v={VERSION}" defer></script>
</body>
</html>
'''
    destino = os.path.join(DOCS, ruta_rel, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(doc)
    return len(doc.encode("utf-8"))


LUPA = ('<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.5" '
        'fill="none" stroke="currentColor" stroke-width="2"/><path d="M15.5 15.5 20 20" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round"/></svg>')


# ------------------------------------------------------------------ ARTÍCULO
def articulo(d):
    sing, plur, _ = TIPOS[d["tipo"]]
    toc = d["indice"]
    orig_url = WIKI + esc(d["original"].replace(" ", "_"))
    lis = "".join('<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in toc)
    toc_lado = '<nav class="p-toc" aria-label="En esta página"><p>En esta página</p><ol>%s</ol></nav>' % lis if len(toc) > 1 else ""
    toc_movil = '<details class="s-toc-movil"><summary>En esta página</summary><ol>%s</ol></details>' % lis if len(toc) > 1 else ""
    entrada = '<p class="p-entrada">%s</p>' % esc(d["nota"]) if d.get("nota") else ""
    atr = ' data-tipo="%s" data-original="%s"' % (d["tipo"], esc(d["original"]))
    if d.get("nota"):
        atr += ' data-nota="%s"' % esc(d["nota"])
    if d.get("alias"):
        atr += ' data-alias="%s"' % esc("|".join(d["alias"]))
    cuerpo = f'''<main id="contenido" class="psi"{atr}>
<header class="p-cabeza t-{d["tipo"]}">
<div class="ancho p-cabeza-in">
<nav class="p-miga" aria-label="Estás en"><a href="../">Psiconáutica</a><span aria-hidden="true">/</span><a href="../?tipo={d["tipo"]}">{plur}</a></nav>
<h1>{esc(d["titulo"])}</h1>
{entrada}
<form class="p-busca p-busca-mini" action="../" method="get" role="search"><label class="p-oculto" for="p-q">Buscar en Psiconáutica</label>{LUPA}<input id="p-q" name="q" type="search" placeholder="Buscar otra sustancia o efecto" autocomplete="off"></form>
</div>
</header>
<div class="ancho p-pagina">
<article class="p-texto">
{toc_movil}
<!--cuerpo-->{d["cuerpo"]}<!--/cuerpo-->
</article>
<aside class="p-lado">
{toc_lado}
<dl class="p-ficha">
<div><dt>Tipo</dt><dd><a class="p-tipo t-{d["tipo"]}" href="../?tipo={d["tipo"]}">{sing}</a></dd></div>
<div><dt>Página original</dt><dd><a class="ext" href="{orig_url}" rel="noopener" lang="en">{esc(d["original"])}</a>, en PsychonautWiki</dd></div>
<div><dt>Dosis</dt><dd>Esta traducción no incluye cifras de dosis.</dd></div>
<div><dt>Licencia</dt><dd>Texto traducido y compartido con licencia <a class="ext" href="{LICENCIA}" rel="license noopener">CC BY-SA 4.0</a>. PsychonautWiki no ha participado en la traducción ni la respalda.</dd></div>
</dl>
</aside>
</div>
</main>'''
    return documento("psiconautica/%s/" % d["slug"], d["titulo"] + " · Psiconáutica", d["desc"], cuerpo, "../../",
                     "sustancias/2c-b/index.html")


# ------------------------------------------------------------------ PORTADA
def portada(pags):
    n = len(pags)
    cuenta = {k: sum(1 for p in pags if p["tipo"] == k) for k in TIPOS}
    filtros = '<button type="button" class="on" data-tipo="" aria-pressed="true">Todo <b>%d</b></button>' % n
    for k, (_, plur, _) in TIPOS.items():
        if cuenta[k]:
            filtros += '<button type="button" data-tipo="%s" aria-pressed="false"><i class="t-%s"></i>%s <b>%d</b></button>' % (k, k, plur, cuenta[k])
    por_orig = {clave_wiki(p["original"]): p for p in pags}
    cuid = [por_orig[clave_wiki(t)] for t in ANTES if clave_wiki(t) in por_orig]
    cuid = (cuid + [p for p in pags if p["tipo"] == "cuidado" and p not in cuid])[:6]
    antes = ""
    if cuid:
        antes = ('<section class="p-sec p-antes" id="antes" aria-labelledby="antes-t"><div class="ancho"><h2 id="antes-t">Antes de una experiencia</h2>'
                 '<p class="p-sub">Cómo llegas, dónde estás y quién te acompaña influyen tanto como la sustancia.</p><ul>%s</ul></div></section>'
                 % "".join('<li><a href="%s/"><b>%s</b><span>%s</span></a></li>' % (p["slug"], esc(p["titulo"]), esc(p["nota"] or p["frase"])) for p in cuid))
    pref = [por_orig[clave_wiki(t)] for t in PREFERIDAS if clave_wiki(t) in por_orig]
    pref = (pref + [p for p in cuid if p not in pref] + [p for p in pags if p not in pref and p not in cuid])[:5]
    atajos = "".join('<a href="%s/">%s</a>' % (p["slug"], esc(p["titulo"])) for p in pref)
    # índice A–Z
    letras = {}
    for p in sorted(pags, key=lambda p: orden(p["titulo"])):
        l = orden(p["titulo"])[:1].upper()
        letras.setdefault(l if l.isalpha() else "#", []).append(p)
    barra = "".join('<a href="#l-%s">%s</a>' % ("num" if l == "#" else l.lower(), l) for l in letras)
    az = ""
    for l, ps in letras.items():
        ident = "num" if l == "#" else l.lower()
        az += '<section class="p-letra" id="l-%s" aria-labelledby="lt-%s"><h3 id="lt-%s">%s</h3><ul>%s</ul></section>\n' % (
            ident, ident, ident, l,
            "".join('<li data-t="%s"><a href="%s/">%s</a></li>' % (p["tipo"], p["slug"], esc(p["titulo"])) for p in ps))
    leyenda = "".join('<span><i class="t-%s"></i>%s</span>' % (k, v[0]) for k, v in TIPOS.items() if cuenta[k])
    desc = "Psiconáutica: sustancias, efectos subjetivos y cuidado de la experiencia, en español. Traducción de PsychonautWiki, sin dosis."
    cuerpo = f'''<main id="contenido" class="psi" data-portada="1">
<header class="p-cabeza p-portada">
<div class="ancho p-cabeza-in">
<h1>Psiconáutica</h1>
<p class="p-entrada">La experiencia por dentro. {n} páginas sobre sustancias psicoactivas, los efectos que producen y cómo cuidar una experiencia, traducidas al español.</p>
<form class="p-busca" id="p-form" action="../buscar/" method="get" role="search"><label class="p-oculto" for="p-q">Buscar en Psiconáutica</label>{LUPA}<input id="p-q" name="q" type="search" placeholder="Busca una sustancia, un efecto o una idea" autocomplete="off" autocapitalize="off" spellcheck="false"></form>
<p class="p-atajos"><span>Por ejemplo</span>{atajos}</p>
</div>
</header>
<div class="ancho">
<div class="p-filtros" id="p-filtros" role="group" aria-label="Ver solo">{filtros}</div>
<p class="p-oculto" id="p-n" role="status" aria-live="polite"></p>
<ol class="p-res" id="p-res" hidden></ol>
</div>
<div id="p-resto">
{antes}
<section class="p-sec p-az" aria-labelledby="az-t"><div class="ancho">
<div class="p-az-cab"><h2 id="az-t">Todas las páginas</h2><p class="p-leyenda" aria-hidden="true">{leyenda}</p></div>
<nav class="p-barra" aria-label="Ir a la letra">{barra}</nav>
{az}</div></section>
</div>
<section class="p-sec p-origen"><div class="ancho"><h2>De dónde viene</h2>
<p>Los textos son traducciones de <a class="ext" href="https://psychonautwiki.org/" rel="noopener">PsychonautWiki</a>, una enciclopedia colaborativa sobre sustancias psicoactivas. Se publican con su misma licencia, <a class="ext" href="{LICENCIA}" rel="license noopener">CC BY-SA 4.0</a>. PsychonautWiki no ha participado en esta traducción ni la respalda.</p>
<p>Hemos dejado fuera las cifras de dosis y las guías de elaboración. Cada página enlaza a su original en inglés.</p></div></section>
</main>'''
    return documento("psiconautica/", "Psiconáutica", desc, cuerpo, "../", "sustancias/index.html", "website")


# ------------------------------------------------------------------ MAPA DEL SITIO
def mapa_sitio(pags, hoy):
    ruta = os.path.join(DOCS, "sitemap.xml")
    s = leer(ruta)
    s = re.sub(r"\s*<url><loc>https://apder\.org/psiconautica/[^<]*</loc>.*?</url>", "", s, flags=re.S)
    urls = ["psiconautica/"] + ["psiconautica/%s/" % p["slug"] for p in pags]
    bloque = "".join("\n<url><loc>https://apder.org/%s</loc><lastmod>%s</lastmod></url>" % (u, hoy) for u in urls)
    s = s.replace("\n</urlset>", bloque + "\n</urlset>")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(s)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", help="carpeta con los .json de las páginas traducidas")
    ap.add_argument("--excluidas", help="archivo con títulos originales o slugs que no se publican (uno por línea)")
    ap.add_argument("--hoy", default="2026-11-25", help="fecha para el mapa del sitio (AAAA-MM-DD)")
    a = ap.parse_args()

    pags = {}
    for ruta in sorted(glob.glob(os.path.join(SALIDA, "*", "index.html"))):
        d = de_html(ruta)
        if d:
            pags[d["slug"]] = d
    if a.json:
        for ruta in sorted(glob.glob(os.path.join(a.json, "*.json"))):
            d = de_json(ruta)
            pags[d["slug"]] = d
    fuera = set()
    if a.excluidas:
        fuera = {clave_wiki(l) for l in leer(a.excluidas).splitlines() if l.strip() and not l.startswith("#")}
    saltadas = []
    for slug in list(pags):
        d = pags[slug]
        if FUERA.search(d.get("original", "")) or clave_wiki(d.get("original", "")) in fuera or slug in fuera:
            saltadas.append(slug)
            del pags[slug]
    mapa = {clave_wiki(d["original"]): s for s, d in pags.items() if d.get("original")}
    for d in pags.values():                                   # también por alias en inglés, si los hay
        for al in d.get("alias_wiki", []):
            mapa.setdefault(clave_wiki(al), d["slug"])

    lista, peso, quitadas, con_cantidades = [], 0, [0], []
    for slug in sorted(pags):
        d = pags[slug]
        d["tipo"] = deducir_tipo(d, d["cuerpo"])
        antes_n = quitadas[0]
        d["cuerpo"], d["indice"] = preparar_cuerpo(d["cuerpo"], mapa, slug, d["tipo"], quitadas)
        if quitadas[0] > antes_n:
            con_cantidades.append("%s (%d)" % (slug, quitadas[0] - antes_n))
        d.setdefault("nota", "")
        d.setdefault("alias", [])
        d["frase"] = primera_frase(d["cuerpo"])
        d["desc"] = descripcion(d, d["cuerpo"])
        peso += articulo(d)
        lista.append(d)
    portada(lista)
    indice = [[d["slug"], d["titulo"], TIPOS[d["tipo"]][2], d["original"], d["nota"] or d["frase"]] + ([d["alias"]] if d["alias"] else [])
              for d in sorted(lista, key=lambda d: orden(d["titulo"]))]
    with open(os.path.join(SALIDA, "indice.json"), "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    mapa_sitio(lista, a.hoy)
    por_tipo = ", ".join("%d %s" % (sum(1 for d in lista if d["tipo"] == k), v[1].lower()) for k, v in TIPOS.items())
    print("%d páginas (%s) · %d KB · %d sin publicar por regla o por lista" % (len(lista), por_tipo, peso // 1024, len(saltadas)))
    if quitadas[0]:
        print("  %d frases con cantidades retiradas: %s" % (quitadas[0], ", ".join(con_cantidades[:60]) + (" …" if len(con_cantidades) > 60 else "")))
    if saltadas:
        print("  fuera: " + ", ".join(saltadas[:40]) + (" …" if len(saltadas) > 40 else ""))
    # carpetas que quedan en docs/psiconautica/ sin página (por si hay que borrarlas a mano)
    sobran = [s for s in saltadas if os.path.isdir(os.path.join(SALIDA, s))]
    if sobran:
        print("  AVISO: siguen en docs/psiconautica/ y hay que borrarlas: " + ", ".join(sobran))


if __name__ == "__main__":
    main()
