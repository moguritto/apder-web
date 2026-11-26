# -*- coding: utf-8 -*-
"""Piezas compartidas de PsychonautWiki que las páginas llaman por nombre y cuyo texto no viene en las traducciones.

Se sacaron de la wiki el 25-11-2026 (API «expandtemplates», desde el navegador de Mannu) y las tradujo Claude.
Mismas reglas que el resto: sin cantidades de dosis, sin métodos de dosificación ni de administración.
Donde la pieza original daba una cifra o un método, se ha dejado fuera y se dice aquí, junto a la pieza.
{pagina} se sustituye por el nombre de la página que la llama.

Licencia del texto original: CC BY-SA 4.0 (PsychonautWiki). Esta traducción, la misma."""

# ------------------------------------------------------------------ avisos que abren una página
AVISOS = {
    "warning/25b-nboh": """'''La 25B-NBOH puede causar lesiones graves y la muerte.'''
Aunque no se han registrado muertes, es probable que comparta el perfil de toxicidad de la [[25B-NBOMe]], relacionada con varias muertes. Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarla]]. Más información en [[25B-NBOH#Toxicity and harm potential|este apartado]].""",
    "warning/25b-nbome": """'''La 25B-NBOMe puede ser mortal a dosis altas.'''
Se desaconseja con firmeza tomar cantidades grandes o [[Routes of administration|esnifarla]]. Más información en [[25B-NBOMe#Toxicity and harm potential|este apartado]].""",
    "warning/25c-nboh": """'''La 25C-NBOH puede causar lesiones graves o la muerte.'''
Aunque no se han registrado muertes, es probable que comparta el perfil de toxicidad de la [[25C-NBOMe]], relacionada con varias muertes. Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarla]]. Más información en [[25C-NBOH#Toxicity and harm potential|este apartado]].""",
    # El original añade la cantidad a partir de la cual se han dado muertes; se deja fuera (regla de dosis).
    "warning/25c-nbome": """'''La 25C-NBOMe puede ser mortal a dosis altas.'''
Se desaconseja con firmeza tomar cantidades grandes o [[Routes of administration|esnifarla]]. Más información en [[25C-NBOMe#Toxicity and harm potential|este apartado]].""",
    "warning/25e-nboh": """'''La 25E-NBOH puede causar lesiones graves o la muerte.'''
Aunque no se han registrado muertes, es probable que comparta el perfil de toxicidad de la [[25I-NBOMe]], relacionada con varias muertes. Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarla]].""",
    "warning/25i-nboh": """'''La 25I-NBOH puede causar lesiones graves o la muerte.'''
Aunque no se han registrado muertes, es probable que comparta el perfil de toxicidad de la [[25I-NBOMe]], relacionada con varias muertes. Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarla]]. Más información en [[25I-NBOH#Toxicity and harm potential|este apartado]].""",
    "warning/25i-nbome": """'''La 25I-NBOMe puede ser mortal a dosis altas.'''
Se desaconseja con firmeza tomar cantidades grandes o [[Routes of administration|esnifarla]]. Más información en [[25I-NBOMe#Toxicity and harm potential|este apartado]].""",
    "warning/25x-nboh": """'''Las sustancias de la [[25x-NBOH|serie NBOH]] pueden ser mortales con facilidad a dosis altas.'''
Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarlas]]. Más información en [[25x-NBOH#Toxicity and harm potential|este apartado]].""",
    "warning/25x-nbome": """'''Las sustancias de la [[NBOMe|serie NBOMe]] se han relacionado con numerosas sobredosis y muertes.'''
Se desaconseja con firmeza [[Routes of administration|esnifarlas]] o tomar dosis altas. Más información en [[25x-NBOMe#Toxicity and harm potential|este apartado]].""",
    "warning/2c-t-7": """'''La 2C-T-7 puede causar lesiones graves o la muerte si se esnifa o se combina con ciertas sustancias y medicamentos (por ejemplo, [[MAOIs|IMAO]] o [[RIMAs|IRMA]]).'''
Se desaconseja con firmeza esnifarla, calcular la cantidad a ojo, tomarla por una vía que no sea la oral o combinarla con [[2C-T-7#Dangerous interactions|otras sustancias]]. Más información en [[2C-T-7#Toxicity and harm potential|este apartado]].""",
    "warning/3-cmc": """'''La 3-CMC puede causar lesiones graves y la muerte.'''
Se han confirmado diez muertes por su consumo mediante análisis de muestras biológicas; seis fueron por policonsumo (alcohol, opioides, cannabinoides sintéticos y benzodiacepinas). Se desaconseja con firmeza tomar dosis altas o [[Routes of administration|esnifarla]].""",
    "warning/3-meo-pce": """'''La 3-MeO-PCE puede causar [[mania|manía]], [[delusions|delirios]] y [[psychosis|psicosis]] con más frecuencia que otros [[dissociatives|disociativos]].'''
Se desaconseja con firmeza tomarla en dosis altas, varios días seguidos o junto con otras sustancias que aumenten el riesgo de psicosis. Más información en [[3-MeO-PCE#Toxicity and harm potential|este apartado]].""",
    "warning/3-meo-pcp": """'''La 3-MeO-PCP puede causar [[mania|manía]], [[delusions|delirios]] y [[psychosis|psicosis]] con más probabilidad que otros [[dissociatives|disociativos]].'''
Se desaconseja con firmeza tomarla en dosis altas, varios días seguidos o junto con otras sustancias que aumenten el riesgo de psicosis. Más información en [[3-MeO-PCP#Toxicity and harm potential|este apartado]].""",
    "warning/5-meo-dmt": """'''Atención: la 5-MeO-DMT ''no'' es un sustituto de la DMT.'''
Aunque sus nombres se parezcan, la [[5-MeO-DMT]] y la [[DMT]] tienen efectos y riesgos distintos y deben considerarse sustancias completamente diferentes. Más información en [[5-MeO-DMT#Toxicity and harm potential|este apartado]].""",
    "warning/acetylfentanyl": """'''El acetilfentanilo puede causar la muerte si se combina con [[depressants|depresores]] como [[opiates|opiáceos]], [[benzodiazepines|benzodiacepinas]], [[barbiturates|barbitúricos]], [[gabapentinoids|gabapentinoides]], [[thienodiazepines|tienodiacepinas]] u otras [[GABA|sustancias gabaérgicas]].'''
Se desaconseja con firmeza combinar estas sustancias, sea cual sea la cantidad.""",
    "warning/barbiturates": """'''Los [[barbiturates|barbitúricos]] pueden causar la muerte si se combinan con [[depressants|depresores]] como [[opiates|opiáceos]], [[benzodiazepines|benzodiacepinas]], [[gabapentinoids|gabapentinoides]], [[thienodiazepines|tienodiacepinas]], [[alcohol]] u otras [[GABA|sustancias gabaérgicas]].'''
Se desaconseja con firmeza combinar estas sustancias, sobre todo en dosis moderadas o altas.""",
    "warning/belladonna": """'''La [[Atropa belladonna (Botany)|belladona]] provoca experiencias peligrosas y muy desagradables.'''
Si se prueba, hay que seguir prácticas de [[responsible use|uso responsable]] y contar siempre con un [[trip sitter|acompañante]].""",
    # El original da instrucciones de esterilización para inyectarla; se dejan fuera (administración).
    "warning/black tar heroin": """'''Inyectarse heroína «black tar» es peligroso.'''
No es posible esterilizarla en condiciones caseras, y su inyección se asocia a infecciones por ''Clostridium botulinum''. No se recomienda inyectarla en ningún caso.""",
    # El original nombra métodos de dosificación concretos; se dejan fuera.
    "warning/bromo-dragonfly": """'''La Bromo-DragonFLY se ha relacionado con un número inusualmente alto de hospitalizaciones y muertes.'''
Por su potencia extrema y sus efectos poco estudiados, se desaconseja con firmeza tomarla sin las mayores precauciones de [[harm reduction practices|reducción de riesgos]] y sin [[trip sitter|acompañante]]. Más información en [[Bromo-DragonFLY#Toxicity and harm potential|este apartado]].""",
    "warning/dxm&dph": """'''La combinación de DXM y DPH puede producir experiencias peligrosas, física y mentalmente, sobre todo a dosis altas.'''
Los efectos [[deliriant|delirantes]] y [[dissociative|disociativos]] de esta combinación son muy impredecibles y pueden llevar a conductas erráticas, autolesiones, efectos físicos como un aumento peligroso del pulso o de la tensión arterial, hospitalización o, en casos extremos, la muerte. Si se usa, hay que seguir prácticas de [[responsible use|reducción de riesgos]] y contar siempre con un [[trip sitter|acompañante]]. Más información en [[DXM & DPH#Toxicity and harm potential|este apartado]].""",
    "warning/datura": """'''La datura es extremadamente peligrosa y puede causar directamente lesiones graves o la muerte.'''
Es muy impredecible y su uso está muy relacionado con la [[psychosis|psicosis]], las lesiones graves y la muerte. Más información en [[Datura#Toxicity and harm potential|este apartado]].""",
    "warning/deliriants": """'''El uso de delirantes se asocia a experiencias muy desagradables o peligrosas.'''
Los [[deliriants|delirantes]] son muy impredecibles y pueden llevar a conductas erráticas, autolesiones, hospitalización o la muerte. La mayoría de las personas no quiere repetir la experiencia por lo desagradable que resulta. Si se usan, hay que seguir prácticas de [[responsible use|reducción de riesgos]] y contar siempre con un [[trip sitter|acompañante]]. Más información en [[Deliriants#Toxicity and harm potential|este apartado]].""",
    "warning/desoxypipradrol": """'''El desoxipipradrol provoca [[psychosis|psicosis]], [[mania|manía]] y [[addiction|adicción]] con bastante más frecuencia que otros estimulantes.'''
Por su vida media inusualmente larga y su potencia extrema, se desaconseja con firmeza tomarlo en dosis altas, varios días seguidos o junto con otras sustancias que aumenten el riesgo de psicosis. Más información en [[Desoxypipradrol#Toxicity and harm potential|este apartado]].""",
    "warning/diphenhydramine": """'''El uso de difenhidramina se asocia a experiencias muy desagradables o peligrosas.'''
Los [[deliriants|delirantes]] son muy impredecibles y pueden llevar a conductas erráticas, autolesiones, hospitalización o la muerte. La mayoría de las personas no quiere repetir la experiencia por lo desagradable que resulta. Si se usa, hay que seguir prácticas de [[responsible use|reducción de riesgos]] y contar siempre con un [[trip sitter|acompañante]]. Más información en [[DPH#Toxicity and harm potential|este apartado]].""",
    "warning/ephylone": """'''La efilona se ha relacionado con numerosas sobredosis y muertes.'''
Se desaconseja con firmeza usarla en dosis altas, varias veces seguidas o junto con otras sustancias que aumenten el riesgo de [[psychosis|psicosis]] o de [[serotonin syndrome|síndrome serotoninérgico]]. Más información en [[Ephylone#Toxicity and harm potential|este apartado]].""",
    # El original añade métodos de medida; se dejan fuera.
    "warning/fentanyl": """'''Esta sustancia es extraordinariamente potente: actúa en cantidades de microgramos. Por eso hay que manipularla con muchísimo cuidado y no calcular ''nunca'' la cantidad a ojo. El fentanilo también puede ser mortal combinado con [[depressants|depresores]] como [[opiates|opiáceos]], [[benzodiazepines|benzodiacepinas]], [[barbiturates|barbitúricos]], [[gabapentinoids|gabapentinoides]], [[thienodiazepines|tienodiacepinas]] u otras [[GABA|sustancias gabaérgicas]].'''
Se recomienda con firmeza manipularlo con guantes y no combinarlo con otros depresores.""",
    "warning/hyoscyamus_niger": """'''El [[Hyoscyamus niger (Botany)|beleño negro]] provoca experiencias peligrosas y muy desagradables.'''
Si se prueba, hay que seguir prácticas de [[responsible use|uso responsable]] y contar siempre con un [[trip sitter|acompañante]].""",
    "warning/ibogaine": """'''La ibogaína puede causar complicaciones cardiacas que ponen en peligro la vida.'''
No debe tomarse nunca sin un [[trip sitter|acompañante]] formado y un desfibrilador en funcionamiento disponibles en el mismo lugar para atender una emergencia, porque la reanimación cardiopulmonar rara vez basta para volver a poner en marcha el corazón. Además, deben evitarla por completo las personas con antecedentes personales o familiares de trastornos cardiacos (como el síndrome de QT largo, las arritmias o las cardiopatías), salvo que un cardiólogo lo haya valorado y lo autorice. Se desaconseja con firmeza usarla en dosis altas o varios días seguidos. Más información en [[Ibogaine#Toxicity and harm potential|este apartado]].""",
    "warning/inhalants": """'''No es nunca seguro ingerir inhalantes (salvo los alcoholes) ni inhalar gases comprimidos directamente. El uso médico breve y moderado de inhalantes administrados correctamente (como los nitritos de alquilo o «poppers», o el óxido nitroso con suplemento de vitamina B12 después) puede ser seguro. En cambio, los inhalantes que no son de uso médico (como la gasolina) son tóxicos: incluso una sola sesión puede causar la muerte súbita, y su uso frecuente puede causar encefalopatía crónica por disolventes y síndrome de abstinencia.'''
A diferencia de otras sustancias, el uso recreativo de disolventes volátiles no tiene una forma segura: sus efectos psicoactivos son inseparables del daño a nervios y órganos. Los aerosoles también pueden causar quemaduras por frío e hipoxia (falta de oxígeno). Se desaconseja con firmeza consumirlos, aunque sea para probar. Más información en [[Inhalants#Toxicity and harm potential|este apartado]].""",
    "warning/mandrake": """'''Las [[Mandragora (Botany)|mandrágoras]] son muy venenosas y provocan experiencias peligrosas y muy desagradables.'''
Si se prueba, hay que seguir prácticas de [[responsible use|uso responsable]] y contar siempre con un [[trip sitter|acompañante]].""",
    "warning/melatonin": """'''El uso prolongado de melatonina se ha asociado a insuficiencia cardiaca.'''
En una revisión a cinco años (130.828 personas, edad media de 55,7 años), quienes tomaban melatonina tenían entre 2 y 4 veces más probabilidades de ser hospitalizados (19,0 % frente a 6,6 %) o de morir (4,6 % frente a 2,7 %) por insuficiencia cardiaca. No se ha demostrado una relación causal, y estos datos se presentaron en un congreso de la American Heart Association, no en una revista científica con revisión por pares.""",
    "warning/mushroom hunting": """'''Buscar hongos psicoactivos en la naturaleza puede ser muy peligroso.'''
Hay que tener mucho cuidado, porque es fácil confundir hongos venenosos o mortales con otros comestibles.""",
    "warning/nitrous_oxide": """'''El óxido nitroso puede causar daños neurotóxicos irreversibles.'''
Su uso frecuente o crónico puede agotar la vitamina B12 y provocar daños nerviosos graves. Se recomienda tomar siempre un suplemento de vitamina B12 si se usa, con cualquier frecuencia, sobre todo quienes la absorben peor (por ejemplo, tras una resección intestinal, con enfermedad inflamatoria intestinal o con anemia perniciosa) y quienes la toman en menor cantidad, como las personas veganas y vegetarianas. Además, un uso inadecuado puede causar falta de oxígeno. Se recomienda seguir prácticas de [[harm reduction practices|reducción de riesgos]].""",
    "warning/pce": """'''La PCE puede causar [[psychosis|psicosis]] y [[mania|manía]] con bastante más frecuencia que otros disociativos.'''
Se desaconseja con firmeza usarla en dosis altas o varios días seguidos. Más información en [[PCP#Toxicity and harm potential|este apartado]].""",
    "warning/pcp": """'''La PCP puede causar [[psychosis|psicosis]] y [[mania|manía]] con bastante más frecuencia que otros disociativos.'''
Se desaconseja con firmeza usarla en dosis altas o varios días seguidos. Más información en [[PCP#Toxicity and harm potential|este apartado]].""",
    "warning/pma": """'''La PMA puede causar efectos que ponen en peligro la vida (como [[increased bodily temperature|hipertermia]] y [[serotonin syndrome|síndrome serotoninérgico]]) incluso a dosis moderadas.'''
Por eso se desaconseja con firmeza su uso. Como es un adulterante frecuente, se recomienda analizar siempre la [[MDMA]] con un [[reagent testing kits|kit de reactivos]] para descartar que contenga PMA. Más información en [[PMA#Toxicity and harm potential|este apartado]].""",
    "warning/peyoteharvesting": """'''Por favor, no recolectes peyote en su hábitat natural.'''
Las poblaciones silvestres de peyote disminuyen rápidamente por la recolección excesiva de personas no indígenas, y hoy es una especie amenazada. Quien quiera tomarlo puede recurrir a otros cactus con mescalina, como el [[San Pedro]] o la [[Peruvian Torch|antorcha peruana]].""",
    "warning/phalaris": """'''Algunas especies del género ''Phalaris'' pueden ser peligrosas y tóxicas.'''
Algunas contienen [[gramine|gramina]], que en ovejas puede causar daño cerebral, daño en otros órganos y en el sistema nervioso central, y la muerte.""",
    "warning/short-acting_intense_trips": """'''Con esta sustancia, que a menudo se fuma en dosis altas, se recomienda un [[trip sitter|acompañante]]. Los viajes breves e intensos pueden tener efectos secundarios mentales y físicos días después.'''
Lo abrumador de la experiencia suele pedir un tiempo de integración. Los efectos físicos, como cambios en la audición, pueden tardar dos días en notarse. Tomar otras sustancias sin dejar un descanso (dos días, más unos cuantos para recuperarse si se nota algún efecto) aumenta el riesgo de pasar un mal posviaje.""",
    # El original añade métodos de medida; se dejan fuera.
    "warning/sufentanil": """'''El sufentanilo es extraordinariamente potente: actúa en cantidades de microgramos, hasta el punto de que el polvo puro puede causar una sobredosis mortal si cae sobre la piel. Por eso no hay que calcular ''nunca'' la cantidad a ojo. También puede ser mortal combinado con [[depressants|depresores]] como [[opiates|opiáceos]], [[benzodiazepines|benzodiacepinas]], [[barbiturates|barbitúricos]], [[gabapentinoids|gabapentinoides]], [[thienodiazepines|tienodiacepinas]] u otras [[GABA|sustancias gabaérgicas]].'''
Se recomienda con firmeza manipularlo con guantes y no combinarlo con otros depresores.""",
    "warning/synthetic cannabinoids": """'''Cannabinoides sintéticos: más de 1.000 hospitalizaciones y 94 muertes relacionadas con tres de ellos.'''
Varios cannabinoides sintéticos suponen riesgos graves para la salud. Solo el MDMB-FUBINACA se ha relacionado con más de 1.000 hospitalizaciones y 40 muertes, sobre todo en Rusia y Bielorrusia. En Europa, el MDMB-CHMICA y el 5F-ADB causaron en conjunto 54 muertes entre 2014 y 2017.""",
    # El original aconseja tener a mano un medicamento; se deja fuera (consejo médico).
    "warning/tizanidine": """'''La tizanidina puede bajar la tensión arterial a niveles peligrosos en dosis excesivas.'''
Hay que tener mucho cuidado con las dosis altas, ''incluso con tolerancia''. A dosis alucinógenas conviene que haya alguien presente que supervise.""",
}

