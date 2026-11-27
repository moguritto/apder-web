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

## Cabecera, menú y pie (25-11-2026)

- **La copia buena está en `scripts/cabecera.py`.** La cabecera y el pie siguen copiados dentro de cada página, pero ya no se tocan a mano: se cambia el guion y se lanza `python3 scripts/cabecera.py` (con `--mira` solo dice cuántas páginas cambiaría). Escribe las direcciones relativas a cada carpeta, marca la sección (`actual`) y pone `aria-current="page"` en el enlace de la propia página. También pone la misma versión de `tierra.css` en todas (`VERSION_CSS`).
- Menú por intención, cuatro puertas y «Quiénes somos»: **Medicinas** (las 19 guías, Todas las guías, Medicinas por familias y la Enciclopedia destacada) · **La experiencia** (set y setting, reducción de riesgos, el acompañante, experiencias difíciles, unidad, microdosis y Psiconáutica) · **Terapia** (guías de terapia, investigación, participar en un ensayo y dónde formarse; el desplegable dice que APDER no ofrece sesiones) · **Biblioteca** (libros, entradas por tema e idioma y Quién es quién). «Aprender» ya no existe. «Terapia asistida con MDMA» sigue fuera del menú.
- Qué sección se marca: `seccion()` en el guion (Enciclopedia → Medicinas; Microdosis y Psiconáutica → La experiencia; Formaciones e Investigación → Terapia; Quién es quién → Biblioteca).
- El logo lleva las letras originales (`docs/img/apder-letras.webp`), no texto. El lema en inglés ya no va bajo el logo: sigue en el pie, en la portada y en el aviso legal.
- Pie: marca, texto y contacto una sola vez, y cinco columnas de navegación (`PIE_COLUMNAS`). Conserva el ancla `#contact`.
- Estilos: bloque «Menú por intención y pie con navegación», al final de `docs/tierra.css`. El desplegable nunca es más alto que la pantalla; entre 1001 y 1079 px se oculta «Quiénes somos» (está en el pie).
- Los generadores de la Enciclopedia y de Quién es quién copian la cabecera de una página publicada y marcan su sección; después de lanzarlos conviene lanzar `scripts/cabecera.py`.
- Los párrafos más antiguos de este archivo que hablan del menú de cinco entradas con «Aprender» quedan como historia.

## Una seña por puerta del menú (25-11-2026, decisión de Mannu)

Mannu pidió que las secciones no se parezcan tanto entre sí. La cabecera, el pie, las letras y la paleta son comunes; cada puerta tiene su seña:

- **Guías de medicinas** (y «Medicinas por familias»): papel cuadriculado, claro, con la molécula y el **símbolo** de cada guía (Ps, LSD, K…) y un color por familia (teja, azul, verde). **Sin fotos**: en las tarjetas mezclar fotos y moléculas no quedaba bien.
- **Enciclopedia**: verde pino y fotos. Las fotos son cosa suya.
- **Biblioteca y Quién es quién**: lacre oscuro; cubiertas en una, monogramas en la otra.
- **Terapia** (guías de terapia e Investigación terapéutica): fondo claro con manchas e ilustración.
- **Psiconáutica**: curvas de nivel (la lleva otro chat).

Si se rehace una página, que siga la seña de su puerta y no la de la vecina.

## Investigación terapéutica y Medicinas por familias (páginas enteras, 27-11-2026)

- Las dos páginas salen **enteras** de un guion (hasta el 26-11 solo salía la apertura y el resto se escribía a mano). El texto vive aparte, en HTML llano, y **ahí se corrige**; el guion le pone el diseño y no cambia ni una palabra. Después de tocar el texto se relanza el guion. Las páginas publicadas no se editan a mano: el guion las reescribe.
  - `python3 scripts/medicinas/generar.py` · texto en `scripts/medicinas/texto.html` · estilos en `docs/medicinas/medicinas.css` (todo bajo `.mf`). Seña de las Guías de medicinas: papel cuadriculado, símbolo y un color por grupo. Portada con la tabla de las nueve familias, índice lateral, «de un vistazo», una lámina por familia (con la molécula de una de sus guías) y una entrada por medicina con su casilla: rellena si tiene guía, punteada si no. Lo que no está en el texto (grupo de cada familia; símbolo, guía y fichas de Enciclopedia y de Psiconáutica de cada entrada) va en `FAMILIAS` y `ENTRADAS`, arriba del guion: si en el texto se añade, se quita o se renombra una entrada, el guion se para y dice cuál. Las seis figuras con fotos son recortes de fotos de la Enciclopedia (`FOTOS`); con `--fotos` se rehacen en `docs/medicinas/img/` (cada recorte, con su fila en `CREDITOS.md`).
  - `python3 scripts/investigacion/generar.py` · texto en `scripts/investigacion/texto.html` · estilos y guion propios: `docs/investigacion-terapeutica/investigacion.css` e `investigacion.js` (todo bajo `.iv`). Seña de Terapia (fondo claro, manchas e ilustración), pero **sin cargar las hojas de `docs/terapia/`**: la página se sostiene sola, para que un cambio en las guías de terapia no la rompa. La pirámide «De un vistazo», el medidor de cada línea (uno, dos o tres trazos), la pista de fases y la ficha de cada problema de salud se leen de la tabla «Cómo va la investigación en cada problema de salud» del texto. El gráfico de tamaños de muestra sale de `ESTUDIOS`: cada cifra va con la frase del texto de donde sale, y el guion se para si esa frase ya no está.
