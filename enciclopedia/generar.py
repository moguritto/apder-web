#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la Enciclopedia de medicinas (docs/enciclopedia/) a partir de los datos de esta carpeta.

    python3 enciclopedia/generar.py

- fichas/<slug>.json  -> docs/enciclopedia/<slug>/index.html   (una ficha por archivo)
- lista.json          -> docs/enciclopedia/index.html          (portada, tarjetas e índice A–Z)
La cabecera y el pie se copian de docs/sustancias/ en cada generación, así siguen al resto del sitio.
Solo usa la biblioteca estándar. Las reglas para escribir una ficha están en enciclopedia/LEEME.md.
Marcas en los textos: [n] = cita a la fuente n · <em>…</em> = cursiva."""
import glob
import json
import os
import re
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.normpath(os.path.join(AQUI, "..", "docs"))
SALIDA = os.path.join(DOCS, "enciclopedia")
HOY = "2026-11-23"

def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()

def marco(origen):
    """Cabecera, pie, hoja de estilos y guiones de una página real del sitio a la misma profundidad."""
    s = leer(os.path.join(DOCS, origen))
    cab = s[s.find('<header class="cabecera"'):s.find("</header>") + 9].replace(' aria-current="page"', "")
    cab = cab.replace("menu-abre actual", "menu-abre").replace('menu-abre" aria-expanded="false" aria-controls="panel-medicinas"', 'menu-abre actual" aria-expanded="false" aria-controls="panel-medicinas"')  # la enciclopedia va en «Medicinas» (menú del 25-11-2026; scripts/cabecera.py es la copia buena)
    pie = s[s.find("<footer"):s.find("</footer>") + 9]
    css = re.search(r'tierra\.css\?v=[^"]+', s)
    return cab, pie, (css.group(0) if css else "tierra.css")

P = lambda d: f'<path d="{d}"></path>'
C = lambda x, y, r: f'<circle cx="{x}" cy="{y}" r="{r}"></circle>'
ICO = {
    "que": P("M5 19c0-8 5-13 14-14 0 9-4 14-12 14") + P("M5 19c3-5 6-8 10-10"),
    "territorio": P("M12 21s-6-5.4-6-10a6 6 0 1 1 12 0c0 4.6-6 10-6 10z") + C(12, 11, 2.2),
    "parte": P("M12 21v-9") + P("M12 12c0-4-3-6-7-6 0 4 3 6 7 6z") + P("M12 14c0-3 2.5-5 6-5 0 3-2.5 5-6 5z"),
    "activos": P("M12 3l7.5 4.3v8.6L12 20.2 4.5 15.9V7.3z") + C(12, 11.6, 2.4),
    "tiempo": C(12, 12, 8.5) + P("M12 7.5V12l3 2"),
    "pueblos": C(9, 8.5, 3) + P("M3.5 19c.6-3.4 2.7-5 5.5-5s4.9 1.6 5.5 5") + C(17, 9.5, 2.3) + P("M16.2 14.2c2.3.1 3.9 1.6 4.3 4.3"),
    "planta": P("M5 19c0-8 5-13 14-14 0 9-4 14-12 14") + P("M5 19c3-5 6-8 10-10"),
    "hongo": P("M4 12c0-4.4 3.6-8 8-8s8 3.6 8 8z") + P("M10 12v6a2 2 0 0 0 4 0v-6"),
    "cactus": P("M10 21V6a2 2 0 1 1 4 0v15") + P("M10 14H8a2.5 2.5 0 0 1-2.5-2.5V9") + P("M14 16h2a2.5 2.5 0 0 0 2.5-2.5V11") + P("M7 21h10"),
    "animal": '<ellipse cx="12" cy="14.5" rx="8" ry="5"></ellipse>' + C(8, 8.5, 2) + C(16, 8.5, 2) + P("M9.5 15.5c1.6.8 3.4.8 5 0"),
    "preparado": P("M4 12h16a8 8 0 0 1-16 0z") + P("M9 8.5c-1-1.3 1-2.2 0-3.5") + P("M13 8.5c-1-1.3 1-2.2 0-3.5"),
    "molecula": P("M9 4l5 2.9v5.8L9 15.6 4 12.700V6.9z") + P("M14 12.7l4 2.3v3") + C(18, 19.5, 1.5),
    "lupa": C(11, 11, 6.5) + P("M16 16l4 4"),
    "flecha": P("M5 12h14M13 6l6 6-6 6"),
    "volver": P("M19 12H5M11 6l-6 6 6 6"),
}
SING = {"planta": "Planta", "hongo": "Hongo", "cactus": "Cactus", "animal": "Animal", "preparado": "Preparado", "molecula": "Molécula"}
UICN = [("NE", "No evaluada", "#6b6257"), ("DD", "Datos insuficientes", "#6b6257"), ("LC", "Preocupación menor", "#4f7350"), ("NT", "Casi amenazada", "#7f8a35"),
        ("VU", "Vulnerable", "#b0811a"), ("EN", "En peligro", "#c2643c"), ("CR", "En peligro crítico", "#9c2b1f")]
ESCALA = ["Uso tradicional documentado", "Estudios de laboratorio", "Estudios en personas", "Ensayos clínicos", "Medicamento aprobado"]

def ico(k, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICO[k]}</svg>'

def fmt(s):
    return re.sub(r"\[(\d+)\]", r'<sup class="ref"><a href="#fuente-\1">\1</a></sup>', s)

def limpio(s):
    return re.sub(r"<[^>]+>", "", s)

def pagina(ruta_rel, titulo, descripcion, cuerpo, pre, origen, extra=""):
    cab, pie, css = marco(origen)
    url = "https://apder.org/" + ruta_rel
    assert 120 <= len(descripcion) <= 160, f"descripción de {len(descripcion)} caracteres en {ruta_rel}"
    assert 'href="#"' not in cuerpo, f"enlace vacío en {ruta_rel}"
    doc = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} | APDER</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="APDER">
<meta property="og:locale" content="es_ES">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://apder.org/img/og-apder.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{titulo} · APDER">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://apder.org/img/og-apder.png">
<script>document.documentElement.classList.add("js")</script>
<link rel="icon" href="{pre}favicon.ico" sizes="32x32">
<link rel="icon" href="{pre}img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{pre}img/apple-touch-icon.png">
<link rel="preload" href="{pre}fuentes/dm-serif-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{pre}fuentes/nunito-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}{css}">
<link rel="stylesheet" href="{pre}enciclopedia/enciclopedia.css?v={HOY.replace("-", "")}">
</head>
<body class="enciclopedia">
<a class="saltar" href="#contenido">Saltar al contenido</a>
{cab}
<main id="contenido" class="enc">
{cuerpo}
</main>
{pie}
<script src="{pre}menu.js?v=20261123a" defer></script>
<script src="{pre}tierra.js" defer></script>
{extra}</body>
</html>
'''
    destino = os.path.join(DOCS, ruta_rel, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(doc)
    return len(doc)

# ------------------------------------------------------------------ FICHA
def ficha(d):
    pre, img = "../../", "../img/"
    def figura(f, cls="f-foto", estilo=""):
        st = f' style="{estilo}"' if estilo else ""
        return f'<figure class="{cls}"><img src="{img}{f["img"]}" alt="{f["alt"]}" loading="lazy"{st}><figcaption class="pie-foto">{f["pie"]}<span class="cred">{f["cred"]}</span></figcaption></figure>'
    def lamina(f):
        return f'<figure class="f-lamina"><img src="{img}{f["img"]}" alt="{f["alt"]}" loading="lazy"><figcaption><b>{f["titulo"]}</b>{f["pie"]} {f["cred"]}.</figcaption></figure>'
    def cab_sec(s):
        return f'<p class="etq">{s["etq"]}</p><h2>{s["titulo"]}</h2>'
    def parrafos(ps, lead=True):
        return "".join(f'<p class="lead">{fmt(p)}</p>' if (lead and i == 0) else f"<p>{fmt(p)}</p>" for i, p in enumerate(ps))

    sin_galeria = not d["galeria"]
    indice = [(d["planta"]["id"], "El hongo" if d["tipo"] == "hongo" else "La planta"), ("memoria", "Memoria y tradición"), ("territorio", "Territorio y cuidado"),
              ("quimica", "Qué contiene"), ("experiencia", "La experiencia"), ("investigacion", "Investigación"), ("cuidado", "Con cuidado"),
              ("galeria", "Galería"), ("seguir", "Para seguir"), ("fuentes", "Fuentes")]
    if sin_galeria:
        indice = [i for i in indice if i[0] != "galeria"]
    creditos = [(d["portada"]["pie"], d["portada"]["cred"])] if d.get("portada") else []
    g = d.get("guia")
    h = []
    ap_foto = f'<figure class="f-ap-foto"><img src="{img}{d["portada"]["img"]}" alt="{d["portada"]["alt"]}"><figcaption>{d["portada"]["pie"]} {d["portada"]["cred"]}</figcaption></figure>' if d.get("portada") else ""
    h.append(f'''<section class="f-apertura"><div class="ancho f-ap-in">
<div class="f-ap-txt"><a class="f-volver" href="../">{ico("volver", "ico peq")} Enciclopedia de medicinas</a>
<p class="etq oro">{d["migas"]}</p><h1>{d["nombre"]}</h1>
<p class="f-lat">{d["cientifico"]} <span>{d["autoridad"]}</span></p>
<p class="f-entrada">{fmt(d["entrada"])}</p>
<p class="f-otros"><b>También se llama</b><i>{d["otros"]}</i></p></div>
{ap_foto}
</div></section>''')
    datos = "".join(f'<div class="f-dato">{ico(k)}<dt>{t}</dt><dd>{v}</dd></div>' for k, t, v in d["vistazo"])
    h.append(f'<section class="f-vistazo ancho" aria-label="De un vistazo"><dl class="f-vistazo-in">{datos}</dl></section>')
    guia_aside = f'<a class="f-guia" href="{pre}{g["url"]}"><span class="etq">Para la práctica</span><b>{g["titulo"]}</b><span>Abrir la guía →</span></a>' if g else ""
    idx = "".join(f'<li><a{" class=\"on\"" if i == 0 else ""} href="#{a}">{t}</a></li>' for i, (a, t) in enumerate(indice))
    h.append(f'''<div class="ancho f-cuerpo"><aside class="f-indice"><p class="etq">En esta ficha</p><ol>{idx}</ol>
{guia_aside}</aside><div class="f-principal">''')
    # la planta / el hongo
    s = d["planta"]
    rasgos = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in s["rasgos"])
    lado = ""
    if s.get("lamina"):
        lado = lamina(s["lamina"]); creditos.append((s["lamina"]["titulo"], s["lamina"]["pie"] + " " + s["lamina"]["cred"]))
    elif s.get("foto"):
        lado = figura(s["foto"], estilo="aspect-ratio:4/5"); creditos.append((s["foto"]["pie"], s["foto"]["cred"]))
    aviso = f'<p class="f-aviso">{s["aviso"]}</p>' if s.get("aviso") else ""
    h.append(f'<section class="f-sec" id="{s["id"]}">{cab_sec(s)}<div class="f-dos"><div>{parrafos(s["parrafos"])}{aviso}</div>{lado}</div><dl class="f-rasgos">{rasgos}</dl></section>')
    # memoria y tradición
    s = d["tradicion"]
    crono = "".join(f"<li><time>{f}</time><p>{fmt(t)}</p></li>" for f, t in s["cronologia"])
    nombres = "".join(f"<div><dt>{n}</dt><dd>{l}</dd></div>" for n, l in s["nombres"])
    nota = f'<p style="margin-top:16px">{fmt(s["nota_nombres"])}</p>' if s.get("nota_nombres") else ""
    banda = ""
    if s.get("banda"):
        banda = figura(s["banda"], "f-banda"); creditos.append((s["banda"]["pie"], s["banda"]["cred"]))
    retr = ""
    if s.get("retratos"):
        retr = '<div class="f-retratos">' + "".join(figura(r) for r in s["retratos"]) + "</div>"
        creditos += [(r["pie"], r["cred"]) for r in s["retratos"]]
    if s.get("lamina"):
        creditos.append((s["lamina"]["titulo"], s["lamina"]["pie"] + " " + s["lamina"]["cred"]))
        cuerpo = f'<div class="f-dos"><div>{parrafos(s["parrafos"])}</div>{lamina(s["lamina"])}</div>'
    else:
        cuerpo = parrafos(s["parrafos"])
    h.append(f'<section class="f-sec" id="memoria">{cab_sec(s)}{cuerpo}{banda}<h3>En el tiempo</h3><ol class="f-crono">{crono}</ol>{retr}<h3>Sus nombres</h3><dl class="f-nombres">{nombres}</dl>{nota}</section>')
    # territorio y cuidado
    s = d["territorio"]
    m = s["mapa"]
    ley = "".join(f'<span><i style="--c:{c}"></i>{t}</span>' for c, t in m["leyenda"])
    mapa = f'<figure><img src="{img}{m["img"]}" alt="{m["alt"]}" loading="lazy"><figcaption class="f-leyenda">{ley}</figcaption></figure>'
    creditos.append(("Mapa", "APDER, con datos de Natural Earth · dominio público"))
    uicn = ""
    if s.get("uicn"):
        fila = "".join(f'<span{" class=\"on\" style=\"--c:" + col + "\"" if cod == s["uicn"]["estado"] else ""} title="{nom}">{cod}</span>' for cod, nom, col in UICN)
        nom = [n for c_, n, _ in UICN if c_ == s["uicn"]["estado"]][0]
        uicn = f'<div class="f-uicn"><p class="etq">Estado de conservación · {s["uicn"]["estado"]}, {nom.lower()}</p><div class="fila" role="img" aria-label="Escala de la Lista Roja de la UICN: {nom}">{fila}</div><p>{fmt(s["uicn"]["nota"])}</p></div>'
    ayuda = '<h3>Qué ayuda</h3><ul class="f-lista">' + "".join(f"<li>{a}</li>" for a in s["ayuda"]) + "</ul>"
    foto = ""
    if s.get("foto"):
        foto = figura(s["foto"], "f-foto ancha"); creditos.append((s["foto"]["pie"], s["foto"]["cred"]))
    cls = "f-mapa mundo" if m["mundo"] else "f-mapa"
    h.append(f'<section class="f-sec" id="territorio">{cab_sec(s)}<div class="{cls}">{mapa}<div>{parrafos(s["parrafos"])}{uicn}</div></div>{foto}{ayuda}</section>')
    # qué contiene
    s = d["quimica"]
    mols = ""
    for mo in s["moleculas"]:
        im = f'<img src="{pre}sustancias/moleculas/{mo["img"]}" alt="Estructura química de {mo["nombre"].lower()}" loading="lazy">' if mo.get("img") else ""
        mols += f'<div class="f-mol">{im}<b>{mo["nombre"]}</b><small>{mo["clase"]}</small><p>{mo["texto"]}</p></div>'
    creditos.append(("Dibujos de moléculas", "APDER"))
    h.append(f'<section class="f-sec" id="quimica">{cab_sec(s)}{parrafos(s["parrafos"])}<div class="f-mols">{mols}</div></section>')
    # la experiencia
    s = d["experiencia"]
    t = s["tiempo"]
    tramos = "".join(f'<span class="tramo {k}" style="left:{a / t["horas"] * 100:.2f}%;width:{(b - a) / t["horas"] * 100:.2f}%">{txt}</span>' for k, a, b, txt in t["tramos"])
    paso = t["horas"] // 4
    u = "min" if t.get("unidad") == "min" else "h"
    horas = "".join(f"<span>{i * paso} {u}</span>" for i in range(5))
    res = "".join(f"<span><b>{k}:</b> {v}</span>" for k, v in t["res"])
    h.append(f'<section class="f-sec" id="experiencia">{cab_sec(s)}{parrafos(s["parrafos"])}<div class="f-tiempo"><div class="pista" role="img" aria-label="Línea de tiempo del efecto">{tramos}</div><div class="horas">{horas}</div><div class="res">{res}</div><p class="nota">Esquema orientativo: cambia con la preparación, la cantidad y la persona.</p></div></section>')
    # investigación
    s = d["investigacion"]
    esc = "".join(f'<div class="{"aqui" if i == s["nivel"] - 1 else ("ok" if i < s["nivel"] - 1 else "")}">{e}</div>' for i, e in enumerate(ESCALA))
    h.append(f'<section class="f-sec" id="investigacion">{cab_sec(s)}<div class="f-escala" role="img" aria-label="Hasta dónde llega la investigación: {ESCALA[s["nivel"] - 1]}">{esc}</div><div style="margin-top:26px">{parrafos(s["parrafos"], lead=False)}</div><p class="f-alcance"><b>Alcance de estos datos</b>{s["alcance"]}</p></section>')
    # con cuidado
    s = d["cuidado"]
    tarj = "".join(f"<div><b>{a}</b><p>{fmt(b)}</p></div>" for a, b in s["tarjetas"])
    par = ""
    if s.get("parecidos"):
        items = ""
        for p in s["parecidos"]:
            if p.get("img"):
                im = f'<img src="{img}{p["img"]}" alt="{p["alt"]}" loading="lazy">'; creditos.append((p["nombre"], p["cred"]))
            else:
                im = '<div class="sin">Sin foto a propósito: no se identifica por una imagen.</div>'
            items += f'<figure class="f-parecido">{im}<figcaption><b>{p["nombre"]}</b><i>{p["lat"]}</i><p>{fmt(p["texto"])}</p></figcaption></figure>'
        par = f'<h3>Parecidos que importan</h3><div class="f-parecidos">{items}</div>'
    puente = f'<a class="f-puente" href="{pre}{g["url"]}"><span><b>{g["titulo"]}</b><span>{g["texto"]}</span></span><span class="btn o">Ir a la guía {ico("flecha", "ico peq")}</span></a>' if g else ""
    h.append(f'<section class="f-sec" id="cuidado">{cab_sec(s)}<div class="f-cuidado">{tarj}</div>{par}{puente}</section>')
    # galería
    gal = "".join(figura(x, x["cls"]) for x in d["galeria"])
    creditos += [(x["pie"], x["cred"]) for x in d["galeria"]]
    if d["galeria"]:
        h.append(f'<section class="f-sec" id="galeria"><p class="etq">Galería</p><h2>Mirar de cerca</h2><div class="f-galeria">{gal}</div></section>')
    # para seguir
    libros = ""
    for b in d["libros"]:
        cub = f'<img src="{pre}{b["img"]}" alt="" loading="lazy">' if b.get("img") else f'<span class="tapa"><small>Biblioteca de APDER</small><span>{b["titulo"]}</span></span>'
        libros += f'<a class="f-libro" href="{pre}{b["url"]}">{cub}<span><b>{b["titulo"]}</b><span>{b["autor"]}</span><em>En la biblioteca de APDER →</em></span></a>'
    par = ""
    for tp, n, c, txt, url in d["parientes"]:
        dentro = f'<span class="tipo t-{tp}">{SING[tp]}</span><b>{n}</b><i>{c}</i><p>{txt}</p>'
        par += f'<a class="f-pariente" href="{pre}{url}">{dentro}</a>' if url else f'<div class="f-pariente">{dentro}</div>'
    h.append(f'<section class="f-sec" id="seguir"><p class="etq">Para seguir</p><h2>Libros y medicinas emparentadas</h2><div class="f-seguir">{libros}</div><div class="f-parientes">{par}</div></section>')
    # fuentes
    fu = "".join(f'<li id="fuente-{i + 1}">{f}</li>' for i, f in enumerate(d["fuentes"]))
    cr = "".join(f"<li><b>{limpio(a)}</b> {b}</li>" for a, b in creditos)
    ant, sig = d["anterior"], d["siguiente"]
    h.append(f'''<section class="f-sec" id="fuentes"><p class="etq">Fuentes</p><h2>De dónde sale cada dato</h2><ol class="f-fuentes">{fu}</ol>
<div class="f-creditos"><b>Créditos de las imágenes</b><ul>{cr}</ul></div>
<p class="f-revision">Última revisión: {d["revisado"]}. Si ves un error, escríbenos a info@apder.org.</p>
<div class="f-paso"><a href="../{ant[1]}/"><small>← Ficha anterior</small><b>{ant[0]}</b></a><a class="sig" href="../{sig[1]}/"><small>Ficha siguiente →</small><b>{sig[0]}</b></a></div></section>''')
    h.append("</div></div>")
    cuerpo = "\n".join(h)
    usadas = set(re.findall(r'href="#fuente-(\d+)"', cuerpo))
    assert all(1 <= int(n) <= len(d["fuentes"]) for n in usadas), f"cita sin fuente en {d['slug']}"
    return pagina(f'enciclopedia/{d["slug"]}/', f'{d["nombre"]} ({d["cientifico"]})', d["descripcion"], cuerpo, pre, "sustancias/ayahuasca/index.html")

# ------------------------------------------------------------------ PORTADA
JS_PORTADA = '''<script>
(function(){
  var norm=function(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();};
  var fichas=document.querySelectorAll('.e-ficha'), b=document.getElementById('busca'), tipo='todas';
  function pinta(){var q=b?norm(b.value.trim()):'';fichas.forEach(function(c){c.hidden=!((tipo==='todas'||c.getAttribute('data-tipo')===tipo)&&(!q||norm(c.textContent).indexOf(q)>=0));});}
  document.querySelectorAll('.e-filtros button').forEach(function(x){x.addEventListener('click',function(){tipo=x.getAttribute('data-f');document.querySelectorAll('.e-filtros button').forEach(function(y){y.classList.toggle('on',y===x);});pinta();});});
  if(b)b.addEventListener('input',pinta);
})();
</script>
'''

def portada(L):
    pre, img = "../", "img/"
    cuenta = {t: sum(1 for x in L["az"] if x["tipo"] == t) for t, _, _ in L["tipos"]}
    total = len(L["az"])
    h = []
    atajos = "".join(f'<a href="{pre}{u}">{n}</a>' for n, u in L["atajos"])
    h.append(f'''<section class="e-portada"><div class="ancho e-portada-in">
<div><p class="etq oro">Medicinas · Enciclopedia</p><h1>Enciclopedia <em>de medicinas</em></h1>
<p class="e-intro">Plantas, hongos, animales y preparados que distintos pueblos llaman medicina. Una ficha para cada uno: cómo es, dónde vive, quién guarda su memoria y qué se ha estudiado.</p>
<label class="e-busca">{ico("lupa", "ico peq")}<input type="search" id="busca" aria-label="Buscar en la enciclopedia" placeholder="Nombre, pueblo, región o principio activo"></label>
<p class="e-atajos">Lo más buscado {atajos}</p></div>
<figure class="e-orbitas"><div class="orb orb-1"><img src="{img}ama-joven.jpg" alt="Matamoscas joven, de sombrero rojo cubierto de verrugas blancas."></div><div class="orb orb-2"><img src="{img}aya-flores.jpg" alt="Flores rosadas de la liana de la ayahuasca."></div><div class="orb orb-3"><img src="{img}idx-loto.jpg" alt="Flor de loto azul."></div><span class="chispa a" aria-hidden="true">✧</span><span class="chispa b" aria-hidden="true">✧</span><figcaption>Matamoscas · flor de ayahuasca · loto azul</figcaption></figure>
</div></section>''')
    tiles = "".join(f'<a class="e-tipo t-{t}" href="#fichas">{ico(t)}<b>{n}</b><span>{cuenta[t]} fichas · {txt}</span></a>' for t, n, txt in L["tipos"])
    h.append(f'<section class="e-sec ancho"><div class="e-cab"><div><p class="etq">Entrar por</p><h2>Seis reinos de medicinas</h2></div><p class="nota">{total} fichas previstas en la primera edición. También puedes buscar por nombre o recorrer el índice alfabético.</p></div><div class="e-tipos">{tiles}</div></section>')
    filtros = '<button type="button" class="on" data-f="todas">Todas</button>' + "".join(f'<button type="button" data-f="{t}">{n}</button>' for t, n, _ in L["tipos"])
    cards = ""
    for c in L["tarjetas"]:
        alt = f'{c["nombre"]} ({c["cientifico"]})'
        tipo = f'<span class="tipo t-{c["tipo"]}">{SING[c["tipo"]]}</span>'
        if c["slug"]:
            abre, cierra, aviso, meta = f'<a class="e-ficha{" grande" if c["grande"] else ""}" data-tipo="{c["tipo"]}" href="{c["slug"]}/">', "</a>", "", c["meta"]
        elif c["guia"]:
            abre, cierra, aviso, meta = f'<a class="e-ficha" data-tipo="{c["tipo"]}" href="{pre}{c["guia"]}">', "</a>", '<span class="aviso">Por ahora, su guía</span>', c["meta"]
        else:
            abre, cierra, aviso, meta = f'<div class="e-ficha" data-tipo="{c["tipo"]}">', "</div>", '<span class="aviso">En preparación</span>', c["meta"]
        if c["grande"] and c["slug"]:
            cards += f'{abre}<figure><img src="{img}{c["img"]}" alt="{alt}">{tipo}<div class="sobre"><h3>{c["nombre"]}</h3><p class="lat">{c["cientifico"]}</p><p class="linea">{c["linea"]}</p></div></figure>{cierra}'
        else:
            cards += f'{abre}<figure><img src="{img}{c["img"]}" alt="{alt}" loading="lazy">{tipo}{aviso}</figure><h3>{c["nombre"]}</h3><p class="lat">{c["cientifico"]}</p><p class="linea">{c["linea"]}</p><p class="meta">{meta}</p>{cierra}'
    h.append(f'<section class="e-sec ancho" id="fichas"><div class="e-cab"><div><p class="etq">Las fichas</p><h2>Mirar de cerca</h2></div><div class="e-filtros" role="group" aria-label="Filtrar por tipo">{filtros}</div></div><div class="e-rejilla">{cards}</div><p class="e-mas"><a href="#az">Ver las {total} fichas en orden alfabético</a></p></section>')
    regs = "".join(f"<li>{r}</li>" for r in L["regiones"])
    h.append(f'''<section class="e-mapa" id="mapa"><div class="ancho e-mapa-in"><div><p class="etq">De dónde vienen</p><h2>Cada una, de su territorio</h2><p>Cada medicina pertenece a un lugar y a los pueblos que la cuidan. El mapa señala el origen de veinte de ellas.</p><ul class="e-regiones">{regs}</ul></div>
<img src="{img}mapa-mundo.svg" alt="Mapa del mundo con el lugar de origen de veinte medicinas: ayahuasca en la Amazonía, peyote en el norte de México, iboga en Gabón, matamoscas en Siberia, kava en Oceanía y otras." loading="lazy"></div></section>''')
    def clave(s):
        return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()
    grupos = {}
    for x in sorted(L["az"], key=lambda x: clave(x["nombre"])):
        letra = clave(x["nombre"])[0].upper()
        grupos.setdefault("0–9" if letra.isdigit() else letra, []).append(x)
    az = ""
    for letra, items in grupos.items():
        filas = ""
        for x in items:
            det = f' <i>{x["detalle"]}</i>' if x["tipo"] in ("planta", "hongo", "cactus", "animal") else f' · {x["detalle"]}'
            filas += f'<a href="{x["slug"]}/">{x["nombre"]}</a>' if x["slug"] else f'<span>{x["nombre"]}{det}</span>'
        az += f'<div class="e-letra"><b>{letra}</b>{filas}</div>'
    h.append(f'<section class="e-sec ancho" id="az"><div class="e-cab"><div><p class="etq">Índice alfabético</p><h2>Todas, de la A a la Z</h2></div><p class="nota">En negrita y con flecha, las fichas ya escritas. Las demás están en preparación.</p></div><div class="e-az">{az}</div></section>')
    libros = ""
    for b in L["libros"]:
        cub = f'<img src="{pre}{b["img"]}" alt="" loading="lazy">' if b.get("img") else f'<span class="tapa"><small>Biblioteca de APDER</small><span>{b["titulo"]}</span></span>'
        libros += f'<a class="e-libro" href="{pre}{b["url"]}">{cub}<b>{b["titulo"]}</b><span>{b["autor"]}</span></a>'
    h.append(f'''<section class="ancho e-doble"><div class="e-caja b"><p class="etq">Cómo se hace</p><h2>Una ficha, muchas comprobaciones</h2><ul>
<li>Cada ficha parte de una obra de referencia y se contrasta con fuentes actuales.</li><li>Los nombres de las plantas siguen a Kew; los de los hongos, a Index Fungorum.</li>
<li>Las referencias van junto al pasaje que apoyan.</li><li>Cada fotografía lleva su autor y su licencia.</li>
<li>Para la práctica y los riesgos, cada ficha enlaza con su guía.</li><li>APDER no anima a consumir: informa.</li></ul></div>
<div class="e-caja o"><p class="etq">Biblioteca de APDER</p><h2>Libros para abrir la enciclopedia</h2><div class="e-libros">{libros}</div></div></section>''')
    return pagina("enciclopedia/", "Enciclopedia de medicinas", L["descripcion"], "\n".join(h), pre, "sustancias/index.html", JS_PORTADA)

if __name__ == "__main__":
    n = portada(json.loads(leer(os.path.join(AQUI, "lista.json"))))
    print("portada", n)
    for ruta in sorted(glob.glob(os.path.join(AQUI, "fichas", "*.json"))):
        d = json.loads(leer(ruta))
        print(d["slug"], ficha(d))