# Familias de depresores (aviso de sobredosis combinada).
DEPRESORES = [("opiates", "opiáceos"), ("benzodiazepines", "benzodiacepinas"), ("barbiturates", "barbitúricos"),
              ("gabapentinoids", "gabapentinoides"), ("thienodiazepines", "tienodiacepinas"), ("alcohol", "alcohol"),
              ("GABAergics", "otras sustancias gabaérgicas")]
NOMBRE_FAMILIA = {"opiates": ("opiates", "los opiáceos"), "benzodiazepines": ("benzodiazepines", "las benzodiacepinas"),
                  "barbiturates": ("barbiturates", "los barbitúricos"), "gabapentinoids": ("gabapentinoids", "los gabapentinoides"),
                  "thienodiazepines": ("thienodiazepines", "las tienodiacepinas"), "alcohol": ("alcohol", "el alcohol"),
                  "gabaergics": ("GABA", "las sustancias gabaérgicas")}


def depresor_od(familia):
    """Texto de {{DepressantOD|familia}}."""
    clave = (familia or "gabaergics").strip().lower()
    destino, nombre = NOMBRE_FAMILIA.get(clave, (familia, familia))
    otros = [es for en, es in DEPRESORES if en.lower() != clave]
    ultimo = otros[-1]
    y = " u " if ultimo[:1] in "oO" or ultimo[:2].lower() == "ho" else " o "
    lista = ", ".join(otros[:-1]) + y + ultimo if len(otros) > 1 else ultimo
    verbo = "se combina" if clave == "alcohol" else "se combinan"
    return ("\'\'\'Puede producirse una [[overdose|sobredosis]] mortal cuando [[%s|%s]] %s con otros "
            "[[depressants|depresores]], como %s.\'\'\'\n"
            "Se desaconseja con firmeza combinar estas sustancias, sobre todo en dosis habituales o altas." % (destino, nombre, verbo, lista))