- Ya no hay `apertura.py` ni marcas `<!-- apertura:… -->`.
- Anclas del menú que los guiones conservan: `/medicinas/#reduccion-de-riesgos` e `/investigacion-terapeutica/#participar`.
- Si se tocan los estilos o el guion de la página, subir `VERSION` en su `generar.py` (va en el `?v=`).
- En el móvil, el título de cada entrada de Medicinas **no** es `flex` a propósito: en `flex`, cada cursiva del título (*Ipomoea*, *Argyreia*) pasa a ser una pieza suelta y el título se rompe.

## Fotos, créditos y pie (25-11-2026, decisiones de Mannu)

- **Fotos, de cuando en cuando.** Mannu quiere que haya fotos repartidas por la web, sin saturar. Dónde van hoy fuera de la Enciclopedia: la portada; una franja en «Todas las guías» («Las plantas, de cerca»); una foto dentro del texto de 11 guías, tras el primer párrafo de «Qué es»; seis figuras en «Medicinas por familias», como láminas de cuaderno entre el texto (desde el 27/11/2026); el fondo de «Buscar» y el de la página no encontrada. Dónde no: en las tarjetas de las guías (ahí, solo molécula) ni en Quién es quién (sin fotos de personas).
- **Créditos en una sola página.** El párrafo de créditos de la portada saturaba. Ahora todos están en `docs/creditos/` (`python3 scripts/creditos.py`, que los lee de `CREDITOS.md`) y el pie de todas las páginas enlaza a ella («Créditos de las fotos»). Las licencias piden citar al autor: la página de créditos y la fila en `CREDITOS.md` no son opcionales. Al añadir una foto: su fila en `CREDITOS.md` y relanzar el guion. Las fichas de la Enciclopedia siguen llevando además sus créditos propios.
- **Pie rehecho:** oscuro, con el lema en grande, el contacto a la derecha, el mapa de la web en cinco columnas y una línea final con los enlaces legales y los créditos. Sale de `scripts/cabecera.py`; estilos al final de `docs/tierra.css` (`footer.pie.pie-2`). El logo del pie es el mismo archivo, aclarado con un filtro.
- **Buscar y página no encontrada:** apertura con foto de fondo y el buscador encima (`docs/buscar/buscar.css`, que también carga `docs/404.html`). Los recortes salen de `scripts/fotos_portada.py`.

## Todas las guías (rehecha el 25-11-2026)

- `docs/sustancias/index.html` ya no se edita a mano: sale de `python3 scripts/guias/generar.py`.
- Parte alta en `<div class="enc gui">` (estilos en `docs/sustancias/guias.css`, todo bajo `.gui`; de `enciclopedia.css` solo usa la rejilla y el buscador): apertura de cuaderno con buscador de guías (por nombre y por apodos) y la **tabla de símbolos** (una celda por guía, una fila por familia; `SIMBOLOS` en el guion), las 19 tarjetas por familias, el esquema «Cuánto dura cada una» y cuatro puertas. Debajo sigue el texto de siempre (`scripts/guias/texto.html`), con los estilos de lectura de `tierra.css`.
- Las familias y el orden son los del menú (`MEDICINAS`, en `scripts/cabecera.py`). Familia y duración de cada tarjeta se leen de la ficha de cada guía publicada; el esquema de duraciones usa la tabla `DURA` del guion, copiada a mano de esas fichas (si cambia una duración en una guía, hay que cambiarla ahí). El tabaco no tiene duración en su guía y no sale en el esquema.
- Cada tarjeta lleva la molécula y su símbolo, sin fotos. Las fotos van en la franja «Las plantas, de cerca» (`FRANJA`), que enlaza a la Enciclopedia.

