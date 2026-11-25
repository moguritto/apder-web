"""Cabecera, menú y pie de apder.org: la única copia buena.

La cabecera y el pie van copiados dentro de cada página. Este guion los escribe
en todas a la vez, con las direcciones relativas a cada carpeta, la sección del
menú marcada (`actual`) y `aria-current="page"` en el enlace de la propia página.

  python3 scripts/cabecera.py            escribe cabecera y pie en docs/**/*.html
  python3 scripts/cabecera.py --mira     dice qué cambiaría, sin escribir

Para cambiar el menú o el pie: se toca aquí (MEDICINAS, EXPERIENCIA, TERAPIA,
BIBLIOTECA, PIE_COLUMNAS) y se vuelve a lanzar. Los generadores de la
Enciclopedia y de Quién es quién copian la cabecera de una página publicada,
así que basta con lanzar este guion después de ellos.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
VERSION_CSS = "20261125b"   # se cambia cuando cambia tierra.css, para que el navegador no use la copia vieja

FLECHA = ('<svg viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2 4.2 6 8l4-3.8" fill="none" '
          'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# --- Medicinas: las guías, por familias (dirección, dibujo, nombre) ---
MEDICINAS = [
    ("Psicodélicos clásicos", [
        ("psilocibina", "psilocibina", "Setas de psilocibina"),
        ("lsd", "lsd", "LSD"),
        ("mescalina", "mescalina", "Mescalina, peyote y San Pedro"),
        ("dmt", "dmt", "DMT"),
        ("ayahuasca", "ayahuasca", "Ayahuasca"),
        ("5-meo-dmt", "5-meo-dmt", "5-MeO-DMT"),
    ]),
    ("Otras medicinas", [
        ("mdma", "mdma", "MDMA"),
        ("ketamina", "ketamina", "Ketamina"),
        ("ibogaina", "ibogaina", "Ibogaína"),
        ("2c-b", "2c-b", "2C-B"),
        ("4-aco-dmt", "4-aco-dmt", "4-AcO-DMT"),
    ]),
    ("Plantas y hongos", [
        ("amanita-muscaria", "amanita", "Amanita muscaria"),
        ("salvia-divinorum", "salvia", "Salvia divinorum"),
        ("cannabis", "cannabis", "Cannabis"),
        ("kanna", "kanna", "Kanna"),
        ("kratom", "kratom", "Kratom"),
        ("datura", "datura", "Datura"),
        ("cacao", "cacao", "Cacao"),
        ("tabaco", "tabaco", "Tabaco"),
    ]),
]

# --- Paneles de texto: (título del grupo, [(dirección, nombre, aclaración)]) ---
EXPERIENCIA = [
    ("Preparar", [
        ("psiconautica/set-y-setting/", "Set y setting", "La disposición y el entorno: lo que más influye"),
        ("medicinas/#reduccion-de-riesgos", "Reducción de riesgos", "Mezclas, análisis y compañía"),
    ]),
    ("Acompañar", [
        ("psiconautica/acompanante/", "El acompañante", "Quién acompaña y cómo hacerlo bien"),
        ("psiconautica/mal-viaje/", "Experiencias difíciles", "Qué son y cómo atravesarlas"),
    ]),
    ("Profundizar", [
        ("psiconautica/unidad-e-interconexion/", "Unidad e interconexión", "La vivencia de que todo está unido"),
        ("sustancias/microdosis/", "Microdosis", "Qué es y qué dice la investigación"),
    ]),
]
TERAPIA = [
    ("Guías de terapia", [
        ("terapia/", "Las ocho guías", "MDMA, psilocibina, LSD, ketamina, ayahuasca, ibogaína, mescalina y 5-MeO-DMT"),
        ("terapia/#en-comun", "Lo que tienen en común", "Preparar, acompañar e integrar"),
    ]),
    ("Investigación", [
        ("investigacion-terapeutica/", "Investigación terapéutica", "Qué se ha estudiado, por problema de salud"),
        ("investigacion-terapeutica/#participar", "Participar en un ensayo", "Cómo hacerlo con garantías"),
    ]),
    ("Formación", [
        ("formaciones/", "Dónde formarse", "Directorio de formaciones en el mundo"),
    ]),
]
BIBLIOTECA = [
    ("Libros", [
        ("biblioteca/", "Todos los libros", "Con buscador y filtros por tema, medicina e idioma"),
        ("biblioteca/?idioma=espa%C3%B1ol", "En español", "Los que se pueden leer en castellano"),
    ]),
    ("Por tema", [
        ("biblioteca/?cat=Terapia%20y%20cl%C3%ADnica", "Terapia y clínica", ""),
        ("biblioteca/?cat=Antropolog%C3%ADa%2C%20etnobot%C3%A1nica%20y%20chamanismo", "Antropología y chamanismo", ""),
        ("biblioteca/?cat=Memorias%20y%20testimonios", "Memorias y testimonios", ""),
    ]),
    ("Personas", [
        ("quien-es-quien/", "Quién es quién", "Hofmann, María Sabina, Grof, Naranjo y otras personas"),
    ]),
]

# --- Pie: columnas de navegación ---
PIE_COLUMNAS = [
    ("Medicinas", [
        ("sustancias/", "Todas las guías"),
        ("medicinas/", "Por familias"),
        ("enciclopedia/", "Enciclopedia"),
    ]),
    ("La experiencia", [
        ("psiconautica/", "Psiconáutica"),
        ("psiconautica/set-y-setting/", "Set y setting"),
        ("psiconautica/mal-viaje/", "Experiencias difíciles"),
        ("sustancias/microdosis/", "Microdosis"),
    ]),
    ("Terapia", [
        ("terapia/", "Guías de terapia"),
        ("investigacion-terapeutica/", "Investigación"),
        ("formaciones/", "Dónde formarse"),
    ]),
    ("Biblioteca", [
        ("biblioteca/", "Libros"),
        ("quien-es-quien/", "Quién es quién"),
    ]),
    ("APDER", [
        ("#about", "Quiénes somos"),
        ("#contacto", "Escríbenos"),
        ("buscar/", "Buscar"),
    ]),
]


def seccion(ruta):
    """Qué entrada del menú se marca como actual para una página (ruta relativa a docs/)."""
    r = ruta.replace("index.html", "")
    if r.startswith("sustancias/microdosis/") or r.startswith("psiconautica/"):
        return "experiencia"
    if r.startswith(("sustancias/", "medicinas/", "enciclopedia/")):
        return "medicinas"
    if r.startswith(("terapia/", "terapia-asistida-mdma/", "investigacion-terapeutica/", "formaciones/")):
        return "terapia"
    if r.startswith(("biblioteca/", "quien-es-quien/")):
        return "biblioteca"
    return ""


class Pagina:
    def __init__(self, ruta):
        self.ruta = ruta                                  # p. ej. "sustancias/lsd/index.html"
        self.propia = ruta.replace("index.html", "")      # "sustancias/lsd/"
        fondo = ruta.count("/")
        self.r = "/" if ruta == "404.html" else "../" * fondo
        self.sec = seccion(ruta)

    def h(self, destino):
        """href hacia una dirección del sitio (relativa a docs/), con aria-current si es esta página."""
        if destino.startswith("#"):
            return f'href="{self.r}{destino}"'
        url = self.r + destino
        aqui = ' aria-current="page"' if destino == self.propia else ""
        return f'href="{url}"{aqui}'

    def boton(self, clave, nombre):
        act = " actual" if self.sec == clave else ""
        return (f'<button type="button" class="menu-enlace menu-abre{act}" aria-expanded="false" '
                f'aria-controls="panel-{clave}">{nombre}{FLECHA}</button>')

    def grupos_texto(self, grupos, pre):
        out = []
        for i, (titulo, enlaces) in enumerate(grupos, 1):
            lis = "".join(
                f'<li><a {self.h(d)}><span>{n}' + (f"<small>{a}</small>" if a else "") + "</span></a></li>"
                for d, n, a in enlaces)
            out.append(f'<div class="panel-grupo"><p class="panel-sub" id="grupo-{pre}{i}">{titulo}</p>'
                       f'<ul aria-labelledby="grupo-{pre}{i}">{lis}</ul></div>')
        return "\n".join(out)

    def grupos_medicinas(self):
        out = []
        for i, (titulo, guias) in enumerate(MEDICINAS, 1):
            lis = "".join(
                f'<li><a {self.h("sustancias/" + d + "/")}><img src="{self.r}sustancias/moleculas/{m}.svg" alt="" '
                f'width="40" height="32" loading="lazy" decoding="async">{n}</a></li>' for d, m, n in guias)
            out.append(f'<div class="panel-grupo"><p class="panel-sub" id="grupo-{i}">{titulo}</p>'
                       f'<ul aria-labelledby="grupo-{i}">{lis}</ul></div>')
        return "\n".join(out)

    def panel_texto(self, clave, nombre, titulo, intro, grupos, pre, atajos=""):
        return f"""        <li class="menu-item menu-desp">
          {self.boton(clave, nombre)}
          <div class="panel panel-aprender" id="panel-{clave}">
            <div class="ancho panel-in">
              <div class="panel-intro">
                <p class="panel-titulo">{titulo}</p>
                <p>{intro}</p>{atajos}
              </div>
              <div class="panel-grupos">
{self.grupos_texto(grupos, pre)}
              </div>
            </div>
          </div>
        </li>"""

    def cabecera(self):
        r = self.r
        inicio = "./" if r == "" else r
        atajos_exp = f"""
                <ul class="panel-atajos">
                  <li><a {self.h("psiconautica/")}>Todo Psiconáutica</a></li>
                </ul>"""
        return f"""<header class="cabecera">
  <div class="ancho cab-fila">
    <a class="marca marca-original" href="{inicio}" aria-label="APDER · Association for Psychedelic Divulgation, Education and Research, inicio"><img src="{r}img/apder-icono.webp" alt="" width="455" height="344"><span class="marca-txt"><img class="marca-letras" src="{r}img/apder-letras.webp" alt="APDER" width="423" height="88"></span></a>
    <nav class="menu" id="menu" aria-label="Menú principal">
      <ul class="menu-lista">
        <li class="menu-item menu-desp">
          {self.boton("medicinas", "Medicinas")}
          <div class="panel" id="panel-medicinas">
            <div class="ancho panel-in">
              <div class="panel-intro">
                <p class="panel-titulo">Medicinas</p>
                <p>Dos maneras de conocer cada una: la guía, para la práctica; la ficha de la Enciclopedia, para la planta y su historia.</p>
                <ul class="panel-atajos">
                  <li><a {self.h("sustancias/")}>Todas las guías</a></li>
                  <li><a {self.h("medicinas/")}>Medicinas por familias</a></li>
                </ul>
                <a class="panel-destacado" {self.h("enciclopedia/")}><img src="{r}img/inicio/matamoscas.webp" alt="" width="560" height="700" loading="lazy" decoding="async"><span><b>Enciclopedia de medicinas</b><small>Plantas, hongos y preparados: origen, territorio y cultura</small></span></a>
              </div>
              <div class="panel-grupos">
{self.grupos_medicinas()}
              </div>
            </div>
          </div>
        </li>
{self.panel_texto("experiencia", "La experiencia", "La experiencia", "Lo que pasa antes, durante y después cuenta tanto como la sustancia. Aquí, lo que ayuda a prepararla, acompañarla y cuidarla.", EXPERIENCIA, "e", atajos_exp)}
{self.panel_texto("terapia", "Terapia", "Terapia e investigación", "Qué se sabe del uso terapéutico de estas medicinas y qué falta todavía por saber. APDER no ofrece sesiones ni terapias.", TERAPIA, "t")}
{self.panel_texto("biblioteca", "Biblioteca", "Biblioteca", "Más de 800 libros para leer a fondo y las personas que abrieron el camino.", BIBLIOTECA, "b")}
        <li class="menu-item menu-somos"><a class="menu-enlace" {self.h("#about")}>Quiénes somos</a></li>
      </ul>
      <div class="menu-pie"><a class="cab-escribe" {self.h("#contacto")}>Escríbenos</a><p>o directamente por <a href="https://wa.me/447916618725">WhatsApp</a></p></div>
    </nav>
    <div class="cab-acciones">
      <div class="idioma" role="group" aria-label="Idioma"><span class="idioma-act" lang="es" aria-current="true">ES</span><button type="button" class="idioma-en" lang="en" disabled title="Próximamente / Coming soon">EN</button></div>
      <a class="cab-buscar" {self.h("buscar/")} aria-label="Buscar"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M15.5 15.5 20 20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span>Buscar</span></a>
      <a class="cab-escribe" {self.h("#contacto")}>Escríbenos</a>
      <button type="button" class="menu-toggle" aria-expanded="false" aria-controls="menu" aria-label="Abrir menú"><i></i><span>Menú</span></button>
    </div>
  </div>
