# APDER: copia calcada; sin tienda, biblioteca ni donaciones (decisión de Mannu)
DOMAIN = "apder.org"
PAGES = {"": "", "terapia-asistida-mdma/": "terapia-asistida-mdma/", "meditacion-corazon-2026/": "meditacion-corazon-2026/", "divulgation/": "divulgation/", "protocolo-meditacion-agosto-2024/": "protocolo-meditacion-agosto-2024/"}
REDIRECTS = {"mdma/": "terapia-asistida-mdma/", "home2/": "", "inicio/": "", "about/": "", "education/": "", "research/": "",
             "meditacion-de-corazon/": "meditacion-corazon-2026/", "terapia-mdma-4/": "terapia-asistida-mdma/"}
EXTERNAL = {"participate/": "mailto:info@apder.org", "aviso-legal/": None, "politica-de-privacidad/": None}
EXTERNAL = {k: v for k, v in EXTERNAL.items() if v}
INSTAGRAM = "https://www.instagram.com/apder.org/"
EVENTON_STATIC = None
BOTONES = ('<div class="elementor-widget-container" style="text-align:center;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'
           '<a class="elementor-button elementor-button-link elementor-size-sm" href="mailto:info@apder.org?subject=Join%20the%20community">'
           '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">JOIN BY EMAIL</span></span></a></div>')
WIDGETS = {"elementor-widget-form": BOTONES}
REMOVE_IF_CONTAINS = ['href="/donations']
SUBS = [
    (r'<li class="menu-item[^"]*"><a href="/shop[^"]*"[^>]*>Library</a></li>', ''),
    (r'<li class="menu-item[^"]*"><a href="/participate/#start"[^>]*>Take an action</a></li>', ''),
]
OLD_REDIRECTS_DIR = None
SUBS += [(r'<a href="https://elarbolsuizo\.com/politica-de-cookies/"[^>]*><br></a>',
          '<br><a href="/aviso-legal/" style="color:inherit">Aviso legal</a> · <a href="/politica-de-privacidad/" style="color:inherit">Política de privacidad</a>')]
EXTRA_PAGES = ["aviso-legal/", "politica-de-privacidad/"]
LIVE_JSON = "/mnt/user-data/uploads/Downloads/apder_html_vivo.json"
SUBS += [(r'href="\+?(?:34)?(\d{9})"', r'href="tel:+34\1"')]
