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
- En el menú, la sección se llama **«Medicinas»** (desde el 21/11/2026; antes «Sustancias»). Las direcciones no cambian: siguen en `/sustancias/`. El desplegable reúne las guías y los atajos «Todas las guías», «Medicinas por familias» (`/medicinas/`) y «Microdosis». «Terapia asistida con MDMA» (`/terapia-asistida-mdma/`) salió del menú el 23/11/2026: se llega desde la guía de MDMA (En pocas palabras y guías relacionadas). La cabecera está copiada en cada página: si se cambia, hay que cambiarla en todas.
- Desde el 23/11/2026 el menú tiene cinco entradas: **Medicinas ▾ · Aprender ▾ · Investigación · Biblioteca · Quiénes somos**. El desplegable «Aprender» (`#panel-aprender`) reúne Enciclopedia de medicinas, Psiconáutica, Quién es quién y Dónde formarse (`/formaciones/`); en esas secciones el botón «Aprender» lleva la clase `actual`. «Enciclopedia de medicinas» también está en los atajos del desplegable Medicinas. `menu.js` admite varios desplegables (al abrir uno se cierran los demás). Para que quepan las cinco entradas, entre 1001 y 1439 px «Buscar» queda solo con su icono y el lema bajo el logo aparece desde 1440 px (antes, 1240).
- `docs/sustancias/microdosis/index.html`: guía de microdosis (setas, LSD, ayahuasca, DMT e ibogaína) con la misma plantilla. A propósito **no da cifras de dosis ni pautas** (ni cantidades, ni calendarios, ni días de toma y descanso). Enlazada desde el megamenú («Microdosis», en los atajos), la cuadrícula, el mapa del sitio y los apartados de microdosis de psilocibina y LSD. Dibujo propio en `moleculas/microdosis.svg`.
- `docs/sustancias/sustancias.css`: estilos solo de estas páginas (títulos Libre Caslon, texto Inter, acento rojo, índice lateral).
- `docs/sustancias/moleculas/`: dibujos de las moléculas (SVG propios, hechos con RDKit).
- Textos propios en español, escritos para APDER. Para añadir otra sustancia, copia una carpeta de guía, cambia los textos y enlázala desde la cuadrícula de `docs/sustancias/index.html` y desde el megamenú.

## Enciclopedia de medicinas (nuevo, 23/11/2026)

- `docs/enciclopedia/`: portada con buscador, tarjetas, mapa e índice A–Z, y una página por ficha (`docs/enciclopedia/<slug>/`). Hoy: ayahuasca y matamoscas.
- No se edita el HTML a mano. Cada ficha es un archivo de datos, `enciclopedia/fichas/<slug>.json`; la portada sale de `enciclopedia/lista.json`. Se genera todo con `python3 enciclopedia/generar.py`, que copia la cabecera y el pie de `docs/sustancias/`.
- Estilos propios en `docs/enciclopedia/enciclopedia.css` (todo bajo `.enc`). Fotos en `docs/enciclopedia/img/`, cada una con su fila en `CREDITOS.md`.
- Cómo escribir una ficha nueva, reglas y lista de pendientes: `enciclopedia/LEEME.md`.
- En el menú desde el 23/11/2026: desplegable «Aprender» y atajo en el desplegable «Medicinas». `generar.py` copia la cabecera de `docs/sustancias/` y marca «Aprender» como sección actual.

## Otras secciones

- `docs/investigacion-terapeutica/`: orientación sobre la investigación por problema de salud y cómo participar en ensayos.
- `docs/medicinas/`: artículo con las medicinas psicodélicas y enteógenas por categorías.
- `docs/biblioteca/`: 425 libros con buscador y filtros (categoría, idioma y sustancia).
- `AUDITORIA.md`: fallos encontrados, propuestas y cómo evitar problemas de derechos de autor.

## Quién es quién (nuevo, 23-11-2026)

