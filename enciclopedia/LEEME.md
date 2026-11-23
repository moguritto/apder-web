# Enciclopedia de medicinas · cómo se hace una ficha

Una ficha = un archivo `fichas/<slug>.json` + sus fotos en `docs/enciclopedia/img/`. El HTML lo escribe `generar.py`; nunca a mano.

```
python3 enciclopedia/generar.py        # regenera docs/enciclopedia/
python3 scripts/construir_indice.py    # buscador
python3 scripts/comprobar_web.py       # no debe dar errores nuevos (línea base: 292)
```

## El molde (copiar `fichas/ayahuasca.json` y cambiar los valores; mismas claves, mismo orden)

| Clave | Qué lleva | Límite |
|---|---|---|
| `slug`, `tipo`, `tipo_txt` | tipo: planta, hongo, cactus, animal, preparado o molecula | — |
| `migas` | Tipo · familia · territorio | 1 línea |
| `nombre`, `cientifico`, `autoridad` | Nombre común en castellano; nombre aceptado (Kew o Index Fungorum) | — |
| `descripcion` | Para buscadores | 120–160 caracteres |
| `entrada` | Dos frases que abren la ficha | ≤ 45 palabras |
| `otros` | Otros nombres, separados por « · » | ≤ 8 |
| `portada` | Foto horizontal: `img`, `alt`, `pie`, `cred` | ≥ 1800 px |
| `vistazo` | 6 datos fijos: que, territorio, parte, activos, tiempo, pueblos | ≤ 12 palabras cada uno |
| `guia` | Guía de APDER de la misma medicina, si existe | — |
| `planta` | La planta o el hongo: 2–3 párrafos, 4 `rasgos`, una `lamina` antigua o una `foto`; en hongos, `aviso` de que no es una clave de identificación | ≤ 60 palabras por párrafo |
| `tradicion` | Memoria y tradición: 2–3 párrafos, `cronologia` (4–7 hitos), `nombres` (4–8, con su lengua o pueblo) | — |
| `territorio` | 1–2 párrafos, `mapa`, `uicn` (solo con estado y fuente comprobados; si no, `null`), `ayuda` (3–4 puntos) | — |
| `quimica` | 1–2 párrafos y 1–3 `moleculas` (dibujo de `docs/sustancias/moleculas/` si existe) | — |
| `experiencia` | 2 párrafos y `tiempo` (los mismos valores que la guía de APDER) | — |
| `investigacion` | `nivel` 1–5 (tradición · laboratorio · estudios en personas · ensayos clínicos · medicamento aprobado), 1–2 párrafos y `alcance` | — |
| `cuidado` | 4 `tarjetas`; `parecidos` cuando haya confusiones peligrosas | ≤ 30 palabras por tarjeta |
| `galeria` | 4 fotos (`cls`: g7 + g5 por fila) | — |
| `libros` | 3 libros que estén en `docs/biblioteca/` | — |
| `parientes` | 4 medicinas emparentadas: tipo, nombre, científico, frase, enlace o `null` | — |
| `fuentes` | 5–10 referencias; cada `[n]` del texto apunta a una | — |
| `revisado`, `anterior`, `siguiente` | Fecha y fichas vecinas en orden alfabético | — |

Marcas en los textos: `[3]` cita la fuente 3; `<em>…</em>` es cursiva. Títulos de apartado narrativos («Una soga que trepa hasta el dosel»), no genéricos.

## Reglas

1. Castellano de España, frases cortas, 600–900 palabras por ficha. Texto propio: los libros dan datos, nunca frases.
2. Cada dato sensible (efectos, riesgos, resultados, conservación, fechas) lleva fuente. Sin fuente, no se escribe.
3. Nada de legalidad. Nada alarmista ni cifras de muertes. Sin cifras de dosis. En hongos, sin claves para identificar.
4. No dar a entender que APDER ofrece sesiones. Sin nombres de personas de APDER. Sin YouTube, Instagram ni Facebook.
5. Coherencia con la guía de APDER de la misma medicina: mismos tiempos y mismos riesgos.
6. Pueblos y lenguas, con el nombre que se dan a sí mismos; una historia situada vale más que una generalidad.
7. Fotos solo de Wikimedia Commons con licencia CC0, dominio público, CC BY o CC BY-SA (nunca NC ni ND). Sin personas reconocibles. Portada a 1800 px, resto a 1400 px, JPEG de menos de 300 KB. Cada foto, con autor y licencia en la ficha y una fila en `CREDITOS.md`.
8. Fuentes de partida: Rätsch, *The Encyclopedia of Psychoactive Plants*; Schultes y Hofmann, *Plantas de los dioses*; Ott, *Pharmacotheon*; la guía de APDER; Kew (Plants of the World Online) o Index Fungorum; Lista Roja de la UICN; PubMed.

## Orden de trabajo

1. Pasar al molde las dos fichas de la primera maqueta: peyote y hierba de la pastora.
2. Las medicinas que ya tienen guía en `docs/sustancias/`.
3. El resto de `lista.json`, por orden alfabético. Las moléculas, al final.

Al añadir una ficha: poner su `slug` en `lista.json` (en `az` y, si tiene tarjeta, en `tarjetas`), actualizar `anterior` y `siguiente` de las vecinas, añadir su dirección a `docs/sitemap.xml` y regenerar.
