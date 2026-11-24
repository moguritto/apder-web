# «Quién es quién» · tanda 2 (parte A). Datos verificados el 23-11-2026; fuentes al final de cada ficha.
from contenido import r, rr

HUXLEY = {
    "slug": "aldous-huxley", "nombre": "Aldous Huxley", "iniciales": "AH", "anio": 1894,
    "que": "el escritor de Las puertas de la percepción",
    "tarjeta": "Escritor británico. Contó su experiencia con mescalina en 1953.",
    "desc": ("Aldous Huxley, el escritor que probó la mescalina en 1953 y escribió Las puertas de la percepción: "
             "su vida, su mirada y por dónde empezar a leerle."),
    "alias": "Escritor y pensador (Godalming, 1894 – Los Ángeles, 1963)",
    "entrada": ("Un novelista conocido por <em>Un mundo feliz</em> que, en 1953, tomó mescalina bajo la mirada de un "
                "psiquiatra y contó lo que vio de una manera que cambió la conversación sobre estas medicinas."),
    "tipo": "Pensamiento y espiritualidad",
    "nacio_iso": "1894-07-26", "murio_iso": "1963-11-22", "lugar": "Reino Unido",
    "datos": [("Nació", "26 de julio de 1894, en el Reino Unido"),
              ("Murió", "22 de noviembre de 1963, en Los Ángeles"),
              ("Ámbito", "literatura y filosofía de la experiencia"),
              ("Le debemos", "<em>Las puertas de la percepción</em> y <em>Cielo e infierno</em>")],
    "titulos": {"aportaciones": "Lo que escribió", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un escritor británico, autor de <em>Un mundo feliz</em> (1932), que vivió en California "
                      "desde hacía años y se interesaba por la mística y la percepción." + r(1)),
        ("Por qué importa", "A comienzos de mayo de 1953 tomó 0,4 g de mescalina en su casa de Los Ángeles, con el "
                            "psiquiatra Humphry Osmond a su lado, y lo contó en <em>Las puertas de la percepción</em>."
                            + rr(2, 3)),
        ("Su mirada", "Propuso, tomando una idea de Bergson, que el cerebro funciona como una válvula que reduce "
                      "lo que percibimos para que podamos vivir." + r(1)),
        ("Por dónde empezar", "<em>Las puertas de la percepción</em> y, para su visión final, la novela <em>La isla</em>. "
                              "Ambos están en la Biblioteca."),
    ],
    "vida": f"""<p>Aldous Huxley nació el 26 de julio de 1894 en el Reino Unido y se hizo famoso como novelista y ensayista. En 1932 publicó <em>Un mundo feliz</em>, una de las distopías más leídas del siglo XX.{r(1)} Con los años se fue interesando por la filosofía perenne, la mística y las técnicas para ampliar la percepción, y se instaló en California.</p>
<p>En 1953 Humphry Osmond, un psiquiatra que investigaba la mescalina, accedió a acompañarle en una primera experiencia. Osmond dudó, porque temía pasar a la historia como el médico que volvió loco al novelista. Aun así, a principios de mayo de ese año (las fuentes dan el día 4 o el 5), Huxley tomó 0,4 g de mescalina en su casa de Los Ángeles.{rr(2, 3)} Fue el principio de una relación de años con estas experiencias, que incluyó el LSD en 1955, de la mano de Al Hubbard.{r(2)}</p>
<p>Desde 1960 tuvo cáncer. El 22 de noviembre de 1963, el mismo día del asesinato de Kennedy, murió en Los Ángeles. Según se cuenta, ese día pidió por escrito a su esposa Laura una dosis de LSD de 100 µg por vía intramuscular.{rr(4, 5)}</p>""",
    "aportaciones": f"""<h3>Las puertas de la percepción (1954)</h3>
<p>El breve ensayo en el que cuenta su experiencia con la mescalina. El título viene de un verso de William Blake. Osmond aparece en el texto simplemente como «el investigador».{r(2)} Fue, para muchos lectores, la primera descripción literaria de lo que puede abrir una medicina psicodélica.</p>
<h3>Cielo e infierno (1956)</h3>
<p>La continuación: Huxley explora cómo la misma experiencia puede abrir hacia lo luminoso o hacia lo oscuro y relaciona las visiones con el arte y con las tradiciones religiosas.{r(2)}</p>
<h3>La isla (1962)</h3>
<p>Su última novela imagina una sociedad utópica en la que se usa una medicina llamada «moksha» para ayudar a la gente a crecer y a morir mejor. Es, quizá, su manera de decir cómo le gustaría que estas experiencias encontraran un lugar en la vida de una comunidad.{r(2)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas y nuestra lectura. No son hechos comprobados.</em></p>
<p>Huxley tomó de Henri Bergson la idea de que el cerebro es una «válvula reductora»: filtra la inmensidad de lo que podríamos percibir para dejarnos pasar solo lo útil para sobrevivir. La mescalina, en su descripción, abriría un poco esa válvula. Es una imagen sugerente y debatida: es una metáfora más que un hallazgo científico.{r(1)}</p>
<p>Desde la psicología transpersonal, su figura es una puerta de entrada: un hombre muy culto que se tomó la experiencia interior como un asunto serio y la unió a la tradición mística de oriente y occidente. También tuvo críticos. El estudioso R. C. Zaehner, en <em>Mysticism Sacred and Profane</em> (1957), discutió que una experiencia con una sustancia fuera equiparable a una experiencia mística.{r(6)}</p>""",
    "cronologia": [
        ("1894", "Nace el 26 de julio en el Reino Unido."),
        ("1932", "Publica <em>Un mundo feliz</em>."),
        ("1953", "A principios de mayo, mescalina en su casa de Los Ángeles, con Humphry Osmond."),
        ("1954", "Publica <em>Las puertas de la percepción</em>."),
        ("1955", "Primera experiencia con LSD, con Al Hubbard."),
        ("1956", "Publica <em>Cielo e infierno</em>."),
        ("1962", "Publica <em>La isla</em>."),
        ("1963", "Muere en Los Ángeles el 22 de noviembre."),
    ],
    "libros": [
        ("the-doors-of-perception", "El relato de su experiencia con la mescalina."),
        ("heaven-and-hell", "Su segundo ensayo sobre la visión y el arte."),
        ("island", "Su novela utópica, con la medicina «moksha»."),
        ("moksha", "Sus escritos sobre psicodélicos reunidos."),
        ("the-perennial-philosophy-739", "Su antología de la filosofía perenne."),
        ("un-mundo-feliz-745", "La novela que le dio fama."),
    ],
    "relacion": [
        ("../../sustancias/mescalina/", "Guía de la mescalina", "La sustancia de su primera experiencia."),
        ("../humphry-osmond/", "Humphry Osmond", "El psiquiatra que le acompañó en 1953."),
        ("../../sustancias/lsd/", "Guía del LSD", "La que probó en 1955."),
    ],
    "refs": [
        'Erowid. «Aldous Huxley», Erowid Character Vaults. <a href="https://erowid.org/culture/characters/huxley_aldous/">https://erowid.org/culture/characters/huxley_aldous/</a>',
        'The MIT Press Reader. Sobre Huxley y la mescalina. <a href="https://thereader.mitpress.mit.edu/?p=8222">https://thereader.mitpress.mit.edu/?p=8222</a>',
        'British Psychological Society. «Looking back: a brief history of psychedelic psychiatry». <a href="https://bps.org.uk/psychologist/looking-back-brief-history-psychedelic-psychiatry">https://bps.org.uk/psychologist/looking-back-brief-history-psychedelic-psychiatry</a>',
        'Erowid. Artículo sobre Laura Huxley. <a href="https://erowid.org/characters/huxley_laura/huxley_laura_article1.shtml">https://erowid.org/characters/huxley_laura/huxley_laura_article1.shtml</a>',
        'JSTOR Daily. «When Aldous Huxley dropped acid». <a href="https://daily.jstor.org/when-aldous-huxley-dropped-acid/">https://daily.jstor.org/when-aldous-huxley-dropped-acid/</a>',
        'Zaehner RC. <em>Mysticism Sacred and Profane</em>. Oxford: Clarendon Press; 1957.',
    ],
}

