// APDER · Formaciones: genera los dos archivos fijos del globo.
//   docs/formaciones/mundo.json  → países del mundo (Natural Earth 1:50 m, simplificado), con el código de país de dos letras
//   docs/formaciones/geo.min.js  → la parte de d3-geo y topojson-client que usa formaciones.js
// Solo hace falta volver a lanzarlo si se quiere más o menos detalle en el mapa.
// Uso (en una carpeta de trabajo, fuera de docs/):
//   npm install d3-geo topojson-client topojson-simplify world-atlas i18n-iso-countries esbuild
//   node mapa.mjs RUTA/docs/formaciones
import fs from "node:fs";
import path from "node:path";
import {createRequire} from "node:module";
import {presimplify, simplify, quantile, filter, filterAttachedWeight, sphericalTriangleArea, sphericalRingArea} from "topojson-simplify";
import {mergeArcs, meshArcs, quantize} from "topojson-client";
import * as esbuild from "esbuild";

const require = createRequire(import.meta.url);
const iso = require("i18n-iso-countries");
const salida = process.argv[2] || ".";
const DETALLE = Number(process.argv[3] || 0.12);   // parte de los puntos que se conserva (0 a 1)
const ISLOTE = Number(process.argv[4] || 8);        // un islote suelto se quita si mide menos que ISLOTE veces el umbral

// ---- mundo.json ----
let topo = JSON.parse(fs.readFileSync(require.resolve("world-atlas/countries-50m.json"), "utf8"));
topo = presimplify(topo, sphericalTriangleArea);
const umbral = quantile(topo, DETALLE);            // los pesos van de mayor a menor: se queda la parte DETALLE
// más detalle donde el globo se acerca (Europa y Norteamérica) y menos en los polos, que casi no se ven
for (const arco of topo.arcs) for (const p of arco) {
  const [lon, lat] = p;
  if (lat > 66 || lat < -56) p[2] *= 0.2;
  else if (lon > -12 && lon < 42 && lat > 34 && lat < 62) p[2] *= 7;
  else if (lon > -130 && lon < -64 && lat > 14 && lat < 52) p[2] *= 3;
}
topo = filter(topo, filterAttachedWeight(topo, umbral * ISLOTE, sphericalRingArea));   // fuera los islotes sueltos
topo = simplify(topo, umbral);
const paises = topo.objects.countries.geometries.filter(g => g.arcs && g.arcs.length);
for (const g of paises) {
  const a2 = g.id ? iso.numericToAlpha2(String(g.id).padStart(3, "0")) : null;
  g.id = a2 || "";
  delete g.properties;
}
// quita polígonos que se han quedado sin superficie tras simplificar
topo.objects = {
  paises: {type: "GeometryCollection", geometries: paises},
  tierra: mergeArcs(topo, paises),
  fronteras: meshArcs(topo, {type: "GeometryCollection", geometries: paises}, (a, b) => a !== b),
};
delete topo.bbox;
// descarta los arcos que ya no se usan y redondea
const usados = new Set();
const anota = a => Array.isArray(a) ? a.forEach(anota) : usados.add(a < 0 ? ~a : a);
for (const o of Object.values(topo.objects)) (o.geometries || [o]).forEach(g => anota(g.arcs));
const mapa = new Map(); const arcos = [];
[...usados].sort((a, b) => a - b).forEach(i => { mapa.set(i, arcos.length); arcos.push(topo.arcs[i]); });
const cambia = a => Array.isArray(a) ? a.map(cambia) : (a < 0 ? ~mapa.get(~a) : mapa.get(a));
for (const o of Object.values(topo.objects)) (o.geometries || [o]).forEach(g => { g.arcs = cambia(g.arcs); });
topo.arcs = arcos;
topo = quantize(topo, 2e4);
fs.writeFileSync(path.join(salida, "mundo.json"), JSON.stringify(topo));
const puntos = topo.arcs.reduce((n, a) => n + a.length, 0);
console.log("mundo.json:", fs.statSync(path.join(salida, "mundo.json")).size, "bytes ·", paises.length, "países ·", puntos, "puntos ·",
  paises.filter(g => !g.id).length, "sin código");

// ---- geo.min.js ----
const entrada = path.join(process.cwd(), "_geo_entrada.mjs");
fs.writeFileSync(entrada, `export {geoOrthographic, geoPath, geoGraticule, geoInterpolate, geoDistance} from "d3-geo";
export {feature} from "topojson-client";\n`);
await esbuild.build({
  entryPoints: [entrada], bundle: true, minify: true, format: "iife", globalName: "apderGeo", target: "es2017",
  outfile: path.join(salida, "geo.min.js"),
  banner: {js: "/* APDER · globo de Formaciones. Incluye partes de d3-geo, d3-array e internmap (ISC, © 2010-2024 Mike Bostock) y de topojson-client (ISC, © 2012-2019 Michael Bostock). https://d3js.org · Se genera con scripts/formaciones/mapa.mjs */"},
});
fs.unlinkSync(entrada);
console.log("geo.min.js:", fs.statSync(path.join(salida, "geo.min.js")).size, "bytes");
