/* APDER · botón «Volver arriba» en páginas largas */
(function(){
  if(!document.querySelector('main'))return;
  var b=document.createElement('a');
  b.className='subir';b.href='#';b.setAttribute('aria-label','Volver arriba');b.hidden=true;
  b.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg><span>Arriba</span>';
  b.addEventListener('click',function(e){e.preventDefault();window.scrollTo({top:0,behavior:window.matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'});var s=document.querySelector('.saltar,header a');if(s)s.focus({preventScroll:true})});
  document.body.appendChild(b);
  var t=false;
  function v(){t=false;b.hidden=window.scrollY<1200}
  window.addEventListener('scroll',function(){if(!t){t=true;requestAnimationFrame(v)}},{passive:true});v();
})();
