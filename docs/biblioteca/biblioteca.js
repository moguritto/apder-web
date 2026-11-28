(function(){
var lista=document.getElementById('b-lista');if(!lista)return;
var filtroToggle=document.getElementById('b-filtros-toggle'), filtroAside=document.getElementById('b-filtros');
filtroToggle.addEventListener('click',function(){var abierto=filtroAside.classList.toggle('bx-abierto');filtroToggle.setAttribute('aria-expanded',String(abierto));filtroToggle.textContent=abierto?'Ocultar filtros':'Mostrar filtros'});

var PAG=36,lim=PAG;
var norm=function(s){return s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()};
[].forEach.call(lista.querySelectorAll('.b-meta'),function(p){if(p.children.length)return;var t=p.textContent.split(' · ');p.textContent='';t.forEach(function(x,i){if(i){var s=document.createElement('span');s.className='bm-sep';s.textContent=' · ';p.appendChild(s)}var e=document.createElement('span');e.textContent=x;p.appendChild(e)})});
var libros=[].slice.call(lista.children).map(function(li,i){
  var d=li.dataset;
  return {li:li,i:i,cat:[d.cat],idioma:[d.idioma],sust:d.sust.split(' '),decada:[d.decada],autor:(d.autores||'').split('|').filter(Boolean),
    anio:+d.anio,portada:li.classList.contains('con-portada'),
    tit:li.querySelector('.b-tit').textContent,autorTxt:li.querySelector('.b-meta').textContent,txt:norm(li.textContent)};
});
var sel={cat:[],sust:[],idioma:[],decada:[],autor:[]};
var cajas=[].slice.call(document.querySelectorAll('.bx-arbol input[data-f]'));
var q=document.getElementById('b-q'),orden=document.getElementById('b-orden'),nres=document.getElementById('b-n'),
  mas=document.getElementById('b-mas'),chips=document.getElementById('b-chips'),vacio=document.getElementById('b-vacio'),
  limpiar=document.getElementById('b-limpiar');
var palabras=[];
function pasa(b,salvo){
  for(var f in sel){if(f===salvo||!sel[f].length)continue;if(!b[f].some(function(x){return sel[f].indexOf(x)>=0}))return false}
  for(var k=0;k<palabras.length;k++)if(b.txt.indexOf(palabras[k])<0)return false;
  return true;
}
function etiqueta(c){return c.parentNode.querySelector('.bx-et').textContent}
function pinta(){
  palabras=norm(q.value).split(/\s+/).filter(Boolean);
  var res=libros.filter(function(b){return pasa(b,null)});
  var o=orden.value;
  res.sort(function(a,b){
    if(o==='new')return (!a.anio)-(!b.anio)||b.anio-a.anio||a.i-b.i;
    if(o==='old')return (!a.anio)-(!b.anio)||a.anio-b.anio||a.i-b.i;
    if(o==='az')return a.tit.localeCompare(b.tit,'es');
    if(o==='autor')return a.autorTxt.localeCompare(b.autorTxt,'es');
    return (b.portada-a.portada)||a.i-b.i;
  });
  var dentro=new Set(res);
  res.forEach(function(b,k){b.li.hidden=k>=lim;b.li.style.animationDelay=(k%PAG<12?(k%PAG)*40:0)+'ms';lista.appendChild(b.li)});
  libros.forEach(function(b){if(!dentro.has(b)){b.li.hidden=true;lista.appendChild(b.li)}});
  // recuentos por faceta, teniendo en cuenta los demás filtros
  var base={};
  ['cat','sust','idioma','decada','autor'].forEach(function(f){base[f]=libros.filter(function(b){return pasa(b,f)})});
  cajas.forEach(function(c){
    var f=c.dataset.f,v=c.value,n=0;
    base[f].forEach(function(b){if(b[f].indexOf(v)>=0)n++});
    c.parentNode.querySelector('.bx-n').textContent=n;
    c.closest('li').classList.toggle('cero',n===0&&!c.checked);
  });
  document.querySelectorAll('.bx-grupo').forEach(function(g){
    var cs=[].slice.call(g.querySelectorAll('input[data-f]'));var f=cs[0].dataset.f;
    var vals=cs.map(function(c){return c.value});
    var n=base[f].filter(function(b){return b[f].some(function(x){return vals.indexOf(x)>=0})}).length;
    g.querySelector('.bx-gn').textContent=n;
  });
  document.querySelectorAll('.bx-sec').forEach(function(s){
    var n=sel[s.dataset.sec].length,bd=s.querySelector('.bx-badge');bd.hidden=!n;bd.textContent=n;
  });
  var total=res.length,vis=Math.min(lim,total);
  nres.textContent=total?('1–'+vis+' de '+total+(total===1?' libro':' libros')+(total===libros.length?'':(total===1?' que coincide':' que coinciden'))):'0 libros';
  vacio.hidden=total>0;
  mas.hidden=total<=lim;
  mas.textContent='Ver '+Math.min(PAG,total-lim)+' libros más';
  chips.textContent='';
  cajas.forEach(function(c){if(c.checked){var bt=document.createElement('button');bt.type='button';bt.textContent=etiqueta(c);
    bt.setAttribute('aria-label','Quitar filtro '+etiqueta(c));bt.addEventListener('click',function(){c.checked=false;cambia(c)});chips.appendChild(bt)}});
  if(palabras.length){var bq=document.createElement('button');bq.type='button';bq.textContent='«'+q.value.trim()+'»';bq.setAttribute('aria-label','Quitar búsqueda');
    bq.addEventListener('click',function(){q.value='';lim=PAG;pinta()});chips.appendChild(bq)}
  limpiar.hidden=!chips.childNodes.length;
}
function cambia(c){
  var f=c.dataset.f,a=sel[f],k=a.indexOf(c.value);
  if(c.checked&&k<0)a.push(c.value);if(!c.checked&&k>=0)a.splice(k,1);
  lim=PAG;pinta();
}
cajas.forEach(function(c){c.checked=false;c.addEventListener('change',function(){cambia(c)})});
var t;q.addEventListener('input',function(){clearTimeout(t);t=setTimeout(function(){lim=PAG;pinta()},120)});
orden.addEventListener('change',function(){lim=PAG;pinta()});
mas.addEventListener('click',function(){var primero=lim;lim+=PAG;pinta();var b=lista.children[primero];if(b){var a=b.querySelector('a');if(a)a.focus({preventScroll:true})}});
limpiar.addEventListener('click',function(){cajas.forEach(function(c){c.checked=false});for(var f in sel)sel[f]=[];q.value='';lim=PAG;pinta()});
document.getElementById('b-compartir').addEventListener('click',async function(){
  var enlace=new URL(location.href); enlace.search=''; enlace.hash='';
  if(q.value.trim())enlace.searchParams.set('q',q.value.trim());
  Object.keys(sel).forEach(function(f){sel[f].forEach(function(v){enlace.searchParams.append(f,v)})});
  if(orden.value!=='rel')enlace.searchParams.set('orden',orden.value);
  var estado=document.getElementById('b-compartir-estado');
  try{await navigator.clipboard.writeText(enlace.href);estado.textContent='Enlace copiado.'}
  catch(e){estado.textContent='Copia este enlace: '+enlace.href}
});
var ps=new URLSearchParams(location.search);
['cat','sust','idioma','decada','autor'].forEach(function(f){ps.getAll(f).forEach(function(v){cajas.forEach(function(c){if(c.dataset.f===f&&c.value===v&&!c.checked){c.checked=true;sel[f].push(v)}})})});
if(ps.get('q')){q.value=ps.get('q')}
if(Array.from(orden.options).some(function(o){return o.value===ps.get('orden')}))orden.value=ps.get('orden');
cajas.forEach(function(c){if(c.checked){var g=c.closest('.bx-grupo');if(g)g.open=true}});
if(window.matchMedia('(max-width:900px)').matches)document.querySelectorAll('.bx-sec').forEach(function(s){s.open=false});
pinta();
})();