## Plantilla de las guías (25-11-2026)

- Las 20 guías (`docs/sustancias/<guía>/`) abren como una hoja de cuaderno, con el color de su familia: título grande, apodos, aviso y, a la derecha, la ficha con el símbolo, la molécula y los datos en líneas (familia, vía, inicio, duración). «En pocas palabras» es una sola tarjeta con la pregunta a la izquierda. Los apartados van separados por una línea fina.
- Estilos en `docs/sustancias/guia.css` (apertura bajo `.s-cab-guia`, resumen bajo `.s-resumen`). El resto sigue en `tierra.css`.
- Las guías se siguen escribiendo a mano. `python3 scripts/guias/plantilla.py` pone al día el marcado de esas dos piezas sin tocar el texto y se puede lanzar las veces que haga falta. Guía nueva: copiar una carpeta, cambiar el texto y lanzarlo. El símbolo de cada guía está en `SIMBOLOS` (`scripts/guias/generar.py`).

## Biblioteca (rehecha el 25-11-2026)

- **Estilos y código compartidos:** `docs/biblioteca/biblioteca.css` y `docs/biblioteca/biblioteca.js`. Antes iban copiados dentro de cada página (unos 7 KB por ficha); ya no. Arriba del CSS están los estilos de siempre y al final, el diseño nuevo.
- **Portada del catálogo** (`docs/biblioteca/index.html`): sale de `python3 scripts/biblioteca/portada.py`. Apertura con buscador y abanico de cubiertas (`ABANICO`), «Por dónde empezar» (cuatro rutas de tres libros, `RUTAS`), entradas por tema, medicina e idioma con recuentos, el catálogo con sus filtros y un enlace a Quién es quién. El guion conserva tal cual la lista de libros (`ul#b-lista`) y el árbol de filtros (`aside#b-filtros`) de la página publicada y vuelve a contar: los libros no se editan en el guion.
- El buscador de la apertura y las entradas mueven los filtros del catálogo sin recargar; si se llega con filtros en la dirección (`?idioma=`, `?cat=`, `?sust=`, `?autor=`, `?q=`, `?orden=`), la página baja sola al catálogo.
- **Ficha de cada libro** (`docs/biblioteca/<libro>/index.html`, 807): apertura en lacre con la cubierta, título, autoría y etiquetas; debajo, la descripción y los datos de edición a la izquierda y «Dónde encontrarlo» a la derecha; al final, lecturas relacionadas. `python3 scripts/biblioteca/plantilla.py` recoloca esas piezas sin tocar el texto (comprueba que las palabras de cada ficha son las mismas antes y después; si no, no la escribe) y se puede lanzar las veces que haga falta. Las fichas siguen siendo HTML publicado: un libro nuevo se añade copiando una ficha y su `<li>` en la portada, y lanzando los dos guiones.
- Datos que faltan, a la vista en la portada: el idioma está anotado en 426 de las 807 fichas y hay 262 con imagen de portada; el resto lleva cubierta tipográfica.

## Portada (rehecha el 24-11-2026)

- `docs/index.html` habla el mismo lenguaje que la Enciclopedia: `<main class="enc ini">` carga `tierra.css`, `enciclopedia/enciclopedia.css` y `inicio.css` (lo propio de la portada, todo bajo `.ini`). Si se cambia `enciclopedia.css`, hay que mirar también la portada.
- Orden: apertura con buscador y tres fotos en arcos; tira de seis puertas; Enciclopedia (tres fichas); Guías de medicinas (las 19, por familias); La experiencia y Terapia e investigación; Biblioteca y Quién es quién; cita; Quiénes somos (`#about`) y Hablemos (`#contacto`). Esas dos anclas se enlazan desde la cabecera de todas las páginas: no hay que cambiarlas.
- Fotos: recortes ligeros en `docs/img/inicio/*.webp`, hechos con `python3 scripts/fotos_portada.py` (necesita `pip install pillow`) a partir de `docs/enciclopedia/img/`. Autor y licencia de cada una, en `CREDITOS.md` y en la página de créditos (la portada ya no los lleva). El arco grande (`peyote.webp`) es la imagen principal de la página: se precarga en el `<head>` y no lleva animación de opacidad.
- Bajo la tira de seis puertas hay una línea de **extras** («Y además»: Quién es quién, Dónde formarse, Medicinas por familias y Microdosis), en pequeño y aparte, para lo que no es una de las seis secciones principales (25-11-2026). Lo nuevo que no sea principal va ahí, no como séptima puerta.
- Recuentos escritos a mano en la portada: «19 guías» y «más de 800 libros». Si cambian, hay que cambiarlos ahí (antes decía 425 libros cuando la Biblioteca ya tenía 807).
- Los enlaces «Entrar por» de la Biblioteca usan sus filtros por dirección (`biblioteca/?idioma=español`, `biblioteca/?cat=…`).
- La portada no regenera `docs/buscar/indice.json`: su resumen se actualiza la próxima vez que alguien lance `scripts/construir_indice.py`.

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

