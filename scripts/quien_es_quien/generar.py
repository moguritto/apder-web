#!/usr/bin/env python3
"""Genera la sección «Quién es quién» de apder.org (docs/quien-es-quien/).
Toma la cabecera y el pie de una guía publicada para que todo sea idéntico al resto de la web.
Uso: python3 generar.py /ruta/apder-web
"""
import html
import json
import os
import re
import sys

from contenido import PERSONAS, PORTADA

REPO = sys.argv[1]
DOCS = os.path.join(REPO, "docs")
FECHA = "2026-11-23"
FECHA_TXT = "23 de noviembre de 2026"
FECHA_PORTADA = "2026-11-24"
BASE = "https://apder.org/"

guia = open(os.path.join(DOCS, "sustancias/2c-b/index.html"), encoding="utf-8").read()
CAB = guia[guia.index('<a class="saltar"'):guia.index("</header>") + len("</header>")]
CAB = CAB.replace(' aria-current="page"', "").replace("menu-abre actual", "menu-abre")
CAB = CAB.replace('menu-abre" aria-expanded="false" aria-controls="panel-aprender"', 'menu-abre actual" aria-expanded="false" aria-controls="panel-aprender"')  # Quién es quién va en «Aprender»
PIE = guia[guia.index('<script src="../../menu.js'):]


def rel(txt, prof):
    """Ajusta las rutas relativas «../../» a la profundidad de la página."""
    return txt if prof == 2 else txt.replace("../../", "../" * prof)


def libro(slug):
    h = open(os.path.join(DOCS, "biblioteca", slug, "index.html"), encoding="utf-8").read()
    t = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S).group(1)
    t = re.sub(r"<.*?>", "", t).strip()
    a = re.search(r'class="lb-autor">([^<]*)', h)
    m = re.search(r'class="lb-meta">([^<]*)', h)
    return t, (a.group(1).strip() if a else ""), (m.group(1).strip() if m else "")


def monograma(iniciales, nombre):
    return (f'<svg class="q-mono" viewBox="0 0 200 200" width="180" height="180" role="img" '
            f'aria-label="Iniciales de {html.escape(nombre)}">'
            f'<circle cx="100" cy="100" r="96" fill="#efe4d0"/>'
            f'<circle cx="100" cy="100" r="84" fill="none" stroke="#9c4a26" stroke-width="2" opacity=".45"/>'
            f'<text x="100" y="{132 if len(iniciales) == 1 else 124}" text-anchor="middle" font-family="\'DM Serif Display\',Georgia,serif" '
            f'font-size="{92 if len(iniciales) == 1 else 68}" fill="#9c4a26">{iniciales}</text></svg>')


ESTILO = """<style>
/* Quién es quién (23-11-2026) */
.q-ficha{text-align:center}
.q-mono{display:block;width:180px;height:auto;margin:4px auto 12px}
.q-ficha .s-ficha-dato{text-align:left;margin:.35em 0 0}
.q-tipo{display:inline-block;font-size:.85rem;letter-spacing:.02em;color:var(--suave);background:var(--arena);border-radius:99px;padding:2px 12px;margin:0 0 .8em}
.q-crono th{white-space:nowrap;vertical-align:top}
.s-refs li{overflow-wrap:anywhere}
.s-cuerpo h2.q-grupo{margin-top:1.6em}
.q-tarjetas{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:1em 0 2em;padding:0;list-style:none}
.q-tarjetas a{display:flex;gap:16px;align-items:center;background:#fff;border-radius:20px;padding:16px 18px;text-decoration:none;color:var(--texto);box-shadow:0 2px 14px rgba(60,40,20,.06);min-height:44px}
.q-tarjetas a:hover,.q-tarjetas a:focus-visible{background:var(--arena)}
.q-tarjetas .q-mono{width:72px;margin:0;flex:none}
.q-tarjetas strong{display:block;font-family:"DM Serif Display",Georgia,serif;font-weight:400;font-size:1.25rem}
.q-tarjetas span{display:block;font-size:.95rem;color:var(--suave)}
.s-cuerpo ul.q-tarjetas{padding:0;margin-left:0}
.s-cuerpo .q-tarjetas li{margin:0;padding:0}
.s-cuerpo .q-tarjetas li::before{content:none}
.s-cuerpo .q-tarjetas a,.s-cuerpo .q-tarjetas a span,.s-cuerpo .q-tarjetas a strong{text-decoration:none}
.s-cuerpo .q-tarjetas a strong{color:var(--tierra-osc)}
.s-cuerpo .q-tarjetas a span{color:var(--suave)}
@media print{.q-tarjetas a{box-shadow:none;border:1px solid #666}}
</style>"""


