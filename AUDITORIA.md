# Auditoría de apder.org (noviembre de 2026)

Este archivo no se publica en la web (está fuera de `docs/`).

## 1. Corregido en esta revisión

| Problema | Qué se ha hecho |
|---|---|
| El menú cambiaba según la página (inglés en unas, español en otras, distinto orden) | Menú único en las 28 páginas: El proyecto (+ Divulgación, Educación, Investigación) · Sustancias (megamenú) · Investigación terapéutica · Biblioteca |
| El menú de WordPress se partía en dos líneas | Ajuste de espacios para que quepa en una línea |
| Páginas legales y 404 marcadas como inglés (`lang="en"`) | Cambiadas a español |
| Guías sin vista previa para redes sociales | Añadidas etiquetas Open Graph y descripción |
| Pie con «© 2024» | Actualizado a 2026 |
| No había sección de investigación terapéutica ni biblioteca | Nuevas páginas `/investigacion-terapeutica/`, `/biblioteca/` y `/medicinas/` |

## 2. Fallos pendientes (por prioridad)

### Alta
1. **Imágenes de terceros (riesgo de derechos de autor).** En `docs/wp-content/uploads/` hay unas 20 imágenes que proceden de medios o de otras organizaciones, por ejemplo:
   - `f.elconfidencial.com_original_…jpg` (El Confidencial)
   - `nyt-md.jpg` (New York Times)
   - `121130042953-02-mdma-pstd-1130.jpg` (CNN)
   - `feed_mit_image_SO21_TR_mdma-1.jpg` (MIT Technology Review)
   - `ketamine-el-mundo.jpg` (El Mundo)
   - `La-revista-Science-…webp`
   - `MAPS_MDMA_therapy.jpg`, `MAPS-2019-08-21-Leiden-…webp`, `maps-2018-01-boulder-…jpeg` (MAPS)
   - `41jvUsmbcjL._SX331_…jpg` (portada de libro descargada de Amazon)

   La mayoría se usan en las páginas de terapia con MDMA y de divulgación. **Propuesta:** sustituirlas por fotos propias o con licencia libre (Pexels, Unsplash, Wikimedia Commons con atribución), o mostrar los artículos como enlaces de texto sin imagen.
2. **Imagen de fondo de la portada.** Parece una obra de arte visionario de un artista conocido. Si no tenéis permiso del autor, conviene cambiarla.
3. **Textos mezclados en inglés y español.** La portada, Divulgación, Terapia con MDMA y las páginas de meditación tienen títulos, botones y pie en inglés («Take an action», «Join the community», «We are a non-profit…»), y están marcadas como `en-US`. **Propuesta:** traducirlas todas al español (y, si se quiere, hacer después una versión en inglés en `/en/`).

### Media
4. **SEO de las páginas de WordPress:** sin descripción para buscadores. La portada y Divulgación no tienen título principal (`h1`) y otras páginas tienen varios.
5. **Peso.** Las páginas de WordPress pesan entre 165 y 270 KB solo de HTML, más los scripts de Elementor. Las imágenes ocupan unos 10 MB y la mayor (`pexels-emre-can-acer-2079451.jpg`) ocupa 530 KB. **Propuesta:** convertir a WebP y reducir tamaños.
6. **Privacidad:** las letras se cargan desde los servidores de Google (Google Fonts). En la UE hay sentencias que lo consideran un envío de datos personales sin consentimiento. **Propuesta:** alojar las letras en la propia web.
7. **El pie dice «Recibe novedades sobre noticias y eventos», pero no hay formulario.** Añadir un formulario o quitar la frase.
8. **El aviso legal muestra el DNI completo de una persona física.** La LSSI exige identificar al titular, pero si existe la asociación con su propio CIF, es mejor que la titular sea la asociación.

### Baja
9. En el móvil, en las páginas de WordPress, «Sustancias» es un enlace simple (sin la lista completa del megamenú). Las demás páginas sí muestran la lista.
10. Muchas imágenes tienen texto alternativo vacío. Conviene describir las que aportan información.
11. Quedan direcciones antiguas que solo redirigen (`/mdma/`, `/home2/`…). Están bien, pero no hay que enlazarlas.

## 3. Cómo mejorar los textos

1. **Firma y revisión.** Cada guía debería indicar quién la escribe y quién la revisa (médico, psiquiatra o psicólogo), con fecha. Da confianza al lector y a los buscadores.
2. **Fuentes primarias.** Basarse en estudios publicados (PubMed, revistas científicas), documentos oficiales (AEMPS, BOE, EMA, FDA) y libros de referencia, no en otras webs divulgativas.
3. **Contexto español.** Añadir más información útil en España: legislación concreta, servicios de análisis (Energy Control), investigación española (Hospital de Sant Pau, IMIM, ICEERS) y ensayos abiertos.
4. **Lenguaje claro.** Frases cortas, una idea por párrafo y un glosario común para todas las páginas (por ejemplo, decidir si se dice «sustancia», «medicina» o «psicodélico» y usarlo siempre igual).
5. **Revisión periódica.** Repasar cada guía cada seis meses: la legislación y la investigación cambian rápido.
6. **Elementos propios.** Infografías, esquemas y fotos hechos por APDER, casos o testimonios con consentimiento, vídeos del canal de YouTube de APDER.
7. **Revisión experta de dosis y legalidad** antes de difundir mucho las guías.

## 4. Cómo evitar problemas de derechos de autor

1. **No copiar ni traducir textos de otras webs**, aunque se cambien palabras. Se puede leer para informarse, pero el texto final debe escribirse desde cero, a partir de las fuentes originales.
2. **La estructura y el diseño sí se pueden parecer** (orden de secciones, índice lateral, tipografía, colores). Lo que no se puede usar es el logo, las imágenes, los textos ni el código de otra web.
3. **Citas breves y con autor**, solo cuando aporten algo y entre comillas.
4. **Imágenes:** solo propias, con licencia libre (guardar en un archivo `CREDITOS.md` la fuente y la licencia de cada una) o generadas por APDER, como los dibujos de moléculas. Nada de fotos de periódicos, de agencias ni portadas descargadas de tiendas.
5. **Portadas de libros:** mejor no mostrarlas. Basta con título, autor y un enlace a la editorial.
6. **Vídeos:** insertar desde YouTube o Vimeo (el reproductor oficial), no descargarlos y volver a subirlos.
7. **Comprobación antes de publicar:** buscar en Google entre comillas dos o tres frases del texto para asegurarse de que no coinciden con otra web.
8. **Registro de fuentes:** guardar en cada artículo la lista de referencias usadas (ya se hace en las guías).