# ------------------------------------------------------------------ textos fijos
PREAMBULO_EFECTOS = """'''''Aviso:''' los efectos que siguen remiten al [[Subjective effect index|índice de efectos subjetivos]], una base abierta de investigación hecha a partir de relatos de personas usuarias y del análisis personal de quienes colaboran en PsychonautWiki. Por eso conviene leerlos con un sano escepticismo.''

''Tampoco aparecen necesariamente de forma predecible ni fiable, aunque a dosis más altas es más probable que se den todos. Del mismo modo, a dosis más altas aumenta la probabilidad de '''efectos adversos''', entre ellos '''adicción, lesiones graves o la muerte'''.''"""

PREAMBULO_ESPIRITUAL = """Estos efectos son los más raros y los menos reproducibles de los que pueden darse en una experiencia [[psychedelic|psicodélica]]. Se consideran únicos porque tomar más cantidad no aumenta necesariamente la probabilidad de que aparezcan: dependen más del contexto, como la disposición y el entorno ([[set and setting]]), que de la sustancia o la dosis. En su forma más plena se les llama a veces experiencias «cumbre», «trascendentes» o «transformadoras», aunque también pueden darse en un plano conceptual o cognitivo y dejar una huella positiva duradera."""

INTERACCIONES_INTRO = """'''''Aviso:''' muchas sustancias psicoactivas razonablemente seguras por sí solas pueden volverse peligrosas, e incluso mortales, al combinarse con otras. La lista que sigue recoge algunas interacciones peligrosas conocidas, pero no garantiza incluirlas todas.''

''Antes de combinar dos o más sustancias, investiga siempre por tu cuenta (por ejemplo, en [https://pubmed.ncbi.nlm.nih.gov/ PubMed]) si la combinación es segura. Algunas de estas interacciones proceden de [https://combo.tripsit.me TripSit].''"""

