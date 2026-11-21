# Comprobador de la web (scripts/comprobar_web.py)
Guion de Python 3 sin dependencias que revisa `docs/` antes de publicar.

## Cómo se lanza
- `python3 scripts/comprobar_web.py` (revisa `../docs` respecto al guion); otra carpeta: `... RUTA/docs`; `--json` para máquina.
- Sale con 0 sin errores y con 1 si hay errores. Los avisos no fallan.
- En GitHub corre en cada pull request hacia main (`.github/workflows/comprobar.yml`).

## Qué revisa (un bloque de salida por regla)
a-enlaces: enlaces/recursos internos rotos (incluye los absolutos a apder.org). b-h1: un solo `<h1>`.
c-descripcion: meta description de 120 a 160 caracteres. d-idioma: `<html lang="es">` y og:locale `es_ES`.
e-alt: `<img>` sin alt (error) o con alt vacío (aviso). f-peso: páginas de más de 60 KB (aviso) y peso total.
g-terceros: css/js/img/fuentes/iframe de otros dominios (los `<a>` externos no cuentan).
h-wp: referencias a wp-content/wp-includes. i-ingles: inglés en el `<footer>`.
j-noindex-sitemap: páginas noindex o inexistentes en sitemap.xml. j-almohadilla: `<a href="#">`.
`docs/wp-content` y `docs/wp-includes` no se analizan como páginas (sí pesan). Las redirecciones (meta refresh)
quedan fuera de b y c; las páginas noindex, de c y de og:locale.

## Cómo leer la salida
Cada `== regla` dice «OK» o cuántos errores/avisos tiene; debajo, `ERROR`/`AVISO` con `docs/ruta:línea — qué pasa`.
Al final, el resumen y el `Resultado`. Errores heredados iniciales: `revision/linea-base-comprobador.txt`.

## Excepciones
`revision/excepciones-comprobador.txt` (opcional): una línea `regla|ruta` (`a` o `a-enlaces`, `*`, comodines en
la ruta). Descuenta errores conocidos; cada bloque se justifica con un comentario `#`. Una excepción sin uso da aviso.
