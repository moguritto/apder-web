/* APDER · Formaciones en el mundo: globo, directorio con filtros, búsqueda y enlace compartible.
   Los datos están en formaciones.json (una ficha por formación). El globo lo dibuja geo.min.js con mundo.json.
   Las etiquetas de cada campo están en la tabla T: un valor nuevo en los datos se ve tal cual hasta que se añade aquí. */
(function(){
'use strict';
var raiz=document.getElementById('directorio');if(!raiz)return;
function $(id){return document.getElementById(id)}
var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
var estrecha=window.matchMedia('(max-width:1000px)');
var HOY=new Date();HOY.setHours(0,0,0,0);

/* ---------- etiquetas ---------- */
var T={
  tipo:{terapia:'Terapia asistida',facilitacion:'Facilitación y acompañamiento',integracion:'Integración',riesgos:'Reducción de riesgos',investigacion:'Investigación',introduccion:'Introducción y fundamentos',tradiciones:'Saberes tradicionales'},
  tipoCorto:{terapia:'Terapia asistida',facilitacion:'Facilitación',integracion:'Integración',riesgos:'Reducción de riesgos',investigacion:'Investigación',introduccion:'Introducción',tradiciones:'Saberes tradicionales'},
  dest:{todos:'Abierta a todo el mundo',ayuda:'Quienes acompañan',clinicos:'Profesionales sanitarios'},
  destCorto:{todos:'Abierta a todo el mundo',ayuda:'Para quienes acompañan',clinicos:'Para profesionales sanitarios'},
  modo:{presencial:'Presencial',mixta:'Mixta (en línea y presencial)',en_linea:'Solo en línea'},
  modoCorto:{presencial:'Presencial',mixta:'Mixta',en_linea:'En línea'},
  sust:{psilocibina:'Psilocibina',mdma:'MDMA',ketamina:'Ketamina',ayahuasca:'Ayahuasca',ibogaina:'Ibogaína','5-meo-dmt':'5-MeO-DMT',lsd:'LSD',mescalina:'Mescalina',cannabis:'Cannabis',varias:'Varias sustancias',sin_sustancias:'Sin sustancias'},
  recon:{universidad:'Universitaria',oregon:'Aprobada en Oregón',colorado:'Aprobada en Colorado',nuevo_mexico:'Aprobada en Nuevo México',ce:'Créditos de formación continuada',certificado:'Certificado propio'},
  entidad:{universidad:'Universidad',instituto:'Instituto o escuela',asociacion:'Asociación o entidad sin ánimo de lucro',empresa:'Empresa',hospital:'Hospital',fundacion:'Fundación'},
  entidadCorta:{universidad:'Universidad',instituto:'Instituto',asociacion:'Asociación',empresa:'Empresa',hospital:'Hospital',fundacion:'Fundación'},
  dur:{breve:'Hasta 20 horas',media:'De 20 a 100 horas',larga:'De 100 a 300 horas',muylarga:'Más de 300 horas',sd:'Sin dato de horas'},
  precio:{gratis:'Gratuita',p1:'Menos de 500 €',p2:'De 500 a 2.000 €',p3:'De 2.000 a 5.000 €',p4:'De 5.000 a 10.000 €',p5:'Más de 10.000 €',sp:'Sin precio publicado'},
  region:{europa:'Europa',norteamerica:'Norteamérica',latam:'América Latina y el Caribe',oceania:'Oceanía',asia:'Asia y Oriente Próximo',africa:'África',otras:'Otras regiones'},
  regionCorta:{europa:'Europa',norteamerica:'Norteamérica',latam:'América Latina',oceania:'Oceanía',asia:'Asia y Oriente Próximo',africa:'África',otras:'Otras regiones'},
  incluye:{practica_supervisada:'Práctica supervisada',supervision:'Supervisión',experiencial:'Trabajo vivencial',mentoria:'Mentoría',examen:'Examen final',retiro:'Retiro presencial'},
  estado:{pausada:'En pausa',por_confirmar:'Edición por confirmar'}
};
function humano(x){x=String(x==null?'':x).replace(/_/g,' ');return x.charAt(0).toUpperCase()+x.slice(1)}
function et(tabla,x){return(T[tabla]&&T[tabla][x])||humano(x)}

var REG={};
[['europa','AD AL AT BA BE BG BY CH CY CZ DE DK EE ES FI FO FR GB GI GR HR HU IE IS IT LI LT LU LV MC MD ME MK MT NL NO PL PT RO RS RU SE SI SK SM UA VA XK'],
 ['norteamerica','US CA'],
 ['latam','MX GT BZ HN SV NI CR PA CU DO HT JM PR TT BS BB AR BO BR CL CO EC GY PE PY SR UY VE'],
 ['oceania','AU NZ FJ PG'],
 ['asia','IL PS TR AE SA QA JO LB IN NP LK TH VN KH LA MY SG ID PH CN HK TW JP KR MN KZ GE AM AZ IR'],
 ['africa','ZA GA CM NG KE GH MA EG TN SN ET UG TZ RW MZ ZW NA BW CI']
].forEach(function(r){r[1].split(' ').forEach(function(c){REG[c]=r[0]})});
/* a dónde mira el globo cuando una región no tiene ninguna ciudad en el mapa */
var REG_CENTRO={europa:[10,50,2.2],norteamerica:[-100,42,1.5],latam:[-66,-14,1.3],oceania:[140,-27,1.7],asia:[88,26,1.2],africa:[20,2,1.3],otras:[0,20,1]};

var nomPais=(function(){var dn=null,fijo={US:'Estados Unidos',GB:'Reino Unido',NL:'Países Bajos',CZ:'Chequia'};try{dn=new Intl.DisplayNames(['es'],{type:'region'})}catch(e){}
  return function(c){if(fijo[c])return fijo[c];try{return(dn&&dn.of(c))||c}catch(e){return c}}})();
var nomIdioma=(function(){var dn=null,fijo={es:'Español',en:'Inglés',pt:'Portugués',fr:'Francés',de:'Alemán',it:'Italiano',nl:'Neerlandés',ca:'Catalán',he:'Hebreo'};try{dn=new Intl.DisplayNames(['es'],{type:'language'})}catch(e){}
  return function(c){if(fijo[c])return fijo[c];var n=c;try{n=(dn&&dn.of(c))||c}catch(e){}return n.charAt(0).toUpperCase()+n.slice(1)}})();
function fecha(iso,o){try{return new Intl.DateTimeFormat('es-ES',o).format(new Date(iso+'T12:00:00'))}catch(e){return iso}}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function norm(s){return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase()}
function slug(s){return norm(s).replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'')}
function banda(h){return h==null?'sd':h<=20?'breve':h<=100?'media':h<=300?'larga':'muylarga'}
function bandaPrecio(e){return e==null?'sp':e===0?'gratis':e<500?'p1':e<2000?'p2':e<5000?'p3':e<=10000?'p4':'p5'}
function plural(n,uno,varios){return n+' '+(n===1?uno:varios)}
function lista(v){return Array.isArray(v)?v:(v==null||v===''?[]:[v])}

var ICO={
  flecha:'<svg class="fm-flecha" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  fuera:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 16 17 7M9 7h8v8"/></svg>',
  casa:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 20V9l8-5 8 5v11M9.5 20v-6h5v6M2.5 20h19"/></svg>',
  lugar:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11Z"/><circle cx="12" cy="10" r="2.3"/></svg>',
  linea:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3.5" y="5" width="17" height="11.5" rx="2"/><path d="M8.5 20h7M12 16.5V20"/></svg>',
  cerrar:'<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18"/></svg>'
};

/* ---------- facetas ---------- */
var FACETAS=[
  {k:'tipo',t:'Tipo de formación',v:function(f){return lista(f.tipo)},abierta:1,orden:Object.keys(T.tipo)},
  {k:'dest',t:'Para quién',v:function(f){return[f.destinatarios]},abierta:1,orden:Object.keys(T.dest)},
  {k:'modo',t:'Modalidad',v:function(f){return[f.modalidad]},abierta:1,orden:['presencial','mixta','en_linea']},
  {k:'idioma',t:'Idioma',v:function(f){return lista(f.idiomas)},abierta:1,max:6,et:nomIdioma,primero:'es'},
  {k:'region',t:'Región',v:function(f){return[f._region]},orden:Object.keys(T.region)},
  {k:'pais',t:'País',v:function(f){return[f.pais]},max:8,et:nomPais},
  {k:'sust',t:'Sustancia o enfoque',v:function(f){return lista(f.sustancias)}},
  {k:'dur',t:'Duración',v:function(f){return[f._dur]},orden:Object.keys(T.dur)},
  {k:'precio',t:'Precio orientativo',v:function(f){return[f._precio]},orden:Object.keys(T.precio)},
  {k:'recon',t:'Reconocimiento',v:function(f){return lista(f.reconocimiento)}},
  {k:'entidad',t:'Quién la imparte',v:function(f){return lista(f.tipo_entidad)},orden:Object.keys(T.entidad)}
];
var FAC={};
FACETAS.forEach(function(F){FAC[F.k]=F;if(!F.et)F.et=function(x){return et(F.k,x)}});

var RAPIDOS=[
  {t:'En español',k:'idioma',v:['es']},
  {t:'Solo en línea',k:'modo',v:['en_linea']},
  {t:'Con parte presencial',k:'modo',v:['presencial','mixta']},
  {t:'Con fecha anunciada',k:'fecha'},
  {t:'Abierta a todo el mundo',k:'dest',v:['todos']},
  {t:'Universitaria',k:'recon',v:['universidad']}
];

var datos=[],ultima=[],lugares=[],LUG={},POR=12,visibles=POR,abiertas={},verTodos={},actualizado='';
var estado={q:'',qn:[],sel:{},prox:false,lugares:[],orden:'fecha'};
FACETAS.forEach(function(F){estado.sel[F.k]=[]});

function prepara(f){
  f.id=String(f.id||slug(f.nombre));
  f._region=REG[f.pais]||'otras';
  f._dur=banda(f.duracion_horas);
  f._precio=bandaPrecio(f.precio_eur);
  var d=f.proxima?new Date(f.proxima+'T12:00:00'):null;f._prox=d&&!isNaN(d)&&d>=HOY?d:null;
  f._lugar='';
  f._txt=norm([f.nombre,f.nombre_es,f.entidad,f.ciudad,f.otros_lugares,nomPais(f.pais),f.descripcion,
    lista(f.tipo).map(function(x){return et('tipo',x)}).join(' '),lista(f.sustancias).map(function(x){return et('sust',x)}).join(' '),
    lista(f.idiomas).map(nomIdioma).join(' '),et('modoCorto',f.modalidad),et('entidadCorta',f.tipo_entidad)].join(' '));
}

/* las ciudades del globo: solo lo presencial o mixto que trae coordenadas */
function creaLugares(){
  lugares=[];LUG={};
  var sinNombre=[];
  datos.forEach(function(f){
    if(f.modalidad==='en_linea'||typeof f.lat!=='number'||typeof f.lon!=='number')return;
    var c=String(f.ciudad||'').trim();
    if(!c){sinNombre.push(f);return}
    var id=slug(c)+'-'+String(f.pais||'').toLowerCase();
    if(!LUG[id]){LUG[id]={id:id,nombre:c,pais:f.pais,fs:[],lat:0,lon:0};lugares.push(LUG[id])}
    LUG[id].fs.push(f);
  });
  lugares.forEach(function(l){l.lat=media(l.fs,'lat');l.lon=media(l.fs,'lon')});
  sinNombre.forEach(function(f){
    var cerca=null;
    lugares.forEach(function(l){if(l.pais===f.pais&&Math.abs(l.lat-f.lat)<.3&&Math.abs(l.lon-f.lon)<.3)cerca=cerca||l});
    if(!cerca){
      var id=String(f.pais||'xx').toLowerCase()+'-'+f.lat.toFixed(1).replace(/[^0-9]/g,'')+'-'+f.lon.toFixed(1).replace(/[^0-9]/g,'');
      cerca=LUG[id];
      if(!cerca){cerca=LUG[id]={id:id,nombre:nomPais(f.pais),pais:f.pais,fs:[],lat:f.lat,lon:f.lon,sinCiudad:true};lugares.push(cerca)}
    }
    cerca.fs.push(f);
  });
  lugares.forEach(function(l){l.region=REG[l.pais]||'otras';l.fs.forEach(function(f){f._lugar=l.id})});
  lugares.sort(function(a,b){return b.fs.length-a.fs.length||a.nombre.localeCompare(b.nombre,'es')});
}
function media(a,k){var s=0;a.forEach(function(x){s+=x[k]});return s/a.length}

function pasa(f,salvo){
  for(var i=0;i<estado.qn.length;i++)if(f._txt.indexOf(estado.qn[i])<0)return false;
  if(estado.prox&&!f._prox)return false;
  if(estado.lugares.length&&estado.lugares.indexOf(f._lugar)<0)return false;
  for(var j=0;j<FACETAS.length;j++){
    var F=FACETAS[j];if(F.k===salvo)continue;
    var s=estado.sel[F.k];if(!s.length)continue;
    var vs=F.v(f),ok=false;
    for(var m=0;m<vs.length;m++)if(s.indexOf(vs[m])>=0){ok=true;break}
    if(!ok)return false;
  }
  return true;
}

function ordena(a){
  var o=estado.orden;
  function c(x,y){return String(x.nombre).localeCompare(String(y.nombre),'es',{sensitivity:'base'})}
  function nulos(x,y){return(x==null)-(y==null)}
  if(o==='nombre')a.sort(c);
  else if(o==='pais')a.sort(function(x,y){return nomPais(x.pais).localeCompare(nomPais(y.pais),'es')||(x.ciudad||'').localeCompare(y.ciudad||'','es')||c(x,y)});
  else if(o==='duracion')a.sort(function(x,y){return nulos(x.duracion_horas,y.duracion_horas)||(x.duracion_horas||0)-(y.duracion_horas||0)||c(x,y)});
  else if(o==='precio')a.sort(function(x,y){return nulos(x.precio_eur,y.precio_eur)||(x.precio_eur||0)-(y.precio_eur||0)||c(x,y)});
  else a.sort(function(x,y){var p=x._prox,q=y._prox;if(p&&q)return p-q||c(x,y);if(p)return -1;if(q)return 1;return c(x,y)});
}

function pintaFacetas(foco){
  var h='';
  FACETAS.forEach(function(F){
    var cuenta={},todos={};
    datos.forEach(function(f){var vs=F.v(f),p=pasa(f,F.k);vs.forEach(function(x){todos[x]=1;if(p)cuenta[x]=(cuenta[x]||0)+1})});
    var vals=Object.keys(todos);if(!vals.length)return;
    if(F.orden)vals.sort(function(a,b){var i=F.orden.indexOf(a),j=F.orden.indexOf(b);return(i<0?99:i)-(j<0?99:j)});
    else vals.sort(function(a,b){return(cuenta[b]||0)-(cuenta[a]||0)||F.et(a).localeCompare(F.et(b),'es')});
    if(F.primero&&vals.indexOf(F.primero)>0){vals.splice(vals.indexOf(F.primero),1);vals.unshift(F.primero)}
    var sel=estado.sel[F.k],abierta=abiertas[F.k]!=null?abiertas[F.k]:(F.abierta||sel.length>0);
    var limite=F.max&&!verTodos[F.k]?F.max:1e9;
    h+='<details class="fm-grupo" data-k="'+F.k+'"'+(abierta?' open':'')+'><summary>'+esc(F.t)+(sel.length?' <span class="fm-insignia">'+sel.length+'</span>':'')+'</summary><ul class="fm-opciones">';
    vals.forEach(function(x,i){
      var n=cuenta[x]||0,m=sel.indexOf(x)>=0;
      h+='<li class="'+(n?'':'cero')+(i>=limite&&!m?' resto':'')+'"><label><input type="checkbox" data-k="'+F.k+'" value="'+esc(x)+'"'+(m?' checked':'')+'><span class="et">'+esc(F.et(x))+'</span><span class="n">'+n+'</span></label></li>';
    });
    h+='</ul>';
    if(F.max&&vals.length>F.max)h+='<button type="button" class="fm-mas-op" data-k="'+F.k+'" aria-expanded="'+(verTodos[F.k]?'true':'false')+'">'+(verTodos[F.k]?'Ver menos':'Ver los '+vals.length)+'</button>';
    h+='</details>';
  });
  $('fm-facetas').innerHTML=h;
  if(foco){var el=$('fm-facetas').querySelector(foco);if(el)el.focus({preventScroll:true})}
}

/* ---------- fichas ---------- */
function durTxt(f){
  var h=f.duracion_horas,t=f.duracion||'';
  if(h!=null&&!/\d\s*h\b|horas/.test(t))return(t?t+' · ':'')+h+' h';
  return t||(h!=null?h+' h':'');
}
function lugarTxt(f){
  if(f.modalidad==='en_linea')return'En línea, desde '+nomPais(f.pais);
  var t=(f.ciudad?f.ciudad+', ':'')+nomPais(f.pais);
  if(f.otros_lugares)t+=' · '+f.otros_lugares;
  return t;
}
function dato(t,v,larga){return v?'<div'+(larga||String(v).length>16?' class="'+(String(v).length>34?'ancho2':'larga')+'"':'')+'><dt>'+esc(t)+'</dt><dd>'+esc(v)+'</dd></div>':''}
function ficha(f){
  var tipos=lista(f.tipo).map(function(x){return et('tipo',x)}).join(' · ');
  var idi=lista(f.idiomas);
  var lang=f.nombre_es&&idi[0]&&idi[0]!=='es'?' lang="'+esc(idi[0])+'"':'';
  var e='<li class="para">'+esc(et('destCorto',f.destinatarios))+'</li>';
  lista(f.reconocimiento).forEach(function(r){e+='<li class="sello">'+esc(et('recon',r))+'</li>'});
  lista(f.sustancias).forEach(function(s){e+='<li>'+esc(et('sust',s))+'</li>'});
  lista(f.incluye).forEach(function(i){e+='<li>'+esc(et('incluye',i))+'</li>'});
  var d=dato('Modalidad',et('modoCorto',f.modalidad))+dato(idi.length>1?'Idiomas':'Idioma',idi.map(nomIdioma).join(', '))
    +dato('Duración',durTxt(f)||'Consultar',true)+dato('Precio',f.precio||'Consultar',true);
  var est=T.estado[f.estado];
  return '<li><article class="fm-ficha" id="f-'+esc(f.id)+'">'
    +'<div class="fm-f-princ">'
    +'<div class="fm-f-arriba"><p class="fm-f-tipo">'+esc(tipos)+'</p>'+(est?'<span class="fm-f-estado">'+esc(est)+'</span>':'')+'</div>'
    +'<h3 class="fm-f-nombre"'+lang+'><a href="'+esc(f.url)+'" target="_blank" rel="noopener">'+esc(f.nombre)+'</a></h3>'
    +(f.nombre_es?'<p class="fm-f-trad">'+esc(f.nombre_es)+'</p>':'')
    +'<ul class="fm-f-quien"><li>'+ICO.casa+'<span><b>'+esc(f.entidad)+'</b>'+(f.tipo_entidad?' <small>· '+esc(et('entidadCorta',f.tipo_entidad))+'</small>':'')+'</span></li>'
    +'<li>'+(f.modalidad==='en_linea'?ICO.linea:ICO.lugar)+'<span>'+esc(lugarTxt(f))+'</span></li></ul>'
    +(f.descripcion?'<p class="fm-f-desc">'+esc(f.descripcion)+'</p>':'')
    +'<ul class="fm-f-etiquetas">'+e+'</ul></div>'
    +'<div class="fm-f-lado">'
    +(f._prox?'<p class="fm-f-empieza"><span>Empieza</span><b><time datetime="'+esc(f.proxima)+'">'+esc(fecha(f.proxima,{day:'numeric',month:'short',year:'numeric'}))+'</time></b></p>':'')
    +'<dl class="fm-f-datos">'+d+'</dl>'
    +'<a class="fm-f-web" href="'+esc(f.url)+'" target="_blank" rel="noopener">Web oficial'+ICO.fuera+'<span class="fm-oculto"> de '+esc(f.nombre)+' (se abre en otra pestaña)</span></a>'
    +(f.revisado?'<span class="fm-f-rev">Revisado en '+esc(fecha(f.revisado,{month:'long',year:'numeric'}))+'</span>':'')
    +'</div></article></li>';
}
function pintaLista(enfocarDesde){
  var l=$('fm-lista');
  if(!ultima.length){
    l.innerHTML='<li class="fm-vacio"><b>No hay formaciones con estos filtros</b><p>Prueba a quitar alguno o a buscar con otras palabras.</p><button type="button" class="fm-quitar" data-limpiar>Quitar todos los filtros</button></li>';
  }else l.innerHTML=ultima.slice(0,visibles).map(ficha).join('');
  var mas=$('fm-mas'),resto=ultima.length-visibles;
  mas.hidden=resto<=0;
  if(resto>0){
    $('fm-mas-btn').textContent='Ver '+plural(Math.min(POR,resto),'formación más','formaciones más');
    $('fm-todas').hidden=resto<=POR;
    $('fm-todas').querySelector('span').textContent='Ver las '+ultima.length;
  }
  if(enfocarDesde!=null){var a=l.querySelectorAll('.fm-f-nombre a')[enfocarDesde];if(a)a.focus()}
}

/* ---------- recuento, chips y atajos ---------- */
function activos(){var n=(estado.q?1:0)+(estado.prox?1:0)+(estado.lugares.length?1:0);FACETAS.forEach(function(F){n+=estado.sel[F.k].length});return n}
function chip(k,v,t){return '<button type="button" data-quita="'+k+'" data-v="'+esc(v)+'" aria-label="Quitar filtro: '+esc(t)+'">'+esc(t)+'</button>'}
function nombreLugares(ids){
  var ls=ids.map(function(i){return LUG[i]}).filter(Boolean);if(!ls.length)return'Ciudad';
  return ls.length===1?ls[0].nombre+(ls[0].sinCiudad?'':' ('+nomPais(ls[0].pais)+')'):ls[0].nombre+' y '+plural(ls.length-1,'ciudad más','ciudades más');
}
function contar(a,k){var s={};a.forEach(function(f){s[f[k]]=1});return Object.keys(s).length}
function pintaEstado(){
  var h='';
  if(estado.q)h+=chip('q','','«'+estado.q+'»');
  if(estado.lugares.length)h+=chip('lugares','',nombreLugares(estado.lugares));
  if(estado.prox)h+=chip('prox','','Con fecha anunciada');
  FACETAS.forEach(function(F){estado.sel[F.k].forEach(function(x){h+=chip(F.k,x,F.et(x))})});
  $('fm-chips').innerHTML=h;
  var n=activos();
  [].forEach.call(raiz.querySelectorAll('[data-limpiar-fijo]'),function(b){b.hidden=!n});
  [].forEach.call(document.querySelectorAll('[data-n-filtros]'),function(b){b.textContent=n;b.hidden=!n});
  $('fm-n-res').innerHTML=n?'<strong>'+plural(ultima.length,'formación','formaciones')+'</strong> de '+datos.length
    :'<strong>'+plural(datos.length,'formación','formaciones')+'</strong> en '+plural(contar(datos,'pais'),'país','países');
  $('fm-ver').textContent=ultima.length?'Ver '+plural(ultima.length,'formación','formaciones'):'Sin resultados';
  $('fm-prox').checked=estado.prox;
  [].forEach.call($('fm-rapidos').querySelectorAll('button'),function(b){b.setAttribute('aria-pressed',rapidoActivo(RAPIDOS[+b.dataset.i])?'true':'false')});
}
function rapidoActivo(r){
  if(r.k==='fecha')return estado.prox;
  var s=estado.sel[r.k];return r.v.every(function(x){return s.indexOf(x)>=0});
}
function pintaRapidos(){
  $('fm-rapidos').innerHTML=RAPIDOS.map(function(r,i){
    return '<li><button type="button" data-i="'+i+'" aria-pressed="false"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'+esc(r.t)+'</button></li>';
  }).join('');
}

/* ---------- dirección compartible ---------- */
function aURL(){
  var p=new URLSearchParams();
  if(estado.q)p.set('q',estado.q);
  FACETAS.forEach(function(F){if(estado.sel[F.k].length)p.set(F.k,estado.sel[F.k].join(','))});
  if(estado.prox)p.set('fecha','1');
  if(estado.lugares.length)p.set('ciudad',estado.lugares.join(','));
  if(estado.orden!=='fecha')p.set('orden',estado.orden);
  var s=p.toString();
  try{history.replaceState(null,'',location.pathname+(s?'?'+s:'')+location.hash)}catch(e){}
}
function deURL(){
  var p=new URLSearchParams(location.search),hay=false;
  estado.q=(p.get('q')||'').slice(0,80);estado.qn=norm(estado.q).split(/\s+/).filter(Boolean);
  FACETAS.forEach(function(F){estado.sel[F.k]=(p.get(F.k)||'').split(',').filter(Boolean);if(estado.sel[F.k].length)hay=true});
  estado.prox=p.get('fecha')==='1';
  estado.lugares=(p.get('ciudad')||'').split(',').filter(Boolean).map(function(c,i,a){
    if(LUG[c])return c;
    /* dirección antigua: «lat,lon» */
    var m=/^-?\d+(\.\d+)?$/.test(c)&&a[i+1]&&/^-?\d+(\.\d+)?$/.test(a[i+1])?[+c,+a[i+1]]:null,mejor='';
    if(m)lugares.forEach(function(l){if(Math.abs(l.lat-m[0])<.2&&Math.abs(l.lon-m[1])<.2)mejor=mejor||l.id});
    return mejor;
  }).filter(Boolean);
  var o=p.get('orden');if(['nombre','pais','duracion','precio'].indexOf(o)>=0)estado.orden=o;
  return hay||!!estado.q||estado.prox||estado.lugares.length>0;
}

/* ---------- pintar todo ---------- */
function calcula(){ultima=datos.filter(function(f){return pasa(f)});ordena(ultima)}
function pinta(foco,sinURL){
  calcula();
  pintaFacetas(foco);pintaLista();pintaEstado();
  if(!sinURL)aURL();
  if(globo.listo)globo.marca();
}
function limpia(){
  estado.q='';estado.qn=[];estado.prox=false;estado.lugares=[];
  FACETAS.forEach(function(F){estado.sel[F.k]=[]});
  $('fm-q').value='';$('fm-q-hero').value='';visibles=POR;
}
function alDirectorio(){
  var y=raiz.getBoundingClientRect().top+window.scrollY-70;
  window.scrollTo({top:y,behavior:reduce?'auto':'smooth'});
}
function atajo(a){
  limpia();
  if(a==='fecha')estado.prox=true;
  else{var p=a.split(':');if(FAC[p[0]])estado.sel[p[0]]=p[1].split(',')}
  pinta();alDirectorio();
}
function irAFicha(id){
  function busca(){for(var i=0;i<ultima.length;i++)if(ultima[i].id===id)return i;return -1}
  var i=busca();
  if(i<0){limpia();pinta();i=busca()}
  if(i<0)return;
  if(i>=visibles){visibles=Math.ceil((i+1)/POR)*POR;pintaLista()}
  var el=$('f-'+id);if(!el)return;
  el.scrollIntoView({behavior:reduce?'auto':'smooth',block:'center'});
  el.classList.remove('marca');void el.offsetWidth;el.classList.add('marca');
  var a=el.querySelector('.fm-f-nombre a');if(a)a.focus({preventScroll:true});
}

/* ---------- cifras, caminos y próximas fechas ---------- */
function sube(el,n){
  if(reduce||n<4||!('requestAnimationFrame' in window)){el.textContent=n;return}
  var t0=null;
  requestAnimationFrame(function paso(t){
    if(t0==null)t0=t;var k=Math.min(1,(t-t0)/800);
    el.textContent=Math.round(n*(1-Math.pow(1-k,3)));
    if(k<1)requestAnimationFrame(paso);
  });
}
function pintaCifras(){
  var es=datos.filter(function(f){return lista(f.idiomas).indexOf('es')>=0}).length;
  sube($('fm-c-total'),datos.length);
  sube($('fm-c-paises'),contar(datos,'pais'));
  sube($('fm-c-es'),es);
  sube($('fm-c-linea'),datos.filter(function(f){return f.modalidad==='en_linea'}).length);
  if(actualizado){$('fm-revisado').hidden=false;$('fm-revisado').innerHTML='Datos revisados el <time datetime="'+esc(actualizado)+'">'+esc(fecha(actualizado,{day:'numeric',month:'long',year:'numeric'}))+'</time>.'}
  [].forEach.call(document.querySelectorAll('[data-n]'),function(e){
    var p=e.getAttribute('data-n').split(':'),F=FAC[p[0]],n=0;
    if(F)datos.forEach(function(f){if(F.v(f).indexOf(p[1])>=0)n++});
    e.textContent=n;
    var li=e.closest('li');if(li&&e.tagName==='EM')li.hidden=!n;
  });
  var caja=$('fm-es');if(caja)caja.hidden=!es;
}
function pintaPronto(){
  var p=datos.filter(function(f){return f._prox}).sort(function(a,b){return a._prox-b._prox}).slice(0,4);
  var sec=$('pronto');if(!p.length){sec.hidden=true;return}
  sec.hidden=false;
  $('fm-citas').innerHTML=p.map(function(f){
    var mes=fecha(f.proxima,{month:'short'}).replace('.',''),anio=fecha(f.proxima,{year:'numeric'});
    return '<li><a class="fm-cita" href="#f-'+esc(f.id)+'" data-ficha="'+esc(f.id)+'">'
      +'<p class="fm-cita-fecha"><b>'+esc(fecha(f.proxima,{day:'numeric'}))+'</b><span>'+esc(mes)+'<i>'+esc(anio)+'</i></span></p>'
      +'<p class="tipo">'+esc(lista(f.tipo).map(function(x){return et('tipoCorto',x)}).join(' · '))+'</p>'
      +'<h3>'+esc(f.nombre)+'</h3>'
      +'<p class="ent">'+esc(f.entidad)+' · '+esc(f.modalidad==='en_linea'?nomPais(f.pais):(f.ciudad?f.ciudad+', ':'')+nomPais(f.pais))+'</p>'
      +'<span class="modo">'+esc(et('modoCorto',f.modalidad))+'</span></a></li>';
  }).join('');
}

/* ==========================================================================
   El globo
   ========================================================================== */
var globo=(function(){
  var caja=$('fm-globo'),mar=$('fm-mar'),lienzo=$('fm-lienzo'),capa=$('fm-pines'),rotulo=$('fm-rotulo'),tarjeta=$('fm-lugar'),nota=$('fm-mundo-nota'),chips=$('fm-regiones');
  var G=window.apderGeo,RAD=Math.PI/180,ZMAX=5,INICIO={lon:-58,lat:30,zoom:1};
  var api={listo:false,marca:function(){}};
  if(!caja||!lienzo)return api;
  var ctx=lienzo.getContext('2d'),S=0,R=0,dpr=1,proy=null,trazo=null;
  var vista={lon:INICIO.lon,lat:INICIO.lat,zoom:1},anim=0,volando=false;
  var tierra=null,fronteras=null,paises=[],reticula=null,reticulaFina=null,conDatos=null;
  var grupos=[],botones=[],region='',elegidos=[];

  function mide(){
    var r=mar.getBoundingClientRect();if(!r.width)return false;
    S=r.width;R=S/2;dpr=Math.min(2,window.devicePixelRatio||1);
    lienzo.width=Math.round(S*dpr);lienzo.height=Math.round(S*dpr);
    return true;
  }
  function dibuja(){
    if(!proy||!S)return;
    proy.translate([R,R]).scale(R*vista.zoom).rotate([-vista.lon,-vista.lat,0]);
    ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,S,S);
    ctx.save();ctx.beginPath();ctx.arc(R,R,R,0,7);ctx.clip();
    ctx.lineJoin='round';
    var ret=vista.zoom>1.8?reticulaFina:reticula;
    ctx.beginPath();trazo(ret);ctx.strokeStyle='rgba(255,255,255,.17)';ctx.lineWidth=1;ctx.stroke();
    ctx.beginPath();trazo(tierra);ctx.fillStyle='#eee3ce';ctx.fill();
    if(conDatos){ctx.beginPath();trazo(conDatos);ctx.fillStyle='#fcf8ef';ctx.fill()}
    ctx.save();ctx.beginPath();trazo(tierra);ctx.clip();
    ctx.beginPath();trazo(ret);ctx.strokeStyle='rgba(150,135,105,.16)';ctx.lineWidth=1;ctx.stroke();ctx.restore();
    ctx.beginPath();trazo(fronteras);ctx.strokeStyle='rgba(125,154,122,'+(vista.zoom<1.4?.3:.6)+')';ctx.lineWidth=vista.zoom<1.4?.6:.9;ctx.stroke();
    ctx.beginPath();trazo(tierra);ctx.strokeStyle='rgba(72,100,70,.5)';ctx.lineWidth=.9;ctx.stroke();
    ctx.restore();
    if(!volando)coloca();
  }

  /* grupos de ciudades según el aumento: lo que queda a menos de unos 30 px se junta */
  function agrupa(){
    var umbral=30/(R*vista.zoom||1);
    grupos=[];
    lugares.forEach(function(l){
      var mejor=null,dm=umbral;
      grupos.forEach(function(g){var d=G.geoDistance([l.lon,l.lat],[g.sem.lon,g.sem.lat]);if(d<dm){dm=d;mejor=g}});
      if(mejor)mejor.ls.push(l);else grupos.push({sem:l,ls:[l]});
    });
    grupos.forEach(function(g){
      var c=centro(g.ls);g.lon=c.lon;g.lat=c.lat;
      g.n=g.ls.reduce(function(s,l){return s+l.fs.length},0);
      g.id=g.ls.map(function(l){return l.id}).join(',');
    });
    capa.innerHTML=grupos.map(function(g,i){
      var t=g.ls.length===1?g.ls[0].nombre:g.ls.slice(0,2).map(function(l){return l.nombre}).join(', ')+(g.ls.length>2?' y '+plural(g.ls.length-2,'ciudad más','ciudades más'):'');
      return '<button type="button" class="fm-pin'+(g.n>1?' grupo':'')+(g.n>9?' g2':'')+'" data-g="'+i+'" style="--d:'+((i*.47)%3.2).toFixed(2)+'s" aria-label="'+esc(t)+': '+plural(g.n,'formación','formaciones')+'" hidden>'+(g.n>1?g.n:'')+'</button>';
    }).join('');
    botones=[].slice.call(capa.children);
    marca();
  }
  function centro(ls){
    var x=0,y=0,z=0;
    ls.forEach(function(l){var f=l.lat*RAD,a=l.lon*RAD;x+=Math.cos(f)*Math.cos(a);y+=Math.cos(f)*Math.sin(a);z+=Math.sin(f)});
    var lon=Math.atan2(y,x)/RAD,lat=Math.atan2(z,Math.sqrt(x*x+y*y))/RAD,dmax=0;
    ls.forEach(function(l){dmax=Math.max(dmax,G.geoDistance([l.lon,l.lat],[lon,lat]))});
    return{lon:lon,lat:lat,dmax:dmax};
  }
  function encuadre(ls,zmin,zmax){
    var c=centro(ls),z=c.dmax>.0015?.6/Math.sin(Math.min(c.dmax,1.3)):4;
    return{lon:c.lon,lat:c.lat,zoom:Math.max(zmin||1,Math.min(zmax||ZMAX,z))};
  }
  function seSepara(ls,z){
    var u=30/(R*z);
    for(var i=1;i<ls.length;i++)if(G.geoDistance([ls[0].lon,ls[0].lat],[ls[i].lon,ls[i].lat])>u)return true;
    return false;
  }
  function coloca(){
    var c=[vista.lon,vista.lat];
    grupos.forEach(function(g,i){
      var b=botones[i];if(!b)return;
      var ve=G.geoDistance([g.lon,g.lat],c)<1.42,p=ve?proy([g.lon,g.lat]):null;
      if(p){var dx=p[0]-R,dy=p[1]-R;ve=dx*dx+dy*dy<(R-5)*(R-5)}
      b.hidden=!ve;g.xy=ve?p:null;
      if(ve)b.style.transform='translate('+p[0].toFixed(1)+'px,'+p[1].toFixed(1)+'px)';
    });
  }
  function marca(){
    var sel={};elegidos.forEach(function(l){sel[l.id]=1});
    grupos.forEach(function(g,i){if(botones[i])botones[i].classList.toggle('activo',g.ls.some(function(l){return sel[l.id]}))});
  }

  /* movimiento */
  function vuela(dest,ms,fin){
    cancelAnimationFrame(anim);
    dest.lat=Math.max(-72,Math.min(80,dest.lat));
    if(reduce||!api.listo||!ms){vista.lon=dest.lon;vista.lat=dest.lat;vista.zoom=dest.zoom;volando=false;caja.classList.remove('vuela');agrupa();dibuja();botonesZoom();if(fin)fin();return}
    var ini={lon:vista.lon,lat:vista.lat,zoom:vista.zoom},inter=G.geoInterpolate([ini.lon,ini.lat],[dest.lon,dest.lat]),t0=null;
    var cambiaZoom=Math.abs(dest.zoom-ini.zoom)>.02;
    volando=true;if(cambiaZoom)caja.classList.add('vuela');
    anim=requestAnimationFrame(function paso(t){
      if(t0==null)t0=t;
      var k=Math.min(1,(t-t0)/ms),e=k<.5?4*k*k*k:1-Math.pow(-2*k+2,3)/2,p=inter(e);
      vista.lon=p[0];vista.lat=p[1];vista.zoom=ini.zoom+(dest.zoom-ini.zoom)*e;
      if(!cambiaZoom){volando=false;dibuja();volando=true}else dibuja();
      if(k<1)anim=requestAnimationFrame(paso);
      else{volando=false;caja.classList.remove('vuela');if(cambiaZoom)agrupa();dibuja();botonesZoom();if(fin)fin()}
    });
  }
  function botonesZoom(){
    var b=caja.querySelectorAll('[data-zoom]');
    if(b[0])b[0].disabled=vista.zoom>=ZMAX-.01;
    if(b[1])b[1].disabled=vista.zoom<=1.01;
  }
  function tocado(){caja.classList.add('tocado')}

  /* tarjeta del lugar */
  function linea(f){
    var p=[lista(f.tipo).map(function(x){return et('tipoCorto',x)}).join(' · '),et('modoCorto',f.modalidad)];
    if(f._prox)p.push('Empieza el '+fecha(f.proxima,{day:'numeric',month:'short',year:'numeric'}));
    return p.filter(Boolean).join(' · ');
  }
  function abreTarjeta(ls,foco){
    elegidos=ls;marca();
    var n=ls.reduce(function(s,l){return s+l.fs.length},0),uno=ls.length===1;
    var paisesT={};ls.forEach(function(l){paisesT[nomPais(l.pais)]=1});
    var h='<div class="fm-lugar-cab"><div><p class="fm-antetitulo">'+esc(uno&&ls[0].sinCiudad?'Sin ciudad indicada':Object.keys(paisesT).join(' · '))+'</p>'
      +'<p class="fm-lugar-tit" id="fm-lugar-tit" tabindex="-1">'+esc(uno?ls[0].nombre:ls[0].nombre+' y alrededores')+'</p></div>'
      +'<button type="button" class="fm-lugar-cierra" data-cierra-lugar aria-label="Cerrar">'+ICO.cerrar+'</button></div><ul>';
    ls.forEach(function(l){
      l.fs.forEach(function(f,i){
        h+='<li><a href="#f-'+esc(f.id)+'" data-ficha="'+esc(f.id)+'">'+(!uno&&i===0?'<span class="ciu">'+esc(l.nombre)+'</span>':'')
          +'<b>'+esc(f.nombre)+'</b><span>'+esc(linea(f))+'</span></a></li>';
      });
    });
    h+='</ul><div class="fm-lugar-pie"><button type="button" class="fm-enlace" data-ver-lugares="'+esc(ls.map(function(l){return l.id}).join(','))+'"><span>'+(n===1?'Verla en el directorio':'Ver las '+n+' en el directorio')+'</span>'+ICO.flecha+'</button></div>';
    tarjeta.innerHTML=h;tarjeta.hidden=false;caja.classList.add('con-tarjeta');
    tarjeta.style.animation='none';void tarjeta.offsetWidth;tarjeta.style.animation='';
    if(foco){var t=$('fm-lugar-tit');if(t)t.focus({preventScroll:true})}
  }
  function cierraTarjeta(foco){
    if(tarjeta.hidden)return;
    var ids=elegidos.map(function(l){return l.id});
    tarjeta.hidden=true;tarjeta.innerHTML='';elegidos=[];marca();caja.classList.remove('con-tarjeta');
    if(foco){var i=-1;grupos.forEach(function(g,j){if(g.ls.some(function(l){return ids.indexOf(l.id)>=0}))i=j});if(botones[i]&&!botones[i].hidden)botones[i].focus({preventScroll:true})}
  }
  function eligeGrupo(g,foco){
    tocado();
    if(g.ls.length>1){
      var e=encuadre(g.ls,1,ZMAX);
      if(e.zoom>vista.zoom*1.25&&seSepara(g.ls,e.zoom)){cierraTarjeta();vuela(e,800,function(){var b=botones[0];if(foco&&b)for(var i=0;i<botones.length;i++)if(!botones[i].hidden){botones[i].focus({preventScroll:true});break}});return}
    }
    abreTarjeta(g.ls,foco);
    var d=encuadre(g.ls,Math.max(vista.zoom,2.2),Math.max(vista.zoom,2.6));
    if(!estrecha.matches&&window.innerWidth>760)d.lat-=Math.asin(Math.min(.9,.4/d.zoom))/RAD;
    vuela(d,750);
  }

  /* regiones */
  function pintaRegiones(){
    var n={};datos.forEach(function(f){n[f._region]=(n[f._region]||0)+1});
    var h='<li><button type="button" data-region="" aria-pressed="'+(region?'false':'true')+'">Todo el mundo</button></li>';
    Object.keys(T.region).forEach(function(r){if(n[r])h+='<li><button type="button" data-region="'+r+'" aria-pressed="'+(region===r?'true':'false')+'">'+esc(et('regionCorta',r))+'<small>'+n[r]+'</small></button></li>'});
    chips.innerHTML=h;
    pintaNota(n);
  }
  function pintaNota(n){
    if(!n){n={};datos.forEach(function(f){n[f._region]=(n[f._region]||0)+1})}
    if(!region){nota.innerHTML=api.listo?'Cada punto es una ciudad con formaciones presenciales o mixtas. Elige uno para ver cuáles son.':'Elige una región para ver sus formaciones.';return}
    var ls=lugares.filter(function(l){return l.region===region}),pres=ls.reduce(function(s,l){return s+l.fs.length},0),tot=n[region]||0;
    nota.innerHTML='<strong>'+plural(tot,'formación','formaciones')+'</strong> en '+esc(et('regionCorta',region))
      +(pres?', '+(pres===tot?(tot===1?'presencial o mixta':'todas con parte presencial'):pres+' con parte presencial')+' en '+plural(ls.length,'ciudad','ciudades'):', todas en línea')
      +'. <button type="button" data-ver-region="'+region+'">Verlas en el directorio</button>';
  }
  function eligeRegion(r){
    region=r;tocado();cierraTarjeta();pintaRegiones();
    if(!proy)return;
    if(!r){vuela({lon:INICIO.lon,lat:INICIO.lat,zoom:1},900);return}
    var ls=lugares.filter(function(l){return l.region===r}),c=REG_CENTRO[r]||REG_CENTRO.otras;
    vuela(ls.length?encuadre(ls,1.15,2.6):{lon:c[0],lat:c[1],zoom:c[2]},900);
  }

  /* gestos */
  var pulsa=null;
  mar.addEventListener('pointerdown',function(e){
    if(!api.listo||e.button>0)return;
    cancelAnimationFrame(anim);if(volando){volando=false;caja.classList.remove('vuela');agrupa();dibuja()}
    pulsa={x:e.clientX,y:e.clientY,lon:vista.lon,lat:vista.lat,mov:false,id:e.pointerId};
  });
  window.addEventListener('pointermove',function(e){
    if(!pulsa||e.pointerId!==pulsa.id)return;
    var dx=e.clientX-pulsa.x,dy=e.clientY-pulsa.y;
    if(!pulsa.mov&&dx*dx+dy*dy<16)return;
    if(!pulsa.mov){pulsa.mov=true;caja.classList.add('arrastra');tocado();ocultaRotulo();try{mar.setPointerCapture(pulsa.id)}catch(err){}}
    var k=1/(R*vista.zoom*RAD);
    vista.lon=pulsa.lon-dx*k;vista.lat=Math.max(-72,Math.min(80,pulsa.lat+dy*k));
    if(vista.lon>180)vista.lon-=360;if(vista.lon<-180)vista.lon+=360;
    if(!pulsa.raf)pulsa.raf=requestAnimationFrame(function(){if(pulsa)pulsa.raf=0;dibuja()});
  });
  function suelta(e){
    if(!pulsa||(e&&e.pointerId!==pulsa.id))return;
    var mov=pulsa.mov;pulsa=null;caja.classList.remove('arrastra');
    if(mov){if(region){region='';pintaRegiones()}dibuja()}
    else if(e&&e.type==='pointerup'&&!tarjeta.hidden&&window.innerWidth>760)cierraTarjeta();
  }
  window.addEventListener('pointerup',suelta);window.addEventListener('pointercancel',suelta);
  mar.addEventListener('keydown',function(e){
    if(!api.listo)return;
    var paso=14/vista.zoom,d={ArrowLeft:[-paso,0],ArrowRight:[paso,0],ArrowUp:[0,paso],ArrowDown:[0,-paso]}[e.key];
    if(d){e.preventDefault();tocado();vuela({lon:vista.lon+d[0],lat:vista.lat+d[1],zoom:vista.zoom},180)}
    else if(e.key==='+'||e.key==='='){e.preventDefault();zoom(1)}
    else if(e.key==='-'){e.preventDefault();zoom(-1)}
  });
  function zoom(s){tocado();vuela({lon:vista.lon,lat:vista.lat,zoom:Math.max(1,Math.min(ZMAX,vista.zoom*(s>0?1.7:1/1.7)))},380)}

  /* rótulo al pasar por un punto */
  function muestraRotulo(b){
    var g=grupos[+b.dataset.g];if(!g||!g.xy)return;
    var t=g.ls.length===1?g.ls[0].nombre:g.ls[0].nombre+' y '+plural(g.ls.length-1,'ciudad más','ciudades más');
    rotulo.innerHTML=esc(t)+'<b>'+g.n+'</b>';
    var a=rotulo.offsetWidth,off=S*.04/.92,x=Math.max(-10,Math.min(S+2*off-a+10,g.xy[0]+off-a/2)),y=g.xy[1]+off-(g.n>1?22:14)-rotulo.offsetHeight;
    rotulo.style.transform='translate('+x.toFixed(0)+'px,'+y.toFixed(0)+'px)';rotulo.classList.add('ver');
  }
  function ocultaRotulo(){rotulo.classList.remove('ver')}
  capa.addEventListener('pointerover',function(e){var b=e.target.closest('.fm-pin');if(b&&e.pointerType!=='touch')muestraRotulo(b)});
  capa.addEventListener('pointerout',function(e){if(e.target.closest('.fm-pin'))ocultaRotulo()});
  capa.addEventListener('focusin',function(e){var b=e.target.closest('.fm-pin');if(b&&b.matches(':focus-visible'))muestraRotulo(b)});
  capa.addEventListener('focusout',ocultaRotulo);
  capa.addEventListener('click',function(e){
    var b=e.target.closest('.fm-pin');if(!b)return;
    ocultaRotulo();var g=grupos[+b.dataset.g];if(g)eligeGrupo(g,e.detail===0);
  });
  caja.addEventListener('click',function(e){var z=e.target.closest('[data-zoom]');if(z&&api.listo)zoom(+z.dataset.zoom)});
  chips.addEventListener('click',function(e){var b=e.target.closest('[data-region]');if(b)eligeRegion(b.dataset.region)});
  tarjeta.addEventListener('click',function(e){
    if(e.target.closest('[data-cierra-lugar]')){cierraTarjeta(true);return}
    var v=e.target.closest('[data-ver-lugares]');
    if(v){limpia();estado.lugares=v.dataset.verLugares.split(',');pinta();alDirectorio();return}
    var a=e.target.closest('[data-ficha]');if(a){e.preventDefault();irAFicha(a.dataset.ficha)}
  });
  tarjeta.addEventListener('keydown',function(e){if(e.key==='Escape'){e.stopPropagation();cierraTarjeta(true)}});
  nota.addEventListener('click',function(e){var b=e.target.closest('[data-ver-region]');if(b)atajo('region:'+b.dataset.verRegion)});

  api.regiones=pintaRegiones;
  api.marca=marca;
  api.inicia=function(mundo){
    if(!G||!mundo||!mide())return;
    try{
      proy=G.geoOrthographic().clipAngle(90).precision(.5);
      trazo=G.geoPath(proy,ctx);
      tierra=G.feature(mundo,mundo.objects.tierra);
      fronteras=G.feature(mundo,mundo.objects.fronteras);
      paises=G.feature(mundo,mundo.objects.paises).features;
      reticula=G.geoGraticule().step([20,20])();
      reticulaFina=G.geoGraticule().step([10,10])();
    }catch(e){proy=null;return}
    var con={};datos.forEach(function(f){con[f.pais]=1});
    var fs=paises.filter(function(p){return con[p.id]});
    conDatos=fs.length?{type:'FeatureCollection',features:fs}:null;
    api.listo=true;
    agrupa();
    var llega=!reduce&&caja.getBoundingClientRect().top<window.innerHeight;
    if(llega){vista.lon=INICIO.lon-42;dibuja();caja.classList.add('listo');vuela({lon:INICIO.lon,lat:INICIO.lat,zoom:1},1700)}
    else{dibuja();caja.classList.add('listo')}
    botonesZoom();pintaNota();
    if('ResizeObserver' in window)new ResizeObserver(function(){var a=S;if(mide()&&Math.abs(a-S)>.5){agrupa();dibuja()}else if(S)dibuja()}).observe(mar);
  };
  return api;
})();

