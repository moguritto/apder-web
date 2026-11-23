#!/usr/bin/env python3
"""Genera docs/buscar/indice.json para el buscador de la web (docs/buscar/).

Solo usa la biblioteca estándar de Python 3. Se lanza desde cualquier carpeta:
    python3 scripts/construir_indice.py [RUTA/docs]

Qué indexa (las páginas ya rehechas con el diseño Tierra):
- Recorre docs/**/index.html. Se salta: 404.html, las redirecciones (meta refresh), las páginas noindex,
  las páginas que todavía son WordPress (cargan wp-content/wp-includes) y la propia página buscar/.
- Por página: url (relativa a docs/), título (h1), descripción (meta description), sección,
  resumen (máx. 600 caracteres de los primeros párrafos de <main>) y los h2/h3 (t = texto; id = ancla del
  propio encabezado o, si no tiene, la del h2 anterior, para enlazar al apartado).
- Por cada libro de docs/biblioteca/index.html (<li class="b-libro" data-cat data-idioma data-sust>,
  el mismo marcado que lee el buscador de esa página): título, autor, año, categoría, idioma, sustancias
  y descripción. Cada resultado enlaza a la ficha del libro cuando existe.
Cuando una página de WordPress se rehaga con el diseño Tierra, vuelve a lanzar este guion.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs'))
MAX_RESUMEN = 600

# sección a partir de la carpeta de primer nivel
SECCIONES = {
    '': 'Inicio',
    'sustancias': 'Sustancias',
    'medicinas': 'Medicinas',
    'investigacion-terapeutica': 'Investigación',
    'biblioteca': 'Biblioteca',
    'quien-es-quien': 'Quién es quién',
    'terapia-asistida-mdma': 'Terapia',
    'aviso-legal': 'Información legal',
    'politica-de-privacidad': 'Información legal',
}
# clases de bloque que no aportan al resumen
OMITIR_CLASES = {'s-nota', 's-antetitulo', 's-formula', 's-revisado', 's-toc-movil', 's-toc', 'b-libro', 'saltar'}
BLOQUES = {'p', 'li', 'td', 'th', 'h1', 'h2', 'h3', 'h4', 'summary', 'div', 'section', 'tr', 'ul', 'ol', 'details'}
VACIAS = {'br', 'img', 'input', 'hr', 'meta', 'link'}


def limpia(t):
    return re.sub(r'\s+', ' ', t).strip()


class Pagina(HTMLParser):
    """Extrae <main>: h1, h2/h3 y los textos de bloque para el resumen."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.en_main = False
        self.pila = []          # una marca por etiqueta abierta dentro de main: ¿zona omitida?
        self.omitir = 0
        self.cab = None         # (etiqueta, [trozos], id) mientras se lee un h1/h2/h3
        self.ultimo_id = ''     # id del último h2 con ancla
        self.h1 = ''
        self.encabezados = []
        self.parrafos = []
        self.actual = None
        self.descripcion = ''
        self.robots = ''
        self.wp = False
        self.refresh = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            n = (a.get('name') or '').lower()
            if n == 'description':
                self.descripcion = a.get('content') or ''
            elif n == 'robots':
                self.robots = (a.get('content') or '').lower()
            elif (a.get('http-equiv') or '').lower() == 'refresh':
                self.refresh = True
        if tag in ('link', 'script', 'img'):
            ref = (a.get('href') or '') + (a.get('src') or '')
            if 'wp-content' in ref or 'wp-includes' in ref:
                self.wp = True
        if tag == 'main':
            self.en_main = True
            return
        if not self.en_main:
            return
        clases = set((a.get('class') or '').split())
        if tag not in VACIAS:
            omite = tag in ('script', 'style', 'nav', 'svg') or bool(clases & OMITIR_CLASES)
            self.pila.append(omite)
            if omite:
                self.omitir += 1
        if tag in ('h1', 'h2', 'h3'):
            self.cab = (tag, [], a.get('id') or '')
        if tag in BLOQUES and not self.omitir:
            self._cierra_bloque()
            self.actual = []

    def handle_endtag(self, tag):
        if tag == 'main':
            self._cierra_bloque()
            self.en_main = False
            return
        if not self.en_main:
            return
        if tag in ('h1', 'h2', 'h3') and self.cab and self.cab[0] == tag:
            t = limpia(''.join(self.cab[1]))
            t = re.sub(r'\s*\(\d+\)$', '', t)   # «Historia (56)» -> «Historia»
            if tag == 'h1' and not self.h1:
                self.h1 = t
            elif tag in ('h2', 'h3') and t:
                if tag == 'h2':
                    self.ultimo_id = self.cab[2]
                e = {'t': t}
                ancla = self.cab[2] or self.ultimo_id
                if ancla:
                    e['id'] = ancla
                self.encabezados.append(e)
            self.cab = None
        if tag in BLOQUES and not self.omitir:
            self._cierra_bloque()
        if tag not in VACIAS and self.pila:
            if self.pila.pop():
                self.omitir -= 1

    def handle_data(self, d):
        if not self.en_main or self.omitir:
            return
        if self.cab is not None:
            self.cab[1].append(d)
        if self.actual is not None:
            self.actual.append(d)

    def _cierra_bloque(self):
        if self.actual:
            t = limpia(''.join(self.actual))
            if t:
                self.parrafos.append(t)
        self.actual = None


