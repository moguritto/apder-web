/* APDER · ayudas de lectura en páginas largas:
   cabecera fija y compacta, botón «Contenido» (móvil) y botón «Volver arriba». */
(function(){
  var main=document.querySelector('main'); if(!main)return;
  var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var header=document.querySelector('header');

  var up=document.createElement('a');
  up.className='subir';up.href='#';up.setAttribute('aria-label','Volver arriba');up.hidden=true;
  up.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg><span>Arriba</span>';
  up.addEventListener('click',function(e){e.preventDefault();window.scrollTo({top:0,behavior:reduce?'auto':'smooth'});var s=document.querySelector('.saltar,header a');if(s)s.focus({preventScroll:true})});
  document.body.appendChild(up);

  var toc=document.querySelector('.s-toc-movil'),cont=null;
  if(toc){
    cont=document.createElement('button');cont.type='button';cont.className='contenido-flotante';cont.hidden=true;
    cont.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg><span>Contenido</span>';
    cont.addEventListener('click',function(){toc.open=true;toc.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});var s=toc.querySelector('summary');if(s)s.focus({preventScroll:true})});
    document.body.appendChild(cont);
  }

  var t=false;
  function v(){
    t=false;var y=window.scrollY;
    up.hidden=y<1200;
    if(header&&document.body.matches('.guia,.art-pagina'))header.classList.toggle('compacta',y>80);
    if(cont){var r=toc.getBoundingClientRect();cont.hidden=!(r.bottom<0)}
  }
  window.addEventListener('scroll',function(){if(!t){t=true;requestAnimationFrame(v)}},{passive:true});v();
})();
