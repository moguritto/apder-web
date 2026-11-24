# Contenido de «Quién es quién» (APDER). Textos propios en español, con fuentes.

def r(n):
    return f'<sup><a href="#ref-{n}">{n}</a></sup>'


def rr(*ns):
    return "<sup>" + ",".join(f'<a href="#ref-{n}">{n}</a>' for n in ns) + "</sup>"


PORTADA = {
    "alias": "Las personas que abrieron el camino",
    "nota": ("Fichas breves de científicos, terapeutas, pensadores y personas de saber tradicional: quiénes fueron, "
             "qué aportaron, cómo veían las cosas y por dónde empezar a leerles."),
    "desc": ("Quién es quién en los psicodélicos: fichas de científicos, terapeutas, pensadores y sabios "
             "tradicionales, con su vida, sus aportaciones y lecturas."),
    "pie": ('<p>Iremos añadiendo personas poco a poco. Si echas en falta a alguien, escríbenos a '
            '<a href="mailto:info@apder.org">info@apder.org</a>.</p>'),
}

HOFMANN = {
    "slug": "albert-hofmann",
    "nombre": "Albert Hofmann",
    "iniciales": "AH",
    "que": "el químico que descubrió el LSD",
    "tarjeta": "Químico suizo. Descubrió el LSD y aisló la psilocibina.",
    "desc": ("Albert Hofmann, el químico suizo que sintetizó el LSD y aisló la psilocibina: su vida, "
             "sus descubrimientos, su mirada y por dónde empezar a leerle."),
    "alias": "Químico suizo (Baden, 1906 – Burg im Leimental, 2008)",
    "entrada": ("Sintetizó el LSD en 1938, descubrió sus efectos por accidente en 1943 y pasó el resto de su "
                "larga vida pensando en lo que había encontrado."),
    "tipo": "Ciencia", "anio": 1906,
    "nacio_iso": "1906-01-11", "murio_iso": "2008-04-29", "lugar": "Baden, Suiza",
    "datos": [("Nació", "11 de enero de 1906, Baden (Suiza)"),
              ("Murió", "29 de abril de 2008, a los 102 años"),
              ("Ámbito", "química de productos naturales"),
              ("Le debemos", "el LSD, la psilocibina y la psilocina")],
    "titulos": {"aportaciones": "Lo que descubrió", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un químico suizo que trabajó toda su carrera en los laboratorios Sandoz de Basilea, "
                      "estudiando moléculas de plantas y hongos medicinales." + r(1)),
        ("Por qué importa", "Sintetizó el LSD en 1938, descubrió sus efectos en 1943 y en 1958 aisló la "
                            "psilocibina y la psilocina de las setas mexicanas." + rr(1, 3)),
        ("Su mirada", "Vio en el LSD una herramienta para la consciencia que pedía respeto. Por eso lo llamó "
                      "su «niño problemático»: le dio alegrías y también preocupaciones." + r(2)),
        ("Por dónde empezar", "<em>La historia del LSD</em>, su relato en primera persona, que está en la "
                              "Biblioteca."),
    ],
    "vida": f"""<p>Albert Hofmann nació en Baden (Suiza) el 11 de enero de 1906, el mayor de cuatro hermanos de una familia modesta.{r(9)} Estudió química en la Universidad de Zúrich y entró a trabajar en los laboratorios farmacéuticos Sandoz, en Basilea, donde pasó toda su vida profesional.{r(1)} Allí se especializó en sustancias de origen natural: primero en los principios activos de la cebolla albarrana y después en los alcaloides del cornezuelo, un hongo que infecta el centeno.</p>
<p>Él mismo contaba que de niño, paseando por el bosque una mañana de primavera, vivió un momento en que el mundo le pareció transfigurado y lleno de sentido. Años después relacionó aquella vivencia con lo que el LSD le mostró.{rr(2, 6)}</p>
<p>Se jubiló en 1971 como director de investigación de productos naturales de Sandoz.{r(9)} Siguió escribiendo y dando conferencias hasta muy mayor. Murió el 29 de abril de 2008 en Burg im Leimental, cerca de Basilea, a los 102 años.{rr(1, 7)}</p>""",
    "aportaciones": f"""<h3>El LSD (1938 y 1943)</h3>
<p>Hofmann buscaba un estimulante de la circulación y la respiración entre los derivados del ácido lisérgico, la base química del cornezuelo. El 16 de noviembre de 1938 preparó el vigésimo quinto de la serie: la dietilamida del ácido lisérgico, LSD-25. En los animales no mostró nada interesante y quedó guardado.{rr(1, 9)}</p>
<p>Cinco años después, el viernes 16 de abril de 1943, volvió a prepararlo porque intuía que se le había escapado algo. Mientras trabajaba sintió un estado extraño, como de sueño, que duró unas dos horas: probablemente había absorbido una cantidad mínima por la piel. El 19 de abril tomó a propósito 0,25 miligramos, una cantidad que creyó prudente y que resultó ser una dosis fuerte. Volvió a casa en bicicleta mientras el efecto subía, y por eso el 19 de abril se recuerda hoy como el «Día de la bicicleta».{rr(2, 7)}</p>
<h3>La psilocibina y la psilocina (1958)</h3>
<p>Tras las expediciones de <a href="../valentina-y-gordon-wasson/">Gordon Wasson</a> y del micólogo francés Roger Heim a México, llegaron a Sandoz setas sagradas mazatecas que se cultivaron en el laboratorio. Hofmann aisló sus dos principios activos, la psilocibina y la psilocina, los nombró, describió su estructura y logró fabricarlos en el laboratorio.{rr(1, 3)}</p>
<h3>El ololiuqui (1960)</h3>
<p>Analizó también las semillas de ololiuqui, una enredadera de la familia de la campanilla que se usaba en ceremonias en México. Encontró en ellas la amida del ácido lisérgico, un pariente cercano del LSD. Le sorprendió que una planta produjera de forma natural algo tan parecido a la molécula que él había fabricado.{r(4)}</p>
<h3>El viaje a México (1962)</h3>
<p>En 1962 viajó con <a href="../valentina-y-gordon-wasson/">Wasson</a> a la sierra Mazateca para estudiar la <em>Salvia divinorum</em>, las «hojas de la pastora». Las muestras que recogieron permitieron describir la planta como especie nueva.{r(5)} En ese viaje conoció a <a href="../maria-sabina/">María Sabina</a> y le ofreció pastillas de psilocibina. Según contó él mismo, tras tomarlas ella dijo que tenían el mismo espíritu que los hongos.{r(2)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas y su interpretación de lo que vivió. No son hechos comprobados.</em></p>
<p>Hofmann llamó a su libro de memorias <em>LSD – mein Sorgenkind</em>, «mi niño problemático». Le alegraba haber dado a la psiquiatría una herramienta tan poderosa para explorar la mente. Le preocupaba que se usara sin cuidado, lejos del contexto médico y contemplativo que él veía como el adecuado.{r(2)}</p>
<p>Creía que la sociedad industrial había perdido la experiencia de unidad con la naturaleza, y que sustancias como el LSD, tomadas con respeto, podían ayudar a recuperarla. Con Wasson y el filólogo Carl Ruck defendió la hipótesis de que la bebida de los misterios de Eleusis, en la antigua Grecia, contenía alcaloides del cornezuelo. Es una hipótesis, todavía discutida.{r(8)} Al cumplir cien años dijo que el LSD era una herramienta para llegar a ser lo que estamos llamados a ser.{r(9)}</p>
<p>Desde la psicología transpersonal, su figura interesa porque en ella se tocan la mirada del químico y la del místico: un hombre de laboratorio que, sin dejar de serlo, se tomó en serio la experiencia interior.</p>""",
    "cronologia": [
        ("1906", "Nace en Baden (Suiza), el 11 de enero."),
        ("1938", "Sintetiza el LSD-25 en Sandoz, el 16 de noviembre."),
        ("1943", "Descubre sus efectos (16 de abril) y lo toma a propósito (19 de abril, el «Día de la bicicleta»)."),
        ("1958", "Aísla la psilocibina y la psilocina de las setas mexicanas."),
        ("1960", "Identifica la amida del ácido lisérgico en las semillas de ololiuqui."),
        ("1962", "Viaja a México con Gordon Wasson; conoce a María Sabina."),
        ("1971", "Se jubila en Sandoz."),
        ("1978", "Publica con Wasson y Ruck <em>El camino a Eleusis</em>."),
        ("1979", "Publica sus memorias, <em>LSD – mein Sorgenkind</em>."),
        ("2008", "Muere el 29 de abril, a los 102 años."),
    ],
    "libros": [
        ("la-historia-del-lsd-461", "Sus memorias: el descubrimiento y lo que vino después."),
        ("mundo-interior-mundo-exterior-462", "Sus reflexiones sobre la consciencia y la naturaleza."),
        ("el-camino-a-eleusis-una-solucion-al-enigma-de-los-misterios-678", "La hipótesis del cornezuelo en Eleusis."),
        ("plants-of-the-gods", "Con el botánico Richard Evans Schultes, sobre las plantas sagradas."),
        ("mystic-chemist-the-life-of-albert-hofmann-and-his-discovery-of-lsd-481", "Su biografía más completa."),
    ],
    "relacion": [
        ("../../sustancias/lsd/", "Guía del LSD", "Qué es, cómo actúa y cómo reducir riesgos."),
        ("../../sustancias/psilocibina/", "Guía de las setas de psilocibina", "La molécula que aisló en 1958."),
        ("../maria-sabina/", "María Sabina", "La sabia mazateca que conoció en 1962."),
        ("../valentina-y-gordon-wasson/", "Valentina y Gordon Wasson", "Quienes trajeron las setas a Sandoz."),
    ],
    "refs": [
        'Encyclopaedia Britannica. «Albert Hofmann». <a href="https://www.britannica.com/biography/Albert-Hofmann">https://www.britannica.com/biography/Albert-Hofmann</a>',
        'Hofmann A. <em>LSD – mein Sorgenkind</em>. Stuttgart: Klett-Cotta; 1979. En español: <em>La historia del LSD</em>.',
        'Wasson RG. The hallucinogenic mushrooms of Mexico and psilocybin: a bibliography. <em>Botanical Museum Leaflets, Harvard University</em>. 1962;20(2). <a href="https://archive.org/download/biostor-160830/biostor-160830.pdf">https://archive.org/download/biostor-160830/biostor-160830.pdf</a>',
        'Hofmann A, Tscherter H. Isolierung von Lysergsäure-Alkaloiden aus der mexikanischen Zauberdroge Ololiuqui (<em>Rivea corymbosa</em>). <em>Experientia</em>. 1960;16(9):414. doi:<a href="https://doi.org/10.1007/BF02178840">10.1007/BF02178840</a>.',
        'Erowid. Cronología de la <em>Salvia divinorum</em>. <a href="https://erowid.org/salvia/salvia_timeline.php">https://erowid.org/salvia/salvia_timeline.php</a>',
        'Novartis. «On the shoulders of a giant». <a href="https://live.novartis.com/en/article/on-the-shoulders-of-a-giant">https://live.novartis.com/en/article/on-the-shoulders-of-a-giant</a>',
        'Scientific American. «Albert Hofmann, inventor of LSD, embarks on final trip» (2008). <a href="https://www.scientificamerican.com/article/inventor-of-lsd-embarks-on-final-trip/">https://www.scientificamerican.com/article/inventor-of-lsd-embarks-on-final-trip/</a>',
        'Wasson RG, Hofmann A, Ruck CAP. <em>The Road to Eleusis</em>. Nueva York: Harcourt Brace Jovanovich; 1978. En español: <em>El camino a Eleusis</em>.',
        'Wikipedia (en inglés). «Albert Hofmann» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Albert_Hofmann">https://en.wikipedia.org/wiki/Albert_Hofmann</a>',
    ],
}