## Psiconáutica (aspecto wiki desde el 26-11-2026)

- `docs/psiconautica/`: PsychonautWiki en español, aparte de la Enciclopedia de medicinas y enlazada en el menú. **Aspecto de la wiki original** (decisión de Mannu, 26-11-2026): panel lateral, pestañas, ficha a la derecha, índice «Contenido» y avisos arriba, sin el logo ni el nombre de PsychonautWiki. El rediseño propio sigue en `psiconautica.css` y sale con `--aspecto apder`.
- No se edita el HTML a mano. Todo sale de `scripts/psiconautica/generar.py` (solo biblioteca estándar):
  - `--wiki CARPETA`: lee el wikitexto traducido (la carpeta del Mac `Documentos/psychonautwiki-es`, con `traducido/` y `original/indice.json`) y lo convierte con `wiki.py`, que despliega las piezas compartidas de la wiki (listas de efectos, interacciones peligrosas, avisos; las 64 traducidas están en `plantillas_es.py`). Las direcciones salen de `generar_web_psiconautica.py` de esa carpeta, para no cambiar ninguna URL.
  - Sin argumentos rehace todo desde lo publicado (para cambiar la plantilla sin las traducciones). Regenerar dos veces da lo mismo.
  - `--excluidas ARCHIVO`: títulos que no se publican. `--sin-legalidad`: quita la situación legal (por defecto se publica: decisión de Mannu, 25-11-2026).
  - Títulos en español: `titulos_es.py`.
- Reglas que aplica siempre: fuera los apartados de dosis y administración; fuera cultivo, extracción, síntesis, recetas y calendarios de reducción; fuera las frases con cantidades («50 mg»); fuera los apartados vacíos; enlaces internos cuando la página existe. Informa de las piezas de la wiki que aún no sabe convertir.
- Orden completo: `python3 scripts/psiconautica/generar.py --wiki CARPETA --excluidas CARPETA/excluidas_web.txt`, después `python3 scripts/construir_indice.py` y `python3 scripts/comprobar_web.py`.
- Estilos: `wiki.css` (todo bajo `.wk`); código: `psiconautica.js` (buscador, filtros, índice lateral y «Página al azar»). Si se tocan, subir `VERSION` en `generar.py`.
- Licencia: CC BY-SA 4.0; cada página enlaza a su original y lo dice en la ficha y al pie.

## Otras secciones

- `docs/investigacion-terapeutica/`: orientación sobre la investigación por problema de salud y cómo participar en ensayos.
- `docs/medicinas/`: artículo con las medicinas psicodélicas y enteógenas por categorías.
- `docs/biblioteca/`: 807 libros con buscador y filtros; ver «Biblioteca (rehecha el 25-11-2026)».
- `AUDITORIA.md`: fallos encontrados, propuestas y cómo evitar problemas de derechos de autor.

## Quién es quién (nuevo, 23-11-2026)

- `docs/quien-es-quien/`: fichas de personas (30 desde el 24/11/2026: Hofmann, Grof, María Sabina, Huxley, Osmond, los Wasson, Schultes, Leary, Ram Dass, Watts, los Shulgin y Zeff; tanda 3, España y Latinoamérica: Naranjo, Roquet, Guzmán, Fericgla, Riba, Bouso, Mestre Irineu, Amaringo y Dobkin de Rios; tanda 4: Christina Grof, McKenna, Ott, Strassman, Doblin, Griffiths, Feilding, Carhart-Harris y Pollan. Sin fecha de nacimiento publicada con fuente no se pone `nacio_iso` (Fericgla, Amaringo); la ficha sin libros en la Biblioteca omite la lista; la portada las agrupa por tipo y año de nacimiento; las fichas conjuntas usan `ld_personas` y una sola inicial) y una portada con tarjetas. En el menú desde el 23/11/2026, dentro de «Aprender» (el generador marca «Aprender» como sección actual).
- Se generan con `python3 scripts/quien_es_quien/generar.py .` (desde la raíz). Los textos y las fuentes están en `scripts/quien_es_quien/contenido.py` (primeras tres) y `personas_tanda2a.py` / `personas_tanda2b.py` / `personas_tanda3.py` / `personas_tanda4.py`; la cabecera y el pie se copian de la guía del 2C-B. Para añadir a alguien: nueva entrada en `contenido.py`, su tarjeta en `scripts/tarjetas_og.py` (`persona-<slug>`), su dirección en `sitemap.xml` y volver a lanzar `construir_indice.py`.
- Sin fotos de personas: cada ficha lleva un monograma con las iniciales.
- Desde el 25-11-2026 lleva la seña de la Biblioteca (lacre): la portada abre con un muro de los 30 monogramas por año de nacimiento (el aro dice el grupo) y las fichas, con el nombre sobre lacre y los datos en líneas. Los estilos salieron del generador a `docs/quien-es-quien/quien.css`. Después de generar hay que lanzar `python3 scripts/cabecera.py`.

