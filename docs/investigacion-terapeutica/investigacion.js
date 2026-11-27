/* Investigación terapéutica: barra de lectura, apartado en curso del índice y gráfico que se dibuja al llegar. */
(function(){
var m=document.querySelector('main.iv');if(!m)return;
var b=m.querySelector('.iv-progreso span');
if(b){var t=false,f=function(){t=false;var h=document.documentElement,a=h.scrollHeight-h.clientHeight;b.style.transform='scaleX('+(a>0?Math.min(1,h.scrollTop/a):0)+')'};
addEventListener('scroll',function(){if(!t){t=true;requestAnimationFrame(f)}},{passive:true});f()}
var d=m.querySelector('.iv-indice-movil');
if(d)d.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){d.open=false})});
if(!('IntersectionObserver' in window))return;
var l=m.querySelectorAll('.iv-indice a'),e={};
l.forEach(function(a){e[a.getAttribute('href').slice(1)]=a});
var o=new IntersectionObserver(function(es){es.forEach(function(x){if(!x.isIntersecting)return;var a=e[x.target.id];if(!a)return;
l.forEach(function(y){y.classList.remove('activo');y.removeAttribute('aria-current')});a.classList.add('activo');a.setAttribute('aria-current','location')})},{rootMargin:'-120px 0px -68% 0px'});
Object.keys(e).forEach(function(id){var h=document.getElementById(id);if(h)o.observe(h)});
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
m.classList.add('js-anima');
var v=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('visto');v.unobserve(x.target)}})},{threshold:.2});
m.querySelectorAll('.iv-grafico').forEach(function(g){v.observe(g)});
})();