GROF = {
    "slug": "stanislav-grof",
    "nombre": "Stanislav Grof",
    "iniciales": "SG",
    "que": "psiquiatra y pionero de la psicología transpersonal",
    "tarjeta": "Psiquiatra checo. Cofundador de la psicología transpersonal.",
    "desc": ("Stanislav Grof, psiquiatra checo y cofundador de la psicología transpersonal: la terapia con LSD, "
             "la respiración holotrópica y la emergencia espiritual."),
    "alias": "Psiquiatra (Praga, 1931)",
    "entrada": ("Acompañó miles de sesiones con LSD, dibujó un mapa de la psique más amplio que la biografía y, "
                "con Christina Grof, creó la respiración holotrópica."),
    "tipo": "Psicología y terapia", "anio": 1931,
    "nacio_iso": "1931-07-01", "lugar": "Praga, Checoslovaquia",
    "datos": [("Nació", "1 de julio de 1931, Praga (entonces Checoslovaquia)"),
              ("Ámbito", "psiquiatría y psicología transpersonal"),
              ("Le debemos", "la cartografía de los estados holotrópicos, la respiración holotrópica y la idea de emergencia espiritual")],
    "titulos": {"aportaciones": "Lo que aportó", "mirada": "Su mirada"},
    "claves": [
        ("Quién es", "Un psiquiatra nacido en Praga en 1931, uno de los fundadores de la psicología "
                     "transpersonal. En julio de 2026 cumplió 95 años." + rr(9, 7)),
        ("Por qué importa", "Dirigió algunos de los programas de terapia con LSD más largos del siglo XX, en Praga "
                            "y en Maryland, y propuso un mapa de la mente que incluye el nacimiento y lo "
                            "transpersonal." + rr(1, 2)),
        ("Lo más conocido", "La respiración holotrópica, que desarrolló con su esposa Christina en Esalen, y el "
                            "concepto de emergencia espiritual." + rr(1, 5)),
        ("Por dónde empezar", "<em>La tormentosa búsqueda del ser</em> o <em>Emergencia espiritual</em>, ambos en "
                              "español y en la Biblioteca."),
    ],
    "vida": f"""<p>Stanislav Grof nació en Praga el 1 de julio de 1931. Se licenció en Medicina en la Universidad Carolina y se doctoró en la Academia de Ciencias de Checoslovaquia.{r(9)} Siendo residente de psiquiatría, su laboratorio recibió ampollas de LSD enviadas por Sandoz para investigación. Su primera sesión, como voluntario, marcó el rumbo de toda su vida.{r(4)}</p>
<p>Entre 1960 y 1967 dirigió el programa de investigación con psicodélicos del Instituto de Investigación Psiquiátrica de Praga.{r(1)} En 1967 una beca le llevó a la Universidad Johns Hopkins, en Baltimore, y de 1969 a 1973 fue jefe de investigación psiquiátrica del Maryland Psychiatric Research Center. Allí, con Walter Pahnke y Bill Richards, entre otros, trabajó en uno de los últimos programas oficiales de terapia psicodélica de Estados Unidos.{rr(2, 4)}</p>
<p>De 1973 a 1987 vivió en el Instituto Esalen, en Big Sur (California), como investigador residente. Allí escribió buena parte de su obra y, con Christina Grof, desarrolló la respiración holotrópica, que presentaron por primera vez en 1976.{rr(3, 4)} En 1977 fue el primer presidente de la Asociación Transpersonal Internacional.{r(9)} Después enseñó en el California Institute of Integral Studies.</p>
<p>Christina murió en 2014. Desde 2016 está casado con la psicóloga Brigitte Grof, con quien creó en 2020 una nueva formación para acompañar estados holotrópicos.{r(9)} En 2026, con 95 años, los primeros Psychedelic Awards, en San Francisco, lo eligieron para homenajear toda su trayectoria.{r(8)}</p>""",
    "aportaciones": f"""<h3>La terapia con LSD</h3>
<p>Durante los años sesenta acompañó miles de sesiones de terapia con psicodélicos.{r(2)} En Maryland trabajó, entre otros, con personas con cáncer avanzado y con alcoholismo.{r(4)} De esa experiencia sacó una idea central: los psicodélicos no producen una experiencia fija, sino que actúan como amplificadores de lo que ya hay en la psique. Lo que aflora depende de la persona, de su historia y del contexto.{r(10)}</p>
<h3>Un mapa de la psique</h3>
<p>Grof propuso una cartografía de la mente con tres territorios:{rr(9, 10)}</p>
<ul>
<li><strong>El biográfico.</strong> Los recuerdos y vivencias de la vida personal, que suelen agruparse en constelaciones con una misma carga emocional. Él las llamó «sistemas COEX».</li>
<li><strong>El perinatal.</strong> Vivencias relacionadas con el nacimiento, que ordenó en cuatro «matrices perinatales básicas»: la unión con la madre, el atrapamiento sin salida, la lucha por pasar y la experiencia de muerte y renacimiento.</li>
<li><strong>El transpersonal.</strong> Experiencias que van más allá de la identidad personal: unidad con la naturaleza o con el cosmos, figuras arquetípicas, vivencias de otras épocas o culturas.</li>
</ul>
<h3>La respiración holotrópica</h3>
<p>«Holotrópico» significa «que se mueve hacia la totalidad». Con Christina desarrolló un método sin sustancias que combina una respiración más rápida y profunda, música evocadora y trabajo corporal.{r(1)} Se practica en grupo y por parejas: una persona respira y la otra acompaña, y luego se intercambian.{r(4)}</p>
<h3>La emergencia espiritual</h3>
<p>Con Christina, Grof acuñó el concepto de «emergencia espiritual»: crisis psicológicas intensas que pueden ser parte de un proceso de transformación y que, si se acompañan bien, abren paso a un crecimiento. Advertían que a veces se confunden con una enfermedad mental.{r(5)} En 1980 fundaron en Esalen una red de apoyo para estas crisis, la Spiritual Emergency Network, rebautizada en 1986 como Spiritual Emergence Network.{r(6)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas y su interpretación. Son propuestas teóricas, no hechos comprobados.</em></p>
<p>Para Grof, los estados no ordinarios de consciencia pueden ser sanadores si se acompañan en lugar de suprimirse. Hablaba de una inteligencia sanadora interior: la tarea de quien acompaña no es dirigir la experiencia, sino sostenerla y confiar en que la psique sabe hacia dónde ir.{rr(1, 10)}</p>
<p>Desde la psicología transpersonal, su obra es una de las grandes columnas de la disciplina. Amplió la mirada de la psicología humanista hacia lo espiritual sin renunciar a la práctica clínica.</p>
<p>También tiene críticas. Su modelo perinatal es discutido, porque es difícil saber si esas vivencias corresponden a recuerdos reales del parto o a imágenes simbólicas. Y la respiración holotrópica cuenta todavía con pocos estudios controlados. Lo justo es presentar su trabajo como lo que es: un mapa nacido de una experiencia clínica enorme, abierto a revisión.</p>""",
    "cronologia": [
        ("1931", "Nace en Praga, el 1 de julio."),
        ("1960–1967", "Dirige la investigación con psicodélicos del Instituto de Investigación Psiquiátrica de Praga."),
        ("1967", "Se traslada a la Universidad Johns Hopkins, en Baltimore."),
        ("1969–1973", "Jefe de investigación psiquiátrica en el Maryland Psychiatric Research Center."),
        ("1973–1987", "Investigador residente en el Instituto Esalen."),
        ("1975", "Publica <em>Realms of the Human Unconscious</em>."),
        ("1976", "Presenta con Christina Grof la respiración holotrópica."),
        ("1977", "Primer presidente de la Asociación Transpersonal Internacional."),
        ("1980", "Fundan la Spiritual Emergency Network."),
        ("2016", "Se casa con Brigitte Grof."),
        ("2026", "Cumple 95 años; los Psychedelic Awards lo eligen para homenajear su trayectoria."),
    ],
    "libros": [
        ("la-tormentosa-busqueda-del-ser-669", "Con Christina Grof: guía para atravesar las crisis de transformación."),
        ("emergencia-espiritual-670", "Con Christina Grof: cuando la transformación personal se vuelve crisis."),
        ("la-respiracion-holotropica-666", "Con Christina Grof: el método, explicado por sus autores."),
        ("realms-of-the-human-unconscious", "Su primer gran libro sobre la investigación con LSD."),
        ("lsd-psychotherapy", "El manual clínico de la terapia con LSD."),
        ("the-way-of-the-psychonaut", "Su síntesis de madurez."),
    ],
    "relacion": [
        ("../../sustancias/lsd/", "Guía del LSD", "La sustancia con la que trabajó en Praga y en Maryland."),
        ("../albert-hofmann/", "Albert Hofmann", "El químico que descubrió el LSD."),
        ("../../investigacion-terapeutica/", "Investigación", "Qué dice hoy la investigación con psicodélicos."),
    ],
    "refs": [
        'Grof S. Biografía de autor en HuffPost. <a href="https://www.huffingtonpost.com/author/stanislav-grof-md-phd">https://www.huffingtonpost.com/author/stanislav-grof-md-phd</a>',
        'Erowid. «Stanislav Grof», Erowid Character Vaults. <a href="https://erowid.org/culture/characters/grof_stanislav/">https://erowid.org/culture/characters/grof_stanislav/</a>',
        'Encyclopedia.com. «Grof, Stanislav (1931–)». <a href="https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/grof-stanislav-1931">https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/grof-stanislav-1931</a>',
        'The Sun Magazine. Entrevista a Stanislav Grof. <a href="https://thesunmagazine.org/article/4320">https://thesunmagazine.org/article/4320</a>',
        'Grof C, Grof S. Spiritual emergency: the understanding and treatment of transpersonal crises. <em>International Journal of Transpersonal Studies</em>. 2017;36(2). doi:<a href="https://doi.org/10.24972/ijts.2017.36.2.30">10.24972/ijts.2017.36.2.30</a>.',
        'Harvard Divinity School, Center for the Study of World Religions. «Christina Grof’s experience of spiritual emergency» (2026). <a href="https://cswr.hds.harvard.edu/news/2026/07/07/christina-grofs-experience-spiritual-emergency">https://cswr.hds.harvard.edu/news/2026/07/07/christina-grofs-experience-spiritual-emergency</a>',
        'MAPS Bulletin. Fragmento de <em>Psyche Unbound</em> por el 95.º cumpleaños de Stanislav Grof (julio de 2026). <a href="https://maps.org/news/bulletin/psyche-unbound-excerpt-perception-and-knowledge/">https://maps.org/news/bulletin/psyche-unbound-excerpt-perception-and-knowledge/</a>',
        'Psychedelic Awards 2026 (San Francisco, 10 de octubre de 2026). <a href="https://luma.com/awards2026">https://luma.com/awards2026</a>',
        'Wikipedia (en inglés). «Stanislav Grof» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Stanislav_Grof">https://en.wikipedia.org/wiki/Stanislav_Grof</a>',
        'Grof S. <em>Realms of the Human Unconscious: Observations from LSD Research</em>. Nueva York: Viking; 1975.',
    ],
}