ESBOZO = {
    "toxicity": "Este apartado sobre toxicidad está incompleto en la wiki original y puede contener información incompleta o incluso peligrosamente errónea. Investiga siempre por tu cuenta y sigue prácticas de [[responsible drug use|reducción de riesgos]].",
    "chemistry": "Este apartado sobre química está incompleto en la wiki original.",
    "pharmacology": "Este apartado sobre farmacología está incompleto en la wiki original.",
    "dangerousinteractions": "Este apartado sobre interacciones peligrosas está incompleto en la wiki original y puede contener información incompleta o errónea.",
}

# ------------------------------------------------------------------ listas de interacciones peligrosas
_PSICOD_ESTIM = "Los efectos ansiógenos y de concentración de los estimulantes aumentan la probabilidad de entrar en [[thought loops|bucles de pensamiento]] desagradables. La combinación suele ser innecesaria, porque los psicodélicos ya estimulan, y la suma de estimulación puede resultar incómoda."
_MAOB_FEN = "Los inhibidores de la MAO-B pueden aumentar la potencia y la duración de las fenetilaminas de forma impredecible"
_IMAO_OPIO = "La combinación de inhibidores de la monoaminooxidasa (IMAO) con ciertos opioides se ha asociado a casos raros de reacciones adversas graves, algunas mortales. Parece haber dos tipos de interacción, una excitatoria y otra depresora. Los síntomas de la excitatoria pueden incluir agitación, dolor de cabeza, sudoración intensa, fiebre muy alta, rubor, escalofríos, mioclonías, rigidez, temblor, diarrea, hipertensión, taquicardia, convulsiones y coma. Ha habido muertes."
_POMELO = "Aunque el pomelo no es psicoactivo, puede alterar el metabolismo de algunos opioides. El tramadol, la oxicodona y el fentanilo se metabolizan sobre todo por la enzima CYP3A4, que el zumo de pomelo inhibe con fuerza. Eso puede hacer que el fármaco tarde más en eliminarse y aumentar su toxicidad con tomas repetidas. La metadona también puede verse afectada. La codeína y la hidrocodona se metabolizan por la CYP2D6: quien toma medicamentos que inhiben esa enzima, o carece de ella por una variante genética, no responde a la codeína, porque no puede transformarla en su producto activo, la morfina."
_GHB_OPIO = "Las dos sustancias se potencian mutuamente con fuerza y de forma impredecible, y llevan muy rápido a la pérdida de conciencia. Inconsciente, hay riesgo de aspirar el vómito si no se coloca a la persona en la [[recovery position|posición lateral de seguridad]]."
_ALC_OPIO = "Ambas sustancias potencian la ataxia y la sedación de la otra y, a dosis altas, pueden provocar una pérdida de conciencia inesperada. Hay que colocar a la persona afectada en la [[recovery position|posición lateral de seguridad]] para evitar que aspire el vómito. Son probables las lagunas de memoria."
_BENZO_OPIO = "Los efectos depresores del sistema nervioso central o de la respiración pueden sumarse o potenciarse. Las dos sustancias se potencian mutuamente con fuerza y de forma impredecible, y llevan muy rápido a la pérdida de conciencia. Inconsciente, hay riesgo de aspirar el vómito si no se coloca a la persona en la [[recovery position|posición lateral de seguridad]]; son probables las lagunas de memoria."
_NITROSO_OPIO = "Ambas sustancias potencian la ataxia y la sedación de la otra y, a dosis altas, pueden provocar una pérdida de conciencia inesperada. Inconsciente, hay riesgo de aspirar el vómito si no se coloca a la persona en la [[recovery position|posición lateral de seguridad]]. Las lagunas de memoria son frecuentes."
_TRAMADOL_OPIO = "Aumenta el riesgo de convulsiones. El tramadol puede provocarlas por sí mismo y sumar su efecto sobre el umbral convulsivo al de otros opioides. Los efectos depresores del sistema nervioso central o de la respiración pueden sumarse o potenciarse."
_IMAO_NT = "Esta combinación puede elevar neurotransmisores como %s hasta niveles peligrosos o incluso mortales. Son ejemplos la [[syrian rue|ruda siria]], la [[banisteriopsis caapi|''Banisteriopsis caapi'']] y algunos [[antidepressants|antidepresivos]]."