## Formaciones en el mundo (rehecha el 26-11-2026)

- `docs/formaciones/index.html`: directorio de formaciones de todo el mundo (terapia asistida, facilitación, integración, reducción de riesgos, investigación, introducción y saberes tradicionales).
- **Rehecha el 26-11-2026** con la seña de Terapia (fondo claro y manchas) y una propia: el globo. La página ya no lleva estilos ni código dentro: están en `docs/formaciones/formaciones.css` (todo bajo `.fm`, prefijo `fm-`) y `docs/formaciones/formaciones.js`. Partes: portada con buscador, atajos y globo; cifras; «¿Qué quieres aprender?»; «Empiezan pronto» (las cuatro fechas más cercanas; se esconde si no hay); directorio con filtros rápidos, filtros con recuentos, orden y enlace compartible; «Cómo elegir»; preguntas frecuentes (también en los datos estructurados de la cabecera: si se cambia una, se cambia en los dos sitios); método y fuentes.
- **Quien cambie datos solo toca `formaciones.json`**: la página lo lee al cargar y saca de ahí cifras, recuentos, fechas, regiones y puntos del globo. No hay que regenerar nada. Las etiquetas visibles de cada valor están en la tabla `T` de `formaciones.js`; un valor nuevo (otro tipo, otro reconocimiento…) se ve tal cual, con la primera letra en mayúscula, hasta que se añade ahí. Las regiones salen del país (tabla `REG`).
- El globo: `docs/formaciones/mundo.json` (países de Natural Earth 1:50 m, dominio público, simplificados y con más detalle en Europa y Norteamérica) y `docs/formaciones/geo.min.js` (la parte de d3-geo y topojson-client que hace falta; licencia ISC, citada en el propio archivo). Los dos salen de `scripts/formaciones/mapa.mjs` y solo hay que rehacerlos si se quiere otro nivel de detalle. Se gira arrastrando o con las flechas; las ciudades cercanas se juntan en un punto con su número y se separan al acercarse. Solo salen en el globo las formaciones presenciales o mixtas que traen `lat` y `lon`; las que no traen `ciudad` se rotulan con el país. Sin JavaScript queda la esfera vacía y el aviso.
- Direcciones que se pueden compartir: `?q=`, `?tipo=`, `?dest=`, `?modo=`, `?idioma=`, `?region=`, `?pais=`, `?sust=`, `?dur=`, `?precio=`, `?recon=`, `?entidad=`, `?fecha=1`, `?ciudad=` (p. ej. `portland-us`; se admite la forma antigua `lat,lon`), `?orden=` y `#f-<id>` para ir a una ficha.
- En el menú desde el 23/11/2026 como «Dónde formarse» (desplegable «Aprender»), pero desde el 24-11-2026 está indexable y en el `sitemap.xml` (se dio por cerrada la primera versión; las fichas `por_confirmar` salen con aviso): el 24-11-2026 tiene 61 formaciones (25-11: añadidas Memoru y Ceremonia Edu desde la lista oficial de Colorado; las otras 13 de esa lista ya estaban con el sello «Colorado»); antes 59 (13 más añadidas el mismo día: Emerald Valley, Hubbard, URV, Clínica Synaptica, ACPT Israel, Psychedelic Sitters School, Equanimity Academy, Beckley Academy, Zendo SIT, Fluence ×2, Harvard CME y NYU; las de «por_confirmar» salen de buscadores, sin leer su web entera). Antes eran 46 (las 6 últimas, de Suiza, Argentina, México, Chile y España, están `por_confirmar` desde resultados de búsqueda de sus webs oficiales): 20 de EE. UU. y Canadá más MIND Foundation, Mind Medicine Australia, Exeter, OPEN (2), IPI nivel I, ICEERS (2, Barcelona), Facultad de Medicina de Lisboa, Alma Viva (Brasil), Institute of Psychedelic Therapy (Reino Unido), Monash (2), Naropa, MAPS México, Tailandia, TheraPsil, Chacruna, Vital y Pacifica. Las de `estado: por_confirmar` salen con ese aviso hasta comprobarlas en su web. Siguen sin cubrirse África, Israel, Asia (salvo Tailandia) y gran parte de Europa; el directorio no es exhaustivo. Cuando esté completa: quitar `noindex` y añadirla al `sitemap.xml`.
- `docs/formaciones/formaciones.json`: una ficha por formación (`id`, `nombre`, `nombre_es`, `entidad`, `tipo_entidad`, `tipo`, `destinatarios`, `modalidad`, `idiomas`, `pais`, `ciudad`, `otros_lugares`, `sustancias`, `duracion_horas`, `duracion`, `precio`, `precio_eur` aproximado solo para el filtro, `reconocimiento`, `incluye`, `proxima`, `descripcion`, `url`, `estado`, `revisado`, `lat`, `lon`). Las fechas pasadas no se muestran; lo solo en línea no lleva `lat`/`lon`.
- APDER no imparte ni recomienda estas formaciones: la página lo dice arriba. Sin temas de legalidad: «Aprobada en Oregón / Colorado» solo como reconocimiento, si figura en la lista oficial.
- Tarjeta para compartir: `docs/img/og/formaciones.png` (dibujo `docs/img/formaciones.svg`).