/* Portada (25-11-2026): el buscador de la apertura y las entradas por tema, medicina o idioma
   mueven los filtros del catálogo sin recargar la página. */
(function(){
var cat=document.getElementById('catalogo-libros'),q=document.getElementById('b-q');if(!cat||!q)return;
var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
function ir(suave){cat.scrollIntoView({behavior:suave&&!reduce?'smooth':'auto',block:'start'})}
function limpia(){var b=document.getElementById('b-limpiar');if(b)b.click()}
var f=document.getElementById('bh-form'),hq=document.getElementById('bh-q');
if(f&&hq)f.addEventListener('submit',function(e){e.preventDefault();limpia();q.value=hq.value.trim();q.dispatchEvent(new Event('input'));setTimeout(function(){ir(true);q.focus({preventScroll:true})},160)});
document.addEventListener('click',function(e){
  var a=e.target.closest&&e.target.closest('.bib a[data-f],.bib a[data-orden]');if(!a)return;
  var o=document.getElementById('b-orden');
  if(a.dataset.orden){e.preventDefault();limpia();o.value=a.dataset.orden;o.dispatchEvent(new Event('change'));ir(true);return}
  var c=[].slice.call(document.querySelectorAll('.bx-arbol input[data-f]')).filter(function(x){return x.dataset.f===a.dataset.f&&x.value===a.dataset.v})[0];
  if(!c)return;
  e.preventDefault();limpia();c.checked=true;c.dispatchEvent(new Event('change'));
  var g=c.closest('.bx-grupo');if(g)g.open=true;
  ir(true);
});
/* si se llega con filtros en la dirección (desde el menú o desde una ficha), se va directo al catálogo */
if(/[?&](q|cat|sust|idioma|decada|autor|orden)=/.test(location.search)&&!location.hash)ir(false);
})();