- `docs/quien-es-quien/`: fichas de personas (30 desde el 24/11/2026: Hofmann, Grof, María Sabina, Huxley, Osmond, los Wasson, Schultes, Leary, Ram Dass, Watts, los Shulgin y Zeff; tanda 3, España y Latinoamérica: Naranjo, Roquet, Guzmán, Fericgla, Riba, Bouso, Mestre Irineu, Amaringo y Dobkin de Rios; tanda 4: Christina Grof, McKenna, Ott, Strassman, Doblin, Griffiths, Feilding, Carhart-Harris y Pollan. Sin fecha de nacimiento publicada con fuente no se pone `nacio_iso` (Fericgla, Amaringo); la ficha sin libros en la Biblioteca omite la lista; la portada las agrupa por tipo y año de nacimiento; las fichas conjuntas usan `ld_personas` y una sola inicial) y una portada con tarjetas. En el menú desde el 23/11/2026, dentro de «Aprender» (el generador marca «Aprender» como sección actual).
- Se generan con `python3 scripts/quien_es_quien/generar.py .` (desde la raíz). Los textos y las fuentes están en `scripts/quien_es_quien/contenido.py` (primeras tres) y `personas_tanda2a.py` / `personas_tanda2b.py` / `personas_tanda3.py` / `personas_tanda4.py`; la cabecera y el pie se copian de la guía del 2C-B. Para añadir a alguien: nueva entrada en `contenido.py`, su tarjeta en `scripts/tarjetas_og.py` (`persona-<slug>`), su dirección en `sitemap.xml` y volver a lanzar `construir_indice.py`.
- Sin fotos de personas: cada ficha lleva un monograma con las iniciales.

## Formaciones en el mundo (en preparación, 23-11-2026)

- `docs/formaciones/index.html`: directorio de formaciones de todo el mundo (terapia asistida, facilitación, integración, reducción de riesgos, investigación, introducción y saberes tradicionales), con mapa de puntos, atajos por tipo, filtros con recuentos, buscador, orden y enlace compartible. Estilos y código viven en la propia página.
- En el menú desde el 23/11/2026 como «Dónde formarse» (desplegable «Aprender»), pero desde el 24-11-2026 está indexable y en el `sitemap.xml` (se dio por cerrada la primera versión; las fichas `por_confirmar` salen con aviso): el 24-11-2026 tiene 59 formaciones (13 más añadidas el mismo día: Emerald Valley, Hubbard, URV, Clínica Synaptica, ACPT Israel, Psychedelic Sitters School, Equanimity Academy, Beckley Academy, Zendo SIT, Fluence ×2, Harvard CME y NYU; las de «por_confirmar» salen de buscadores, sin leer su web entera). Antes eran 46 (las 6 últimas, de Suiza, Argentina, México, Chile y España, están `por_confirmar` desde resultados de búsqueda de sus webs oficiales): 20 de EE. UU. y Canadá más MIND Foundation, Mind Medicine Australia, Exeter, OPEN (2), IPI nivel I, ICEERS (2, Barcelona), Facultad de Medicina de Lisboa, Alma Viva (Brasil), Institute of Psychedelic Therapy (Reino Unido), Monash (2), Naropa, MAPS México, Tailandia, TheraPsil, Chacruna, Vital y Pacifica. Las de `estado: por_confirmar` salen con ese aviso hasta comprobarlas en su web. Siguen sin cubrirse África, Israel, Asia (salvo Tailandia) y gran parte de Europa; el directorio no es exhaustivo. Cuando esté completa: quitar `noindex` y añadirla al `sitemap.xml`.
- `docs/formaciones/formaciones.json`: una ficha por formación (`id`, `nombre`, `nombre_es`, `entidad`, `tipo_entidad`, `tipo`, `destinatarios`, `modalidad`, `idiomas`, `pais`, `ciudad`, `otros_lugares`, `sustancias`, `duracion_horas`, `duracion`, `precio`, `precio_eur` aproximado solo para el filtro, `reconocimiento`, `incluye`, `proxima`, `descripcion`, `url`, `estado`, `revisado`, `lat`, `lon`). Las fechas pasadas no se muestran; lo solo en línea no lleva `lat`/`lon`.
- APDER no imparte ni recomienda estas formaciones: la página lo dice arriba. Sin temas de legalidad: «Aprobada en Oregón / Colorado» solo como reconocimiento, si figura en la lista oficial.
- Tarjeta para compartir: `docs/img/og/formaciones.png` (dibujo `docs/img/formaciones.svg`).

## Imágenes para compartir (WhatsApp y redes)