</header>"""

    def pie(self):
        r = self.r
        inicio = "./" if r == "" else r
        cols = []
        for i, (titulo, enlaces) in enumerate(PIE_COLUMNAS, 1):
            lis = "".join(f"<li><a {self.h(d)}>{n}</a></li>" for d, n in enlaces)
            cols.append(f'<div class="pie-grupo"><p class="pie-tit" id="pie-g{i}">{titulo}</p>'
                        f'<ul aria-labelledby="pie-g{i}">{lis}</ul></div>')
        cols = "\n".join(cols)
        return f"""<footer class="pie pie-nav pie-2">
<div class="ancho">
<span class="ancla" id="contact"></span>
<div class="pie-lema">
<div>
<a class="pie-logo" href="{inicio}" aria-label="APDER, inicio"><img src="{r}img/apder-icono.webp" alt="" width="455" height="344" loading="lazy" decoding="async"><img class="pie-letras" src="{r}img/apder-letras.webp" alt="APDER" width="423" height="88" loading="lazy" decoding="async"></a>
<p class="pie-frase">Información rigurosa sobre los psicodélicos: su historia, lo que dice la investigación sobre su uso terapéutico y cómo reducir sus riesgos.</p>
</div>
<div class="pie-contacto">
<p>Escríbenos. Respondemos en cuanto podemos.</p>
<div class="contacto-directo"><a class="btn t" href="https://wa.me/447916618725">WhatsApp</a><a class="btn c" href="mailto:info@apder.org">info@apder.org</a></div>
<p class="pie-tel"><a href="tel:+447916618725">+44 7916 618725</a></p>
</div>
</div>
<nav class="pie-cols" aria-label="Mapa de la web">
{cols}
</nav>
<div class="pie-abajo">
<p>Somos una asociación sin ánimo de lucro dedicada a la divulgación. <span lang="en">Association for Psychedelic Divulgation, Education and Research</span><br/>© 2026 APDER. Todos los derechos reservados.</p>
<p><a {self.h("aviso-legal/")}>Aviso legal</a> <a {self.h("politica-de-privacidad/")}>Privacidad y cookies</a> <a {self.h("creditos/")}>Créditos de las fotos</a></p>
</div>
</div>
</footer>"""


RE_CAB = re.compile(r'<header class="cabecera".*?</header>', re.S)
RE_PIE = re.compile(r'<footer class="pie.*?</footer>', re.S)
RE_CSS = re.compile(r'tierra\.css\?v=[0-9a-z]+')


def aplicar(texto, ruta):
    p = Pagina(ruta)
    texto, n1 = RE_CAB.subn(lambda m: p.cabecera(), texto, count=1)
    texto, n2 = RE_PIE.subn(lambda m: p.pie(), texto, count=1)
    texto = RE_CSS.sub("tierra.css?v=" + VERSION_CSS, texto)
    return texto, n1, n2


def main():
    mira = "--mira" in sys.argv
    cambiadas = sin_cab = sin_pie = 0
    for f in sorted(DOCS.rglob("*.html")):
        ruta = f.relative_to(DOCS).as_posix()
        antes = f.read_text(encoding="utf-8")
        if '<header class="cabecera"' not in antes:
            continue
        despues, n1, n2 = aplicar(antes, ruta)
        sin_cab += not n1
        if not n2:
            sin_pie += 1
            print("sin pie:", ruta)
        if despues != antes:
            cambiadas += 1
            if not mira:
                f.write_text(despues, encoding="utf-8")
    print(f"{'cambiarían' if mira else 'cambiadas'}: {cambiadas} · sin pie: {sin_pie}")


if __name__ == "__main__":
    main()
