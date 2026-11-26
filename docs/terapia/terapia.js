/* APDER · guías de terapia: índice que acompaña, barra de lectura,
   gráfico que se dibuja al llegar y vídeos que solo se cargan al pulsar. */
(function () {
  var main = document.querySelector('main.tg');
  if (!main) return;
  var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  /* Barra de lectura */
  var barra = main.querySelector('.tg-progreso span');
  if (barra) {
    var pend = false;
    var pinta = function () {
      pend = false;
      var total = document.documentElement.scrollHeight - window.innerHeight;
      barra.style.transform = 'scaleX(' + (total > 0 ? Math.min(1, window.scrollY / total) : 0) + ')';
    };
    window.addEventListener('scroll', function () { if (!pend) { pend = true; requestAnimationFrame(pinta); } }, { passive: true });
    window.addEventListener('resize', pinta);
    pinta();
  }

  /* Índice lateral: marca el apartado que se está leyendo */
  var enlaces = main.querySelectorAll('.tg-indice a');
  if (enlaces.length && 'IntersectionObserver' in window) {
    var mapa = {};
    enlaces.forEach(function (a) { mapa[a.getAttribute('href').slice(1)] = a; });
    var obs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var a = mapa[e.target.id];
        if (!a) return;
        enlaces.forEach(function (x) { x.classList.remove('activo'); x.removeAttribute('aria-current'); });
        a.classList.add('activo');
        a.setAttribute('aria-current', 'location');
        var g = a.closest('.grupo');
        if (g) g.querySelector(':scope > a').classList.add('activo');
      });
    }, { rootMargin: '-110px 0px -68% 0px' });
    Object.keys(mapa).forEach(function (id) { var x = document.getElementById(id); if (x) obs.observe(x); });
  }

  /* Índice del móvil: se cierra al elegir un apartado */
  var movil = main.querySelector('.tg-indice-movil');
  if (movil) movil.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () { movil.open = false; });
  });

  /* Gráfico: las barras crecen al entrar en pantalla */
  var graficos = main.querySelectorAll('.tg-grafico');
  if (graficos.length && 'IntersectionObserver' in window && !reduce) {
    main.classList.add('js-anima');
    var og = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visto'); og.unobserve(e.target); } });
    }, { threshold: 0.35 });
    graficos.forEach(function (g) { og.observe(g); });
  }

  /* Vídeos: solo se conecta con YouTube (sin cookies) al pulsar */
  main.querySelectorAll('.tg-video .marco').forEach(function (m) {
    var b = m.querySelector('button');
    if (!b) return;
    b.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + m.dataset.video + '?autoplay=1&rel=0';
      f.title = m.dataset.titulo;
      f.allow = 'autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      m.replaceChildren(f);
      f.focus();
    });
  });
})();