- Cada página tiene su tarjeta de 1200×630 en `docs/img/og/`, a propósito sencilla: solo el título, el dibujo (la molécula en las guías) y la marca APDER. La portada, las páginas legales y la 404 usan `docs/img/og-apder.png`, hecha con el mismo guion.
- Se generan con `python3 scripts/tarjetas_og.py` (necesita `pip install pillow cairosvg fonttools brotli`). Para una página nueva: añade su línea en `TARJETAS`, genera y pon en su `<head>` `og:image` y `twitter:image` con la dirección absoluta `https://apder.org/img/og/<nombre>.png`.
- WhatsApp no enseña la imagen si pesa más de 300 KB: las tarjetas pesan entre 10 y 35 KB. WhatsApp guarda la vista previa de cada enlace; si un enlace ya se había enviado antes del cambio, puede tardar en verse la nueva.

## Guías de terapia (24-11-2026)

- `docs/terapia/index.html`: portada con tarjetas de las ocho guías, tabla «De un vistazo» (experiencia, duración, sesiones, lo más estudiado y punto de la investigación), lo que tienen en común, mirada humanista y transpersonal, preguntas antes de dar el paso y preguntas frecuentes.
- `docs/terapia/<slug>/index.html`: siete guías rehechas con la plantilla y los componentes `art-*` de `/terapia-asistida-mdma/` (portada con dibujo y dos chips, «En pocas palabras», «Lo que da seguridad», menú en cuatro partes: Conocer, El proceso, Lo que se sabe y Si te interesa): `psilocibina`, `lsd`, `ketamina`, `ayahuasca`, `ibogaina`, `mescalina` y `5-meo-dmt`. Cada una con referencias numeradas, medios y libros de la Biblioteca enlazados a su ficha.
- La guía de MDMA es `/terapia-asistida-mdma/` (no se toca desde aquí). `/terapia/mdma/` redirige a ella y `/terapia/marco-comun/` redirige a la portada (el marco común está ahora en la portada).
- Cada guía de medicina (`/sustancias/<slug>/`) enlaza a su guía de terapia (tarjeta en «guías relacionadas» y una frase antes de «Integración»).
- Estilos propios: `.tg-cards` y `.tg-tabla`, al final de `docs/tierra.css`; las páginas de terapia cargan `tierra.css?v=20261124b`. Tarjetas para compartir: `terapia-guias` y `terapia-<slug>` en `scripts/tarjetas_og.py`.
- Reglas: sin cifras de dosis; sin legalidad («dónde se ofrece» solo en lenguaje clínico); sin tono alarmista; APDER no ofrece terapias (lo dicen el aviso y el descargo). Pendiente de revisión experta.
- Se generaron con un guion que vive fuera del repo: los cambios futuros se hacen sobre el HTML publicado. Las cifras de ensayos recientes (psilocibina, LSD, 5-MeO-DMT) vienen de notas de las empresas y de prensa médica especializada; hay que revisarlas cuando se publiquen los artículos.
- Excepciones del comprobador (`revision/excepciones-comprobador.txt`): `h-wp` en ayahuasca e ibogaína, por dos PDF de ICEERS alojados en `wp-content`.

## Ayudas de lectura (tierra.js)

- `docs/tierra.js` (se carga en guías, medicinas, investigación, biblioteca y terapia asistida): cabecera fija que se encoge al bajar, botón «Contenido» en móvil y botón «Volver arriba».
- Las 19 guías siguen la misma plantilla (desde el 23/11/2026): En pocas palabras, Qué es, Cómo actúa, La experiencia, Dosis, Interacciones, Quién no debería, Cómo reducir riesgos, Si algo va mal, Investigación, Integración, Mitos, Historia, Preguntas frecuentes, Para leer más y Referencias. Todas se titulan «Guía completa». En 5-MeO-DMT, ibogaína, kratom y tabaco el apartado Dosis no da cifras a propósito; en el resto, las cifras de dosis no se han tocado y siguen pendientes de revisión experta.
- El esquema «Cuándo empieza y cuánto dura» (`.s-tiempos`) está en 9 guías, hecho a mano a partir de su tabla resumen: si cambian esos valores, hay que cambiar también el esquema.
