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

## Sustancias (nuevo)

- `docs/sustancias/index.html`: página general de sustancias psicodélicas (tarjetas, comparativa, riesgos, preguntas).
- `docs/sustancias/<sustancia>/index.html`: 19 guías (psilocibina, LSD, MDMA, ketamina, ayahuasca, DMT, 5-MeO-DMT, mescalina, ibogaína, 2C-B, 4-AcO-DMT, Amanita muscaria, Salvia divinorum, cannabis, kanna, kratom, datura, cacao, tabaco).
- Megamenú «Sustancias»: en las páginas de sustancias va dentro de la cabecera; en el resto de páginas se añade al menú y usa `docs/sustancias/mega-wp.css`.
- `docs/sustancias/sustancias.css`: estilos solo de estas páginas (títulos Libre Caslon, texto Inter, acento rojo, índice lateral).
- `docs/sustancias/moleculas/`: dibujos de las moléculas (SVG propios, hechos con RDKit).
- Textos propios en español, escritos para APDER. Para añadir otra sustancia, copia una carpeta de guía, cambia los textos y enlázala desde la cuadrícula de `docs/sustancias/index.html` y desde el megamenú.

## Otras secciones

- `docs/investigacion-terapeutica/`: orientación sobre la investigación por problema de salud y cómo participar en ensayos.
- `docs/medicinas/`: artículo con las medicinas psicodélicas y enteógenas por categorías.
- `docs/biblioteca/`: 425 libros con buscador y filtros (categoría, idioma y sustancia).
- `AUDITORIA.md`: fallos encontrados, propuestas y cómo evitar problemas de derechos de autor.
