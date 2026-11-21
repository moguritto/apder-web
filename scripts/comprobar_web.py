#!/usr/bin/env python3
"""Comprobador de la web de APDER (carpeta docs/).

Solo biblioteca estándar. Uso:
    python3 scripts/comprobar_web.py [carpeta_docs] [--json] [--excepciones ARCHIVO]

Sale con 0 si no hay errores y con 1 si los hay. Los avisos no hacen fallar.
Más información en scripts/COMPROBADOR.md.
"""
import argparse
import fnmatch
import json
import posixpath
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

DOMINIO = "apder.org"
PESO_AVISO = 60 * 1024  # bytes por página HTML
DESC_MIN, DESC_MAX = 120, 160
PREFIJOS_IGNORADOS = ("wp-content", "wp-includes")
REL_NO_RECURSO = {"canonical", "alternate", "author", "license", "me", "next", "prev",
                  "help", "search", "shortlink", "bookmark"}
INGLES_PIE = re.compile(
    r"\b(all rights reserved|subscribe|privacy(?: policy)?|terms (?:of use|and conditions)|"
    r"home|contact us|powered by|follow us|read more|copyright)\b", re.I)

REGLAS = {
    "a-enlaces": "Enlaces internos rotos (href/src)",
    "b-h1": "Exactamente un <h1> por página",
    "c-descripcion": f"<meta name=\"description\" presente y de {DESC_MIN} a {DESC_MAX} caracteres",
    "d-idioma": "<html lang=\"es\"> y og:locale es_ES",
    "e-alt": "Imágenes sin alt (alt vacío = aviso)",
    "f-peso": f"Peso de las páginas HTML (aviso > {PESO_AVISO // 1024} KB) y peso total",
    "g-terceros": "Llamadas a recursos de terceros (css/js/img/fuentes/iframe)",
    "h-wp": "Referencias a wp-content / wp-includes",
    "i-ingles": "Texto en inglés residual en el pie",
    "j-noindex-sitemap": "Páginas noindex (o inexistentes) en sitemap.xml",
    "j-almohadilla": "Enlaces a \"#\" vacíos",
}