## Imágenes para compartir (WhatsApp y redes)

- Cada página tiene su tarjeta de 1200×630 en `docs/img/og/`, a propósito sencilla: solo el título, el dibujo (la molécula en las guías) y la marca APDER. La portada, las páginas legales y la 404 usan `docs/img/og-apder.png`, hecha con el mismo guion.
- Se generan con `python3 scripts/tarjetas_og.py` (necesita `pip install pillow cairosvg fonttools brotli`). Para una página nueva: añade su línea en `TARJETAS`, genera y pon en su `<head>` `og:image` y `twitter:image` con la dirección absoluta `https://apder.org/img/og/<nombre>.png`.
- WhatsApp no enseña la imagen si pesa más de 300 KB: las tarjetas pesan entre 10 y 35 KB. WhatsApp guarda la vista previa de cada enlace; si un enlace ya se había enviado antes del cambio, puede tardar en verse la nueva.

## Guías de terapia (24-11-2026)

- `docs/terapia/index.html`: portada de la puerta Terapia, rehecha a mano el 26-11-2026 (ver «Portada de Guías de terapia» más abajo).
- `docs/terapia/<slug>/index.html`: siete guías rehechas con la plantilla y los componentes `art-*` de `/terapia-asistida-mdma/` (portada con dibujo y dos chips, «En pocas palabras», «Lo que da seguridad», menú en cuatro partes: Conocer, El proceso, Lo que se sabe y Si te interesa): `psilocibina`, `lsd`, `ketamina`, `ayahuasca`, `ibogaina`, `mescalina` y `5-meo-dmt`. Cada una con referencias numeradas, medios y libros de la Biblioteca enlazados a su ficha.
- La guía de MDMA es `/terapia-asistida-mdma/` (no se toca desde aquí). `/terapia/mdma/` redirige a ella y `/terapia/marco-comun/` redirige a la portada (el marco común está ahora en la portada).
- Cada guía de medicina (`/sustancias/<slug>/`) enlaza a su guía de terapia (tarjeta en «guías relacionadas» y una frase antes de «Integración»).
- Estilos: las siete guías usan los componentes `art-*` de `docs/tierra.css`. `.tg-cards` y `.tg-tabla` (al final de `tierra.css`) eran de la portada antigua y ya no los usa ninguna página: se pueden borrar la próxima vez que se cambie la versión de `tierra.css`. Tarjetas para compartir: `terapia-guias` y `terapia-<slug>` en `scripts/tarjetas_og.py`.
- Reglas: sin cifras de dosis; sin legalidad («dónde se ofrece» solo en lenguaje clínico); sin tono alarmista; APDER no ofrece terapias (lo dicen el aviso y el descargo). Pendiente de revisión experta.
- Se generaron con un guion que vive fuera del repo: los cambios futuros se hacen sobre el HTML publicado. Las cifras de ensayos recientes (psilocibina, LSD, 5-MeO-DMT) vienen de notas de las empresas y de prensa médica especializada; hay que revisarlas cuando se publiquen los artículos.
- Excepciones del comprobador (`revision/excepciones-comprobador.txt`): `h-wp` en ayahuasca e ibogaína, por dos PDF de ICEERS alojados en `wp-content`.

