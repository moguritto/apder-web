# Web de apder.org

Copia **calcada** de apder.org (26/10/2026): la web original de WordPress guardada tal cual con el plugin Simply Static, solo con las páginas elegidas. Se ve igual que la original en ordenador y en móvil.

- Dirección de prueba: https://moguritto.github.io/apder-web/
- La web está en **`docs/`**. Cada página es un `index.html` dentro de una carpeta con el nombre de su dirección (`docs/index.html` es la portada).
- Estilos, letras, fotos y vídeos están en `docs/wp-content/` y `docs/wp-includes/`, como en WordPress. No hace falta tocarlos.

## Cambiar un texto

1. Entra en https://github.com/moguritto/apder-web y abre `docs/`.
2. Abre la página (por ejemplo `docs/index.html`) y pulsa el lápiz (**Edit this file**).
3. Busca el texto (Ctrl+F) y cámbialo. Toca solo el texto entre `>` y `<`.
4. Pulsa **Commit changes…** y otra vez **Commit changes**. En uno o dos minutos está en la web.

## Para quien mantenga la web

- `scripts/calcada/build.py` + `cfg_*.py`: generan `docs/` desde el ZIP de Simply Static (direcciones relativas, sin rastreadores, formularios y widgets que necesitan servidor cambiados por WhatsApp/correo, redirecciones desde direcciones antiguas).
- `scripts/calcada/test.cjs` y `extra.txt`: comprobación con Playwright y archivos que Elementor carga a demanda.
- El resto de `scripts/` y `contenido/` es de la primera copia (reconstruida), ya sustituida.

## Regla de contenido: sin temas de legalidad

Decisión de Mannu (21-11-2026), para toda la web:

- No se tratan temas de legalidad: ni la situación legal de las sustancias, ni leyes, sanciones o listas de fiscalización, ni «dónde es legal», ni avisos de «no es asesoramiento jurídico».
- Sí se habla de investigación y de uso clínico, en lenguaje clínico: ensayos clínicos, medicamentos aprobados y dónde la ofrecen psiquiatras acreditados o equipos sanitarios.
- Para la seguridad se habla de análisis de sustancias, pureza y contexto («fuera del ámbito médico»), no de «mercado ilegal».
- Se mantienen las páginas obligatorias: Aviso legal y Política de privacidad y cookies.
- La biblioteca puede describir libros cuyo tema sea la historia o la política de las drogas.

## Nombre de APDER: siempre en inglés

Decisión de Mannu (21-11-2026): el nombre completo va **siempre en inglés y nunca en español**: **Association for Psychedelic Divulgation, Education and Research** (de ahí la sigla APDER).

- Aparece bajo el logo de la cabecera (pantallas de 1240 px o más), sobre el titular de la portada con las iniciales marcadas, en el pie de todas las páginas, en el aviso legal y en el texto alternativo de las tarjetas para compartir.
- En el HTML va dentro de `lang="en"`. Estilos al final de `docs/tierra.css` (`.marca-txt`, `.portada-sigla`).
- Si se regeneran páginas con guiones que viven fuera del repo (por ejemplo, las fichas de la biblioteca), hay que mantener el nombre en inglés en el pie.

## Sustancias (nuevo)

- `docs/sustancias/index.html`: página general de sustancias psicodélicas (tarjetas, comparativa, riesgos, preguntas).
- `docs/sustancias/<sustancia>/index.html`: 19 guías (psilocibina, LSD, MDMA, ketamina, ayahuasca, DMT, 5-MeO-DMT, mescalina, ibogaína, 2C-B, 4-AcO-DMT, Amanita muscaria, Salvia divinorum, cannabis, kanna, kratom, datura, cacao, tabaco).
- En el menú, la sección se llama **«Medicinas»** (desde el 21/11/2026; antes «Sustancias»). Las direcciones no cambian: siguen en `/sustancias/`. El desplegable reúne las 19 guías, «Medicinas por categorías» (`/medicinas/`) y «Terapia asistida con MDMA» (`/terapia-asistida-mdma/`), que ya no tienen entrada propia en el menú principal. La cabecera está copiada en cada página: si se cambia, hay que cambiarla en todas.
- `docs/sustancias/sustancias.css`: estilos solo de estas páginas (títulos Libre Caslon, texto Inter, acento rojo, índice lateral).
- `docs/sustancias/moleculas/`: dibujos de las moléculas (SVG propios, hechos con RDKit).
- Textos propios en español, escritos para APDER. Para añadir otra sustancia, copia una carpeta de guía, cambia los textos y enlázala desde la cuadrícula de `docs/sustancias/index.html` y desde el megamenú.

## Otras secciones

- `docs/investigacion-terapeutica/`: orientación sobre la investigación por problema de salud y cómo participar en ensayos.
- `docs/medicinas/`: artículo con las medicinas psicodélicas y enteógenas por categorías.
- `docs/biblioteca/`: 425 libros con buscador y filtros (categoría, idioma y sustancia).
- `AUDITORIA.md`: fallos encontrados, propuestas y cómo evitar problemas de derechos de autor.

## Imágenes para compartir (WhatsApp y redes)

- Cada página tiene su tarjeta de 1200×630 en `docs/img/og/`, a propósito sencilla: solo el título, el dibujo (la molécula en las guías) y la marca APDER. La portada, las páginas legales y la 404 usan `docs/img/og-apder.png`, hecha con el mismo guion.
- Se generan con `python3 scripts/tarjetas_og.py` (necesita `pip install pillow cairosvg fonttools brotli`). Para una página nueva: añade su línea en `TARJETAS`, genera y pon en su `<head>` `og:image` y `twitter:image` con la dirección absoluta `https://apder.org/img/og/<nombre>.png`.
- WhatsApp no enseña la imagen si pesa más de 300 KB: las tarjetas pesan entre 10 y 35 KB. WhatsApp guarda la vista previa de cada enlace; si un enlace ya se había enviado antes del cambio, puede tardar en verse la nueva.

## Guía para participantes

- `docs/guia-sesion/`: guía para enviar a quien tiene una sesión acordada (antes, salud, qué traer, el día, durante, música, después). No se indexa (`noindex`), no está en el mapa del sitio ni en el buscador, y no se enlaza desde el menú: solo se llega por el enlace.
- Sustituye en contenido a `docs/meditacion-corazon-2026/` y `docs/protocolo-meditacion-agosto-2024/`, que se conservan tal cual (con su tarjeta nueva para compartir).

## Ayudas de lectura (tierra.js)

- `docs/tierra.js` (se carga en guías, medicinas, investigación, biblioteca y terapia asistida): cabecera fija que se encoge al bajar, botón «Contenido» en móvil y botón «Volver arriba».
- Las guías de sustancias con menos de ~1.500 palabras se llaman **«Ficha breve»**; las completas (ayahuasca, ketamina, LSD, MDMA, psilocibina) siguen como «Guía completa».
- El esquema «Cuándo empieza y cuánto dura» (`.s-tiempos`) está en 9 guías, hecho a mano a partir de su tabla resumen: si cambian esos valores, hay que cambiar también el esquema.