/* ==========================================================================
   Eventos del directorio
   ========================================================================== */
var tq=0;
$('fm-q').addEventListener('input',function(){
  var v=this.value;clearTimeout(tq);
  tq=setTimeout(function(){estado.q=v.trim().slice(0,80);estado.qn=norm(estado.q).split(/\s+/).filter(Boolean);$('fm-q-hero').value=estado.q;visibles=POR;pinta()},160);
});
$('fm-busca-dir').addEventListener('submit',function(e){e.preventDefault();$('fm-q').blur()});
$('fm-busca-hero').addEventListener('submit',function(e){
  e.preventDefault();
  var v=$('fm-q-hero').value.trim().slice(0,80);
  estado.q=v;estado.qn=norm(v).split(/\s+/).filter(Boolean);$('fm-q').value=v;visibles=POR;pinta();alDirectorio();
});
$('fm-orden').addEventListener('change',function(){estado.orden=this.value;visibles=POR;pinta()});
$('fm-prox').addEventListener('change',function(){estado.prox=this.checked;visibles=POR;pinta()});
$('fm-facetas').addEventListener('change',function(e){
  var i=e.target;if(!i.matches('input[type=checkbox]'))return;
  var s=estado.sel[i.dataset.k],p=s.indexOf(i.value);
  if(i.checked&&p<0)s.push(i.value);else if(!i.checked&&p>=0)s.splice(p,1);
  visibles=POR;pinta('input[data-k="'+i.dataset.k+'"][value="'+(window.CSS&&CSS.escape?CSS.escape(i.value):i.value)+'"]');
});
$('fm-facetas').addEventListener('toggle',function(e){var d=e.target;if(d.matches&&d.matches('details'))abiertas[d.dataset.k]=d.open},true);
$('fm-facetas').addEventListener('click',function(e){
  var b=e.target.closest('.fm-mas-op');if(!b)return;
  verTodos[b.dataset.k]=!verTodos[b.dataset.k];pintaFacetas('.fm-mas-op[data-k="'+b.dataset.k+'"]');
});
$('fm-rapidos').addEventListener('click',function(e){
  var b=e.target.closest('button');if(!b)return;
  var r=RAPIDOS[+b.dataset.i],on=rapidoActivo(r);
  if(r.k==='fecha')estado.prox=!on;
  else{var s=estado.sel[r.k];r.v.forEach(function(x){var p=s.indexOf(x);if(on&&p>=0)s.splice(p,1);else if(!on&&p<0)s.push(x)})}
  visibles=POR;pinta();
});
$('fm-chips').addEventListener('click',function(e){
  var b=e.target.closest('[data-quita]');if(!b)return;
  var k=b.dataset.quita;
  if(k==='q'){estado.q='';estado.qn=[];$('fm-q').value='';$('fm-q-hero').value=''}
  else if(k==='prox')estado.prox=false;
  else if(k==='lugares')estado.lugares=[];
  else{var s=estado.sel[k],p=s.indexOf(b.dataset.v);if(p>=0)s.splice(p,1)}
  visibles=POR;pinta();
  var sig=$('fm-chips').querySelector('button')||$('fm-q');sig.focus({preventScroll:true});
});
raiz.addEventListener('click',function(e){
  if(e.target.closest('[data-limpiar],[data-limpiar-fijo]')){limpia();pinta();if(!$('fm-filtros').classList.contains('abierto'))$('fm-q').focus({preventScroll:true})}
});
$('fm-mas-btn').addEventListener('click',function(){var desde=visibles;visibles+=POR;pintaLista(desde)});
$('fm-todas').addEventListener('click',function(){var desde=visibles;visibles=ultima.length;pintaLista(desde)});
$('fm-copiar').addEventListener('click',function(){
  var b=this,t=b.querySelector('span'),antes=t.textContent,url=location.origin+location.pathname+location.search+'#directorio';
  function hecho(ok){t.textContent=ok?'Enlace copiado':'No se pudo copiar';setTimeout(function(){t.textContent=antes},2200)}
  if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(url).then(function(){hecho(true)},function(){hecho(false)});
  else hecho(false);
});
document.addEventListener('click',function(e){
  var a=e.target.closest('[data-atajo]');if(a){atajo(a.dataset.atajo);return}
  var c=e.target.closest('[data-camino]');if(c){atajo(c.dataset.camino);return}
  var f=e.target.closest('.fm-cita[data-ficha]');if(f){e.preventDefault();irAFicha(f.dataset.ficha)}
});