def cabeza(titulo, desc, url, og, og_alt, ld, prof):
    assert 120 <= len(desc) <= 160, (url, len(desc))
    p = "../" * prof
    e = html.escape
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titulo)} | APDER</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="APDER">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/og/{og}.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{BASE}img/og/{og}.png">
<meta name="twitter:image:alt" content="{e(og_alt)}">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{p}favicon.ico" sizes="32x32">
<link rel="icon" href="{p}img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}img/apple-touch-icon.png">
<link rel="preload" href="{p}fuentes/dm-serif-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}fuentes/nunito-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}tierra.css?v=20261123a">
{ESTILO}
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body class="guia">
"""


ORDEN_TIPOS = ["Ciencia", "Psicología y terapia", "Pensamiento y espiritualidad", "Saber tradicional"]

TOC = [("claves", "En pocas palabras"), ("vida", "Vida"), ("aportaciones", None),
       ("mirada", None), ("cronologia", "Cronología"), ("leer-mas", "Para leer más"),
       ("referencias", "Referencias")]


def ficha(p):
    fecha, fecha_txt = p.get("fecha", (FECHA, FECHA_TXT))
    url = f"{BASE}quien-es-quien/{p['slug']}/"
    secciones = [(i, t or p["titulos"][i]) for i, t in TOC]
    toc = "\n".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in secciones)
    if p.get("ld_personas"):
        personas = []
        for i, q in enumerate(p["ld_personas"]):
            d = {"@type": "Person", "@id": f"{url}#persona" + ("" if i == 0 else str(i + 1)), "name": q["name"],
                 "description": q["description"]}
            if q.get("birthDate"):
                d["birthDate"] = q["birthDate"]
            if q.get("deathDate"):
                d["deathDate"] = q["deathDate"]
            if q.get("birthPlace"):
                d["birthPlace"] = {"@type": "Place", "name": q["birthPlace"]}
            personas.append(d)
    else:
        persona = {"@type": "Person", "@id": url + "#persona", "name": p["nombre"]}
        if p.get("nacio_iso"):  # sin fecha publicada, no se pone
            persona["birthDate"] = p["nacio_iso"]
        persona["description"] = p["que"]
        if p.get("murio_iso"):
            persona["deathDate"] = p["murio_iso"]
        if p.get("lugar"):
            persona["birthPlace"] = {"@type": "Place", "name": p["lugar"]}
        personas = [persona]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfilePage", "@id": url, "url": url, "name": p["nombre"], "inLanguage": "es-ES",
         "dateModified": fecha, "mainEntity": {"@id": url + "#persona"},
         "publisher": {"@type": "Organization", "@id": BASE + "#organizacion", "name": "APDER", "url": BASE}},
        *personas,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "Quién es quién", "item": BASE + "quien-es-quien/"},
            {"@type": "ListItem", "position": 3, "name": p["nombre"], "item": url}]}]}
    claves = "\n".join(f"<li><strong>{k}.</strong> {v}</li>" for k, v in p["claves"])
    crono = "\n".join(f"<tr><th>{a}</th><td>{h}</td></tr>" for a, h in p["cronologia"])
    libros = []
    for slug, nota in p["libros"]:
        t, a, m = libro(slug)
        extra = f" ({html.escape(m)})" if m else ""
        libros.append(f'<li>{html.escape(a)}, <a href="../../biblioteca/{slug}/"><em>{html.escape(t)}</em></a>{extra}. {nota}</li>')
    lista_libros = (f'<p>Libros de la <a href="../../biblioteca/">Biblioteca</a>:</p>\n<ul>\n{chr(10).join(libros)}\n</ul>'
                    if libros else "")
    relacion = "\n".join(f'<a href="{h}"><strong>{t}</strong><span>{s}</span></a>' for h, t, s in p["relacion"])
    refs = "\n".join(f'<li id="ref-{n}">{r}</li>' for n, r in enumerate(p["refs"], 1))
    datos = "\n".join(f'<p class="s-ficha-dato"><strong>{k}:</strong> {v}</p>' for k, v in p["datos"])
    cuerpo = f"""{CAB}
<main id="contenido" class="guia-cuerpo">
<section class="s-cabeza">
<div class="s-ancho">
<div>
<p class="s-antetitulo"><a href="../">Quién es quién</a> · Ficha</p>
<h1>{p['nombre']}</h1>
<p class="s-alias">{p['alias']}</p>
<p class="s-nota">{p['entrada']}</p>
</div>
<aside class="s-ficha-mol q-ficha">
{monograma(p['iniciales'], p['nombre'])}
<p class="q-tipo">{p['tipo']}</p>
{datos}
</aside>
</div>
</section>

<div class="s-ancho s-guia">
<nav class="s-toc" aria-label="Índice">
<strong>Contenido</strong>
<ol>
{toc}
</ol>
</nav>