OSMOND = {
    "slug": "humphry-osmond", "nombre": "Humphry Osmond", "iniciales": "HO", "anio": 1917,
    "que": "el psiquiatra que inventó la palabra «psicodélico»",
    "tarjeta": "Psiquiatra británico. Acuñó el término «psicodélico».",
    "desc": ("Humphry Osmond, el psiquiatra que acuñó la palabra «psicodélico», investigó el LSD en Canadá y "
             "acompañó la mescalina de Huxley: vida, aportaciones y lecturas."),
    "alias": "Psiquiatra (Surrey, 1917 – Appleton, 2004)",
    "entrada": ("Trabajó con LSD y mescalina en un hospital de Saskatchewan, acompañó a Aldous Huxley en 1953 y "
                "puso nombre a la familia de sustancias: «psicodélico», lo que manifiesta la mente."),
    "tipo": "Psicología y terapia",
    "nacio_iso": "1917-07-01", "murio_iso": "2004-02-06", "lugar": "Surrey, Reino Unido",
    "datos": [("Nació", "1 de julio de 1917, Surrey (Reino Unido)"),
              ("Murió", "6 de febrero de 2004, Appleton (Wisconsin)"),
              ("Ámbito", "psiquiatría"),
              ("Le debemos", "la palabra «psicodélico» y los primeros estudios de LSD y alcoholismo")],
    "titulos": {"aportaciones": "Lo que aportó", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un psiquiatra británico que se formó en el Guy's Hospital de Londres y trabajó como "
                      "psiquiatra de la Marina en la Segunda Guerra Mundial." + r(1)),
        ("Por qué importa", "En 1951 se trasladó con John Smythies al hospital de Weyburn (Saskatchewan, Canadá), "
                            "donde estudió el LSD y la mescalina; en una carta a Huxley (1956) propuso la palabra "
                            "«psicodélico»." + rr(1, 2)),
        ("Su mirada", "Cuidó el ambiente de la sesión y llegó a ver el hospital como un diseño que podía ayudar "
                      "o dañar: lo llamó «socioarquitectura»." + r(1)),
        ("Por dónde empezar", "<em>Psychedelics</em> y <em>The Hallucinogens</em>, ambos en la Biblioteca."),
    ],
    "vida": f"""<p>Humphry Osmond nació el 1 de julio de 1917 en Surrey (Reino Unido). Estudió Medicina en el Guy's Hospital y, durante la Segunda Guerra Mundial, fue psiquiatra de la Marina.{r(1)} En 1951 se trasladó con John Smythies al hospital de Weyburn, en Saskatchewan (Canadá), donde fue director clínico y después superintendente. Allí trabajó con Abram Hoffer.{rr(1, 2)}</p>
<p>En 1953 supervisó la primera experiencia con mescalina de <a href="../aldous-huxley/">Aldous Huxley</a>. Después siguieron los años de Nueva Jersey y, más tarde, la Universidad de Alabama en Birmingham. Murió en Appleton (Wisconsin) el 6 de febrero de 2004, a los 86 años.{rr(1, 4)}</p>""",
    "aportaciones": f"""<h3>La palabra «psicodélico»</h3>
<p>Osmond la propuso en una carta a Huxley en 1956 y la presentó en público en una reunión de la Academia de Ciencias de Nueva York en 1957. Significa «que manifiesta la mente» y buscaba un nombre más neutral que «psicotomimético», que daba a entender que estas sustancias solo imitaban la locura.{rr(3, 4)}</p>
<h3>El LSD y el alcoholismo</h3>
<p>En Saskatchewan, entre 1954 y 1960, casi 2.000 personas con alcoholismo recibieron LSD en un entorno cuidado. Sus equipos comunicaron que entre un 40 % y un 45 % seguían sin beber al cabo de un año. Un metaanálisis posterior, de Krebs y Johansen (2012), encontró que una dosis de LSD se asocia a un menor consumo problemático de alcohol, aunque los estudios de entonces tenían limitaciones de método.{rr(2, 5)}</p>
<h3>Cuidar el lugar y el ambiente</h3>
<p>Con Al Hubbard aprendió a cuidar el ambiente de la sesión, y de ahí vino su interés por cómo los edificios influyen en quienes los habitan. Llamó a esa mirada «socioarquitectura» y convirtió el hospital en un laboratorio de diseño.{r(1)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas y nuestra lectura. No son hechos comprobados.</em></p>
<p>Osmond defendía que lo que se vive en una sesión depende de la persona, de la preparación y del lugar. Esa idea conecta con lo que la psicología humanista llama presencia y encuentro: cuidar las condiciones para que algo pueda ocurrir, sin forzarlo.</p>
<p>Conviene leer sus resultados con cautela. Los estudios de los años cincuenta no seguían los métodos actuales (no había grupos de control comparables ni seguimiento independiente), de modo que sus cifras son un punto de partida, no una prueba.</p>""",
    "cronologia": [
        ("1917", "Nace el 1 de julio en Surrey (Reino Unido)."),
        ("1951", "Llega con John Smythies al hospital de Weyburn (Saskatchewan)."),
        ("1953", "Supervisa la mescalina de Aldous Huxley."),
        ("1954–1960", "Casi 2.000 personas con alcoholismo reciben LSD en Saskatchewan."),
        ("1956", "En una carta a Huxley propone la palabra «psicodélico»."),
        ("1957", "La presenta en público en la Academia de Ciencias de Nueva York."),
        ("2004", "Muere el 6 de febrero en Appleton (Wisconsin)."),
    ],
    "libros": [
        ("the-hallucinogens", "Con Abram Hoffer: el estudio de referencia de su época."),
        ("psychedelics", "Una recopilación de textos de los primeros años."),
        ("how-to-live-with-schizophrenia-764", "Con Abram Hoffer, su libro sobre la esquizofrenia."),
    ],
    "relacion": [
        ("../aldous-huxley/", "Aldous Huxley", "El escritor al que acompañó en 1953."),
        ("../../sustancias/lsd/", "Guía del LSD", "La sustancia de sus estudios en Saskatchewan."),
        ("../../investigacion-terapeutica/", "Investigación", "Qué dice hoy la investigación con psicodélicos."),
    ],
    "refs": [
        'Smythies J. Obituario de Humphry Osmond. <em>BMJ</em>. 2004. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC381240/">https://pmc.ncbi.nlm.nih.gov/articles/PMC381240/</a>',
        'The Canadian Encyclopedia. «Psychedelic research in 1950s Saskatchewan». <a href="https://thecanadianencyclopedia.ca/en/article/psychedelic-research-in-1950s-saskatchewan">https://thecanadianencyclopedia.ca/en/article/psychedelic-research-in-1950s-saskatchewan</a>',
        'New York Academy of Sciences. Sobre la reunión de 1957. <a href="https://www.nyas.org/?p=14936">https://www.nyas.org/?p=14936</a>',
        'Erowid. «Humphry Osmond», Erowid Character Vaults. <a href="https://erowid.org/characters/osmond_humphry/osmond_humphry.shtml">https://erowid.org/characters/osmond_humphry/osmond_humphry.shtml</a>',
        'Krebs TS, Johansen PØ. Lysergic acid diethylamide (LSD) for alcoholism: meta-analysis of randomized controlled trials. <em>J Psychopharmacol</em>. 2012;26(7):994-1002. doi:<a href="https://doi.org/10.1177/0269881112439253">10.1177/0269881112439253</a>.',
    ],
}

