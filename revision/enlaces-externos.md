# Revisión de enlaces externos (P2-9)

Fecha: 21-11-2026. Rama: `claude/enlaces-externos`. No se ha modificado ninguna página de `docs/`.

## Alcance y método

- Extracción con un script de Python (en `/tmp`, no incluido en el repositorio) de todos los `href="http(s)://…"` de `docs/**/*.html`, sin `apder.org`, y excluyendo `docs/wp-content`, `docs/wp-includes` y las páginas de WordPress (`terapia-asistida-mdma`, `divulgation`, `meditacion-corazon-2026`, `protocolo-meditacion-agosto-2024`). Se revisaron 39 archivos HTML.
- Además se buscaron URL escritas como texto (sin `href`) en las mismas páginas: solo aparece una (`sedeagpd.gob.es`, en la política de privacidad); se incluye.
- Comprobación con WebFetch (y WebSearch para confirmar la sede de la AEPD). El shell del sandbox no tiene red.
- Biblioteca: los 100 y pico libros no llevan enlace (son fichas de texto `<li class="b-libro">` con atributos `data-*`, sin `href` ni URL en el JavaScript). No hay, por tanto, enlaces de libros que comprobar ni muestra que tomar.
- Las guías de sustancias, Medicinas y el resto de páginas solo contienen enlaces externos del pie (redes y WhatsApp). Los únicos enlaces externos «de contenido» son los tres registros de ensayos clínicos de `investigacion-terapeutica` y la sede electrónica de la AEPD en la política de privacidad. Las fuentes científicas de las guías se citan como texto, sin enlace.

## Resumen con cifras

URL externas únicas: 9 (8 en `href` y 1 como texto).

| Categoría | Cifra | URL |
|---|---|---|
| ROTO | 0 | — |
| REDIRIGE | 1 | `sedeagpd.gob.es/sede-electronica-web/` |
| DUDOSO | 0 | — |
| BLOQUEADO (el bot no puede entrar; no cuenta como roto) | 4 | Instagram, Facebook, las dos formas de `wa.me` |
| OK | 4 | `reec.aemps.es`, `euclinicaltrials.eu`, `clinicaltrials.gov`, YouTube `@apderorg` |

Por zona: pie de todas las páginas (redes y WhatsApp): 5 URL; `investigacion-terapeutica`: 3 URL; política de privacidad: 1 URL. Portada: solo las del pie. Sustancias, Medicinas y Biblioteca: solo las del pie.

## Tabla (ordenada: ROTO, REDIRIGE, DUDOSO, BLOQUEADO, OK)

| URL | Páginas donde aparece | Estado | Detalle | Sustituto propuesto (fuente) |
|---|---|---|---|---|
| `https://sedeagpd.gob.es/sede-electronica-web/` (en texto, no es enlace) | `politica-de-privacidad/index.html` (línea 82) | REDIRIGE | El servidor responde 302 hacia `https://sedeaepd.gob.es/sede-electronica/home`. Esa dirección carga con el título «Sede Electrónica - Agencia Española de Protección de Datos». | `https://sedeaepd.gob.es/sede-electronica/home`. Fuente: la propia AEPD, en su ficha «¿Qué es la sede electrónica?» (https://www.aepd.es/preguntas-frecuentes/12-sede-electronica/FAQ-1201-que-es-la-sede-electronica), enlaza la sede en esa dirección. Se trata de la misma sede (el dominio es `sedeaepd`, con «e», no `sedeagpd`). |
| `https://www.instagram.com/apder` | 27 páginas (todas las de la lista de abajo, pie) | BLOQUEADO | WebFetch no puede entrar (robots.txt de Instagram). No se pudo comprobar que el perfil exista ni que sea de APDER. | Sin sustituto. Conviene que Mannu lo abra a mano. |
| `https://www.facebook.com/apder` | 27 páginas (pie) | BLOQUEADO | Igual que Instagram (robots.txt). No comprobado. | Sin sustituto. Conviene abrirlo a mano. |
| `https://wa.me/16693068938` | 27 páginas (pie y botón de la portada) | BLOQUEADO | WebFetch no puede salir de `wa.me`. No comprobado. | Sin sustituto necesario. |
| `https://wa.me/+16693068938` | 26 páginas (pie; todas salvo `index.html`) | BLOQUEADO | Igual. Observación: el mismo número aparece con dos formas distintas (con y sin «+») según la página. El formato que documenta WhatsApp para `wa.me` es sin «+», que además es el que usa la portada. | Opcional, por coherencia: `https://wa.me/16693068938` (la forma ya usada en la portada). |
| `https://reec.aemps.es/` | `investigacion-terapeutica/index.html` | OK | La raíz devolvió una página con el título «Insert title here» (plantilla de la aplicación), pero la ruta `https://reec.aemps.es/reec/estudio/buscar` responde con el título «.:: REEC ::. Registro Español de Estudios Clínicos». Es el REEC de la AEMPS, lo citado. | — |
| `https://euclinicaltrials.eu/` | `investigacion-terapeutica/index.html` | OK | Título «Clinical Trials in the European Union - EMA»; sitio mantenido por la EMA y apoyado en CTIS. Coincide con lo citado. | — |
| `https://clinicaltrials.gov/` | `investigacion-terapeutica/index.html` | OK | Título «ClinicalTrials.gov». Es el registro de EE. UU. citado. | — |
| `https://www.youtube.com/@apderorg` | 27 páginas (pie) | OK | El canal existe (nombre «APDER», identificador `@apderorg`). El contenido recuperado no incluía descripción ni vídeos, así que no se pudo confirmar el tema del canal. | — |

Páginas con las URL del pie (27): `404.html`, `aviso-legal`, `biblioteca`, `index.html`, `investigacion-terapeutica`, `medicinas`, `politica-de-privacidad`, `sustancias/index.html` y las 19 guías de `sustancias/` (2c-b, 4-aco-dmt, 5-meo-dmt, amanita-muscaria, ayahuasca, cacao, cannabis, datura, dmt, ibogaina, kanna, ketamina, kratom, lsd, mdma, mescalina, psilocibina, salvia-divinorum, tabaco). Todas llevan Instagram, Facebook, YouTube y `wa.me/16693068938`; todas salvo `index.html` llevan además `wa.me/+16693068938`.

## No comprobado

- Instagram, Facebook y las dos URL de `wa.me`: la herramienta no puede entrar (robots.txt / bloqueo del dominio). No se afirma que funcionen ni que estén rotos.
- Que el canal de YouTube trate de la temática de APDER: solo se confirmó que existe.
- No se han comprobado los enlaces a `apder.org` (fuera del alcance) ni los de las páginas de WordPress excluidas.

## Cambios propuestos (listos para aplicar)

1. `politica-de-privacidad/index.html` (línea 82, texto): `https://sedeagpd.gob.es/sede-electronica-web/` → `https://sedeaepd.gob.es/sede-electronica/home`
2. Opcional, por coherencia, en las 26 páginas del pie que lo usan (todas las del listado salvo `index.html`): `https://wa.me/+16693068938` → `https://wa.me/16693068938`

No se propone ningún otro cambio.