## Portada de Guías de terapia (26-11-2026)

- `docs/terapia/index.html` se rehízo a mano (diseño y texto) con la seña de la puerta Terapia: fondo claro, manchas e ilustración. No carga `terapia.js` ni ningún guion propio.
- Orden: portada con un dibujo (el camino entre colinas hacia el sol, con los tres tiempos: preparar, la sesión e integrar) y tres datos; aviso; tira «En esta página»; **las ocho guías** (una mancha y un emblema dibujado por medicina, lema y duración en palabras, sin cajas); **De un vistazo** (los arcos de «Cuánto dura la experiencia» y la tabla «Cómo se vive y cómo se acompaña», de la más breve a la más larga); **Lo que tienen en común** (`#en-comun`, al que enlaza el menú: tres tiempos, disposición y contexto, acompañar sin dirigir y «Lo que cuida un buen acompañamiento»); **De dónde vienen** (cuatro fotos en forma de piedra que llevan a la Enciclopedia y una línea del tiempo); mirada humanista y transpersonal; «Lo que han visto los estudios» (un párrafo, en pequeño); siete preguntas frecuentes; «Para seguir leyendo»; referencias y descargo.
- Estilos: `docs/terapia/terapia.css` (las piezas comunes `tg-…`, sin tocar) y `docs/terapia/portada.css` (solo lo de la portada, con prefijo `tgp-`). Al cambiar `portada.css`, sube su versión en el `<link>` de la página.
- Dibujos: SVG escritos a mano dentro de la página, con la paleta Tierra. Los ocho emblemas llevan `id="e-<slug>"` y la tabla los reutiliza con `<use>`; sirven tal cual para rehacer las siete guías. No hay moléculas ni fotos en las tarjetas (regla de Mannu del 25-11: no mezclar).
- Fotos: cuatro recortes en `docs/terapia/img/portada-*.webp` (hongos, peyote, liana de ayahuasca e iboga), de fotos con licencia de la Enciclopedia, con su fila en `CREDITOS.md`.
- Enfoque del texto (decisiones de Mannu del 25 y 26-11-2026): desde la experiencia y las raíces; la ciencia es una voz más, en pequeño, y el detalle está en Investigación terapéutica. Fuera lo que había de requisitos y de marco médico-legal: «Lo que da seguridad» (evaluación médica, profesionales, calidad farmacéutica), «Antes de dar el paso», las fases de investigación en tarjetas y tabla, la pregunta sobre España y «dónde se ofrece». La duración va en palabras, sin horas ni número de sesiones. Se mantiene, con calma, lo que protege: «Lo que cuida un buen acompañamiento» y la pregunta «¿Son para todo el mundo?».
- Datos estructurados: `CollectionPage` con la lista de las ocho guías, migas y `FAQPage` con las siete preguntas (el mismo texto que se ve).
- Las siete guías de `docs/terapia/<slug>/` siguen con la plantilla `art-*` y el enfoque anterior: están pendientes de pasar a este diseño.

## Terapia asistida con MDMA: diseño editorial (26-11-2026)

- `docs/terapia-asistida-mdma/index.html` está hecha a mano (diseño y texto). Todo el cuerpo va en un `<main class="tg">`.
- Orden: portada con una escena dibujada (la sala con una ventana al valle, el antifaz y la música, quien acompaña); franja de cuatro datos (qué es, para qué, cómo es, qué se siente); tira «Lo han contado»; barra de capítulos que acompaña al leer (en el móvil, un índice plegable) y cinco capítulos con portadilla:
  1. **Conocer**: qué es y para qué se busca.
  2. **Vivirlo**: cómo se vive, «Lo que suele quedar» y «Voces».
  3. **Con cuidado**: «Si te da miedo», el proceso (con «Lo que cuida una sesión») y el cuerpo y los cuidados.
  4. **Comprender**: la mirada humanista y transpersonal (con «Un atisbo de la cumbre»), de dónde viene, los libros y los estudios.
  5. **Seguir**: en los medios, primeros pasos, preguntas frecuentes, «Sigue por aquí» y referencias.