WASSON = {
    "slug": "valentina-y-gordon-wasson", "nombre": "Valentina y Gordon Wasson", "iniciales": "W", "anio": 1898,
    "que": "el matrimonio que dio a conocer al mundo los hongos sagrados",
    "tarjeta": "Pediatra y banquero. Dieron a conocer los hongos sagrados de México.",
    "desc": ("Valentina y Gordon Wasson, el matrimonio que dio a conocer los hongos sagrados de México y acuñó "
             "«enteógeno»: su vida, sus aportaciones y sus sombras."),
    "alias": "Pediatra y banquero (ella, Moscú, 1901 – 1958; él, Montana, 1898 – Connecticut, 1986)",
    "entrada": ("Ella, médica rusa, recogía setas desde niña; él, banquero de Nueva York, las temía. De esa "
                "diferencia nació una investigación que llegó hasta la sierra Mazateca."),
    "tipo": "Ciencia",
    "nacio_iso": "1898-09-22", "murio_iso": "1986-12-23", "lugar": "Great Falls, Montana",
    "ld_personas": [
        {"name": "Gordon Wasson", "birthDate": "1898-09-22", "deathDate": "1986-12-23",
         "birthPlace": "Great Falls, Montana", "description": "banquero y etnomicólogo"},
        {"name": "Valentina Pávlovna Wasson", "birthDate": "1901", "deathDate": "1958-12-31",
         "birthPlace": "Moscú", "description": "pediatra y etnomicóloga"},
    ],
    "datos": [("Valentina", "Moscú, 1901 – 31 de diciembre de 1958"),
              ("Gordon", "Great Falls (Montana), 22 de septiembre de 1898 – Danbury (Connecticut), 23 de diciembre de 1986"),
              ("Ámbito", "etnomicología"),
              ("Les debemos", "dar a conocer los hongos sagrados mazatecos y la palabra «enteógeno»")],
    "titulos": {"aportaciones": "Lo que hicieron", "mirada": "Luces y sombras"},
    "claves": [
        ("Quiénes fueron", "Valentina, pediatra nacida en Moscú, y Gordon, banquero de J. P. Morgan. Se casaron "
                           "en 1926 y se interesaron por el papel de los hongos en las culturas." + rr(1, 2)),
        ("Por qué importan", "En 1955 participaron en una velada con <a href=\"../maria-sabina/\">María Sabina</a>. "
                             "Su relato en <em>Life</em>, en 1957, dio a conocer los hongos al público." + rr(3, 4)),
        ("Su legado", "Además, dieron nombre a una forma de ver estas medicinas: la palabra «enteógeno» se "
                      "propuso en 1979 con su colaboración." + r(5)),
        ("Por dónde empezar", "<em>Mushrooms, Russia and History</em> o <em>La búsqueda de Perséfone</em>, "
                              "en la Biblioteca."),
    ],
    "vida": f"""<p>Valentina Pávlovna nació en Moscú en 1901; su familia emigró tras la Revolución. Estudió Medicina en Londres (1927) y fue pediatra, con trabajo sobre la sinusitis y la fiebre reumática infantil. Gordon Wasson nació en Great Falls (Montana) el 22 de septiembre de 1898, fue periodista y, desde 1928, trabajó en la banca; en J. P. Morgan estuvo de 1934 a 1963 y llegó a vicepresidente. Se casaron en 1926.{rr(1, 2)}</p>
<p>La leyenda familiar cuenta que, en su luna de miel en los Catskills (1927), Valentina recogió setas del bosque como en Rusia y Gordon se negó a comerlas. De esa diferencia salieron los términos «micófilos» y «micófobos», con los que describieron culturas que aman o temen los hongos.{r(3)}</p>
<p>Valentina murió de cáncer el 31 de diciembre de 1958, a los 57 años. Gordon siguió escribiendo hasta su muerte en Danbury (Connecticut) el 23 de diciembre de 1986.{rr(1, 2)}</p>""",
    "aportaciones": f"""<h3>De Rusia a México</h3>
<p>Su libro <em>Mushrooms, Russia and History</em> (1957) reunió décadas de pesquisas sobre cómo distintas culturas se relacionan con los hongos.{r(3)}</p>
<h3>La velada de 1955 y el artículo de Life (1957)</h3>
<p>A finales de junio de 1955, Gordon participó en una velada con <a href="../maria-sabina/">María Sabina</a>. El 13 de mayo de 1957, <em>Life</em> publicó su relato, y Valentina publicó el suyo en <em>This Week</em> el 19 de mayo.{r(4)} Por primera vez, el gran público oyó hablar de los hongos sagrados mazatecos.</p>
<h3>La teoría de los hongos en la historia</h3>
<p>En <em>Soma</em> (1968) Gordon propuso que el soma védico fue la amanita muscaria. En <em>El camino a Eleusis</em> (1978), con Albert Hofmann y Carl Ruck, defendió una hipótesis sobre los misterios de Eleusis. Más tarde publicó <em>The Wondrous Mushroom</em> (1980) y <em>Persephone's Quest</em> (1986).{r(3)} Algunas de estas ideas siguen debatidas.</p>
<h3>La palabra «enteógeno»</h3>
<p>En 1979, Ruck, Bigwood, Staples, Ott y Wasson propusieron «enteógeno», que significa «que genera lo divino en el interior», para designar plantas y sustancias usadas en contextos espirituales.{r(5)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER. No habla en nombre de las comunidades de las que se habla.</em></p>
<p>Los Wasson abrieron una puerta que muchas personas han agradecido, y también dejaron sombras. Está el engaño a María Sabina, que se cuenta en <a href="../maria-sabina/">su ficha</a>, y la oleada de forasteros que su relato llevó a Huautla. Por otro lado, la expedición de 1956 se financió en parte con un subproyecto de la CIA vinculado a MK-Ultra; los documentos indican que Wasson participó sin saberlo.{rr(6, 7)} Y el papel de Valentina, que investigó a su lado, no siempre se ha reconocido.</p>
<p>Desde la psicología transpersonal, su historia plantea una pregunta que sigue viva: ¿cómo se acerca uno a un saber ajeno con respeto, y qué se le devuelve a quien lo comparte?</p>""",
    "cronologia": [
        ("1898", "Nace Gordon Wasson, el 22 de septiembre."),
        ("1901", "Nace Valentina Pávlovna en Moscú."),
        ("1926", "Se casan."),
        ("1927", "Luna de miel en los Catskills: «micófilos» y «micófobos»."),
        ("1955", "Velada con María Sabina, a finales de junio."),
        ("1957", "<em>Life</em> (13 de mayo) y <em>This Week</em> (19 de mayo); <em>Mushrooms, Russia and History</em>."),
        ("1958", "Muere Valentina el 31 de diciembre."),
        ("1968", "Publica <em>Soma</em>."),
        ("1978", "<em>El camino a Eleusis</em>, con Hofmann y Ruck."),
        ("1979", "Se propone la palabra «enteógeno»."),
        ("1986", "Muere Gordon el 23 de diciembre."),
    ],
    "libros": [
        ("mushrooms-russia-and-history", "El libro de los dos sobre la historia cultural de los hongos."),
        ("soma", "La hipótesis de Gordon sobre el soma védico."),
        ("el-camino-a-eleusis-una-solucion-al-enigma-de-los-misterios-678", "Con Hofmann y Ruck."),
        ("the-wondrous-mushroom", "Sobre los hongos de México."),
        ("persephone-s-quest", "Su último libro."),
        ("maria-sabina-and-her-mazatec-mushroom-velada", "La velada, desde el lado de ella."),
    ],
    "relacion": [
        ("../maria-sabina/", "María Sabina", "La sabia mazateca con quien participó Gordon en 1955."),
        ("../albert-hofmann/", "Albert Hofmann", "Aisló la psilocibina de las setas que trajeron."),
        ("../../sustancias/psilocibina/", "Guía de las setas de psilocibina", "Qué son y cómo actúan."),
    ],
    "refs": [
        'Wikipedia (en inglés). «R. Gordon Wasson» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/R._Gordon_Wasson">https://en.wikipedia.org/wiki/R._Gordon_Wasson</a>',
        'Wikipedia (en inglés). «Valentina Pavlovna Wasson» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Valentina_Pavlovna_Wasson">https://en.wikipedia.org/wiki/Valentina_Pavlovna_Wasson</a>',
        'JSTOR Daily. «The nice married couple who inspired people to shroom». <a href="https://daily.jstor.org/the-nice-married-couple-who-inspired-people-to-shroom/">https://daily.jstor.org/the-nice-married-couple-who-inspired-people-to-shroom/</a>',
        'Wasson RG. Seeking the magic mushroom. <em>Life</em>, 13 de mayo de 1957; Wasson V. <em>This Week</em>, 19 de mayo de 1957.',
        'Ruck CAP, Bigwood J, Staples D, Ott J, Wasson RG. Entheogens. <em>J Psychedelic Drugs</em>. 1979;11(1-2):145-146. doi:<a href="https://doi.org/10.1080/02791072.1979.10472098">10.1080/02791072.1979.10472098</a>.',
        'MAPS. Bibliografía. <a href="https://bibliography.maps.org/resources/download/12543">https://bibliography.maps.org/resources/download/12543</a>',
        'Psychedelic Review. «Valentina Wasson». <a href="https://psychedelicreview.com/person/valentina-wasson/">https://psychedelicreview.com/person/valentina-wasson/</a>',
    ],
}

