/* Buscador de APDER: sin servicios externos. Lee indice.json (lo genera scripts/construir_indice.py). */
(function () {
  'use strict';
  var campo = document.getElementById('bq-q');
  var form = campo && campo.form;
  var recuento = document.getElementById('bq-n');
  var salida = document.getElementById('bq-res');
  if (!campo || !salida) return;

  var datos = null;
  var cargando = false;
  var temporizador = null;
  var PAGINA_LIBROS = 20;
  var MIN = 2;

  /* minúsculas y sin acentos (NFD) */
  function norm(t) {
    return t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  /* texto normalizado + correspondencia de cada carácter normalizado con su posición original */
  function mapa(t) {
    var s = '', m = [];
    for (var i = 0; i < t.length; i++) {
      var c = norm(t.charAt(i));
      for (var j = 0; j < c.length; j++) { s += c.charAt(j); m.push(i); }
    }
    return { s: s, m: m };
  }
  function terminos(v) {
    return norm(v.trim()).split(/\s+/).filter(function (x) { return x; });
  }

  /* ---- índice ---- */
  function preparar(d) {
    d.paginas.forEach(function (p) {
      p._t = norm(p.titulo);
      p._d = norm(p.descripcion);
      p._r = norm(p.resumen);
      p._h = p.encabezados.map(function (e) { return norm(e.t); });
      p._todo = p._t + ' ' + p._d + ' ' + p._r + ' ' + p._h.join(' ');
    });
    d.libros.forEach(function (l) {
      l._t = norm(l.titulo);
      l._a = norm(l.autor);
      l._s = norm(l.sustancia.join(' '));
      l._c = norm(l.categoria + ' ' + l.idioma);
      l._d = norm(l.descripcion);
      l._todo = l._t + ' ' + l._a + ' ' + l._s + ' ' + l._c + ' ' + l._d;
    });
    return d;
  }
  function cuenta(texto, t) {
    var n = 0, i = texto.indexOf(t);
    while (i > -1 && n < 5) { n++; i = texto.indexOf(t, i + t.length); }
    return n;
  }
  function puntuaPagina(p, ts) {
    var pt = 0;
    for (var k = 0; k < ts.length; k++) {
      var t = ts[k];
      if (p._t === t) pt += 30;
      pt += cuenta(p._t, t) * 10;
      for (var j = 0; j < p._h.length; j++) if (p._h[j].indexOf(t) > -1) { pt += 4; }
      pt += cuenta(p._d, t) * 3 + cuenta(p._r, t);
    }
    return pt;
  }
  function puntuaLibro(l, ts) {
    var pt = 0;
    for (var k = 0; k < ts.length; k++) {
      var t = ts[k];
      pt += cuenta(l._t, t) * 10 + cuenta(l._a, t) * 8 + cuenta(l._s, t) * 6 + cuenta(l._c, t) * 2 + cuenta(l._d, t) * 3;
    }
    return pt;
  }
  function todos(texto, ts) {
    for (var i = 0; i < ts.length; i++) if (texto.indexOf(ts[i]) < 0) return false;
    return true;
  }

  /* ---- resaltado ---- */
  function rangos(texto, ts) {
    var mp = mapa(texto), r = [];
    ts.forEach(function (t) {
      var i = mp.s.indexOf(t);
      while (i > -1) {
        r.push([mp.m[i], mp.m[i + t.length - 1] + 1]);
        i = mp.s.indexOf(t, i + t.length);
      }
    });
    r.sort(function (a, b) { return a[0] - b[0]; });
    var f = [];
    r.forEach(function (x) {
      var u = f[f.length - 1];
      if (u && x[0] <= u[1]) { if (x[1] > u[1]) u[1] = x[1]; } else f.push([x[0], x[1]]);
    });
    return f;
  }
  /* añade a `el` el texto con las coincidencias en <mark> */
  function marca(el, texto, ts) {
    var pos = 0;
    rangos(texto, ts).forEach(function (r) {
      if (r[0] > pos) el.appendChild(document.createTextNode(texto.slice(pos, r[0])));
      var m = document.createElement('mark');
      m.textContent = texto.slice(r[0], r[1]);
      el.appendChild(m);
      pos = r[1];
    });
    if (pos < texto.length) el.appendChild(document.createTextNode(texto.slice(pos)));
    return el;
  }
  /* fragmento de `texto` alrededor de la primera coincidencia */
  function fragmento(texto, ts, largo) {
    if (texto.length <= largo) return texto;
    var r = rangos(texto, ts);
    var ini = r.length ? Math.max(0, r[0][0] - Math.floor(largo / 3)) : 0;
    if (ini > 0) { var e = texto.indexOf(' ', ini); if (e > -1 && e < r[0][0]) ini = e + 1; }
    var fin = Math.min(texto.length, ini + largo);
    if (fin < texto.length) { var b = texto.lastIndexOf(' ', fin); if (b > ini + largo / 2) fin = b; }
    return (ini > 0 ? '… ' : '') + texto.slice(ini, fin).trim() + (fin < texto.length ? ' …' : '');
  }

  /* ---- DOM ---- */
  function el(tag, clase, texto) {
    var e = document.createElement(tag);
    if (clase) e.className = clase;
    if (texto) e.textContent = texto;
    return e;
  }
  function enlace(href, texto, ts) {
    var a = document.createElement('a');
    a.href = href;
    marca(a, texto, ts);
    return a;
  }
  var ETIQUETA = { 'Sustancias': 'Sustancias', 'Medicinas': 'Medicinas', 'Investigación': 'Investigación', 'Terapia': 'Terapia', 'Biblioteca': 'Biblioteca', 'Inicio': 'Inicio', 'Información legal': 'Información legal' };

  function itemPagina(p, ts) {
    var url = '../' + p.url;
    var li = el('li', 'bq-item');
    var h = el('h3');
    h.appendChild(enlace(url, p.titulo, ts));
    li.appendChild(h);
    li.appendChild(el('p', 'bq-etiqueta', ETIQUETA[p.seccion] || p.seccion));
    var base = p.descripcion || p.resumen;
    var fuente = base;
    if (!rangos(base, ts).length && rangos(p.resumen, ts).length) fuente = p.resumen;
    var d = el('p', 'bq-desc');
    marca(d, fragmento(fuente, ts, 220), ts);
    li.appendChild(d);
    var aps = [];
    for (var i = 0; i < p.encabezados.length && aps.length < 4; i++) {
      var hit = false;
      for (var k = 0; k < ts.length; k++) if (p._h[i].indexOf(ts[k]) > -1) hit = true;
      if (hit && p._h[i] !== p._t) aps.push(p.encabezados[i]);
    }
    if (aps.length) {
      var ap = el('p', 'bq-aps');
      ap.appendChild(document.createTextNode('En esta página: '));
      aps.forEach(function (e, i) {
        if (i) ap.appendChild(document.createTextNode(' · '));
        ap.appendChild(enlace(url + (e.id ? '#' + e.id : ''), e.t, ts));
      });
      li.appendChild(ap);
    }
    return li;
  }
  function itemLibro(l, ts) {
    var li = el('li', 'bq-item');
    var h = el('h3');
    h.appendChild(enlace('../' + l.url, l.titulo, ts));
    li.appendChild(h);
    var m = el('p', 'bq-meta');
    marca(m, [l.autor, l.anio, l.idioma].filter(function (x) { return x; }).join(' · '), ts);
    li.appendChild(m);
    var c = el('p', 'bq-meta');
    marca(c, l.categoria + (l.sustancia.length ? ' · ' + l.sustancia.join(', ') : ''), ts);
    li.appendChild(c);
    if (l.descripcion) li.appendChild(marca(el('p', 'bq-desc'), l.descripcion, ts));
    return li;
  }
  function grupo(id, titulo, n) {
    var s = el('section', 'bq-grupo');
    s.setAttribute('aria-labelledby', id);
    var h = el('h2', '', titulo);
    h.id = id;
    h.appendChild(el('small', '', '(' + n + ')'));
    s.appendChild(h);
    var ol = el('ol', 'bq-lista');
    s.appendChild(ol);
    s._lista = ol;
    return s;
  }

  function pinta(valor) {
    var ts = terminos(valor);
    salida.textContent = '';
    if (!ts.length) { recuento.textContent = ''; return; }
    if (norm(valor.trim()).length < MIN) {
      recuento.textContent = 'Escribe al menos dos letras para buscar.';
      return;
    }
    var pags = datos.paginas.filter(function (p) { return todos(p._todo, ts); });
    pags.forEach(function (p) { p._pt = puntuaPagina(p, ts); });
    pags.sort(function (a, b) { return b._pt - a._pt; });
    var libs = datos.libros.filter(function (l) { return todos(l._todo, ts); });
    libs.forEach(function (l) { l._pt = puntuaLibro(l, ts); });
    libs.sort(function (a, b) { return b._pt - a._pt; });

    var guias = pags.filter(function (p) { return p.seccion === 'Sustancias'; });
    var medinv = pags.filter(function (p) { return p.seccion === 'Medicinas' || p.seccion === 'Investigación' || p.seccion === 'Terapia'; });
    var otras = pags.filter(function (p) { return guias.indexOf(p) < 0 && medinv.indexOf(p) < 0; });
    var total = pags.length + libs.length;
    var txt = valor.trim();

    if (!total) {
      recuento.textContent = 'Sin resultados para «' + txt + '».';
      var v = el('div', 'bq-vacio');
      v.appendChild(el('p', '', 'No hemos encontrado nada para «' + txt + '». Prueba con otra palabra, con menos palabras o revisa la ortografía.'));
      var p2 = el('p');
      p2.appendChild(document.createTextNode('También puedes explorar las '));
      [['../sustancias/', 'guías de sustancias'], ['../medicinas/', 'medicinas'], ['../investigacion-terapeutica/', 'investigación'], ['../biblioteca/', 'biblioteca']].forEach(function (x, i, a) {
        var l = document.createElement('a');
        l.href = x[0]; l.textContent = x[1];
        p2.appendChild(l);
        p2.appendChild(document.createTextNode(i < a.length - 2 ? ', ' : i === a.length - 2 ? ' o la ' : '.'));
      });
      v.appendChild(p2);
      salida.appendChild(v);
      return;
    }
    var partes = [];
    if (guias.length) partes.push(guias.length + (guias.length === 1 ? ' guía' : ' guías'));
    if (medinv.length) partes.push(medinv.length + ' de medicinas e investigación');
    if (libs.length) partes.push(libs.length + (libs.length === 1 ? ' libro' : ' libros'));
    if (otras.length) partes.push(otras.length + (otras.length === 1 ? ' página más' : ' páginas más'));
    recuento.textContent = total + (total === 1 ? ' resultado' : ' resultados') + ' para «' + txt + '»: ' + partes.join(', ') + '.';

    function simple(id, titulo, lista) {
      if (!lista.length) return;
      var g = grupo(id, titulo, lista.length);
      lista.forEach(function (p) { g._lista.appendChild(itemPagina(p, ts)); });
      salida.appendChild(g);
    }
    simple('bq-g-guias', 'Guías', guias);
    simple('bq-g-medinv', 'Medicinas e Investigación', medinv);
    if (libs.length) {
      var g = grupo('bq-g-libros', 'Libros', libs.length);
      var mostrados = 0;
      var boton = el('button', 'btn c');
      boton.type = 'button';
      var envoltura = el('p', 'bq-mas');
      envoltura.appendChild(boton);
      function mas() {
        var hasta = Math.min(libs.length, mostrados + PAGINA_LIBROS);
        var primero = null;
        for (; mostrados < hasta; mostrados++) {
          var it = itemLibro(libs[mostrados], ts);
          if (!primero) primero = it;
          g._lista.appendChild(it);
        }
        var resto = libs.length - mostrados;
        envoltura.hidden = !resto;
        boton.textContent = 'Mostrar más libros (' + resto + ' más)';
        return primero;
      }
      mas();
      boton.addEventListener('click', function () {
        var ya = mostrados;
        mas();
        var it = g._lista.children[ya];
        var a = it && it.querySelector('a');
        if (a) a.focus();
      });
      g.appendChild(envoltura);
      salida.appendChild(g);
    }
    simple('bq-g-otras', 'Otras páginas', otras);
  }

  /* ---- arranque ---- */
  function lanza() {
    clearTimeout(temporizador);
    var v = campo.value;
    if (history.replaceState) {
      var u = location.pathname + (v.trim() ? '?q=' + encodeURIComponent(v.trim()) : '');
      history.replaceState(null, '', u);
    }
    if (datos) { pinta(v); return; }
    if (cargando) return;
    cargando = true;
    recuento.textContent = 'Cargando el índice de búsqueda…';
    fetch('indice.json').then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    }).then(function (d) {
      datos = preparar(d);
      cargando = false;
      pinta(campo.value);
    }).catch(function () {
      cargando = false;
      recuento.textContent = 'No se ha podido cargar el índice de búsqueda. Recarga la página o prueba más tarde.';
    });
  }

  campo.addEventListener('input', function () {
    clearTimeout(temporizador);
    temporizador = setTimeout(lanza, 250);
  });
  campo.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && campo.value) { campo.value = ''; lanza(); }
  });
  form.addEventListener('submit', function (e) { e.preventDefault(); lanza(); });

  var inicial = '';
  try { inicial = new URLSearchParams(location.search).get('q') || ''; } catch (e) { inicial = ''; }
  campo.value = inicial;
  if (inicial.trim()) lanza();
  else if (window.matchMedia && matchMedia('(pointer:fine)').matches) campo.focus();
})();
