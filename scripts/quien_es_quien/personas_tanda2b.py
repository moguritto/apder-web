# «Quién es quién» · tanda 2 (parte B). Datos verificados el 23-11-2026; fuentes al final de cada ficha.
from contenido import r, rr

RAMDASS = {
    "slug": "ram-dass", "nombre": "Ram Dass", "iniciales": "RD", "anio": 1931,
    "que": "el psicólogo de Harvard que se hizo maestro espiritual",
    "tarjeta": "Antes Richard Alpert. Autor de <em>Be Here Now</em>.",
    "desc": ("Ram Dass, antes Richard Alpert, profesor de Harvard que viajó a la India y escribió Be Here Now: su "
             "vida, su camino espiritual y por dónde empezar a leerle."),
    "alias": "Psicólogo y maestro espiritual (Boston, 1931 – Maui, 2019)",
    "entrada": ("Fue Richard Alpert, profesor de Psicología en Harvard. Tras ser despedido viajó a la India, "
                "encontró a su maestro y volvió con otro nombre y un libro que muchos aún releen."),
    "tipo": "Pensamiento y espiritualidad",
    "nacio_iso": "1931-04-06", "murio_iso": "2019-12-22", "lugar": "Boston, Massachusetts",
    "datos": [("Nació", "6 de abril de 1931, Boston (Massachusetts)"),
              ("Murió", "22 de diciembre de 2019, Maui (Hawái), a los 88 años"),
              ("Ámbito", "psicología y espiritualidad"),
              ("Le debemos", "<em>Be Here Now</em> y la Fundación Hanuman")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Richard Alpert, profesor de Psicología en Harvard, despedido en mayo de 1963. En 1967 viajó "
                      "a la India y allí recibió el nombre de Ram Dass, «servidor de Dios»." + rr(1, 2)),
        ("Por qué importa", "<em>Be Here Now</em> (1971) vendió más de dos millones de ejemplares y llevó la espiritualidad "
                            "oriental a muchas personas." + rr(1, 3)),
        ("Su legado", "Fundó la Fundación Hanuman (1974) y cofundó Seva, una organización contra la ceguera "
                      "evitable." + rr(2, 3)),
        ("Por dónde empezar", "<em>Be Here Now</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Richard Alpert nació en Boston el 6 de abril de 1931. Fue profesor de Psicología en Harvard y, con Timothy Leary, participó en el Proyecto Psilocibina. Harvard lo despidió en mayo de 1963.{rr(1, 2)}</p>
<p>En 1967 viajó a la India. Allí, Bhagavan Das lo llevó hasta Neem Karoli Baba (Maharaj-ji), quien lo llamó Ram Dass, «servidor de Dios».{rr(2, 3)} Al volver, publicó <em>Be Here Now</em> (1971, Lama Foundation). En 1997 sufrió un ictus mientras terminaba <em>Still Here</em>; el documental <em>Fierce Grace</em> (2001) cuenta esa época.{rr(1, 4)}</p>
<p>Murió en Maui el 22 de diciembre de 2019, a los 88 años.{rr(1, 4)}</p>""",
    "aportaciones": f"""<h3>Be Here Now (1971)</h3>
<p>Un libro mezcla de relato, ilustraciones y consejos de práctica espiritual. Vendió más de dos millones de ejemplares.{r(1)}</p>
<h3>Servicio</h3>
<p>Fundó la Fundación Hanuman en 1974 (con el Prison Ashram Project), cofundó Seva (prevención de la ceguera) y la iniciativa Love Serve Remember.{rr(2, 3)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Ram Dass decía que las experiencias psicodélicas le habían mostrado una puerta, pero que no sabía cómo mantenerla abierta; la práctica espiritual y el servicio fueron su camino para sostener lo que había entrevisto. Para la psicología transpersonal es una figura puente entre la investigación y la espiritualidad vivida.</p>""",
    "cronologia": [
        ("1931", "Nace en Boston, el 6 de abril."),
        ("1960–1962", "Proyecto Psilocibina de Harvard, con Timothy Leary."),
        ("1963", "Harvard lo despide, en mayo."),
        ("1967", "Viaja a la India; Neem Karoli Baba lo llama Ram Dass."),
        ("1971", "Publica <em>Be Here Now</em>."),
        ("1974", "Funda la Fundación Hanuman."),
        ("1997", "Ictus mientras terminaba <em>Still Here</em>."),
        ("2001", "Documental <em>Fierce Grace</em>."),
        ("2019", "Muere en Maui, el 22 de diciembre."),
    ],
    "libros": [
        ("be-here-now", "Su libro más conocido."),
        ("being-ram-dass", "Su autobiografía."),
        ("birth-of-a-psychedelic-culture", "Con Ralph Metzner y Gary Bravo: sus primeros años."),
        ("lsd-alpert", "Sus primeros trabajos con LSD."),
    ],
    "relacion": [
        ("../timothy-leary/", "Timothy Leary", "Su colega del Proyecto Psilocibina."),
        ("../../sustancias/lsd/", "Guía del LSD", "Una de las sustancias de su primera etapa."),
        ("../alan-watts/", "Alan Watts", "Otra voz que acercó la espiritualidad oriental."),
    ],
    "refs": [
        'NPR. «Ram Dass, spiritual teacher and psychedelics pioneer, dies at 88» (2019). <a href="https://www.npr.org/2019/12/23/790769546/ram-dass-spiritual-teacher-and-psychedelics-pioneer-dies-at-88">https://www.npr.org/2019/12/23/790769546/ram-dass-spiritual-teacher-and-psychedelics-pioneer-dies-at-88</a>',
        'Ram Dass Foundation. Obituario. <a href="https://www.ramdass.org/obituary-ram-dass/">https://www.ramdass.org/obituary-ram-dass/</a>',
        'Lion’s Roar. «Ram Dass, spiritual pioneer, dies at 88». <a href="https://lionsroar.com/ram-dass-spiritual-pioneer-dies-at-88/">https://lionsroar.com/ram-dass-spiritual-pioneer-dies-at-88/</a>',
        'Courthouse News. «Baba Ram Dass, counterculture hero, dies at 88». <a href="https://www.courthousenews.com/baba-ram-dass-counterculture-hero-dies-at-88/">https://www.courthousenews.com/baba-ram-dass-counterculture-hero-dies-at-88/</a>',
    ],
}

WATTS = {
    "slug": "alan-watts", "nombre": "Alan Watts", "iniciales": "AW", "anio": 1915,
    "que": "el filósofo que explicó el budismo zen a Occidente",
    "tarjeta": "Filósofo británico. Explicó el zen y escribió sobre psicodélicos.",
    "desc": ("Alan Watts, el filósofo británico que acercó el budismo zen a Occidente y reflexionó sobre la "
             "experiencia psicodélica: su vida, su obra y por dónde empezar."),
    "alias": "Filósofo y divulgador (Chislehurst, 1915 – Druid Heights, 1973)",
    "entrada": ("Un británico instalado en California que explicó el zen y la filosofía oriental en libros, "
                "radio y televisión, y que escribió con lucidez sobre la experiencia psicodélica."),
    "tipo": "Pensamiento y espiritualidad",
    "nacio_iso": "1915-01-06", "murio_iso": "1973-11-16", "lugar": "Chislehurst, Kent",
    "datos": [("Nació", "6 de enero de 1915, Chislehurst (Kent)"),
              ("Murió", "16 de noviembre de 1973, Druid Heights (California)"),
              ("Ámbito", "filosofía y religiones comparadas"),
              ("Le debemos", "<em>El camino del zen</em> y <em>La alegre cosmología</em>")],
    "titulos": {"aportaciones": "Lo que escribió", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un filósofo británico que publicó su primer libro, <em>The Spirit of Zen</em>, en 1936, y se "
                      "trasladó a Estados Unidos en 1938." + rr(1, 2)),
        ("Por qué importa", "<em>The Way of Zen</em> (1957) fue para muchos lectores la puerta de entrada al "
                            "zen; más tarde escribió sobre psicodélicos y religión." + rr(1, 3)),
        ("Su voz", "Dio conferencias y programas de radio y televisión que aún se escuchan." + r(1)),
        ("Por dónde empezar", "<em>La alegre cosmología</em> y <em>Psicodélicos y experiencia religiosa</em>, "
                              "en la Biblioteca."),
    ],
    "vida": f"""<p>Alan Watts nació en Chislehurst (Kent) el 6 de enero de 1915. En 1936 publicó <em>The Spirit of Zen</em> y en 1938 se fue a Estados Unidos. Estudió en el seminario Seabury-Western, fue capellán episcopaliano en la Universidad Northwestern (1944–1950) y dejó la Iglesia en 1950. Después enseñó en la Academia Americana de Estudios Asiáticos, en San Francisco.{rr(1, 2)}</p>
<p>Murió el 16 de noviembre de 1973, dormido, en su cabaña de Druid Heights, cerca de Mill Valley (California).{rr(1, 3)}</p>""",
    "aportaciones": f"""<h3>El zen y la filosofía oriental</h3>
<p>Con <em>The Way of Zen</em> (1957) y <em>Psychotherapy East and West</em> (1961) acercó las filosofías de Asia a la psicología y al lector occidental.{rr(1, 2)}</p>
<h3>Los psicodélicos</h3>
<p>Escribió «The New Alchemy» (1958), <em>The Joyous Cosmology</em> (1962) y <em>Psychedelics and Religious Experience</em> (1968), donde reflexionó sobre qué puede decir una experiencia con estas sustancias sobre la vida religiosa.{rr(1, 2)}</p>
<h3>Radio y televisión</h3>
<p>Llevó sus ideas a un público muy amplio con programas de radio y televisión.{r(1)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Watts decía que una experiencia psicodélica no sustituye a la práctica espiritual: puede mostrar una dirección, pero lo que cuenta es lo que uno hace después. Por eso le interesaba más el sentido de la experiencia que la sustancia. Desde la psicología transpersonal, su obra une filosofía, psicoterapia y vida contemplativa de una forma muy accesible.</p>""",
    "cronologia": [
        ("1915", "Nace en Chislehurst (Kent), el 6 de enero."),
        ("1936", "Publica <em>The Spirit of Zen</em>."),
        ("1938", "Se traslada a Estados Unidos."),
        ("1944–1950", "Capellán episcopaliano en Northwestern; deja la Iglesia en 1950."),
        ("1957", "Publica <em>The Way of Zen</em>."),
        ("1962", "Publica <em>The Joyous Cosmology</em>."),
        ("1968", "Publica <em>Psychedelics and Religious Experience</em>."),
        ("1973", "Muere el 16 de noviembre en Druid Heights."),
    ],
    "libros": [
        ("the-joyous-cosmology", "Su libro más cercano a la experiencia psicodélica."),
        ("psychedelics-and-religious-experience-460", "Su reflexión sobre psicodélicos y religión."),
    ],
    "relacion": [
        ("../ram-dass/", "Ram Dass", "Otra voz que unió psicodélicos y espiritualidad."),
        ("../aldous-huxley/", "Aldous Huxley", "Un escritor con quien compartió intereses."),
        ("../../sustancias/lsd/", "Guía del LSD", "La sustancia de buena parte de su reflexión."),
    ],
    "refs": [
        'Encyclopaedia Britannica. «Alan Watts». <a href="https://www.britannica.com/biography/Alan-Watts">https://www.britannica.com/biography/Alan-Watts</a>',
        'Encyclopedia.com. «Alan Watts». <a href="https://www.encyclopedia.com/topic/Alan_Watts.aspx">https://www.encyclopedia.com/topic/Alan_Watts.aspx</a>',
        'Alan Watts Organization. Biografía. <a href="https://alanwatts.org/biography">https://alanwatts.org/biography</a>',
    ],
}

SHULGIN = {
    "slug": "ann-y-alexander-shulgin", "nombre": "Ann y Alexander Shulgin", "iniciales": "S", "anio": 1925,
    "que": "el matrimonio de químicos que exploró cientos de moléculas",
    "tarjeta": "Químico y terapeuta. Autores de PiHKAL y TiHKAL.",
    "desc": ("Ann y Alexander Shulgin, el matrimonio que exploró moléculas como la 2C-B, redescubrió la MDMA y "
             "escribió PiHKAL y TiHKAL: su vida, su obra y por dónde empezar."),
    "alias": "Químico y terapeuta (él, Berkeley, 1925 – Lafayette, 2014; ella, hasta 2022)",
    "entrada": ("Él fue un químico que pasó décadas diseñando y probando moléculas en su laboratorio; ella, su "
                "compañera de trabajo y de vida, exploró los usos terapéuticos de la MDMA y del 2C-B."),
    "tipo": "Ciencia",
    "nacio_iso": "1925-06-17", "murio_iso": "2014-06-02", "lugar": "Berkeley, California",
    "ld_personas": [
        {"name": "Alexander Shulgin", "birthDate": "1925-06-17", "deathDate": "2014-06-02",
         "birthPlace": "Berkeley, California", "description": "químico"},
        {"name": "Ann Shulgin", "deathDate": "2022-07-09", "description": "terapeuta y escritora"},
    ],
    "datos": [("Sasha", "Berkeley, 17 de junio de 1925 – Lafayette, 2 de junio de 2014"),
              ("Ann", "Murió en su casa el 9 de julio de 2022, a los 91 años"),
              ("Ámbito", "química y psicoterapia"),
              ("Les debemos", "<em>PiHKAL</em>, <em>TiHKAL</em> y el redescubrimiento de la MDMA")],
    "titulos": {"aportaciones": "Lo que hicieron", "mirada": "Su mirada"},
    "claves": [
        ("Quiénes fueron", "Alexander («Sasha») Shulgin, químico, y su esposa Ann, terapeuta. Se conocieron en "
                           "1978." + rr(1, 3)),
        ("Por qué importan", "Sasha redescubrió la MDMA (sintetizada en 1912) y se la presentó a Leo Zeff en 1977; "
                             "con David Nichols publicó en 1978 el primer informe en humanos." + rr(1, 3)),
        ("Su obra", "<em>PiHKAL</em> (1991) y <em>TiHKAL</em> (1997), con la descripción de cientos de moléculas, "
                    "y <em>The Shulgin Index</em> (2011)." + rr(1, 3)),
        ("Por dónde empezar", "<em>PiHKAL</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Alexander Shulgin nació en Berkeley el 17 de junio de 1925. Se doctoró en Berkeley en 1955 y trabajó en Bio-Rad y después en Dow Chemical. Allí creó Zectran, el primer pesticida biodegradable, un éxito que le dio libertad para investigar por su cuenta. Su primera experiencia con mescalina fue en 1960. Montó un laboratorio detrás de su casa.{rr(1, 2)}</p>
<p>Ann y Sasha se conocieron en 1978. Murió él en Lafayette el 2 de junio de 2014, tras una demencia desde 2010 y un cáncer de hígado. Ann murió en su casa el 9 de julio de 2022, a los 91 años.{rr(1, 3)}</p>""",
    "aportaciones": f"""<h3>La MDMA</h3>
<p>La molécula se había sintetizado en 1912. Sasha la redescubrió: en 1977 se la presentó a <a href="../leo-zeff/">Leo Zeff</a> y en 1978 publicó con David Nichols el primer informe sobre sus efectos en humanos. Ann exploró sus usos terapéuticos, y también los del 2C-B.{rr(2, 3)}</p>
<h3>Familias de moléculas</h3>
<p>Su laboratorio estudió familias como la 2C (de la que sale el 2C-B) y la DOx (de la que sale el DOM). Hablaban de «la mágica posición 4» de la molécula.{r(1)}</p>
<h3>Los libros</h3>
<p><em>PiHKAL</em> (1991) y <em>TiHKAL</em> (1997), en su propia editorial, Transform Press, mezclan novela autobiográfica y fichas de síntesis. <em>The Shulgin Index</em> (2011) reúne los datos.{rr(1, 3)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas y nuestra lectura. No son hechos comprobados.</em></p>
<p>Los Shulgin defendían una exploración cuidadosa y responsable, con la propia persona como instrumento de observación, y la libertad de investigar la mente. Es una postura que no todos comparten, y sus textos no son una guía de uso.</p>
<p>Desde la psicología humanista, interesa su insistencia en la atención y en la honestidad con lo que ocurre en la experiencia.</p>""",
    "cronologia": [
        ("1925", "Nace Sasha el 17 de junio en Berkeley."),
        ("1955", "Doctorado en Berkeley."),
        ("1960", "Primera experiencia con mescalina."),
        ("1977", "Presenta la MDMA a Leo Zeff."),
        ("1978", "Informe en humanos con David Nichols; Sasha y Ann se conocen."),
        ("1991", "<em>PiHKAL</em>."),
        ("1997", "<em>TiHKAL</em>."),
        ("2011", "<em>The Shulgin Index</em>."),
        ("2014", "Muere Sasha el 2 de junio."),
        ("2022", "Muere Ann el 9 de julio."),
    ],
    "libros": [
        ("p-i-h-k-a-l-una-historia-quimica-de-amor-682", "<em>PiHKAL</em> en español."),
        ("pihkal", "<em>PiHKAL</em>, edición original."),
        ("tihkal", "La continuación, centrada en triptaminas."),
        ("the-shulgin-index-volume-one", "El índice de datos."),
        ("the-simple-plant-isoquinolines", "Sobre las isoquinolinas de plantas."),
    ],
    "relacion": [
        ("../leo-zeff/", "Leo Zeff", "El terapeuta al que Sasha presentó la MDMA."),
        ("../../sustancias/mdma/", "Guía de la MDMA", "La molécula que redescubrió."),
        ("../../sustancias/2c-b/", "Guía del 2C-B", "Una de las moléculas que exploraron."),
    ],
    "refs": [
        'Erowid. Obituario de Alexander Shulgin. <a href="https://erowid.org/characters/shulgin_alexander/shulgin_alexander_obituary1.shtml">https://erowid.org/characters/shulgin_alexander/shulgin_alexander_obituary1.shtml</a>',
        'UC Berkeley News. «Hail and farewell to a legendary Cal grad» (2014). <a href="https://blogs.berkeley.edu/2014/06/09/hail-and-farewell-to-a-legendary-cal-grad/">https://blogs.berkeley.edu/2014/06/09/hail-and-farewell-to-a-legendary-cal-grad/</a>',
        'MAPS. «In memoriam: Ann Shulgin» (2022). <a href="https://maps.org/news/bulletin/in-memoriam-ann-shulgin-forerunner-of-todays-psychedelic-re-emergence-dies-at-91/">https://maps.org/news/bulletin/in-memoriam-ann-shulgin-forerunner-of-todays-psychedelic-re-emergence-dies-at-91/</a>',
        'openDemocracy. «Alexander Theodore Shulgin 1925–2014». <a href="https://www.opendemocracy.net/en/alexander-theodore-shulgin-19252014/">https://www.opendemocracy.net/en/alexander-theodore-shulgin-19252014/</a>',
    ],
}

ZEFF = {
    "slug": "leo-zeff", "nombre": "Leo Zeff", "iniciales": "LZ", "anio": 1912,
    "que": "el terapeuta que llevó la MDMA a la psicoterapia",
    "tarjeta": "Psicólogo de Oakland. El «jefe secreto» de la terapia con MDMA.",
    "desc": ("Leo Zeff, el psicólogo de Oakland conocido como «el jefe secreto», que llevó la MDMA a la psicoterapia "
             "y formó a decenas de terapeutas: vida, método y lecturas."),
    "alias": "Psicólogo (1912 – 1988)",
    "entrada": ("Un psicólogo junguiano de Oakland que usó LSD desde 1961, conoció la MDMA en 1977 y, de manera "
                "discreta, formó a más de 150 terapeutas."),
    "tipo": "Psicología y terapia",
    "nacio_iso": "1912-05-14", "murio_iso": "1988-04-13",
    "datos": [("Nació", "14 de mayo de 1912"),
              ("Murió", "13 de abril de 1988, a los 75 años"),
              ("Ámbito", "psicoterapia"),
              ("Le debemos", "difundir la MDMA como herramienta terapéutica")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un psicólogo de Oakland (California), de formación junguiana." + r(1)),
        ("Por qué importa", "Usó el LSD en terapia desde 1961 y, en 1977, a punto de jubilarse, conoció la MDMA "
                            "por Sasha Shulgin. La llamó «Adam»." + rr(1, 2)),
        ("Su método", "Según Stolaroff y Passie, la llevó a unas 4.000 personas y formó a más de 150 "
                      "terapeutas, con un estilo no directivo." + rr(2, 3)),
        ("Por dónde empezar", "<em>The Secret Chief Revealed</em> (MAPS, 2004), en la Biblioteca."),
    ],
    "vida": f"""<p>Leo Zeff nació el 14 de mayo de 1912 y murió el 13 de abril de 1988, a los 75 años. Fue psicólogo en Oakland, de formación junguiana. Empezó a usar el LSD en terapia en 1961, después de que sus pacientes le hablaran de sus experiencias.{rr(1, 2)}</p>
<p>En 1977, cuando estaba a punto de jubilarse, <a href="../ann-y-alexander-shulgin/">Sasha Shulgin</a> le presentó la MDMA. La llamó «Adam».{rr(1, 2)} Trabajó de forma discreta y, con el seudónimo «Jacob», contó su experiencia en <em>The Secret Chief</em> (1997). Después se publicó <em>The Secret Chief Revealed</em> (MAPS, 2004). En <em>PiHKAL</em> aparece como «Adam Fisher».{rr(1, 2)}</p>""",
    "aportaciones": f"""<h3>La MDMA en la psicoterapia</h3>
<p>Según Stolaroff y Passie, Zeff llevó la MDMA a unas 4.000 personas y formó a más de 150 terapeutas.{rr(2, 3)}</p>
<h3>Un estilo no directivo</h3>
<p>Su forma de acompañar era no directiva: acompañaba sin dirigir la experiencia ni imponer interpretaciones. Hay un paralelismo claro con el enfoque centrado en la persona de Carl Rogers.{r(4)}</p>""",
    "mirada": f"""<p><em>Esta sección es una lectura de APDER. No son hechos comprobados.</em></p>
<p>Desde la psicología humanista, el estilo de Zeff interesa porque confía en la capacidad de la persona de moverse hacia su propia sanación si se le ofrece un espacio seguro. Con su base junguiana, daba también valor a lo simbólico. Sus cifras son estimaciones de personas que lo conocieron, no resultados de estudios controlados.</p>""",
    "cronologia": [
        ("1912", "Nace el 14 de mayo."),
        ("1961", "Empieza a usar LSD en terapia."),
        ("1977", "Sasha Shulgin le presenta la MDMA."),
        ("1988", "Muere el 13 de abril, a los 75 años."),
        ("1997", "Se publica <em>The Secret Chief</em>."),
        ("2004", "Se publica <em>The Secret Chief Revealed</em> (MAPS)."),
    ],
    "libros": [
        ("the-secret-chief-revealed-655", "Su historia, ya con nombre."),
        ("the-secret-chief", "Las entrevistas con el seudónimo «Jacob»."),
    ],
    "relacion": [
        ("../ann-y-alexander-shulgin/", "Ann y Alexander Shulgin", "Quienes le presentaron la MDMA."),
        ("../../sustancias/mdma/", "Guía de la MDMA", "La molécula con la que trabajó."),
        ("../../terapia-asistida-mdma/", "Terapia con MDMA", "Cómo se usa hoy en investigación."),
    ],
    "refs": [
        'Erowid. «Leo Zeff», Erowid Character Vaults. <a href="https://erowid.org/characters/zeff_leo/">https://erowid.org/characters/zeff_leo/</a>',
        'Erowid. Reseña de <em>The Secret Chief</em>. <a href="https://erowid.org/library/review/review.php?ID=195">https://erowid.org/library/review/review.php?ID=195</a>',
        'Passie T. The early use of MDMA («Adam») in psychotherapy in the USA and Europe. <em>Drug Science, Policy and Law</em>. 2018;4. doi:<a href="https://doi.org/10.1177/2050324518767442">10.1177/2050324518767442</a>.',
        'Lucid News. «Leo Zeff and the non-directive style of being a psychedelic guide». <a href="https://www.lucid.news/leo-zeff-and-the-non-directive-style-of-being-a-psychedelic-guide/">https://www.lucid.news/leo-zeff-and-the-non-directive-style-of-being-a-psychedelic-guide/</a>',
    ],
}
