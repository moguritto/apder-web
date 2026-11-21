# Créditos de imágenes y recursos

Qué consta en este repositorio sobre el origen y la licencia de cada imagen de `docs/img/` y de los recursos propios de la web nueva. Donde no consta, pone **por confirmar**: no se ha inventado ninguna licencia. Cuando se confirme, hay que completar la tabla.

| Archivo | Qué es | Autoría / origen | Licencia | Estado |
|---|---|---|---|---|
| `docs/img/og-apder.png` | Imagen para compartir en redes (1200×630) | Propia: composición hecha para APDER con el logo `apder-icono.webp`, el texto «APDER» y el título de la web, con las letras DM Serif Display y Nunito Sans y la paleta Tierra | Propia de APDER (depende de la del logo) | Hecha en noviembre de 2026 |
| `docs/img/apder-icono.webp` | Logo de APDER (icono de seta y hojas), usado en la cabecera | Por confirmar (forma parte de la web original apder.org copiada el 26/10/2026) | Por confirmar | Por confirmar |
| `docs/img/apder-1-transparent.webp` | Logo de APDER con fondo transparente, usado en el pie | Por confirmar (web original apder.org) | Por confirmar | Por confirmar |
| `docs/img/favicon.png` | Icono de pestaña | Por confirmar | Por confirmar | Por confirmar |
| `docs/img/setas-amanita.png` | Ilustración de setas de APDER (portada de Sustancias) | Por confirmar | Por confirmar | Por confirmar |
| `docs/img/og/*.png` | Tarjetas para compartir de cada página (1200×630) | Propias: generadas para APDER con `scripts/tarjetas_og.py`, con las letras DM Serif Display y Nunito Sans, la paleta Tierra, los dibujos de moléculas y el logo | Propia de APDER (la parte del logo depende de la licencia del logo) | Hechas el 21/11/2026 |
| `docs/img/corazon.svg` | Dibujo de un corazón con un brote (guía para participantes) | Propio: dibujado para APDER | Propia de APDER | Hecho el 21/11/2026 |
| `docs/sustancias/moleculas/*.svg` | Dibujos de las 19 moléculas de las guías | Generados para APDER con RDKit (según `LEEME.md`) | Por confirmar | Por confirmar |
| `docs/fuentes/*.woff2` | Letras DM Serif Display y Nunito Sans (no son imágenes) | Paquetes npm @fontsource/dm-serif-display y @fontsource/nunito-sans 5.3.0, sin modificar | SIL Open Font License 1.1 (textos en `docs/fuentes/`) | Confirmado en `docs/fuentes/LEEME.txt` |

## Fuera de esta tabla

- Las imágenes de `docs/wp-content/uploads/` (páginas de WordPress todavía no rehechas) no se han revisado aquí. `AUDITORIA.md` (punto 1 de prioridad alta) señala unas 20 que proceden de medios u otras organizaciones y propone sustituirlas por fotos propias o con licencia libre. Cuando se rehagan esas páginas, cada imagen que se conserve debe añadirse a esta tabla con su origen y su licencia.
- Regla de `AUDITORIA.md` (punto 4): imágenes solo propias, con licencia libre (con fuente y licencia anotadas aquí) o generadas por APDER.