INTERACCIONES = {
    "dangerousinteractions/2c-x": """*'''[[5-MeO-xxT]]''' - Los psicodélicos 5-MeO pueden interactuar de forma impredecible y potenciar a otros psicodélicos.
*'''[[Amphetamines|Anfetaminas]]''' - %(e)s
*'''[[Cannabis]]''' - El cannabis tiene una sinergia fuerte e inestable con los psicodélicos. Aunque a menudo se usa para intensificar o alargar sus efectos, la combinación aumenta el riesgo de efectos psicológicos adversos como [[anxiety|ansiedad]], [[paranoia]], ataques de pánico y [[psychosis|psicosis]]. Hay muchos relatos en los que el cannabis desencadena un mal viaje o una psicosis. Se aconseja precaución.
*'''[[Cocaine|Cocaína]]''' - %(e)s
*'''[[MAOIs|IMAO]]''' - %(m)s.
*'''[[NBOMe|NBOMes]]''' - Las NBOMe y las NBOH pueden causar vasoconstricción y estimulación. La combinación suele ser innecesaria, porque los psicodélicos (en especial la serie 2C-x) ya estimulan, y la suma puede resultar incómoda.
*'''[[Tramadol]]''' - El tramadol baja el umbral convulsivo, y los psicodélicos aumentan el riesgo de convulsiones.
*'''[[AMT|aMT]]'''""" % {"e": _PSICOD_ESTIM, "m": _MAOB_FEN},
    "dangerousinteractions/5-meo-xxt": """*'''[[2C-T-x|2C-T-X]]''' - Las dos clases de compuestos pueden ser impredecibles por sí solas.
*'''[[2C-x|2C-X]]''' - Los psicodélicos 5-MeO pueden interactuar de forma impredecible y potenciar a otros psicodélicos.
*'''[[Cannabis]]''' - Puede aumentar el riesgo de efectos psicológicos negativos como [[anxiety|ansiedad]], [[paranoia]] y [[psychosis|psicosis]].
*'''[[DOx]]''' - Las triptaminas 5-MeO pueden ser impredecibles en sus interacciones, sobre todo por el aumento del riesgo de efectos físicos desagradables.
*'''[[MDMA]]''' - Algunas triptaminas 5-MeO son algo impredecibles y deben combinarse con MDMA con cuidado.
*'''[[Mescaline|Mescalina]]''' - Las triptaminas 5-MeO pueden ser impredecibles en sus interacciones.
*'''[[NBOMe]]''' - Las triptaminas 5-MeO pueden ser impredecibles en sus interacciones, y las NBOMe lo son incluso solas. Es mejor evitar esta combinación.
*'''[[Amphetamines|Anfetaminas]]''' - Los efectos ansiógenos y de concentración de los estimulantes aumentan la probabilidad de entrar en bucles de pensamiento desagradables. La combinación suele ser innecesaria, porque los psicodélicos ya estimulan.
*'''[[Cocaine|Cocaína]]''' - Los efectos ansiógenos y de concentración de los estimulantes aumentan la probabilidad de entrar en bucles de pensamiento desagradables. La combinación suele ser innecesaria, porque los psicodélicos ya estimulan.
*'''[[DXM]]''' - Hay poca información sobre esta combinación.
*'''[[Tramadol]]''' - Aumenta el riesgo de [[serotonin syndrome|síndrome serotoninérgico]].
*'''[[AMT|aMT]]''' - Aumenta el riesgo de [[serotonin syndrome|síndrome serotoninérgico]].
*'''[[MAOIs|IMAO]]''' - Aumenta el riesgo de [[serotonin syndrome|síndrome serotoninérgico]].
*'''[[PCP]]''' - Hay poca información sobre esta combinación. Puede aumentar el riesgo de psicosis y de estimulación excesiva.""",
    "dangerousinteractions/amphetamines": """*'''[[Alcohol]]''' - Beber alcohol con estimulantes es arriesgado porque reduce los efectos sedantes del alcohol, que el cuerpo usa para calibrar la embriaguez. Eso suele llevar a beber en exceso con la desinhibición muy aumentada, lo que eleva el riesgo de daño hepático y de deshidratación. Los estimulantes también permiten seguir bebiendo más allá del punto en que normalmente uno perdería el conocimiento, lo que aumenta el riesgo. Si se combinan, conviene fijar de antemano un límite de bebida por hora y respetarlo, teniendo en cuenta que se notarán menos el alcohol y el estimulante.
*'''[[GHB]]'''/'''[[GBL]]''' - Los estimulantes aceleran la respiración, lo que permite tomar más sedante. Si el estimulante se pasa antes, los efectos depresores del GHB/GBL pueden imponerse y causar una parada respiratoria.
*'''[[Opioids|Opioides]]''' - Los estimulantes aceleran la respiración, lo que permite tomar más opiáceo. Si el estimulante se pasa antes, el opiáceo puede imponerse y causar una parada respiratoria.
*'''[[Cocaine|Cocaína]]''' - La cocaína y la anfetamina actúan sobre el transportador de dopamina por mecanismos opuestos, y la anfetamina revierte los efectos gratificantes de la cocaína. La combinación tiene efectos cardiacos: las anfetaminas suelen subir la tensión arterial, y esta mezcla puede aumentar el riesgo de síncope por alteraciones del flujo sanguíneo en las válvulas del corazón.
*'''[[Cannabis]]''' - Los estimulantes aumentan la [[anxiety|ansiedad]] y el riesgo de [[thought loops|bucles de pensamiento]] y de [[paranoia]], lo que puede llevar a experiencias negativas.
*'''[[Caffeine|Cafeína]]''' - Combinar estimulantes suele ser innecesario y puede forzar el corazón, además de causar ansiedad y malestar físico.
*'''[[Tramadol]]''' - El tramadol y los estimulantes aumentan los dos el riesgo de convulsiones.
*'''[[DXM]]''' - Ambas sustancias aceleran el pulso; en casos extremos, los ataques de pánico que provocan han desembocado en problemas cardiacos más graves.
*'''[[Ketamine|Ketamina]]''' - Combinar anfetamina y ketamina puede producir cuadros psicóticos parecidos a la esquizofrenia, aunque se discute si son peores que los que produce cada sustancia por separado. La anfetamina sola puede causar grandiosidad, paranoia o delirios somáticos; la ketamina, trastornos del pensamiento, alteración de las funciones ejecutivas y delirios. Juntas, cabe esperar sobre todo trastornos del pensamiento con síntomas positivos.
*'''[[PCP]]''' - Aumenta el riesgo de taquicardia, hipertensión y estados maníacos.
*'''[[Methoxetamine|Metoxetamina]]''' - Aumenta el riesgo de taquicardia, hipertensión y estados maníacos.
*'''[[Psychedelics|Psicodélicos]]''' (por ejemplo, '''''[[LSD]], [[mescaline|mescalina]], [[psilocybin|psilocibina]]''''') - Aumenta el riesgo de [[anxiety|ansiedad]], [[paranoia]] y [[thought loops|bucles de pensamiento]].
**'''[[25x-NBOMe]]''' - Las anfetaminas y las NBOMe estimulan mucho; juntas pueden causar taquicardia, hipertensión, vasoconstricción y, en casos extremos, insuficiencia cardiaca. Los efectos ansiógenos y de concentración de los estimulantes tampoco combinan bien con los psicodélicos, porque pueden llevar a bucles de pensamiento desagradables. Las NBOMe pueden causar convulsiones, y los estimulantes aumentan ese riesgo.
**'''[[2C-T-x]]''' - Se sospecha que tienen propiedades IMAO leves. Puede aumentar el riesgo de crisis hipertensiva.
**'''[[5-MeO-xxT]]''' - Se sospecha que tienen propiedades IMAO leves. Puede aumentar el riesgo de crisis hipertensiva.
**'''[[DOx]]'''
*'''[[AMT|aMT]]''' - La aMT tiene propiedades IMAO que pueden interactuar mal con las anfetaminas.
*'''[[MAOIs|IMAO]]''' - %(m)s. Los inhibidores de la MAO-A con anfetamina pueden provocar crisis hipertensivas.""" % {"m": _MAOB_FEN},
    "dangerousinteractions/cannabis": """*'''[[2C-T-x]]'''
*'''[[2C-x]]'''
*'''[[5-MeO-xxT]]'''
*'''[[Amphetamines|Anfetaminas]]''' - Los estimulantes aumentan la ansiedad y el riesgo de bucles de pensamiento, lo que puede llevar a experiencias negativas.
*'''[[AMT|aMT]]'''
*'''[[Cocaine|Cocaína]]''' - Los estimulantes aumentan la ansiedad y el riesgo de bucles de pensamiento, lo que puede llevar a experiencias negativas.
*'''[[DMT]]'''
*'''[[DOx]]'''
*'''[[Lithium|Litio]]''' - El litio se receta a menudo para el trastorno bipolar, pero hay muchos relatos que indican que tomarlo con cannabinoides aumenta mucho el riesgo de psicosis y de convulsiones. Por eso esta combinación debe evitarse por completo.
*'''[[LSD]]'''
*'''[[Mescaline|Mescalina]]'''
*'''[[Psilocybin mushrooms|Setas de psilocibina]]'''
*'''[[25x-NBOMe]]'''""",
    "dangerousinteractions/depressants": """*'''[[Depressants|Depresores]]''' (''[[1,4-Butanediol|1,4-butanodiol]], [[2M2B]], [[alcohol]], [[benzodiazepines|benzodiacepinas]], [[barbiturates|barbitúricos]], [[GHB]]/[[GBL]], [[methaqualone|metacualona]], [[opioids|opioides]]'') - Esta combinación potencia la [[muscle relaxation|relajación muscular]], la [[amnesia]], la [[sedation|sedación]] y la [[respiratory depression|depresión respiratoria]] que causa cada uno. A dosis altas puede provocar una pérdida de conciencia repentina e inesperada con una depresión respiratoria peligrosa. También aumenta el riesgo de asfixiarse con el propio vómito estando inconsciente. Si aparecen [[nausea|náuseas]] o vómitos antes de perder el conocimiento, hay que intentar dormirse en la [[recovery position|posición lateral de seguridad]] o pedir a alguien que te coloque así.
*'''[[Dissociatives|Disociativos]]''' - Esta combinación puede potenciar de forma impredecible la [[amnesia]], la [[sedation|sedación]], la [[motor control loss|pérdida de control motor]] y los [[delusions|delirios]] que causa cada uno. También puede provocar una pérdida de conciencia repentina con una [[respiratory depression|depresión respiratoria]] peligrosa. Si aparecen [[nausea|náuseas]] o vómitos antes de perder el conocimiento, hay que intentar dormirse en la [[recovery position|posición lateral de seguridad]] o pedir a alguien que te coloque así.
*'''[[Stimulants|Estimulantes]]''' - Los estimulantes enmascaran la [[sedation|sedación]] de los depresores, que es lo que la mayoría de la gente usa para calibrar lo intoxicada que está. Cuando el estimulante se pasa, los efectos del depresor aumentan mucho, con más [[disinhibition|desinhibición]], [[motor control loss|pérdida de control motor]] y estados peligrosos de [[amnesia|lagunas]]. La combinación también puede causar una deshidratación grave si no se vigila lo que se bebe. Si se combinan, hay que fijar de antemano cuánto se toma por hora y un máximo, y respetarlos.""",
    "dangerousinteractions/dissociatives": """*'''[[Depressants|Depresores]]''' (por ejemplo, '''''[[2M2B]], [[alcohol]], [[barbiturates|barbitúricos]], [[benzodiazepines|benzodiacepinas]], [[GHB]]/[[GBL]], [[methaqualone|metacualona]], [[opioids|opioides]]''''') - Esta combinación potencia la [[muscle relaxation|relajación muscular]], la [[amnesia]], la [[sedation|sedación]] y la [[respiratory depression|depresión respiratoria]] que causa cada uno y, a dosis altas, puede provocar una pérdida de conciencia repentina con una respiración peligrosamente deprimida. También aumenta el riesgo de vomitar estando inconsciente y morir asfixiado. Si aparecen [[nausea|náuseas]] o vómitos antes de perder el conocimiento, hay que intentar dormirse en la [[recovery position|posición lateral de seguridad]] o pedir a alguien que te coloque así.
*'''[[Stimulants|Estimulantes]]''' (por ejemplo, '''''[[amphetamine|anfetamina]], [[cocaine|cocaína]], [[methylphenidate|metilfenidato]], [[MDMA]]''''') - Esta combinación puede potenciar los efectos [[anxiety|ansiógenos]], [[mania|maníacos]], [[delusion|delirantes]] y [[disinhibition|desinhibidores]] de los disociativos, sobre todo de los que apenas reducen el movimiento, como la [[ketamine|ketamina]]. La suma aumenta la probabilidad de una crisis de ansiedad, de delirios o de un [[psychosis|episodio psicótico]]. Hay indicios de que la combinación aumenta además su neurotoxicidad.{{citation needed}} También se cuenta a menudo que empeora la bajada.
*'''[[Dissociatives|Disociativos]]''' (por ejemplo, '''''[[dextromethorphan|dextrometorfano]], [[ketamine|ketamina]], [[methoxetamine|metoxetamina]], [[PCP]]''''') - La combinación puede potenciar de forma impredecible la [[amnesia]], la [[sedation|sedación]], la [[motor control loss|pérdida de control motor]] y los [[delusions|delirios]]. También puede provocar una pérdida de conciencia repentina con una [[respiratory depression|depresión respiratoria]] peligrosa. Si aparecen [[nausea|náuseas]] o vómitos antes de perder el conocimiento, hay que intentar dormirse en la [[recovery position|posición lateral de seguridad]] o pedir a alguien que te coloque así.""",
    "dangerousinteractions/dissos": """*'''[[Stimulants|Estimulantes]]''' - Estimulantes y disociativos tienen riesgo de reacciones psicológicas adversas como [[anxiety|ansiedad]], [[mania|manía]], [[delusions|delirios]] y [[psychosis|psicosis]], y ese riesgo aumenta al combinarlos.
*'''[[Depressants|Depresores]]''' - Como ambos deprimen la respiración, la combinación aumenta el riesgo de perder el conocimiento de repente, vomitar y morir asfixiado. Si aparecen [[nausea|náuseas]] o vómitos, hay que intentar dormirse en la [[recovery position|posición lateral de seguridad]] o pedir a alguien que te coloque así.""",
    "dangerousinteractions/maois": """*'''[[2C-T-x]]''' - %(m)s, lo que puede ser peligroso dado lo impredecible de la serie 2C-T-x.
*'''[[2C-x]]''' - %(m)s.
*'''[[DOx]]''' - %(m)s.
*'''[[Ketamine|Ketamina]]''' - Los inhibidores de la MAO-B parecen aumentar la potencia de la ketamina. Con los inhibidores de la MAO-A hay algunos relatos negativos, pero poca información.
*'''[[Mescaline|Mescalina]]'''
*'''[[NBOMe|NBOMes]]''' - %(m)s.
*'''[[Opioids|Opioides]]''' - %(o)s
*'''[[Alcohol]]''' - La tiramina de muchas bebidas alcohólicas puede reaccionar peligrosamente con los IMAO y subir la tensión arterial.
*'''[[MXE]]''' - Los inhibidores de la MAO-B parecen aumentar la potencia de la MXE. Con los inhibidores de la MAO-A hay algunos relatos negativos, pero poca información.
*'''[[5-MeO-xxT]]'''
*'''[[Amphetamines|Anfetaminas]]''' - %(m)s. Los inhibidores de la MAO-A con anfetamina pueden provocar crisis hipertensivas.
*'''[[AMT|aMT]]''' - La aMT ya es un IMAO por sí misma. Usar inhibidores enzimáticos reduce mucho la previsibilidad de los efectos.
*'''[[Cocaine|Cocaína]]''' - Combinación poco explorada.
*'''[[DXM]]''' - Riesgo alto de síndrome serotoninérgico.
*'''[[MDMA]]''' - %(m)s. Los inhibidores de la MAO-A con MDMA provocan crisis hipertensivas.
*'''[[PCP]]''' - Combinación muy poco explorada.
*'''[[SSRIs|ISRS]]'''
*'''[[Tramadol]]'''""" % {"m": _MAOB_FEN, "o": _IMAO_OPIO},
    "dangerousinteractions/maoi|nt=dopamine": "*'''[[MAOIs|IMAO]]''' - " + _IMAO_NT % "la dopamina",
    "dangerousinteractions/maoi|nt=serotonin and dopamine": "*'''[[MAOIs|IMAO]]''' - " + _IMAO_NT % "la serotonina y la dopamina",
    "dangerousinteractions/maoi|nt=serotonin": "*'''[[MAOIs|IMAO]]''' - " + _IMAO_NT % "la serotonina",
    "dangerousinteractions/nbome": """Por lo impredecible de la serie NBOMe, en general se aconseja no mezclarlas con otras sustancias psicoactivas.
*'''[[2C-T-x|2C-T-X]]''' - Las fenetilaminas 2C-T-X pueden ser impredecibles en sus interacciones, y las NBOMe lo son incluso solas. Por eso esta combinación debe evitarse.
*'''[[5-MeO-xxT]]''' - Las triptaminas 5-MeO pueden ser impredecibles en sus interacciones, y las NBOMe lo son incluso solas. Por eso esta combinación debe evitarse.
*'''[[Amphetamines|Anfetaminas]]''' - Las anfetaminas y las NBOMe estimulan mucho; juntas pueden causar taquicardia, hipertensión, vasoconstricción y, en casos extremos, insuficiencia cardiaca. Los efectos ansiógenos y de concentración de los estimulantes tampoco combinan bien con los psicodélicos, porque pueden llevar a bucles de pensamiento desagradables. Las NBOMe pueden causar convulsiones, y los estimulantes aumentan ese riesgo.
*'''[[AMT|aMT]]'''
*'''[[Caffeine|Cafeína]]''' - La cafeína puede acentuar la estimulación propia de los psicodélicos hasta hacerla incómoda. En cantidad, puede causar una ansiedad difícil de llevar durante el viaje.
*'''[[Cannabis]]''' - El cannabis tiene una sinergia fuerte e impredecible con los psicodélicos. Se aconseja precaución, porque puede aumentar mucho el riesgo de reacciones psicológicas adversas como [[anxiety|ansiedad]], [[paranoia]], [[panic attacks|ataques de pánico]] y [[psychosis|psicosis]]. Se recomienda empezar con mucho menos cannabis de lo habitual y espaciar mucho las caladas.
*'''[[Cocaine|Cocaína]]''' - La cocaína y las NBOMe estimulan mucho; juntas pueden causar vasoconstricción grave, taquicardia, hipertensión y, en casos extremos, insuficiencia cardiaca.
*'''[[DOx]]'''
*'''[[DXM]]'''
*'''[[Lithium|Litio]]''' - El litio se receta a menudo para el trastorno bipolar. Hay muchos relatos que indican que tomarlo con psicodélicos aumenta mucho el riesgo de [[psychosis|psicosis]] y de [[seizures|convulsiones]]. Por eso se desaconseja por completo.
*'''[[MAOIs|IMAO]]''' - %(m)s.
*'''[[MDMA]]'''
*'''[[MXE]]''' - Como antagonista NMDA, la MXE potencia las NBOMe, lo que puede resultar desagradablemente intenso.
*'''[[Tramadol]]''' - El tramadol baja el umbral convulsivo, y las NBOMe también tienden a causar convulsiones graves.""" % {"m": _MAOB_FEN},
    "dangerousinteractions/opioids": """*'''[[Alcohol]]''' - %(alc)s
*'''[[Stimulants|Estimulantes]]''' - Los estimulantes aceleran la respiración, lo que permite tomar más opiáceo del que se tomaría de otro modo. Si el estimulante se pasa antes, el opiáceo puede imponerse y causar una parada respiratoria.
*'''[[Benzodiazepines|Benzodiacepinas]]''' - %(benzo)s
*'''[[DXM]]''' - Se considera en general tóxica. Se han observado depresión del sistema nervioso central, dificultad para respirar, problemas cardiacos y toxicidad hepática. Además, el DXM reduce un poco la tolerancia a los opiáceos, lo que suma efectos.
*'''[[GHB]]'''/'''[[GBL]]''' - %(ghb)s
*'''[[Ketamine|Ketamina]]''' - Las dos sustancias pueden causar vómitos y pérdida de conciencia. Si la persona pierde el conocimiento, hay un riesgo grave de que aspire el vómito si no se la coloca en la [[recovery position|posición lateral de seguridad]].
*'''[[MAOIs|IMAO]]''' - %(imao)s
*'''[[MXE]]''' - La MXE puede potenciar los opioides, pero también aumenta el riesgo de depresión respiratoria y de toxicidad en los órganos.
*'''[[Nitrous|Óxido nitroso]]''' - %(nit)s
*'''[[PCP]]''' - La PCP puede reducir la tolerancia a los opioides y aumentar así el riesgo de sobredosis.
*'''[[Tramadol]]''' - %(tram)s
*'''[[Grapefruit|Pomelo]]''' - %(pom)s""" % {"alc": _ALC_OPIO, "benzo": _BENZO_OPIO, "ghb": _GHB_OPIO, "imao": _IMAO_OPIO, "nit": _NITROSO_OPIO, "tram": _TRAMADOL_OPIO, "pom": _POMELO},
    "dangerousinteractions/phenylpropylamineopioids": """*'''[[Amphetamines|Anfetaminas]]''' - Los estimulantes aumentan la actividad de la dopamina, la noradrenalina y la serotonina. Como el tramadol inhibe la recaptación de serotonina y noradrenalina y además libera algo de serotonina, mezclarlos puede causar síndrome serotoninérgico.
*'''[[Cocaine|Cocaína]]''' - Los estimulantes aumentan la actividad de la dopamina, la noradrenalina y la serotonina. Como el tramadol inhibe la recaptación de serotonina y noradrenalina y además libera algo de serotonina, mezclarlos puede causar síndrome serotoninérgico.
*'''[[DXM]]''' - El dextrometorfano inhibe la recaptación de serotonina. Como el tramadol inhibe la recaptación de serotonina y noradrenalina y además libera algo de serotonina, combinarlos causa síndrome serotoninérgico.
*'''[[GHB]]'''/'''[[GBL]]''' - %(ghb)s
*'''[[MAOIs|IMAO]]''' - %(imao)s
*'''[[Benzodiazepines|Benzodiacepinas]]''' - %(benzo)s
*'''[[MXE]]''' - La MXE puede potenciar los opioides, pero también aumenta el riesgo de depresión respiratoria y de toxicidad en los órganos.
*'''[[Alcohol]]''' - %(alc)s
*'''[[Nitrous|Óxido nitroso]]''' - %(nit)s
*'''[[Tramadol]]''' - %(tram)s
*'''[[Grapefruit|Pomelo]]''' - %(pom)s""" % {"alc": _ALC_OPIO, "benzo": _BENZO_OPIO, "ghb": _GHB_OPIO, "imao": _IMAO_OPIO, "nit": _NITROSO_OPIO, "tram": _TRAMADOL_OPIO, "pom": _POMELO},
    "dangerousinteractions/psychedelics": """*'''[[Lithium|Litio]]''' - El litio se receta a menudo para el trastorno bipolar. Hay muchos relatos que indican que tomarlo con [[psychedelics|psicodélicos]] aumenta mucho el riesgo de [[psychosis|psicosis]] y de [[seizures|convulsiones]]. Por eso se desaconseja por completo.
*'''[[Cannabis]]''' - El cannabis puede tener una sinergia fuerte e impredecible con los efectos de {pagina}. Se aconseja precaución, porque puede aumentar mucho el riesgo de reacciones psicológicas adversas como [[anxiety|ansiedad]], [[paranoia]], [[panic attacks|ataques de pánico]] y [[psychosis|psicosis]]. Se recomienda empezar con mucho menos cannabis de lo habitual y espaciar mucho las caladas.
*'''[[Stimulants|Estimulantes]]''' - Estimulantes como la [[amphetamine|anfetamina]], la [[cocaine|cocaína]] o el [[methylphenidate|metilfenidato]] actúan en muchas zonas del cerebro y alteran la función [[dopamine|dopaminérgica]]. La combinación puede aumentar el riesgo de [[anxiety|ansiedad]], [[paranoia]], [[panic attacks|ataques de pánico]] y [[thought loops|bucles de pensamiento]], y también de [[mania|manía]] y [[psychosis|psicosis]].{{citation needed}}
*'''[[Tramadol]]''' - Está bien documentado que el tramadol baja el umbral convulsivo, y los [[psychedelics|psicodélicos]] pueden desencadenar convulsiones en personas predispuestas.{{citation needed}}""",
    "dangerousinteractions/serotoninsyndrome": """Las combinaciones con las sustancias siguientes pueden elevar la [[serotonin|serotonina]] a niveles peligrosos. El [[serotonin syndrome|síndrome serotoninérgico]] necesita atención médica inmediata y puede ser mortal si no se trata.
*'''[[MAOIs|IMAO]]''' - Como la [[banisteriopsis caapi|''Banisteriopsis caapi'']], la [[syrian rue|ruda siria]], la fenelzina, la selegilina y la moclobemida.
*'''[[Serotonin releasers|Liberadores de serotonina]]''' - Como la [[MDMA]], la [[4-FA]], la [[methamphetamine|metanfetamina]], la [[methylone|metilona]] y la [[AMT|αMT]].
*'''[[SSRIs|ISRS]]''' - Como el citalopram y la sertralina.
*'''[[SNRIs|IRSN]]''' - Como el [[tramadol]] y la venlafaxina.
*'''[[5-HTP]]'''""",
    "dangerousinteractions/stimulants": """*'''[[25x-NBOMe]] y [[25x-NBOH]]''' - Los compuestos 25x estimulan mucho y fuerzan el cuerpo. Las combinaciones con {pagina} deben evitarse por completo por el riesgo de [[stimulation|estimulación]] excesiva y de sobrecarga cardiaca, que puede causar [[increased blood pressure|subida de la tensión arterial]], [[vasoconstriction|vasoconstricción]], ataques de pánico, [[thought loops|bucles de pensamiento]], [[seizures|convulsiones]] y, en casos extremos, insuficiencia cardiaca.
*'''[[Alcohol]]''' - Combinar alcohol con [[stimulants|estimulantes]] puede ser peligroso por el riesgo de intoxicarse sin darse cuenta. Los estimulantes enmascaran los efectos [[depressant|depresores]] del alcohol, que es lo que la mayoría de la gente usa para calibrar su embriaguez. Cuando el estimulante se pasa, los efectos depresores quedan sin freno, lo que puede causar lagunas y una [[respiratory depression|depresión respiratoria]] grave. Si se mezclan, hay que limitarse estrictamente a una cantidad de alcohol por hora.
*'''[[DXM]]''' - Deben evitarse, porque el DXM inhibe la recaptación de [[serotonin|serotonina]] y [[norepinephrine|noradrenalina]]. Aumenta el riesgo de [[panic attacks|ataques de pánico]] y de crisis hipertensiva, o de [[serotonin syndrome|síndrome serotoninérgico]] con liberadores de serotonina ([[MDMA]], [[methylone|metilona]], [[mephedrone|mefedrona]], etc.). Hay que vigilar la tensión arterial y evitar el ejercicio intenso.
*'''[[MDMA]]''' - Los posibles efectos neurotóxicos de la MDMA probablemente aumentan con otros [[stimulants|estimulantes]]. También hay riesgo de tensión arterial excesiva y de sobrecarga cardiaca (cardiotoxicidad).
*'''[[MXE]]''' - Algunos relatos indican que la combinación con MXE puede subir peligrosamente la tensión arterial y aumentar el riesgo de [[mania|manía]] y [[psychosis|psicosis]].
*'''[[Dissociatives|Disociativos]]''' - Ambas clases tienen riesgo de [[delusions|delirios]], [[mania|manía]] y [[psychosis|psicosis]], y ese riesgo puede multiplicarse al combinarlas.
*'''[[Stimulants|Estimulantes]]''' - Combinar {pagina} con otros [[stimulants|estimulantes]] como la [[cocaine|cocaína]] puede ser peligroso, porque pueden subir el [[increased heart rate|pulso]] y la [[increased blood pressure|tensión arterial]] a niveles peligrosos.
*'''[[Tramadol]]''' - El tramadol baja el umbral convulsivo, y combinarlo con estimulantes puede aumentar ese riesgo.""",
}

# Las claves se comparan con espacios, como las escribe la wiki al llamarlas («Short-acting intense trips»).
AVISOS = {k.replace("_", " "): v for k, v in AVISOS.items()}