<article class="s-cuerpo">
<details class="s-toc-movil">
<summary>Contenido</summary>
<ol>
{toc}
</ol>
</details>

<h2 id="claves">En pocas palabras</h2>
<ul class="s-claves">
{claves}
</ul>

<h2 id="vida">Vida</h2>
{p['vida']}

<h2 id="aportaciones">{p['titulos']['aportaciones']}</h2>
{p['aportaciones']}

<h2 id="mirada">{p['titulos']['mirada']}</h2>
{p['mirada']}

<h2 id="cronologia">Cronología</h2>
<div class="s-tabla q-crono" role="region" tabindex="0" aria-label="Tabla: Cronología">
<table>
<tbody>
{crono}
</tbody>
</table>
</div>

<h2 id="leer-mas">Para leer más</h2>
{lista_libros}
<div class="s-relacion">
{relacion}
</div>

<h2 id="referencias">Referencias</h2>
<ol class="s-refs">
{refs}
</ol>
<p class="s-revisado">Última revisión: {fecha_txt}.</p>
<div class="s-nota s-descargo" role="note"><p><strong>Antes de seguir.</strong> Esta ficha es divulgativa. La hemos preparado con cuidado a partir de las fuentes citadas, pero puede tener errores o quedarse antigua. Si ves un error, escríbenos a <a href="mailto:info@apder.org">info@apder.org</a>.</p></div>
<p class="s-solo-impresion">Dirección canónica: {url}</p>
</article>
</div>

</main>
<script>
(function(){{var l=document.querySelectorAll('.s-toc a');if(!l.length||!('IntersectionObserver' in window))return;
var m={{}};l.forEach(function(a){{m[a.getAttribute('href').slice(1)]=a}});
var o=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{l.forEach(function(a){{a.classList.remove('activo')}});var a=m[e.target.id];if(a)a.classList.add('activo')}}}})}},{{rootMargin:'-140px 0px -70% 0px'}});
Object.keys(m).forEach(function(id){{var h=document.getElementById(id);if(h)o.observe(h)}});}})();
</script>
{PIE}"""
    pagina = cabeza(p["nombre"] + ": " + p["que"], p["desc"], url, "persona-" + p["slug"],
                    p["nombre"] + ": ficha de APDER", ld, 2) + cuerpo
    destino = os.path.join(DOCS, "quien-es-quien", p["slug"])
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(destino, "index.html"), "w", encoding="utf-8").write(pagina)


def portada():
    url = BASE + "quien-es-quien/"
    grupos = []
    for tipo in ORDEN_TIPOS:
        ps = sorted((q for q in PERSONAS if q["tipo"] == tipo), key=lambda q: q["anio"])
        if not ps:
            continue
        tarjetas = "\n".join(
            f'<li><a href="{p["slug"]}/">{monograma(p["iniciales"], p["nombre"])}'
            f'<div><strong>{p["nombre"]}</strong><span>{p["tarjeta"]}</span></div></a></li>' for p in ps)
        grupos.append(f'<h2 class="q-grupo">{tipo}</h2>\n<ul class="q-tarjetas">\n{tarjetas}\n</ul>')
    assert sum(1 for q in PERSONAS if q["tipo"] not in ORDEN_TIPOS) == 0
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": url, "url": url, "name": "Quién es quién", "inLanguage": "es-ES",
         "dateModified": FECHA_PORTADA, "description": PORTADA["desc"],
         "hasPart": [{"@id": f"{url}{p['slug']}/"} for p in PERSONAS],
         "publisher": {"@type": "Organization", "@id": BASE + "#organizacion", "name": "APDER", "url": BASE}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "Quién es quién", "item": url}]}]}
    cab = rel(CAB, 1)
    pie = rel(PIE, 1)
    pagina = cabeza("Quién es quién", PORTADA["desc"], url, "quien-es-quien", "Quién es quién: APDER", ld, 1)
    pagina = pagina.replace('<meta property="og:type" content="profile">', '<meta property="og:type" content="website">')
    pagina += f"""{cab}
<main id="contenido" class="guia-cuerpo">
<section class="s-cabeza">
<div class="s-ancho">
<div>
<p class="s-antetitulo">Personas</p>
<h1>Quién es quién</h1>
<p class="s-alias">{PORTADA['alias']}</p>
<p class="s-nota">{PORTADA['nota']}</p>
</div>
</div>
</section>
<div class="s-ancho">
<article class="s-cuerpo">
{chr(10).join(grupos)}
{PORTADA['pie']}
</article>
</div>
</main>
{pie}"""
    destino = os.path.join(DOCS, "quien-es-quien")
    os.makedirs(destino, exist_ok=True)
    open(os.path.join(destino, "index.html"), "w", encoding="utf-8").write(pagina)


for p in PERSONAS:
    ficha(p)
portada()
print("ok")
