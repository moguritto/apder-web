/* APDER · guía de terapia (docs/terapia/guia.js, va con guia.css): barra de lectura, capítulo en curso,
   aparición suave al llegar y vídeos que solo se cargan al pulsar. */
(function () {
  var main = document.querySelector('main.tg');
  if (!main) return;
  var reduce = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var hayIO = 'IntersectionObserver' in window;

  /* Barra de lectura y capítulo en curso: un solo cálculo por fotograma */
  var barra = main.querySelector('.tg-progreso span');
  var enlaces = main.querySelectorAll('.tg-capnav a');
  var caps = main.querySelectorAll('.tg-cap[data-cap]');
  var actual = null;
  var pend = false;
  var pinta = function () {
    pend = false;
    if (barra) {
      var total = document.documentElement.scrollHeight - window.innerHeight;
      barra.style.transform = 'scaleX(' + (total > 0 ? Math.min(1, window.scrollY / total) : 0) + ')';
    }
    if (!enlaces.length) return;
    /* el capítulo en curso es el último cuya portadilla ya ha pasado bajo la barra */
    var cap = null;
    for (var i = 0; i < caps.length; i++) {
      if (caps[i].getBoundingClientRect().top <= 260) cap = caps[i].dataset.cap; else break;
    }
    if (cap === actual) return;
    actual = cap;
    enlaces.forEach(function (a) {
      var si = a.dataset.cap === cap;
      a.classList.toggle('activo', si);
      if (si) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
  };
  if (barra || enlaces.length) {
    window.addEventListener('scroll', function () { if (!pend) { pend = true; requestAnimationFrame(pinta); } }, { passive: true });
    window.addEventListener('resize', pinta);
    pinta();
  }

  /* Índice del móvil: se cierra al elegir un apartado */
  var movil = main.querySelector('.tg-indice-movil');
  if (movil) movil.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () { movil.open = false; });
  });

  /* Aparición suave: solo lo que aún no está en pantalla, para que nada parpadee */
  var piezas = main.querySelectorAll('.tg-aparece');
  if (piezas.length && hayIO && !reduce) {
    var alto = window.innerHeight;
    var ver = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('tg-visto');
        e.target.classList.remove('tg-prep');
        ver.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    piezas.forEach(function (p) {
      if (p.getBoundingClientRect().top > alto * 0.92) { p.classList.add('tg-prep'); ver.observe(p); }
    });
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