/* panel de filtros en pantallas estrechas */
var panel=$('fm-filtros'),abridor=null;
function abreFiltros(b){
  abridor=b||null;panel.classList.add('abierto');document.documentElement.classList.add('fm-sin-scroll');
  panel.setAttribute('role','dialog');panel.setAttribute('aria-modal','true');
  $('fm-cierra-filtros').focus({preventScroll:true});
}
function cierraFiltros(ir){
  if(!panel.classList.contains('abierto'))return;
  panel.classList.remove('abierto');document.documentElement.classList.remove('fm-sin-scroll');
  panel.removeAttribute('role');panel.removeAttribute('aria-modal');
  if(ir){var y=$('fm-estado').getBoundingClientRect().top+window.scrollY-80;window.scrollTo({top:y,behavior:'auto'})}
  if(abridor&&abridor.offsetParent)abridor.focus({preventScroll:true});else $('fm-abre-filtros').focus({preventScroll:true});
}
$('fm-abre-filtros').addEventListener('click',function(){abreFiltros(this)});
$('fm-flota').addEventListener('click',function(){abreFiltros(this)});
$('fm-cierra-filtros').addEventListener('click',function(){cierraFiltros(false)});
$('fm-ver').addEventListener('click',function(){cierraFiltros(true)});
panel.addEventListener('keydown',function(e){
  if(!panel.classList.contains('abierto'))return;
  if(e.key==='Escape'){e.preventDefault();cierraFiltros(false);return}
  if(e.key!=='Tab')return;
  var fs=[].filter.call(panel.querySelectorAll('button,input,summary,a[href]'),function(x){return x.offsetParent!==null&&!x.disabled});
  if(!fs.length)return;
  if(e.shiftKey&&document.activeElement===fs[0]){e.preventDefault();fs[fs.length-1].focus()}
  else if(!e.shiftKey&&document.activeElement===fs[fs.length-1]){e.preventDefault();fs[0].focus()}
});
function alCambiarAncho(){if(!estrecha.matches)cierraFiltros(false)}
if(estrecha.addEventListener)estrecha.addEventListener('change',alCambiarAncho);else if(estrecha.addListener)estrecha.addListener(alCambiarAncho);
var flota=$('fm-flota'),cuerpo=$('fm-cuerpo'),tf=false;
function miraFlota(){
  tf=false;
  var r=cuerpo.getBoundingClientRect();
  flota.classList.toggle('ver',estrecha.matches&&r.top<90&&r.bottom>window.innerHeight*.7&&!panel.classList.contains('abierto'));
}
window.addEventListener('scroll',function(){if(!tf){tf=true;requestAnimationFrame(miraFlota)}},{passive:true});
window.addEventListener('beforeprint',function(){if(visibles<ultima.length){visibles=ultima.length;pintaLista()}});