ATRIBUTOS_RECURSO = {
    "link": ("href",), "script": ("src",), "img": ("src", "srcset"),
    "source": ("src", "srcset"), "iframe": ("src",), "video": ("src", "poster"),
    "audio": ("src",), "embed": ("src",), "object": ("data",), "input": ("src",),
}
URL_CSS = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)|@import\s+(['\"])(.*?)\3", re.I)


def es_interno(host):
    host = (host or "").lower().split(":")[0]
    return host == DOMINIO or host.endswith("." + DOMINIO)


def partir_srcset(valor):
    return [p.strip().split()[0] for p in valor.split(",") if p.strip()]


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.h1 = 0
        self.descripcion = None
        self.og_locale = None
        self.robots = ""
        self.redireccion = False
        self.enlaces = []      # (linea, atributo, url) para comprobar existencia
        self.recursos = []     # (linea, etiqueta, url) para terceros
        self.imagenes = []     # (linea, alt) alt None = sin atributo
        self.almohadillas = []
        self.pie = []
        self.css_inline = []
        self._pie = 0
        self._oculto = None    # 'script' o 'style' mientras estamos dentro

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        linea = self.getpos()[0]
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "footer":
            self._pie += 1
        elif tag == "meta":
            nombre = a.get("name", "").lower()
            prop = a.get("property", "").lower()
            if nombre == "description" and self.descripcion is None:
                self.descripcion = a.get("content", "")
            elif nombre == "robots":
                self.robots += " " + a.get("content", "").lower()
            elif prop == "og:locale":
                self.og_locale = a.get("content", "")
            elif a.get("http-equiv", "").lower() == "refresh":
                self.redireccion = True
                m = re.search(r"url\s*=\s*['\"]?([^'\"]+)", a.get("content", ""), re.I)
                if m:
                    self.enlaces.append((linea, "meta refresh", m.group(1).strip()))
        elif tag == "img":
            self.imagenes.append((linea, a.get("alt")))
        elif tag in ("script", "style"):
            self._oculto = tag
        if tag == "a" and "href" in a:
            if a["href"].strip() == "#":
                self.almohadillas.append(linea)
            else:
                self.enlaces.append((linea, "href", a["href"]))
        if tag in ATRIBUTOS_RECURSO:
            rels = set(a.get("rel", "").lower().split())
            for atr in ATRIBUTOS_RECURSO[tag]:
                if atr not in a or (tag == "input" and a.get("type") != "image"):
                    continue
                urls = partir_srcset(a[atr]) if atr == "srcset" else [a[atr]]
                for u in urls:
                    if tag == "link" and rels & REL_NO_RECURSO:
                        # canonical, alternate...: no son recursos, pero sí deben existir si son locales
                        self.enlaces.append((linea, "href", u))
                        continue
                    self.recursos.append((linea, tag, u))
                    self.enlaces.append((linea, atr, u))
        if "style" in a:
            self.css_inline.append((linea, a["style"]))

    def handle_endtag(self, tag):
        if tag == "footer" and self._pie:
            self._pie -= 1
        elif tag in ("script", "style") and self._oculto == tag:
            self._oculto = None

    def handle_data(self, data):
        if self._oculto == "style":
            self.css_inline.append((self.getpos()[0], data))
        elif self._oculto is None and self._pie:
            self.pie.append((self.getpos()[0], data))


class Comprobador:
    def __init__(self, docs):
        self.docs = docs
        self.hallazgos = []
        self.total_bytes = 0
        self.wp_bytes = 0

    def anota(self, regla, sev, ruta, mensaje, linea=None):
        self.hallazgos.append({"regla": regla, "severidad": sev, "ruta": ruta,
                               "linea": linea, "mensaje": mensaje})

    def ruta(self, f):
        return f.relative_to(self.docs).as_posix()

    def es_wp(self, rel):
        return rel.split("/", 1)[0] in PREFIJOS_IGNORADOS

    def existe(self, destino):
        """destino: ruta POSIX relativa a docs. Carpeta -> index.html."""
        if destino in ("", "."):
            return (self.docs / "index.html").is_file()
        p = self.docs / destino
        if p.is_file():
            return True
        return p.is_dir() and (p / "index.html").is_file()

    def resolver(self, rel_pagina, url):
        """Devuelve ruta relativa a docs, None si no se comprueba, o False si no es resoluble."""
        url = url.strip()
        if not url or url.startswith("#"):
            return None
        partes = urlsplit(url)
        if partes.scheme and partes.scheme not in ("http", "https"):
            return None
        if partes.scheme or url.startswith("//"):
            if not es_interno(partes.hostname):
                return None
            ruta = partes.path or "/"
            base = ""
        elif url.startswith("/"):
            ruta, base = partes.path, ""
        else:
            ruta = partes.path
            base = "" if rel_pagina == "404.html" else posixpath.dirname(rel_pagina)
            if not ruta:
                return None
        ruta = unquote(ruta)
        destino = posixpath.normpath(posixpath.join(base, ruta.lstrip("/") if base == "" else ruta))
        if destino == ".":
            destino = ""
        if destino.startswith(".."):
            return False
        return destino

    def comprobar_html(self, f):
        rel = self.ruta(f)
        datos = f.read_bytes()
        texto = datos.decode("utf-8", errors="replace")
        p = Pagina()
        p.feed(texto)
        p.close()
        redir = p.redireccion
        noindex = "noindex" in p.robots
        sin_seo = redir or noindex

        # a) enlaces rotos
        vistos = set()
        for linea, atr, url in p.enlaces:
            destino = self.resolver(rel, url)
            if destino is None or (destino, url) in vistos:
                continue
            vistos.add((destino, url))
            if destino is False or not self.existe(destino):
                self.anota("a-enlaces", "error", rel, f"enlace roto ({atr}): {url}", linea)

        # b) h1
        if not redir and p.h1 != 1:
            self.anota("b-h1", "error", rel, f"tiene {p.h1} etiquetas <h1> (debe haber exactamente 1)")

        # c) descripción
        if not sin_seo:
            if p.descripcion is None or not p.descripcion.strip():
                self.anota("c-descripcion", "error", rel, "falta <meta name=\"description\">")
            else:
                n = len(p.descripcion.strip())
                if not DESC_MIN <= n <= DESC_MAX:
                    self.anota("c-descripcion", "error", rel,
                               f"descripción de {n} caracteres (debe tener de {DESC_MIN} a {DESC_MAX})")

        # d) idioma
        lang = (p.lang or "").lower()
        if not (lang == "es" or lang.startswith("es-")):
            self.anota("d-idioma", "error", rel, f"<html lang> es {p.lang!r} (debe ser \"es\")")
        if not sin_seo and p.og_locale != "es_ES":
            self.anota("d-idioma", "error", rel,
                       f"og:locale es {p.og_locale!r} (debe ser \"es_ES\")" if p.og_locale
                       else "falta <meta property=\"og:locale\" content=\"es_ES\">")

        # e) alt
        for linea, alt in p.imagenes:
            if alt is None:
                self.anota("e-alt", "error", rel, "<img> sin atributo alt", linea)
            elif not alt.strip():
                self.anota("e-alt", "aviso", rel, "<img alt=\"\"> (válido solo si es decorativa)", linea)

        # f) peso de la página
        if len(datos) > PESO_AVISO:
            self.anota("f-peso", "aviso", rel, f"pesa {len(datos) / 1024:.0f} KB (aviso a partir de {PESO_AVISO // 1024} KB)")

        # g) terceros (recursos, no <a>) e inline CSS
        ext = set()
        for linea, tag, url in p.recursos:
            partes = urlsplit(url.strip())
            if (partes.scheme in ("http", "https") or url.strip().startswith("//")) and not es_interno(partes.hostname):
                clave = (tag, url)
                if clave not in ext:
                    ext.add(clave)
                    self.anota("g-terceros", "error", rel, f"<{tag}> carga {url}", linea)
        for linea, css in p.css_inline:
            for url in self.urls_css(css):
                if self.es_tercero(url) and ("css", url) not in ext:
                    ext.add(("css", url))
                    self.anota("g-terceros", "error", rel, f"CSS en línea carga {url}", linea)

        # h) wp-content / wp-includes
        coincid = [(i + 1, l) for i, l in enumerate(texto.splitlines()) if re.search(r"wp-(content|includes)", l)]
        if coincid:
            n = sum(len(re.findall(r"wp-(?:content|includes)", l)) for _, l in coincid)
            ejemplo = ", ".join(sorted(set(m.group(0) for _, l in coincid
                                         for m in re.finditer(r"wp-(?:content|includes)/[^\s\"'()<>,]{0,50}", l)))[:3])
            self.anota("h-wp", "error", rel, f"{n} referencias a wp-content/wp-includes (p. ej. {ejemplo})", coincid[0][0])

        # i) inglés residual en el pie
        frases = set()
        primera = None
        for linea, t in p.pie:
            for m in INGLES_PIE.finditer(t):
                frases.add(m.group(0).lower())
                primera = primera or linea
        if frases:
            self.anota("i-ingles", "error", rel, "texto en inglés en el pie: " + ", ".join(sorted(frases)), primera)

        # j) almohadillas vacías
        for linea in p.almohadillas:
            self.anota("j-almohadilla", "error", rel, "enlace <a href=\"#\"> vacío", linea)

        return {"noindex": noindex, "redir": redir}

    @staticmethod
    def urls_css(css):
        for m in URL_CSS.finditer(css):
            yield (m.group(2) if m.group(2) is not None else m.group(4)).strip()

    @staticmethod
    def es_tercero(url):
        if url.startswith("//"):
            url = "https:" + url
        partes = urlsplit(url)
        return partes.scheme in ("http", "https") and not es_interno(partes.hostname)

    def comprobar_css(self, f):
        rel = self.ruta(f)
        texto = f.read_text(encoding="utf-8", errors="replace")
        vistos = set()
        for url in self.urls_css(texto):
            if self.es_tercero(url) and url not in vistos:
                vistos.add(url)
                self.anota("g-terceros", "error", rel, f"CSS carga {url}")
        n = len(re.findall(r"wp-(?:content|includes)", texto))
        if n:
            self.anota("h-wp", "error", rel, f"{n} referencias a wp-content/wp-includes")

    def comprobar_sitemap(self, info):
        sm = self.docs / "sitemap.xml"
        if not sm.is_file():
            self.anota("j-noindex-sitemap", "aviso", "sitemap.xml", "no existe sitemap.xml")
            return
        for loc in re.findall(r"<loc>\s*([^<]+?)\s*</loc>", sm.read_text(encoding="utf-8", errors="replace")):
            partes = urlsplit(loc)
            if not es_interno(partes.hostname):
                continue
            ruta = unquote(partes.path).strip("/")
            if not self.existe(ruta):
                self.anota("j-noindex-sitemap", "error", "sitemap.xml", f"{loc} no existe en docs/")
                continue
            pagina = (ruta + "/index.html") if (self.docs / ruta).is_dir() or ruta == "" else ruta
            pagina = pagina.lstrip("/")
            if info.get(pagina, {}).get("noindex"):
                self.anota("j-noindex-sitemap", "error", "sitemap.xml", f"{loc} es noindex ({pagina}) pero está en el sitemap")

    def ejecutar(self):
        info = {}
        for f in sorted(self.docs.rglob("*")):
            if not f.is_file():
                continue
            rel = self.ruta(f)
            tam = f.stat().st_size
            self.total_bytes += tam
            if self.es_wp(rel):
                self.wp_bytes += tam
                continue
            if f.suffix.lower() in (".html", ".htm"):
                info[rel] = self.comprobar_html(f)
            elif f.suffix.lower() == ".css":
                self.comprobar_css(f)
        self.comprobar_sitemap(info)
        self.paginas = len(info)
        resto = self.total_bytes - self.wp_bytes
        self.anota("f-peso", "info", "(docs/)",
                   f"peso total {self.total_bytes / 1048576:.1f} MB "
                   f"(wp-content + wp-includes {self.wp_bytes / 1048576:.1f} MB, resto {resto / 1048576:.1f} MB); "
                   f"{self.paginas} páginas HTML analizadas")


def leer_excepciones(archivo):
    reglas = []
    if archivo and archivo.is_file():
        for n, l in enumerate(archivo.read_text(encoding="utf-8").splitlines(), 1):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            if "|" not in l:
                print(f"aviso: {archivo}:{n}: línea sin 'regla|ruta', ignorada", file=sys.stderr)
                continue
            r, ruta = (x.strip() for x in l.split("|", 1))
            reglas.append((r, ruta))
    return reglas


def coincide(exc, h):
    r, ruta = exc
    ok_regla = r == "*" or r == h["regla"] or r == h["regla"].split("-")[0]
    return ok_regla and fnmatch.fnmatch(h["ruta"], ruta)


def main(argv=None):
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description="Comprueba la web estática de APDER (docs/).")
    ap.add_argument("docs", nargs="?", default=str(aqui.parent / "docs"),
                    help="carpeta a revisar (por defecto ../docs respecto al script)")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    ap.add_argument("--excepciones", help="archivo regla|ruta (por defecto revision/excepciones-comprobador.txt junto a docs/)")
    args = ap.parse_args(argv)

    docs = Path(args.docs).resolve()
    if not docs.is_dir():
        print(f"No existe la carpeta {docs}", file=sys.stderr)
        return 2
    exc_arch = Path(args.excepciones) if args.excepciones else docs.parent / "revision" / "excepciones-comprobador.txt"
    excepciones = leer_excepciones(exc_arch)

    c = Comprobador(docs)
    c.ejecutar()

    usadas = set()
    finales, descontados = [], []
    for h in c.hallazgos:
        hit = next((e for e in excepciones if h["severidad"] == "error" and coincide(e, h)), None)
        if hit:
            usadas.add(hit)
            descontados.append(h)
        else:
            finales.append(h)
    for e in excepciones:
        if e not in usadas:
            finales.append({"regla": "excepciones", "severidad": "aviso", "ruta": e[1], "linea": None,
                            "mensaje": f"excepción sin uso: {e[0]}|{e[1]}"})

    errores = [h for h in finales if h["severidad"] == "error"]
    avisos = [h for h in finales if h["severidad"] == "aviso"]
    nombre = docs.name

    if args.json:
        print(json.dumps({
            "docs": str(docs), "paginas": c.paginas,
            "peso_total_bytes": c.total_bytes, "peso_wp_bytes": c.wp_bytes,
            "errores": len(errores), "avisos": len(avisos), "descontados": len(descontados),
            "hallazgos": finales,
        }, ensure_ascii=False, indent=2))
        return 1 if errores else 0

    print(f"Comprobador de la web · carpeta {docs} · {c.paginas} páginas HTML analizadas")
    ids = list(REGLAS) + ["excepciones"]
    for rid in ids:
        hs = [h for h in finales if h["regla"] == rid]
        titulo = REGLAS.get(rid, "Excepciones")
        ne = sum(h["severidad"] == "error" for h in hs)
        na = sum(h["severidad"] == "aviso" for h in hs)
        if rid == "excepciones" and not hs:
            continue
        estado = "OK" if not ne and not na else f"{ne} errores, {na} avisos"
        print(f"\n== {rid} · {titulo} → {estado}")
        for h in hs:
            etiqueta = {"error": "ERROR", "aviso": "AVISO", "info": "INFO "}[h["severidad"]]
            donde = h["ruta"] if h["ruta"].startswith("(") else f"{nombre}/{h['ruta']}"
            if h["linea"]:
                donde += f":{h['linea']}"
            print(f"  {etiqueta} {donde} — {h['mensaje']}")
    print(f"\nResumen: {len(errores)} errores, {len(avisos)} avisos"
          + (f", {len(descontados)} errores descontados por {exc_arch.name}" if descontados else ""))
    print("Resultado: " + ("FALLA (hay errores)" if errores else "CORRECTO (sin errores)"))
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