SABINA = {
    "slug": "maria-sabina",
    "nombre": "María Sabina",
    "iniciales": "MS",
    "que": "la sabia mazateca de los niños santos",
    "tarjeta": "Sabia mazateca de Huautla. Curaba con los niños santos.",
    "desc": ("María Sabina, sabia mazateca de Huautla de Jiménez: las veladas con los niños santos, su encuentro "
             "con Wasson y lo que su fama costó a su comunidad."),
    "alias": "Sabia mazateca (Huautla de Jiménez, hacia 1894 – 1985)",
    "entrada": ("Curaba en veladas nocturnas con los hongos que llamaba niños santos, guiada por su canto. Su "
                "encuentro con un banquero de Nueva York cambió la historia de los psicodélicos, y también su vida."),
    "tipo": "Saber tradicional", "anio": 1894,
    "nacio_iso": "1894", "murio_iso": "1985-11", "lugar": "Huautla de Jiménez, Oaxaca, México",
    "datos": [("Nació", "hacia 1894 (se suele dar el 22 de julio), en Huautla de Jiménez (Oaxaca, México)"),
              ("Murió", "noviembre de 1985, a los 91 años"),
              ("Pueblo y lengua", "mazateco"),
              ("Su saber", "las veladas de curación con hongos sagrados y el canto")],
    "titulos": {"aportaciones": "La velada y el encuentro con Wasson", "mirada": "Lo que nos deja"},
    "claves": [
        ("Quién fue", "Una sabia mazateca de la sierra de Oaxaca, en México, que curaba en veladas nocturnas con "
                      "hongos sagrados, a los que llamaba niños santos, y con su canto." + rr(1, 10)),
        ("Por qué importa", "En 1955 dejó participar en una velada a Gordon Wasson. Su artículo en la revista "
                            "<em>Life</em>, en 1957, dio a conocer al mundo los hongos de psilocibina." + rr(2, 3)),
        ("El precio", "La fama llevó a Huautla una oleada de forasteros. Ella sintió que los niños santos "
                      "habían perdido su pureza, y parte de su comunidad la culpó." + rr(1, 4)),
        ("Por dónde empezar", "<em>Vida de María Sabina</em>, de Álvaro Estrada, su vida contada con su propia voz. "
                              "Está en la Biblioteca."),
    ],
    "vida": f"""<p>María Sabina nació en Huautla de Jiménez o en sus alrededores, en la sierra Mazateca del estado de Oaxaca (México). Ella misma no sabía bien la fecha: creía haber nacido en 1894, y se suele dar el 22 de julio.{r(10)} Hablaba solo mazateco, y sus palabras llegaron al resto del mundo a través de traductores.{r(8)}</p>
<p>Su padre murió cuando ella era muy pequeña y creció en casa de sus abuelos maternos. En la familia de su padre había tradición de sabios. Conoció los hongos de niña, en una velada que se hizo en su casa para curar a un pariente enfermo.{rr(1, 10)} Se casó muy joven y tuvo hijos. Vivió siempre de forma humilde, trabajando la tierra.{r(1)}</p>
<p>Ella insistía en que no era curandera, sino sabia: una persona que sabe, a la que el lenguaje le llega en la velada.{r(10)} Contaba que sus cantos le habían sido dados, y que ella solo era «la intérprete».{r(1)} Murió en noviembre de 1985, a los 91 años, en la pobreza.{rr(8, 10)}</p>""",
    "aportaciones": f"""<h3>La velada</h3>
<p>La velada mazateca es una ceremonia nocturna de curación. Quienes participan comen los hongos sagrados, y la sabia canta y habla durante horas en mazateco: pregunta por la enfermedad, busca lo que se ha perdido, habla con los santos y con las fuerzas de la naturaleza.{rr(1, 10)} En la tradición de María Sabina, el poder de los niños santos está en el lenguaje que hacen brotar.{r(1)}</p>
<h3>El encuentro con Gordon Wasson (1955)</h3>
<p>Robert Gordon Wasson (<a href="../valentina-y-gordon-wasson/">su ficha</a>) era un banquero de Nueva York apasionado por los hongos, que investigaba con su esposa, la pediatra Valentina Pávlovna Wasson. A finales de junio de 1955, él y el fotógrafo Allan Richardson participaron en una velada con María Sabina.{r(3)} Para que les dejara entrar, Wasson le dijo que estaba preocupado por su hijo, que estaba lejos. No era verdad.{r(4)}</p>
<p>El 13 de mayo de 1957, la revista <em>Life</em> publicó su relato con el título «Seeking the Magic Mushroom». Wasson la llamó «Eva Méndez» para protegerla, pero los detalles bastaban para encontrarla, y en publicaciones posteriores apareció su nombre real y sus fotos.{rr(2, 4)} El artículo se leyó en plena Guerra Fría y con una mirada exótica sobre los pueblos indígenas, que hoy se analiza de forma crítica.{r(7)}</p>
<p>En 1962, <a href="../albert-hofmann/">Albert Hofmann</a> le ofreció en persona pastillas de psilocibina fabricadas en Sandoz. Según contó él, ella dijo que tenían el mismo espíritu que los hongos.{r(5)}</p>
<h3>Las consecuencias</h3>
<p>Desde comienzos de los años sesenta empezaron a llegar a Huautla jóvenes de Estados Unidos, investigadores y buscadores de experiencias.{r(10)} Para muchos, la velada dejó de ser una ceremonia de curación de una comunidad y se convirtió en una experiencia que se iba a buscar. Parte del pueblo culpó a María Sabina de lo que estaba pasando.{r(4)} Se cuentan muchas visitas de músicos famosos, pero buena parte de esas historias no está documentada.{r(9)}</p>
<p>Ella misma lo resumió años después: desde que llegaron los extranjeros, los niños santos perdieron su pureza y su fuerza, y los de fuera nunca llegaron a entender que su poder estaba en el lenguaje.{r(1)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER, desde fuera de la cultura mazateca. No habla en su nombre.</em></p>
<p>María Sabina es hoy un icono, pero conviene recordarla como lo que fue: una mujer de su pueblo, con un saber que pertenecía a una comunidad y a una lengua. Su historia se cuenta a menudo como el comienzo de la era psicodélica. Desde la perspectiva de los pueblos indígenas, también es una historia de extracción y de apropiación cultural.{r(10)}</p>
<p>Su vida deja preguntas que siguen abiertas para quien se acerca hoy a las medicinas tradicionales. ¿Se respeta el consentimiento de quien comparte su saber? ¿Qué vuelve a la comunidad de lo que se lleva? ¿Se entiende la ceremonia en su contexto, o solo se busca el efecto?</p>
<p>Desde la psicología transpersonal, su velada recuerda que en muchas tradiciones la curación es un hecho comunitario y simbólico, sostenido por el canto, la palabra y la relación con lo sagrado. No es solo un efecto químico sobre un individuo.</p>
<p>Su voz ha llegado hasta nosotros en el libro de Álvaro Estrada (1977), en las grabaciones de sus cantos y en el documental <em>María Sabina, mujer espíritu</em> (1979), de Nicolás Echevarría.{rr(6, 12)} Camilo José Cela le dedicó un oratorio.{r(11)}</p>""",
    "cronologia": [
        ("Hacia 1894", "Nace en Huautla de Jiménez o en sus alrededores (Oaxaca, México)."),
        ("1955", "A finales de junio, Gordon Wasson y Allan Richardson participan en una velada con ella."),
        ("1957", "<em>Life</em> publica «Seeking the Magic Mushroom» (13 de mayo)."),
        ("1958", "Albert Hofmann aísla la psilocibina de las setas mexicanas."),
        ("Años sesenta", "Llegada masiva de forasteros a Huautla."),
        ("1962", "Albert Hofmann y Wasson la visitan; prueba las pastillas de psilocibina."),
        ("1977", "Álvaro Estrada publica <em>Vida de María Sabina: la sabia de los hongos</em>."),
        ("1979", "Documental <em>María Sabina, mujer espíritu</em>, de Nicolás Echevarría."),
        ("1985", "Muere en noviembre, a los 91 años."),
    ],
    "libros": [
        ("vida-de-maria-sabina", "Su vida contada en primera persona, a partir de entrevistas en mazateco."),
        ("maria-sabina-and-her-mazatec-mushroom-velada", "La velada completa, con sus cantos transcritos y traducidos."),
        ("maria-sabina-rothenberg", "Una selección de sus cantos como poesía."),
        ("maria-sabina", "Homenaje colectivo, con textos de varios autores."),
    ],
    "relacion": [
        ("../../sustancias/psilocibina/", "Guía de las setas de psilocibina", "Qué son, cómo actúan y cómo reducir riesgos."),
        ("../albert-hofmann/", "Albert Hofmann", "El químico que aisló la psilocibina y la visitó en 1962."),
        ("../valentina-y-gordon-wasson/", "Valentina y Gordon Wasson", "Quienes dieron a conocer su velada."),
        ("../../sustancias/salvia-divinorum/", "Guía de la Salvia divinorum", "La otra planta sagrada de la sierra Mazateca."),
    ],
    "refs": [
        'Estrada Á. <em>Vida de María Sabina: la sabia de los hongos</em>. México: Siglo XXI; 1977.',
        'Wasson RG. Seeking the magic mushroom. <em>Life</em>, 13 de mayo de 1957.',
        'Erowid. Cronología de las setas de psilocibina. <a href="https://erowid.org/plants/mushrooms/mushrooms_timeline.php">https://erowid.org/plants/mushrooms/mushrooms_timeline.php</a>',
        'Wikipedia (en inglés). «R. Gordon Wasson» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/R._Gordon_Wasson">https://en.wikipedia.org/wiki/R._Gordon_Wasson</a>',
        'Hofmann A. <em>LSD – mein Sorgenkind</em>. Stuttgart: Klett-Cotta; 1979. En español: <em>La historia del LSD</em>.',
        'Glockner J. Reseña de <em>Vida de María Sabina</em>. <em>Elementos</em> (BUAP). 2023;131:101-104. <a href="https://elementos.buap.mx/directus/storage/uploads//00000008655.pdf">https://elementos.buap.mx/directus/storage/uploads//00000008655.pdf</a>',
        'Feinberg B. «Cute as children, but not handsome as adults: María Sabina, <em>Life</em> magazine, and Cold War propaganda». Chacruna. <a href="https://chacruna.net/cute-as-children-but-not-handsome-as-adults-maria-sabina-life-magazine-and-cold-war-propaganda/">https://chacruna.net/cute-as-children-but-not-handsome-as-adults-maria-sabina-life-magazine-and-cold-war-propaganda/</a>',
        'UPI. Nota sobre su muerte, 22 de noviembre de 1985. <a href="https://www.upi.com/Archives/1985/11/22/Mexicos-queen-of-hallucinogenic-mushrooms-dies-at-97/2265501483600/">https://www.upi.com/Archives/1985/11/22/Mexicos-queen-of-hallucinogenic-mushrooms-dies-at-97/2265501483600/</a>',
        'Courthouse News. «Seeking authentic in Mexican town that introduced world to magic mushrooms». <a href="https://www.courthousenews.com/seeking-authentic-in-mexican-town-that-introduced-world-to-magic-mushrooms/">https://www.courthousenews.com/seeking-authentic-in-mexican-town-that-introduced-world-to-magic-mushrooms/</a>',
        'Wikipedia (en inglés). «María Sabina» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Mar%C3%ADa_Sabina">https://en.wikipedia.org/wiki/María_Sabina</a>',
        'EcuRed. «María Sabina». <a href="https://www.ecured.cu/Mar%C3%ADa_Sabina">https://www.ecured.cu/María_Sabina</a>',
        'Echevarría N. <em>María Sabina, mujer espíritu</em> (documental). México; 1979.',
    ],
}

from personas_tanda2a import HUXLEY, OSMOND, WASSON, SCHULTES, LEARY
from personas_tanda2b import RAMDASS, WATTS, SHULGIN, ZEFF

PERSONAS = [HOFMANN, GROF, SABINA, HUXLEY, OSMOND, WASSON, SCHULTES, LEARY, RAMDASS, WATTS, SHULGIN, ZEFF]