/* ---------- carga ---------- */
function pide(url){return fetch(url,{credentials:'same-origin'}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})}
var mundo=window.apderGeo?pide('mundo.json').catch(function(){return null}):Promise.resolve(null);
pide('formaciones.json').then(function(j){
  actualizado=j.actualizado||'';
  datos=lista(j.formaciones||j).filter(function(f){return f&&f.nombre&&f.url&&f.estado!=='retirada'});
  datos.forEach(prepara);
  creaLugares();
  pintaRapidos();
  var filtrado=deURL();
  $('fm-q').value=estado.q;$('fm-q-hero').value=estado.q;$('fm-orden').value=estado.orden;
  raiz.classList.add('cargado');
  pinta(null,true);
  pintaCifras();pintaPronto();globo.regiones();
  var h=location.hash;
  if(/^#f-/.test(h))setTimeout(function(){irAFicha(decodeURIComponent(h.slice(3)))},60);
  else if(filtrado&&!h)window.scrollTo({top:raiz.getBoundingClientRect().top+window.scrollY-70,behavior:'auto'});
  mundo.then(function(m){if(m)globo.inicia(m)});
}).catch(function(){
  $('fm-lista').innerHTML='<li class="fm-vacio"><b>No se ha podido cargar el directorio</b><p>Recarga la página o vuelve a intentarlo dentro de un momento.</p></li>';
});
})();