def resumen(parrafos, h1, encabezados):
    """Primeros textos de <main> sin repetir títulos, hasta ~600 caracteres (corta en palabra)."""
    saltar = {h1} | {e['t'] for e in encabezados}
    partes = []
    for t in parrafos:
        if t in saltar or len(t) < 25:
            continue
        partes.append(t)
        if sum(len(p) + 1 for p in partes) >= MAX_RESUMEN:
            break
    r = ' '.join(partes)
    if len(r) > MAX_RESUMEN:
        r = r[:MAX_RESUMEN].rsplit(' ', 1)[0].rstrip(' ,;:.') + '…'
    return r


def seccion_de(rel):
    carpeta = rel.split('/')[0] if '/' in rel else ''
    return SECCIONES.get(carpeta, 'Otras páginas')


def paginas():
    res = []
    for dirpath, _, ficheros in sorted(os.walk(RAIZ)):
        for f in sorted(ficheros):
            if f != 'index.html':
                continue
            ruta = os.path.join(dirpath, f)
            rel = os.path.relpath(ruta, RAIZ).replace(os.sep, '/')
            if rel.startswith('buscar/') or rel.startswith('wp-'):
                continue
            with open(ruta, encoding='utf-8') as fh:
                texto = fh.read()
            p = Pagina()
            p.feed(texto)
            if p.refresh or 'noindex' in p.robots or p.wp or not p.h1:
                continue
            url = '' if rel == 'index.html' else rel[:-len('index.html')]
            res.append({
                'url': url,
                'titulo': p.h1,
                'descripcion': limpia(p.descripcion),
                'seccion': seccion_de(rel),
                'resumen': resumen(p.parrafos, p.h1, p.encabezados),
                'encabezados': p.encabezados,
            })
    return res


class Libros(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.libros = []
        self.libro = None
        self.campo = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        clases = (a.get('class') or '').split()
        if tag == 'li' and 'b-libro' in clases:
            self.libro = {'cat': a.get('data-cat', ''), 'idioma': a.get('data-idioma', ''),
                          'sust': (a.get('data-sust') or '').split(), 'tit': [], 'meta': [], 'desc': [], 'url': ''}
        elif self.libro is not None and tag == 'p':
            for c, k in (('b-tit', 'tit'), ('b-meta', 'meta'), ('b-desc', 'desc')):
                if c in clases:
                    self.campo = k
        elif self.libro is not None and tag == 'a' and self.campo == 'tit':
            href = a.get('href', '')
            if href and not href.startswith(('/', 'http:', 'https:', '//')) and '..' not in href.split('/'):
                self.libro['url'] = 'biblioteca/' + href

    def handle_endtag(self, tag):
        if tag == 'p':
            self.campo = None
        elif tag == 'li' and self.libro is not None:
            l = self.libro
            partes = [x.strip() for x in limpia(''.join(l['meta'])).split(' · ')]
            autor = partes[0] if partes else ''
            anio = partes[1] if len(partes) > 2 and partes[1].isdigit() else ''
            self.libros.append({
                'titulo': limpia(''.join(l['tit'])),
                'autor': autor,
                'anio': anio,
                'categoria': l['cat'],
                'idioma': l['idioma'],
                'sustancia': l['sust'],
                'descripcion': limpia(''.join(l['desc'])),
                'url': l['url'] or 'biblioteca/',
            })
            self.libro = None

    def handle_data(self, d):
        if self.libro is not None and self.campo:
            self.libro[self.campo].append(d)


def libros():
    ruta = os.path.join(RAIZ, 'biblioteca', 'index.html')
    with open(ruta, encoding='utf-8') as fh:
        p = Libros()
        p.feed(fh.read())
    return p.libros


def main():
    global RAIZ
    if len(sys.argv) > 1:
        RAIZ = os.path.abspath(sys.argv[1])
    pag = paginas()
    lib = libros()
    salida = os.path.join(RAIZ, 'buscar', 'indice.json')
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    with open(salida, 'w', encoding='utf-8') as fh:
        json.dump({'paginas': pag, 'libros': lib}, fh, ensure_ascii=False, separators=(',', ':'))
        fh.write('\n')
    print('%d páginas y %d libros -> %s (%d KB)' % (len(pag), len(lib), salida, os.path.getsize(salida) // 1024))


if __name__ == '__main__':
    main()
