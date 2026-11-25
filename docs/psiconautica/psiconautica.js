/* Psiconáutica: buscador y filtros de la portada, e índice lateral de cada página.
   Sin servicios externos. La portada lee indice.json (lo escribe scripts/psiconautica/generar.py):
   [slug, título, letra del tipo, título original, frase, [alias]] */
(function () {
  'use strict';
  var main = document.querySelector('main.psi');
  if (!main) return;

  /* alto de la cabecera fija del sitio, para lo que se queda pegado debajo */
  var cab = document.querySelector('.cabecera');
  function medir() { if (cab) main.style.setProperty('--p-cab', Math.round(cab.getBoundingClientRect().height) + 'px'); }
  medir();
  if (cab && 'ResizeObserver' in window) new ResizeObserver(medir).observe(cab);

  /* ---- página de artículo: marca en el índice el apartado que se está leyendo ---- */
  var toc = main.querySelector('.p-toc');
  if (toc) {
    var enlaces = {}, visto = null, pendiente = false;
    toc.querySelectorAll('a').forEach(function (a) { enlaces[a.getAttribute('href').slice(1)] = a; });
    var titulos = [].slice.call(main.querySelectorAll('.p-texto h2[id]'));
    var espiar = function () {
      pendiente = false;
      var limite = (cab ? cab.getBoundingClientRect().bottom : 0) + 48, ahora = null;
      for (var i = 0; i < titulos.length; i++) { if (titulos[i].getBoundingClientRect().top <= limite) ahora = enlaces[titulos[i].id]; else break; }
      if (ahora === visto) return;
      if (visto) { visto.classList.remove('on'); visto.removeAttribute('aria-current'); }
      visto = ahora;
      if (visto) { visto.classList.add('on'); visto.setAttribute('aria-current', 'true'); }
    };
    window.addEventListener('scroll', function () { if (!pendiente) { pendiente = true; requestAnimationFrame(espiar); } }, { passive: true });
    espiar();
  }

  /* ---- portada ---- */
  if (!main.hasAttribute('data-portada')) return;
  var campo = document.getElementById('p-q');
  var form = document.getElementById('p-form');
  var filtros = document.getElementById('p-filtros');
  var salida = document.getElementById('p-res');
  var aviso = document.getElementById('p-n');
  var resto = document.getElementById('p-resto');
  var antes = document.getElementById('antes');
  if (!campo || !salida) return;

  var TIPO = { s: 'sustancia', e: 'efecto', c: 'cuidado', o: 'concepto' };
  var NOMBRE = { sustancia: 'Sustancia', efecto: 'Efecto', cuidado: 'Cuidado', concepto: 'Concepto' };
  var PLURAL = { sustancia: 'Sustancias', efecto: 'Efectos', cuidado: 'Cuidado', concepto: 'Conceptos' };
  var PASO = 30;
  var datos = null, pidiendo = false, tipo = '', cuantos = PASO, espera = null;

  function norm(t) { return t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function esc(t) { return t.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function cargar(luego) {
    if (datos) { luego(); return; }
    if (pidiendo) return;
    pidiendo = true;
    fetch('indice.json').then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (d) {
      datos = d.map(function (p) {
        return { slug: p[0], titulo: p[1], tipo: TIPO[p[2]] || 'concepto', frase: p[4] || '',
                 _t: norm(p[1]), _o: norm(p[3] + ' ' + (p[5] || []).join(' ')), _f: norm(p[4] || '') };
      });
      pidiendo = false;
      pintar();
    }).catch(function () {
      pidiendo = false;
      salida.hidden = false;
      salida.innerHTML = '<li class="p-vacio">No se ha podido cargar el buscador. Recarga la página o usa el <a href="../buscar/?q=' +
        encodeURIComponent(campo.value.trim()) + '">buscador general</a>.</li>';
    });
  }

  function puntos(p, ts) {
    var total = 0;
    for (var i = 0; i < ts.length; i++) {
      var t = ts[i], n = 0;
      if (p._t === t) n = 120;
      else if (p._t.indexOf(t) === 0) n = 100;
      else if ((' ' + p._t).indexOf(' ' + t) > -1) n = 60;
      else if (p._t.indexOf(t) > -1) n = 40;
      else if ((' ' + p._o).indexOf(' ' + t) > -1) n = 30;
      else if (p._o.indexOf(t) > -1) n = 20;
      else if (p._f.indexOf(t) > -1) n = 8;
      if (!n) return 0;
      total += n;
    }
    return total;
  }

  /* resalta en el título lo que coincide, sin romper acentos */
  function resaltar(titulo, ts) {
    var s = '', m = [];
    for (var i = 0; i < titulo.length; i++) { var c = norm(titulo.charAt(i)); for (var j = 0; j < c.length; j++) { s += c.charAt(j); m.push(i); } }
    var marca = [];
    ts.forEach(function (t) {
      var k = s.indexOf(t);
      while (k > -1) { for (var x = k; x < k + t.length; x++) marca[m[x]] = true; k = s.indexOf(t, k + t.length); }
    });
    var out = '', dentro = false;
    for (var p = 0; p < titulo.length; p++) {
      if (marca[p] && !dentro) { out += '<mark>'; dentro = true; }
      if (!marca[p] && dentro) { out += '</mark>'; dentro = false; }
      out += esc(titulo.charAt(p));
    }
    return out + (dentro ? '</mark>' : '');
  }

  function filtrarIndice() {
    var vivas = {};
    main.querySelectorAll('.p-letra').forEach(function (sec) {
      var n = 0;
      sec.querySelectorAll('li').forEach(function (li) {
        var ver = !tipo || li.getAttribute('data-t') === tipo;
        li.hidden = !ver;
        if (ver) n++;
      });
      sec.hidden = !n;
      vivas['#' + sec.id] = n > 0;
    });
    main.querySelectorAll('.p-barra a').forEach(function (a) {
      var ok = vivas[a.getAttribute('href')];
      a.classList.toggle('no', !ok);
      if (ok) a.removeAttribute('tabindex'); else a.setAttribute('tabindex', '-1');
    });
    if (antes) antes.hidden = !!tipo && tipo !== 'cuidado';
  }

  function direccion(q) {
    var p = [];
    if (q) p.push('q=' + encodeURIComponent(q));
    if (tipo) p.push('tipo=' + tipo);
    try { history.replaceState(null, '', location.pathname + (p.length ? '?' + p.join('&') : '') + (q ? '' : location.hash)); } catch (e) {}
  }

  function pintar() {
    var q = campo.value.trim();
    var ts = norm(q).split(/\s+/).filter(function (x) { return x; });
    direccion(q);
    if (!ts.length) {
      salida.hidden = true; salida.innerHTML = ''; resto.hidden = false; aviso.textContent = '';
      filtrarIndice();
      return;
    }
    if (!datos) { cargar(pintar); return; }
    var res = [];
    datos.forEach(function (p) {
      if (tipo && p.tipo !== tipo) return;
      var n = puntos(p, ts);
      if (n) res.push([n, p]);
    });
    res.sort(function (a, b) { return b[0] - a[0] || a[1]._t.localeCompare(b[1]._t); });
    resto.hidden = true; salida.hidden = false;
    if (!res.length) {
      aviso.textContent = 'Sin resultados';
      salida.innerHTML = '<li class="p-vacio">No hay ninguna página' + (tipo ? ' en ' + PLURAL[tipo] : '') +
        ' con «' + esc(q) + '». Prueba con otro nombre, también en inglés, o búscalo en <a href="../buscar/?q=' + encodeURIComponent(q) + '">toda la web</a>.</li>';
      return;
    }
    aviso.textContent = res.length === 1 ? '1 página' : res.length + ' páginas';
    var h = res.slice(0, cuantos).map(function (r) {
      var p = r[1];
      return '<li><a href="' + p.slug + '/"><b>' + resaltar(p.titulo, ts) + '</b><em class="t-' + p.tipo + '">' + NOMBRE[p.tipo] + '</em>' +
        (p.frase ? '<span>' + esc(p.frase) + '</span>' : '') + '</a></li>';
    }).join('');
    if (res.length > cuantos) h += '<li class="p-mas"><button type="button">Ver ' + Math.min(PASO, res.length - cuantos) + ' más de ' + res.length + '</button></li>';
    salida.innerHTML = h;
  }

  salida.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.p-mas button')) { cuantos += PASO; pintar(); }
  });
  campo.addEventListener('focus', function () { cargar(function () {}); });
  campo.addEventListener('input', function () {
    cuantos = PASO;
    clearTimeout(espera);
    espera = setTimeout(pintar, 90);
  });
  campo.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && campo.value) { campo.value = ''; cuantos = PASO; pintar(); }
  });
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var primero = salida.querySelector('li a');
    if (primero && campo.value.trim()) primero.focus();
  });
  if (filtros) filtros.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('button') : null;
    if (!b) return;
    tipo = b.getAttribute('data-tipo') || '';
    filtros.querySelectorAll('button').forEach(function (x) {
      var on = x === b;
      x.classList.toggle('on', on);
      x.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    cuantos = PASO;
    pintar();
  });

  /* llegada con ?q= o ?tipo= (desde el buscador de una página o desde su tipo) */
  var par = new URLSearchParams(location.search);
  var t0 = par.get('tipo'), q0 = par.get('q');
  if (t0 && NOMBRE[t0] && filtros) {
    var b0 = filtros.querySelector('button[data-tipo="' + t0 + '"]');
    if (b0) {
      tipo = t0;
      filtros.querySelectorAll('button').forEach(function (x) { var on = x === b0; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    }
  }
  if (q0) campo.value = q0;
  if (q0 || tipo) pintar();
})();
