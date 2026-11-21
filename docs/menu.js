/* APDER · menú principal: panel «Medicinas», menú de móvil y cabecera compacta al bajar. */
(function(){
  var cab=document.querySelector('.cabecera'); if(!cab)return;
  var html=document.documentElement,menu=cab.querySelector('#menu'),tog=cab.querySelector('.menu-toggle');
  var desp=cab.querySelector('.menu-desp'),abre=desp&&desp.querySelector('.menu-abre');
  var ancho=window.matchMedia('(min-width:1001px)'),raton=window.matchMedia('(hover:hover)');

  function movil(o){
    cab.classList.toggle('menu-abierto',o);html.classList.toggle('menu-fijo',o);
    if(tog){tog.setAttribute('aria-expanded',o?'true':'false');tog.setAttribute('aria-label',o?'Cerrar menú':'Abrir menú')}
    if(o)html.style.setProperty('--cab-alto',cab.getBoundingClientRect().height+'px');
  }
  if(tog)tog.addEventListener('click',function(){movil(tog.getAttribute('aria-expanded')!=='true')});

  var fijo=false,t;
  function panel(o){if(!desp)return;desp.classList.toggle('abierto',o);abre.setAttribute('aria-expanded',o?'true':'false');if(!o)fijo=false}
  function porRaton(){return ancho.matches&&raton.matches}
  if(abre){
    abre.addEventListener('click',function(){
      var abierto=abre.getAttribute('aria-expanded')==='true';
      if(abierto&&!fijo&&porRaton()){fijo=true;return}   /* abierto al pasar el ratón: el clic lo deja fijo */
      panel(!abierto);fijo=!abierto;
    });
    desp.addEventListener('mouseenter',function(){if(porRaton()){clearTimeout(t);t=setTimeout(function(){panel(true)},90)}});
    desp.addEventListener('mouseleave',function(){if(porRaton()&&!fijo){clearTimeout(t);t=setTimeout(function(){panel(false)},220)}});
    desp.addEventListener('focusout',function(e){if(ancho.matches&&e.relatedTarget&&!desp.contains(e.relatedTarget))panel(false)});
    document.addEventListener('click',function(e){if(ancho.matches&&!desp.contains(e.target))panel(false)});
  }
  document.addEventListener('keydown',function(e){
    if(e.key!=='Escape')return;
    if(desp&&desp.classList.contains('abierto')&&ancho.matches){panel(false);abre.focus();return}
    if(cab.classList.contains('menu-abierto')){movil(false);if(tog)tog.focus()}
  });
  if(menu)menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){if(!ancho.matches)movil(false)})});
  ancho.addEventListener('change',function(){movil(false);panel(false)});

  var r=false;
  function baja(){r=false;cab.classList.toggle('compacta',window.scrollY>40)}
  window.addEventListener('scroll',function(){if(!r){r=true;requestAnimationFrame(baja)}},{passive:true});baja();

  /* impresión: enseña las direcciones de los enlaces y abre los desplegables */
  window.addEventListener('beforeprint',function(){document.querySelectorAll('main a[href]').forEach(function(a){var h=a.getAttribute('href');if(h.charAt(0)!=='#'&&!/^(https?:|mailto:)/.test(h))a.setAttribute('data-url',a.href)});document.querySelectorAll('main details').forEach(function(d){if(!d.open){d.open=true;d.setAttribute('data-impresion','1')}})});
  window.addEventListener('afterprint',function(){document.querySelectorAll('main details[data-impresion]').forEach(function(d){d.open=false;d.removeAttribute('data-impresion')})});
})();

/* Enlace de búsqueda para las fichas de la biblioteca. */
(function(){
  var ficha=document.querySelector('aside.lb-caja');
  var titulo=document.querySelector('main h1');
  if(!ficha||!titulo)return;
  var autor='';
  document.querySelectorAll('.lb-dl dt').forEach(function(campo){
    if(campo.textContent.trim()==='Autoría'&&campo.nextElementSibling)autor=campo.nextElementSibling.textContent.trim();
  });
  var firma=document.querySelector('.lb-autor');
  if(!autor&&firma)autor=firma.textContent.trim();
  var enlace=document.createElement('a');
  enlace.className='btn c';
  enlace.href='https://www.amazon.es/s?k='+encodeURIComponent(titulo.textContent.trim()+' '+autor)+'&i=stripbooks';
  enlace.target='_blank';
  enlace.rel='noopener noreferrer';
  enlace.textContent='Buscar en Amazon';
  ficha.insertBefore(enlace,ficha.querySelector('.lb-guias')||ficha.querySelector('.lb-volver'));
})();