SCHULTES = {
    "slug": "richard-evans-schultes", "nombre": "Richard Evans Schultes", "iniciales": "RS", "anio": 1915,
    "que": "el botánico que recorrió la Amazonía buscando plantas sagradas",
    "tarjeta": "Botánico de Harvard. Recopiló miles de plantas en la Amazonía.",
    "desc": ("Richard Evans Schultes, el botánico de Harvard que estudió el peyote, las setas y el yagé y reunió "
             "miles de plantas en la Amazonía: vida, obra y lecturas."),
    "alias": "Botánico (Boston, 1915 – 2001)",
    "entrada": ("Un botánico de Harvard que pasó años en la selva colombiana, estudió el peyote, el teonanácatl y el "
                "yagé, y dejó una obra que sostiene buena parte de la etnobotánica."),
    "tipo": "Ciencia",
    "nacio_iso": "1915-01-12", "murio_iso": "2001-04-10", "lugar": "Boston, Massachusetts",
    "datos": [("Nació", "12 de enero de 1915, Boston (Massachusetts)"),
              ("Murió", "10 de abril de 2001, Boston"),
              ("Ámbito", "etnobotánica"),
              ("Le debemos", "décadas de estudio sobre las plantas sagradas de América")],
    "titulos": {"aportaciones": "Lo que investigó", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un botánico estadounidense, hijo de un fontanero de East Boston, inspirado por el naturalista "
                      "Richard Spruce, que estudió en Harvard con Oakes Ames." + rr(1, 2)),
        ("Por qué importa", "Identificó la botánica de las plantas psicoactivas de México y de la Amazonía, y "
                            "recopiló más de 20.000 ejemplares de plantas." + rr(1, 2)),
        ("Su legado", "Fue profesor y conservador en Harvard; formó a generaciones de etnobotánicos y fue un "
                      "defensor de la conservación de la selva." + rr(1, 3)),
        ("Por dónde empezar", "<em>Plantas de los dioses</em> (<em>Plants of the Gods</em>), en la Biblioteca."),
    ],
    "vida": f"""<p>Richard Evans Schultes nació en Boston el 12 de enero de 1915. Era hijo de un fontanero de East Boston y se interesó por las plantas leyendo al naturalista Richard Spruce. Entró en Harvard en 1933, con Oakes Ames como mentor.{rr(1, 2)}</p>
<p>En 1936 viajó a Oklahoma para estudiar el peyote con los kiowa, junto a Weston La Barre, y le dedicó su tesina (1937). En 1938 fue a Oaxaca por las setas sagradas. Su tesis doctoral (1941) trató la identidad del teonanácatl (<em>Psilocybe</em>) y del ololiuqui, una campanilla.{rr(1, 2)}</p>
<p>Desde 1941 vivió años en la Amazonía colombiana. Allí estudió el curare y, durante la guerra, colaboró en la búsqueda de caucho para el Gobierno de Estados Unidos. El curandero Salvador Chindoy le dio a conocer el yagé. Fue conservador del Museo Botánico de Harvard, catedrático desde 1970 y se jubiló en 1985. Murió en Boston el 10 de abril de 2001.{rr(1, 2, 3)}</p>""",
    "aportaciones": f"""<h3>El peyote, las setas y el ololiuqui</h3>
<p>Sus trabajos en Oklahoma y Oaxaca aclararon qué plantas y hongos se usaban en las ceremonias mexicanas y cuál era su identidad botánica.{r(1)}</p>
<h3>La Amazonía</h3>
<p>Reunió más de 20.000 ejemplares de plantas (el <em>New York Times</em> habla de más de 24.000) y documentó el uso del curare, el caucho y el yagé.{rr(1, 2)}</p>
<h3>Los libros</h3>
<p>Con Albert Hofmann escribió <em>Plants of the Gods</em>, una obra de referencia sobre plantas alucinógenas. <em>Vine of the Soul</em>, sobre el yagé, y otros textos de etnobotánica.{r(3)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER. No son hechos comprobados.</em></p>
<p>Schultes unía el rigor del botánico con una mirada respetuosa hacia los pueblos con los que trabajó: aprendía de ellos, dejaba constancia de su saber y defendía la selva en la que ese saber vive. Para la psicología transpersonal, su obra recuerda que muchas de estas medicinas nacieron dentro de culturas concretas y que conviene mirarlas desde ahí.</p>""",
    "cronologia": [
        ("1915", "Nace en Boston, el 12 de enero."),
        ("1933", "Entra en Harvard."),
        ("1936", "Estudia el peyote con los kiowa, en Oklahoma."),
        ("1938", "Viaja a Oaxaca por las setas sagradas."),
        ("1941", "Doctorado; empieza su etapa en la Amazonía colombiana."),
        ("1953", "Conservador en Harvard; catedrático en 1970."),
        ("1985", "Se jubila."),
        ("2001", "Muere en Boston, el 10 de abril."),
    ],
    "libros": [
        ("plants-of-the-gods", "Con Albert Hofmann: la obra de referencia."),
        ("vine-of-the-soul", "Sobre el yagé y la liana del alma."),
        ("hallucinogenic-plants", "Una guía breve."),
        ("where-the-gods-reign", "Sus plantas y su selva."),
        ("the-botany-and-chemistry-of-hallucinogens", "Con Hofmann: los aspectos técnicos."),
    ],
    "relacion": [
        ("../albert-hofmann/", "Albert Hofmann", "Coautor de <em>Plants of the Gods</em>."),
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "El yagé que él estudió."),
        ("../../sustancias/mescalina/", "Guía de la mescalina", "El peyote de su primera investigación."),
    ],
    "refs": [
        'The New York Times, vía Erowid. Obituario de Richard Evans Schultes. <a href="https://www.erowid.org/characters/schultes_richard/schultes_richard_obituary1.shtml">https://www.erowid.org/characters/schultes_richard/schultes_richard_obituary1.shtml</a>',
        'National Academy of Sciences. Memoria biográfica. <a href="https://nap.nationalacademies.org/read/11807/chapter/19">https://nap.nationalacademies.org/read/11807/chapter/19</a>',
        'Harvard Magazine. Sobre Richard Evans Schultes. <a href="https://www.harvardmagazine.com/print/80165">https://www.harvardmagazine.com/print/80165</a>',
    ],
}