- Se lee en una columna centrada, sin índice lateral. Dos bandas a todo el ancho rompen el ritmo: «Voces» (oscura) y «Si te da miedo» (clara).
- Enfoque: que quien lea salga informado, con ganas y sin desconfianza, pero sin que la página venda nada. Cuenta los beneficios con la voz de quienes lo han vivido y responde a los miedos uno a uno, siempre con su contrapeso («Con los pies en el suelo», «No todas las historias son redondas», «Nadie promete curas ni presiona»). No hay llamadas a la acción: APDER no ofrece terapias ni sesiones, y lo dice arriba y en las preguntas.
- No es cientificista: el texto sale de la experiencia acumulada (terapeutas desde 1977, relatos, libros) y la ciencia es «una voz más», con un párrafo y una cifra. Para el detalle científico ya están la guía de MDMA e Investigación terapéutica. Tampoco habla de requisitos, países, costes, permisos ni del estado regulatorio.
- Reglas que respeta el texto: sin número de sesiones, horas ni dosis; sin legalidad; sin tono alarmista; y los registros separados (experiencia, interpretación humanista y transpersonal, investigación).
- «Voces»: cada tarjeta enlaza a la entrevista, el reportaje o el artículo donde esa persona lo cuenta. Las citas literales son breves (menos de quince palabras), una por fuente y con su atribución; las de otros idiomas son traducción de APDER y la página lo dice. Antes de añadir una voz hay que abrir la fuente y comprobar la cita.
- «Lo que suele quedar»: seis cambios que se repiten en los relatos y dos recuentos (29 de 29 en el primero que se publicó, de 1986, y 19 de 19 en un seguimiento a un año), con el párrafo de realismo debajo. Si se tocan las cifras, hay que volver a las referencias 2 y 3.
- Lo que se mantiene a propósito, en tono sereno y sin lista de requisitos: un párrafo sobre a quién y cuándo no le conviene y sobre la medicación («El cuerpo y los cuidados»). Los titulares de prensa son los de cada medio; alguno habla de aprobaciones en otros países.
- Estilos y guion propios, pensados para llevarlos después a las otras siete guías: `docs/terapia/guia.css` (todo bajo `.tg`, con prefijo `tg-`) y `docs/terapia/guia.js` (barra de lectura, capítulo en curso, aparición suave al llegar y vídeos que solo conectan con YouTube al pulsar). Esta página no usa las clases `art-*`; las otras siete guías sí, y no se han tocado. Si cambia cualquiera de los dos archivos, hay que subir el `?v=` con el que la página los pide.
- Ojo con las dos hojas de Terapia: `docs/terapia/terapia.css` es ahora solo de la portada de Guías de terapia (junto a `portada.css`) y no se ha tocado; `guia.css` es la de esta página. Comparten el prefijo `tg-` con definiciones distintas, así que no deben cargarse juntas en una misma página. `docs/terapia/terapia.js` ya no lo pide ninguna página (era el guion anterior de esta); se puede borrar en la próxima limpieza.
- Las ilustraciones (portada, portadillas y «Un atisbo de la cumbre») son SVG escritos dentro de la página, sin archivos aparte.
- Fotos: cinco recortes en `docs/terapia/img/` (peregrinación wixárika, kené shipibo, monguis, loto azul y río), sacados de las fotos con licencia de la Enciclopedia; cada uno con su fila en `CREDITOS.md`. Las portadas de los libros son las de la Biblioteca (`docs/biblioteca/portadas/`); los libros sin portada buena llevan una tapa dibujada con CSS.
- La cabecera y el pie siguen saliendo de `scripts/cabecera.py`. El índice del móvil lleva también la clase `s-toc-movil` para que `tierra.js` ponga el botón «Contenido».
- Los datos estructurados (artículo, migas y preguntas frecuentes) van en el `<head>`. Si cambian las preguntas frecuentes, hay que rehacer ese bloque para que digan lo mismo.
- La selección de medios, voces y vídeos se revisa con la página, cada tres meses: los enlaces externos caducan.

## Ayudas de lectura (tierra.js)

- `docs/tierra.js` (se carga en guías, medicinas, investigación, biblioteca y terapia asistida): cabecera fija que se encoge al bajar, botón «Contenido» en móvil y botón «Volver arriba».
- Las 19 guías siguen la misma plantilla (desde el 23/11/2026): En pocas palabras, Qué es, Cómo actúa, La experiencia, Dosis, Interacciones, Quién no debería, Cómo reducir riesgos, Si algo va mal, Investigación, Integración, Mitos, Historia, Preguntas frecuentes, Para leer más y Referencias. Todas se titulan «Guía completa». En 5-MeO-DMT, ibogaína, kratom y tabaco el apartado Dosis no da cifras a propósito; en el resto, las cifras de dosis no se han tocado y siguen pendientes de revisión experta.
- El esquema «Cuándo empieza y cuánto dura» (`.s-tiempos`) está en 9 guías, hecho a mano a partir de su tabla resumen: si cambian esos valores, hay que cambiar también el esquema.