LEARY = {
    "slug": "timothy-leary", "nombre": "Timothy Leary", "iniciales": "TL", "anio": 1920,
    "que": "el psicólogo de Harvard que popularizó «set y setting»",
    "tarjeta": "Psicólogo estadounidense. Dirigió el Proyecto Psilocibina de Harvard.",
    "desc": ("Timothy Leary, el psicólogo del Proyecto Psilocibina de Harvard: su vida, el «set y setting», sus "
             "luces y sus sombras, y por dónde empezar a leerle."),
    "alias": "Psicólogo (Springfield, 1920 – Beverly Hills, 1996)",
    "entrada": ("Un psicólogo de Harvard que, en 1960, probó setas en Cuernavaca, dirigió el Proyecto Psilocibina "
                "y se convirtió en la cara pública, y polémica, de los psicodélicos."),
    "tipo": "Psicología y terapia",
    "nacio_iso": "1920-10-22", "murio_iso": "1996-05-31", "lugar": "Springfield, Massachusetts",
    "datos": [("Nació", "22 de octubre de 1920, Springfield (Massachusetts)"),
              ("Murió", "31 de mayo de 1996, Beverly Hills (California)"),
              ("Ámbito", "psicología"),
              ("Le debemos", "la difusión de «set y setting» y el Proyecto Psilocibina de Harvard")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada y sus críticas"},
    "claves": [
        ("Quién fue", "Un psicólogo formado en Berkeley, profesor en Harvard desde 1959." + r(1)),
        ("Por qué importa", "En agosto de 1960 probó setas en Cuernavaca y puso en marcha el Proyecto Psilocibina "
                            "de Harvard (1960–1962) con Richard Alpert." + rr(1, 2)),
        ("Su sombra", "Harvard los despidió en 1963 y el trabajo de Concord fue criticado: se ha dicho que sus "
                      "resultados publicados eran erróneos." + rr(3, 4)),
        ("Por dónde empezar", "<em>La experiencia psicodélica</em> (1964), en la Biblioteca."),
    ],
    "vida": f"""<p>Timothy Leary nació en Springfield (Massachusetts) el 22 de octubre de 1920. Se formó como psicólogo en Berkeley y llegó a Harvard en 1959.{r(1)} En agosto de 1960, durante unas vacaciones en Cuernavaca (México), tomó setas de psilocibina, y volvió decidido a estudiarlas.{rr(1, 2)}</p>
<p>Murió de cáncer de próstata en Beverly Hills el 31 de mayo de 1996. Contó su proceso de morir en internet.{r(1)}</p>""",
    "aportaciones": f"""<h3>El Proyecto Psilocibina de Harvard (1960–1962)</h3>
<p>Con Richard Alpert (el futuro <a href="../ram-dass/">Ram Dass</a>) estudió los efectos de la psilocibina en personas voluntarias. Hicieron también el estudio de Concord (1961–1963) y el experimento de Marsh Chapel.{rr(2, 3)} Harvard los despidió en 1963.{r(2)}</p>
<h3>«Set y setting»</h3>
<p>Leary difundió la idea de que lo que se vive depende del «set» (la mente, el estado y las expectativas de la persona) y del «setting» (el lugar y las personas). Es una de las ideas más duraderas de su obra y hoy se usa en la investigación clínica.{r(2)}</p>
<h3>Libros</h3>
<p><em>La experiencia psicodélica</em> (1964), con Ralph Metzner y Richard Alpert, es una guía inspirada en el <em>Libro tibetano de los muertos</em>. Después vinieron otros textos y su autobiografía.{r(2)}</p>""",
    "mirada": f"""<p><em>Esta sección resume ideas y críticas. No son hechos comprobados.</em></p>
<p>Leary ayudó a poner los psicodélicos en el mapa, pero su estilo público marcó también el freno posterior a la investigación.{r(4)} Un análisis de Rick Doblin concluyó que los resultados publicados del estudio de Concord eran erróneos.{r(3)}</p>
<p>Desde una mirada humanista y transpersonal, su figura recuerda tanto el valor de abrir estas preguntas como la importancia de hacerlo con cuidado, rigor y respeto por las personas.</p>""",
    "cronologia": [
        ("1920", "Nace el 22 de octubre en Springfield (Massachusetts)."),
        ("1959", "Llega a Harvard."),
        ("1960", "Setas en Cuernavaca (agosto); empieza el Proyecto Psilocibina."),
        ("1961–1963", "Estudio de Concord."),
        ("1963", "Harvard los despide."),
        ("1964", "Publica <em>La experiencia psicodélica</em>."),
        ("1996", "Muere el 31 de mayo en Beverly Hills."),
    ],
    "libros": [
        ("la-experiencia-psicodelica-o-el-libro-tibetano-de-los-muertos-677", "Con Metzner y Alpert."),
        ("the-politics-of-ecstasy", "Sus ensayos de los años sesenta."),
        ("high-priest", "Su relato de aquellos años."),
        ("flashbacks", "Su autobiografía."),
        ("timothy-leary-greenfield", "Una biografía."),
    ],
    "relacion": [
        ("../ram-dass/", "Ram Dass", "Su colega en Harvard."),
        ("../../sustancias/psilocibina/", "Guía de las setas de psilocibina", "La sustancia del Proyecto Psilocibina."),
        ("../../investigacion-terapeutica/", "Investigación", "Qué dice hoy la investigación."),
    ],
    "refs": [
        'Encyclopaedia Britannica. «Timothy Leary». <a href="https://www.britannica.com/biography/Timothy-Leary">https://www.britannica.com/biography/Timothy-Leary</a>',
        'Erowid. «Timothy Leary», Erowid Character Vaults. <a href="https://erowid.org/culture/characters/leary_timothy/">https://erowid.org/culture/characters/leary_timothy/</a>',
        'Doblin R. Dr. Leary’s Concord Prison Experiment: a 34-year follow-up study. <em>J Psychoactive Drugs</em>. 1998;30(4):419-426. doi:<a href="https://doi.org/10.1080/02791072.1998.10399715">10.1080/02791072.1998.10399715</a>.',
        'Lattin D. Sobre el legado de Leary. <em>Harvard Library Bulletin</em>. 2017;28(1):65-74. <a href="https://dash.harvard.edu/handle/1/41647383">https://dash.harvard.edu/handle/1/41647383</a>',
    ],
}
