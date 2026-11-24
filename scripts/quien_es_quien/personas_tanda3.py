# «Quién es quién» · tanda 3 (España y Latinoamérica). Datos verificados el 24-11-2026; fuentes al final de cada ficha.
# Cuando las fuentes no coinciden (fechas de nacimiento de Mestre Irineu y Pablo Amaringo), se dice en el texto.
# Si no hay fecha de nacimiento publicada con fuente, no se pone «nacio_iso»; «anio» solo sirve para ordenar la portada.
from contenido import r, rr

NARANJO = {
    "slug": "claudio-naranjo", "nombre": "Claudio Naranjo", "iniciales": "CN", "anio": 1932,
    "que": "el psiquiatra chileno que unió psicoterapia, espiritualidad y psicodélicos",
    "tarjeta": "Psiquiatra chileno. Creó el programa SAT y escribió <em>The Healing Journey</em>.",
    "desc": ("Claudio Naranjo, el psiquiatra chileno pionero de la terapia psicodélica y creador del programa "
             "SAT: su vida, sus aportaciones y por dónde empezar a leerle."),
    "alias": "Psiquiatra y psicoterapeuta (Valparaíso, 1932 – Berkeley, 2019)",
    "entrada": ("Médico chileno que pasó su vida tendiendo puentes entre la psicoterapia, las tradiciones "
                "espirituales y la experiencia psicodélica. Su programa SAT formó a generaciones de terapeutas "
                "en España y Latinoamérica."),
    "tipo": "Psicología y terapia",
    "nacio_iso": "1932-11-24", "murio_iso": "2019-07-12", "lugar": "Valparaíso, Chile",
    "datos": [("Nació", "24 de noviembre de 1932, Valparaíso (Chile)"),
              ("Murió", "12 de julio de 2019, Berkeley (California), a los 86 años"),
              ("Ámbito", "psiquiatría, psicoterapia y espiritualidad"),
              ("Le debemos", "<em>The Healing Journey</em> y el programa SAT")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un psiquiatra chileno, formado en la Universidad de Chile, considerado un pionero en unir "
                      "psicoterapia y tradiciones espirituales." + rr(1, 2)),
        ("Por qué importa", "Participó en el grupo de terapia psicodélica de Leo Zeff y estudió la harmalina, la MDA "
                            "y la ibogaína como ayudas para la psicoterapia." + rr(2, 4)),
        ("Su legado", "El programa SAT, que reúne terapia Gestalt, eneagrama, meditación y música, y por el que "
                      "han pasado muchos terapeutas Gestalt de España y Latinoamérica." + rr(2, 7)),
        ("Por dónde empezar", "<em>The Healing Journey</em> y <em>Ayahuasca</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Claudio Naranjo nació en Valparaíso (Chile) el 24 de noviembre de 1932. Estudió Medicina en la Universidad de Chile, donde se tituló en 1959. Más tarde dio clases en Harvard.{rr(2, 3)}</p>
<p>En los años sesenta, en California, entró en contacto con buena parte de los pioneros de la investigación psicodélica: Leo Zeff, Stanislav Grof, Michael Harner o Willis Harman.{r(4)} A comienzos de los setenta formó en Chile un grupo que empezó como una improvisación y acabó convertido en programa: el SAT (<em>Seekers After Truth</em>, «buscadores de la verdad»). En 1987 lo refundó en España.{r(2)}</p>
<p>En enero de 2019 publicó sus memorias, <em>Ascenso y descenso de la montaña sagrada</em>.{r(3)} Su última gran charla fue en la Conferencia Mundial de Ayahuasca de Girona, ese mismo año, ya afectado por el párkinson.{r(5)} Murió en su casa de Berkeley el 12 de julio de 2019, a los 86 años.{rr(1, 2)}</p>""",
    "aportaciones": f"""<h3>La terapia psicodélica</h3>
<p>En el grupo de Leo Zeff (1965–1966) y en su propia práctica exploró sustancias poco estudiadas entonces, como la harmalina, la MDA y la ibogaína, como ayudas para la psicoterapia.{r(2)} Lo contó en <em>The Healing Journey</em> (1973).{r(1)}</p>
<h3>El programa SAT</h3>
<p>Reúne la terapia Gestalt y su supervisión, las aplicaciones del eneagrama a la personalidad, la meditación, la música como recurso terapéutico y el autoconocimiento guiado.{rr(2, 5)} En el mundo hispano de la Gestalt es una referencia: muchos terapeutas han pasado por él.{r(7)}</p>
<h3>El eneagrama</h3>
<p>Desarrolló el eneagrama como descripción de tipos de carácter y le dedicó varios libros, como <em>Carácter y neurosis</em> y <em>El eneagrama de la sociedad</em>.{rr(3, 6)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Naranjo veía en los psicodélicos un catalizador, no una cura en sí: abren una puerta que la persona tiene que aprender a cruzar con trabajo terapéutico y práctica espiritual. Creía que una sociedad más sana necesitaba personas más conscientes, y por eso dedicó sus últimos años a proponer cambios en la educación.{r(3)}</p>
<p>Desde la psicología humanista, su obra es un puente entre la Gestalt y lo transpersonal. En los últimos años también se han publicado críticas sobre el clima de algunos grupos SAT; conviene leerle con espíritu crítico.{r(7)}</p>""",
    "cronologia": [
        ("1932", "Nace en Valparaíso, el 24 de noviembre."),
        ("1959", "Se titula en Medicina en la Universidad de Chile."),
        ("1965–1966", "Forma parte del grupo de terapia psicodélica de Leo Zeff."),
        ("1973", "Publica <em>The Healing Journey</em>."),
        ("Años setenta", "Nace el programa SAT."),
        ("1987", "Refunda el SAT en España."),
        ("2019", "Publica sus memorias; muere en Berkeley el 12 de julio."),
    ],
    "libros": [
        ("the-healing-journey", "Su libro clásico sobre terapia psicodélica."),
        ("my-psychedelic-explorations", "Sus exploraciones con distintas sustancias, publicadas tras su muerte."),
        ("ayahuasca-naranjo", "Sus escritos sobre la ayahuasca."),
    ],
    "relacion": [
        ("../leo-zeff/", "Leo Zeff", "El terapeuta en cuyo grupo participó."),
        ("../stanislav-grof/", "Stanislav Grof", "Otro pionero con quien compartió camino."),
        ("../../sustancias/ibogaina/", "Guía de la ibogaína", "Una de las sustancias que estudió."),
    ],
    "refs": [
        'MAPS. «In memoriam: Claudio Naranjo, M.D.» (2019). <a href="https://maps.org/?p=11016">https://maps.org/?p=11016</a>',
        'Wikipedia (en inglés). «Claudio Naranjo» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Claudio_Naranjo">https://en.wikipedia.org/wiki/Claudio_Naranjo</a>',
        'La Tercera. «La partida del psiquiatra que dio clases en Harvard y fue precursor de las drogas en psicoterapia» (2019). <a href="https://www.latercera.com/que-pasa/noticia/la-partida-del-psiquiatra-que-dio-clases-en-harvard-y-fue-precursor-de-las-drogas-en-psicoterapia/738461/">https://www.latercera.com/que-pasa/noticia/la-partida-del-psiquiatra-que-dio-clases-en-harvard-y-fue-precursor-de-las-drogas-en-psicoterapia/738461/</a>',
        'Erowid. «Claudio Naranjo». <a href="https://www.erowid.org/characters/naranjo_claudio/naranjo_claudio.shtml">https://www.erowid.org/characters/naranjo_claudio/naranjo_claudio.shtml</a>',
        'Badiner A. «The world of Claudio Naranjo». Psychedelics Today. <a href="https://psychedelicstoday.com/?p=6148">https://psychedelicstoday.com/?p=6148</a>',
        'Meer. «Claudio Naranjo» (nota biográfica). <a href="https://www.meer.com/es/authors/184-claudio-naranjo">https://www.meer.com/es/authors/184-claudio-naranjo</a>',
        'Evans J, Krecké J. «Does Dionysian Gestalt have an abuse problem? On Claudio Naranjo’s Seekers After Truth course». Ecstatic Integration (12 de abril de 2024). <a href="https://www.ecstaticintegration.org/p/does-dionysian-gestalt-have-an-abuse">https://www.ecstaticintegration.org/p/does-dionysian-gestalt-have-an-abuse</a>',
    ],
}

ROQUET = {
    "slug": "salvador-roquet", "nombre": "Salvador Roquet", "iniciales": "SR", "anio": 1920,
    "que": "el psiquiatra mexicano que llevó la sabiduría de los curanderos a la clínica",
    "tarjeta": "Psiquiatra mexicano. Creó la psicosíntesis con medicinas tradicionales.",
    "desc": ("Salvador Roquet, el psiquiatra mexicano que aprendió de curanderos y creó la psicosíntesis, una "
             "terapia psicodélica en grupo: su vida y su método."),
    "alias": "Psiquiatra (Veracruz, 1920 – 1995)",
    "entrada": ("Médico de salud pública y luego psiquiatra, recorrió México aprendiendo de curanderos y "
                "chamanes, y con lo aprendido creó una terapia en grupo muy intensa que hoy casi nadie recuerda."),
    "tipo": "Psicología y terapia",
    "nacio_iso": "1920", "murio_iso": "1995", "lugar": "Veracruz, México",
    "datos": [("Nació", "1920, Veracruz (México)"),
              ("Murió", "1995"),
              ("Ámbito", "psiquiatría y terapia psicodélica en grupo"),
              ("Le debemos", "la psicosíntesis (sin relación con la de Assagioli)")],
    "titulos": {"aportaciones": "Su método", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un psiquiatra mexicano que, entre 1967 y 1974, trabajó con curanderos de todo México y "
                      "dirigió en la capital una clínica de terapia psicodélica en grupo." + rr(1, 2)),
        ("Por qué importa", "Unió el saber de los curanderos con la psicoterapia occidental y atendió a cientos de "
                            "pacientes; el psicólogo Stanley Krippner lo recuerda como un innovador." + rr(1, 2)),
        ("Su frase", "Decía que las sustancias no eran más que la plataforma de lanzamiento: lo importante era "
                     "lo que venía después." + r(2)),
        ("Por dónde empezar", "El artículo de Stanley Krippner en Chacruna y el de Alberto Villoldo (1977)."),
    ],
    "vida": f"""<p>Salvador Roquet nació en Veracruz en 1920.{r(1)} Fue médico de salud pública antes de hacerse psiquiatra, y se psicoanalizó con Erich Fromm.{rr(2, 5)}</p>
<p>En 1957 participó como voluntario en un estudio con mescalina del doctor José Rodríguez, en un sanatorio psiquiátrico de la Ciudad de México. La experiencia le asustó y le paralizó, pero con el tiempo llegó a la conclusión de que estas sustancias podían ser herramientas muy poderosas para la psiquiatría.{r(4)}</p>
<p>Su Clínica de Psicosíntesis funcionó en la Ciudad de México de 1967 a 1974.{rr(2, 4)} En sus últimos años dirigió «convivencias» sin sustancias y dio talleres y conferencias. Murió en 1995.{r(2)}</p>""",
    "aportaciones": f"""<h3>Aprender de los curanderos</h3>
<p>Entre 1967 y 1974 trabajó con curanderos y chamanes de distintos lugares de México.{r(1)} Según Krippner, colaboró durante años con María Sabina y en 1980 organizó un viaje a Huautla de Jiménez para trabajar con otra curandera, doña Clotilde.{r(2)}</p>
<h3>La psicosíntesis</h3>
<p>Llamó a su método «psicosíntesis», sin relación con la de Roberto Assagioli.{r(3)} Las sesiones duraban unas ocho horas y se hacían en grupo, a veces con decenas de personas: un encuentro previo, yoga o meditación, y después una estimulación sensorial intensa con diapositivas, películas, música y luces, acompañada de distintas sustancias, entre ellas setas, peyote, semillas de ololiuqui, LSD y ketamina.{rr(1, 2, 5)}</p>
<p>A cada sesión le seguía un trabajo de integración, por lo general de diez a treinta encuentros mensuales.{r(2)} Usaba también la Gestalt, el psicodrama, el arte y la bioenergética.{r(1)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Roquet creía que la sustancia solo abría la puerta: el trabajo de verdad estaba en la integración, en el grupo y en lo que la persona hacía con lo vivido. Por eso, en sus últimos años, buscó reproducir esas vivencias sin sustancias.{r(2)} En una de sus frases más citadas decía que en la muerte se puede sentir el amor y que, cuando se siente el amor, la muerte queda vencida.{r(2)}</p>
<p>Desde la psicología humanista y transpersonal, su método recuerda dos cosas: la importancia del acompañamiento y la deuda que la terapia psicodélica tiene con los saberes tradicionales. Su forma de trabajar, muy intensa, también invita a pensar en los límites del cuidado.</p>""",
    "cronologia": [
        ("1920", "Nace en Veracruz."),
        ("1957", "Participa en un estudio con mescalina en la Ciudad de México."),
        ("1967", "Abre su Clínica de Psicosíntesis en la Ciudad de México."),
        ("1971", "Stanley Krippner asiste a una de sus sesiones en grupo."),
        ("1974", "Termina la etapa de la clínica."),
        ("1977", "Alberto Villoldo publica una introducción a su método."),
        ("1980", "Organiza un viaje a Huautla de Jiménez."),
        ("1995", "Muere."),
    ],
    "libros": [
        ("the-peyote-effect-548", "Una historia del peyote en México que sitúa su trabajo en la psiquiatría mexicana."),
    ],
    "relacion": [
        ("../maria-sabina/", "María Sabina", "La sabia mazateca con quien colaboró."),
        ("../../sustancias/ketamina/", "Guía de la ketamina", "Una de las sustancias que usó."),
        ("../claudio-naranjo/", "Claudio Naranjo", "Otro psiquiatra latinoamericano pionero."),
    ],
    "refs": [
        'Erowid. «Salvador Roquet». <a href="https://www.erowid.org/culture/characters/roquet_salvador">https://www.erowid.org/culture/characters/roquet_salvador</a>',
        'Krippner S. «Salvador Roquet remembered: an innovative psychedelic therapist in 1960s Mexico». Chacruna (2017). <a href="https://chacruna.net/?p=1281">https://chacruna.net/?p=1281</a>',
        'Villoldo A. An introduction to the psychedelic psychotherapy of Salvador Roquet. <em>Journal of Humanistic Psychology</em>. 1977;17(4):45-58. <a href="https://doi.org/10.1177/002216787701700406">https://doi.org/10.1177/002216787701700406</a>',
        'Dawson AS. <em>The peyote effect: from the Inquisition to the War on Drugs</em>. University of California Press; 2018. Capítulo sobre la psiquiatría mexicana. <a href="https://www.sciencegate.app/document/10.1525/california/9780520285422.003.0008">https://www.sciencegate.app/document/10.1525/california/9780520285422.003.0008</a>',
        'MAPS, bibliografía. Texto sobre el Instituto de Psicosíntesis y sus pacientes. <a href="https://bibliography.maps.org/resources/download/8596">https://bibliography.maps.org/resources/download/8596</a>',
    ],
}

GUZMAN = {
    "slug": "gaston-guzman", "nombre": "Gastón Guzmán", "iniciales": "GG", "anio": 1932,
    "que": "el micólogo mexicano que más sabía de las setas Psilocybe",
    "tarjeta": "Micólogo mexicano. La gran autoridad mundial en el género <em>Psilocybe</em>.",
    "desc": ("Gastón Guzmán, el micólogo mexicano que describió decenas de especies de Psilocybe y estudió los "
             "hongos sagrados de México: su vida, su obra y sus libros."),
    "alias": "Micólogo (Xalapa, 1932 – 2016)",
    "entrada": ("Pasó sesenta años recorriendo bosques, describiendo hongos y formando micólogos. Si hoy sabemos "
                "cuántas setas con psilocibina existen y dónde crecen, es en buena parte gracias a él."),
    "tipo": "Ciencia",
    "nacio_iso": "1932-08-26", "murio_iso": "2016-01-12", "lugar": "Xalapa, Veracruz",
    "datos": [("Nació", "26 de agosto de 1932, Xalapa (Veracruz, México)"),
              ("Murió", "12 de enero de 2016, a los 83 años"),
              ("Ámbito", "micología y etnomicología"),
              ("Le debemos", "<em>The genus Psilocybe</em> (1983) y dos grandes herbarios de hongos")],
    "titulos": {"aportaciones": "Lo que descubrió", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Un biólogo mexicano, doctor por el Instituto Politécnico Nacional, considerado una "
                      "autoridad mundial en el género <em>Psilocybe</em>." + r(1)),
        ("Por qué importa", "Su monografía de 1983 reunió 144 especies de <em>Psilocybe</em>, 91 de ellas "
                            "alucinógenas; antes se conocían una veintena." + r(2)),
        ("Su legado", "Fundó dos herbarios de hongos, cofundó la Sociedad Mexicana de Micología y formó a más de "
                      "25 especialistas en América Latina." + r(1)),
        ("Por dónde empezar", "<em>The genus Psilocybe</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Gastón Guzmán Huerta nació en Xalapa (Veracruz) el 26 de agosto de 1932. Estudió Biología en la Escuela Nacional de Ciencias Biológicas del Instituto Politécnico Nacional, donde se licenció en 1959 y se doctoró en 1967.{r(1)}</p>
<p>A finales de 1956 recibió el encargo de recolectar hongos alucinógenos para unos laboratorios suizos. En 1957 acompañó al micólogo Rolf Singer por Oaxaca y el Estado de México, y en 1958 siguió solo por el sureste y el centro del país. Ese año publicó su primer artículo.{rr(1, 2)}</p>
<p>En 1982 se trasladó a Xalapa para organizar la colección de hongos de lo que hoy es el Instituto de Ecología (INECOL), donde fue investigador emérito. Murió el 12 de enero de 2016, a los 83 años.{rr(1, 3)}</p>""",
    "aportaciones": f"""<h3>El género Psilocybe</h3>
<p>Su gran obra, <em>The genus Psilocybe</em> (1983), describió 144 especies, 91 de ellas alucinógenas. Hasta entonces, los estudios de Singer y Smith o de Heim y Wasson trataban una veintena como mucho. Publicó un suplemento en 1995. A lo largo de su vida describió más de 80 especies nuevas.{r(2)}</p>
<h3>Etnomicología</h3>
<p>Estudió el hábitat y la distribución de las setas sagradas de México, recogió sus nombres en lenguas indígenas y aclaró que «teonanácatl» es una palabra de los aztecas que no conviene aplicar a todos los pueblos de México. En 1975 estudió con Wasson una iglesia de Chignahuapan (Puebla) dedicada a un hongo, y en 1976 colaboró con Jonathan Ott en la medición de psilocibina en varias especies.{r(2)}</p>
<h3>Maestro y fundador</h3>
<p>Publicó 428 trabajos, dirigió 105 tesis y formó a más de 25 especialistas en México, Brasil, Colombia y Guatemala. Fundó la colección micológica del Politécnico (1955), con más de 120&nbsp;000 ejemplares, y la del INECOL, con unos 55&nbsp;000. Cofundó en 1965 la Sociedad Mexicana de Micología y creó la revista que hoy es la <em>Revista Mexicana de Micología</em>.{r(1)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER.</em></p>
<p>Guzmán representa una forma de ciencia paciente y de campo: caminar, recolectar, describir y nombrar. Su trabajo permitió distinguir unas especies de otras y entender que las setas sagradas forman parte de la vida de muchos pueblos, cada uno con su lengua y sus nombres. Esa precisión es también una forma de respeto hacia esos saberes.</p>""",
    "cronologia": [
        ("1932", "Nace en Xalapa, el 26 de agosto."),
        ("1955", "Funda la colección micológica de la ENCB del Politécnico."),
        ("1957", "Acompaña a Rolf Singer en busca de hongos sagrados."),
        ("1958", "Publica su primer artículo."),
        ("1965", "Cofunda la Sociedad Mexicana de Micología."),
        ("1967", "Se doctora en el Instituto Politécnico Nacional."),
        ("1982", "Se traslada a Xalapa para organizar la colección del actual INECOL."),
        ("1983", "Publica <em>The genus Psilocybe</em>."),
        ("2016", "Muere el 12 de enero."),
    ],
    "libros": [
        ("the-genus-psilocybe", "Su monografía sobre el género."),
    ],
    "relacion": [
        ("../../sustancias/psilocibina/", "Guía de las setas de psilocibina", "Las setas que estudió toda su vida."),
        ("../maria-sabina/", "María Sabina", "La sabia mazateca de las setas sagradas."),
        ("../valentina-y-gordon-wasson/", "Valentina y Gordon Wasson", "Con Gordon Wasson estudió la iglesia de Chignahuapan."),
    ],
    "refs": [
        'Mata G, Salmones D. In memoriam: Gastón Guzmán (1932-2016). <em>Revista Mexicana de Micología</em>. 2016;43:51-53. <a href="https://www.scielo.org.mx/pdf/rmm/v43/0187-3180-rmm-43-00051.pdf">https://www.scielo.org.mx/pdf/rmm/v43/0187-3180-rmm-43-00051.pdf</a>',
        'Mata G, Trigos A, Salmones D. Aportaciones de Gastón Guzmán al conocimiento de los hongos alucinógenos. <em>Revista Mexicana de Micología</em>. 2005;21:5-9. <a href="https://scientiafungorum.org.mx/index.php/micologia/article/download/949/1129/2758">https://scientiafungorum.org.mx/index.php/micologia/article/download/949/1129/2758</a>',
        'Universidad de Guadalajara. «Simposio en homenaje a la memoria del doctor Gastón Guzmán 1932-2016». <a href="https://comsoc.udg.mx/printpdf/47217">https://comsoc.udg.mx/printpdf/47217</a>',
    ],
}

FERICGLA = {
    "slug": "josep-maria-fericgla", "nombre": "Josep Maria Fericgla", "iniciales": "JF", "anio": 1948,
    "que": "el antropólogo catalán de la ayahuasca y los estados de consciencia",
    "tarjeta": "Antropólogo catalán. Convivió con los shuar y estudia los estados de consciencia.",
    "desc": ("Josep Maria Fericgla, el antropólogo catalán que convivió con los shuar de Ecuador y estudia la "
             "ayahuasca y los estados de consciencia: su obra y sus libros."),
    "alias": "Antropólogo y etnopsicólogo (Cataluña)",
    "entrada": ("Doctor en Antropología, vivió con los shuar de la Amazonía ecuatoriana y dedicó su carrera a "
                "estudiar los chamanismos, los ritos de paso y los estados modificados de consciencia."),
    "tipo": "Ciencia",
    "datos": [("Ámbito", "antropología cultural y etnopsicología"),
              ("Campo", "con los shuar de la Alta Amazonía ecuatoriana"),
              ("Le debemos", "<em>Al trasluz de la ayahuasca</em> y <em>Los jíbaros, cazadores de sueños</em>")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada"},
    "claves": [
        ("Quién es", "Un doctor en Antropología cultural y etnopsicólogo, especialista en chamanismos y "
                     "experiencias extáticas, que ha sido profesor en Barcelona, Salamanca y América." + r(2)),
        ("Por qué importa", "Su trabajo de campo con los shuar y sus libros sobre la ayahuasca son una referencia "
                            "en español." + rr(3, 5)),
        ("Su legado", "Ha dirigido la Societat d’Etnopsicologia Aplicada i Estudis Cognitius y en 1994 organizó "
                      "en Lleida un gran congreso internacional sobre estados de consciencia." + rr(1, 4)),
        ("Por dónde empezar", "<em>Los jíbaros, cazadores de sueños</em>, su diario de campo, en la Biblioteca."),
    ],
    "vida": f"""<p>Josep Maria Fericgla es doctor en Antropología cultural y etnopsicólogo. Ha sido profesor en la Universidad de Barcelona, en la de Salamanca y en varias universidades americanas.{r(2)}</p>
<p>Vivió una larga temporada con el pueblo shuar (los «jíbaros») de la Alta Amazonía ecuatoriana. Su diario de aquella estancia se publicó en catalán en 1994 y después en castellano y otros idiomas.{r(3)}</p>
<p>En octubre de 1994 dirigió en el Institut d’Estudis Ilerdencs de Lleida el II Congreso Internacional para el Estudio de los Estados Modificados de Consciencia, con más de sesenta especialistas de veinte países.{r(1)} Ha dirigido la Societat d’Etnopsicologia Aplicada i Estudis Cognitius y fundó el centro Can Benet Vives, donde da talleres y seminarios.{rr(4, 6)}</p>""",
    "aportaciones": f"""<h3>La ayahuasca vista desde la antropología</h3>
<p><em>Al trasluz de la ayahuasca</em> (1997) se presentó como el primer libro transdisciplinar sobre los efectos de la ayahuasca en la mente humana: une su trabajo de campo con los shuar y la antropología cognitiva.{r(5)} Más tarde escribió <em>Ayahuasca, la realidad detrás de la realidad</em> (2018), sobre sus usos en psicoterapia y en el cultivo del mundo interior.</p>
<h3>Chamanismos y ritos de paso</h3>
<p>En <em>Los chamanismos a revisión</em> repasa el chamanismo de la vía del éxtasis a internet y critica con ironía algunas formas de neochamanismo y el «supermercado de creencias» de la sociedad actual.{r(2)}</p>
<h3>Un puente hacia la investigación clínica</h3>
<p>Fue él quien puso en contacto al farmacólogo Jordi Riba con grupos que usaban ayahuasca en España, algo que influyó en la decisión de Riba de investigarla.{r(7)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Fericgla sostiene que las experiencias intensas y bien enmarcadas, como los ritos de paso, ayudan a estructurar a la persona y a la sociedad, y que su falta deja un vacío que nuestra cultura no sabe llenar. Es crítico con la espiritualidad de consumo y con el «supermercado de creencias».{r(2)} Desde la psicología transpersonal, su obra recuerda que la experiencia visionaria siempre se da dentro de una cultura que le da forma y sentido.</p>""",
    "cronologia": [
        ("1994", "Publica en catalán su diario entre los shuar y <em>El hongo y la génesis de las culturas</em>; dirige en Lleida el II Congreso Internacional para el Estudio de los Estados Modificados de Consciencia."),
        ("1997", "Publica <em>Al trasluz de la ayahuasca</em>."),
        ("2018", "Publica <em>Ayahuasca, la realidad detrás de la realidad</em>."),
    ],
    "libros": [
        ("los-jibaros-cazadores-de-suenos", "Su diario de campo entre los shuar."),
        ("al-trasluz-de-la-ayahuasca", "Su estudio de la ayahuasca desde la antropología."),
        ("ayahuasca-la-realidad-detras-de-la-realidad", "Una introducción divulgativa."),
        ("el-hongo-y-la-genesis-de-las-culturas", "Sobre la amanita y su papel en las culturas."),
    ],
    "relacion": [
        ("../jordi-riba/", "Jordi Riba", "El farmacólogo al que acercó a la ayahuasca."),
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "La medicina a la que ha dedicado buena parte de su obra."),
        ("../../enciclopedia/ayahuasca/", "Ayahuasca en la Enciclopedia", "Su historia y sus usos tradicionales."),
    ],
    "refs": [
        'El Temps. Entrevista a Josep Maria Fericgla (noviembre de 1994). <a href="https://www.eltemps.cat/documents/el-temps_1994_11_0542_0066_0070.pdf">https://www.eltemps.cat/documents/el-temps_1994_11_0542_0066_0070.pdf</a>',
        'Editorial Kairós. <em>Los chamanismos a revisión</em>: nota del autor. <a href="https://www.editorialkairos.com/catalogo/p/los-chamanismos-a-revision">https://www.editorialkairos.com/catalogo/p/los-chamanismos-a-revision</a>',
        'Casa del Libro. <em>Los jíbaros, cazadores de sueños</em>: sinopsis. <a href="https://www.casadellibro.com/libro-los-jibaros-cazadores-de-suenos/9788492470372/2671506">https://www.casadellibro.com/libro-los-jibaros-cazadores-de-suenos/9788492470372/2671506</a>',
        'Fericgla JM. Las experiencias activadoras de estructuras en el desarrollo individual y de las sociedades. <em>Cultura y Droga</em>. 2003;8(10). <a href="https://revistasojs.ucaldas.edu.co/index.php/culturaydroga/article/download/5938/5363/10381">https://revistasojs.ucaldas.edu.co/index.php/culturaydroga/article/download/5938/5363/10381</a>',
        'Lecturalia. <em>Al trasluz de la ayahuasca</em>: sinopsis. <a href="https://www.lecturalia.com/libro/63772/whatsapp:/send">https://www.lecturalia.com/libro/63772</a>',
        'IPG. <em>Ayahuasca</em>, de Josep María Fericgla: nota del autor. <a href="https://www.ipgbook.com/ayahuasca-products-9788499886190.php">https://www.ipgbook.com/ayahuasca-products-9788499886190.php</a>',
        'Virdi J. «Remembering Dr. Jordi Riba, ayahuasca research pioneer (1968–2020)». Chacruna. <a href="https://chacruna.net/?p=18947">https://chacruna.net/?p=18947</a>',
    ],
}

RIBA = {
    "slug": "jordi-riba", "nombre": "Jordi Riba", "iniciales": "JR", "anio": 1968,
    "que": "el farmacólogo catalán que llevó la ayahuasca al ensayo clínico",
    "tarjeta": "Farmacólogo catalán. Primeros ensayos controlados con ayahuasca.",
    "desc": ("Jordi Riba, el farmacólogo catalán que hizo en el Hospital de Sant Pau los primeros ensayos "
             "controlados con ayahuasca: su vida y sus descubrimientos."),
    "alias": "Farmacólogo (Barcelona, 1968 – 2020)",
    "entrada": ("En el Hospital de Sant Pau de Barcelona hizo los primeros estudios con placebo de la ayahuasca "
                "en voluntarios sanos. Su trabajo abrió el camino a buena parte de lo que hoy se sabe de ella."),
    "tipo": "Ciencia",
    "nacio_iso": "1968-09-12", "murio_iso": "2020-08-14", "lugar": "Barcelona",
    "datos": [("Nació", "12 de septiembre de 1968, Barcelona"),
              ("Murió", "14 de agosto de 2020, a los 51 años"),
              ("Ámbito", "farmacología humana"),
              ("Le debemos", "los primeros ensayos controlados con ayahuasca")],
    "titulos": {"aportaciones": "Lo que descubrió", "mirada": "Su legado"},
    "claves": [
        ("Quién fue", "Un farmacólogo catalán, doctor por la Universidad Autónoma de Barcelona, que dirigió el "
                      "grupo de Neuropsicofarmacología Humana del Hospital de Sant Pau." + rr(1, 3)),
        ("Por qué importa", "Fue el primero en hacer ensayos con placebo de la ayahuasca en voluntarios sanos, a "
                            "finales de los años noventa." + rr(1, 4)),
        ("Lo último", "Estudió cómo algunos componentes de la ayahuasca favorecen la formación de neuronas nuevas "
                      "en el laboratorio." + rr(3, 5)),
        ("Por dónde empezar", "El homenaje de Rafael Guimarães dos Santos y sus colegas en la "
                              "<em>Brazilian Journal of Psychiatry</em>."),
    ],
    "vida": f"""<p>Jordi Riba nació en Barcelona el 12 de septiembre de 1968 y se licenció en Farmacia por la Universidad de Barcelona en 1993.{r(2)} El antropólogo Josep Maria Fericgla le presentó a grupos que usaban ayahuasca en España, y eso influyó en su decisión de investigarla.{r(2)}</p>
<p>En 1996 empezó, con su maestro Manel Barbanoj, un programa de investigación en el Hospital de Sant Pau. En 2003 se doctoró en Farmacología por la Universidad Autónoma de Barcelona con una tesis sobre la farmacología humana de la ayahuasca.{rr(2, 4, 5)} De 2006 a 2018 dirigió el grupo de Neuropsicofarmacología Humana de Sant Pau; en 2018 se incorporó a la Universidad de Maastricht.{r(3)}</p>
<p>Murió el 14 de agosto de 2020, a los 51 años.{r(1)}</p>""",
    "aportaciones": f"""<h3>La ayahuasca en el laboratorio</h3>
<p>A finales de los noventa hizo en Sant Pau el primer estudio clínico controlado con ayahuasca, con placebo y voluntarios sanos.{rr(1, 4, 6)}</p>
<h3>El cerebro de quienes la toman</h3>
<p>Su equipo encontró diferencias estructurales en el cerebro de personas que llevaban años tomando ayahuasca, en concreto una corteza más delgada en la zona cingulada posterior, una región relacionada con la sensación del yo.{r(7)}</p>
<h3>Neuronas nuevas</h3>
<p>Desde 2013, en un programa con la Fundación Beckley, estudió cómo los alcaloides de la harmala favorecen la neurogénesis, es decir, la formación de neuronas nuevas, en estudios de laboratorio.{rr(3, 5)} La revista <em>Rolling Stone</em> lo incluyó entre las 25 personas que marcarían el futuro de la ciencia.{r(7)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER.</em></p>
<p>Riba trabajó con rigor en una época en que investigar estas sustancias era casi impensable, y lo hizo sin perder el respeto por las tradiciones de donde venían. Buena parte de la investigación actual sobre la ayahuasca en España y Brasil parte de lo que él hizo.</p>""",
    "cronologia": [
        ("1968", "Nace en Barcelona, el 12 de septiembre."),
        ("1993", "Se licencia en Farmacia por la Universidad de Barcelona."),
        ("1996", "Empieza su programa de investigación sobre la ayahuasca en Sant Pau."),
        ("2003", "Se doctora en Farmacología con una tesis sobre la ayahuasca."),
        ("2006", "Dirige el grupo de Neuropsicofarmacología Humana de Sant Pau."),
        ("2013", "Programa de investigación con la Fundación Beckley."),
        ("2018", "Se incorpora a la Universidad de Maastricht."),
        ("2020", "Muere el 14 de agosto."),
    ],
    "libros": [
        ("ayahuasca-y-salud", "Un volumen colectivo, editado por Labate y Bouso, sobre lo que se sabe de la ayahuasca y la salud."),
    ],
    "relacion": [
        ("../jose-carlos-bouso/", "José Carlos Bouso", "Su colega en la investigación sobre la ayahuasca."),
        ("../josep-maria-fericgla/", "Josep Maria Fericgla", "Quien le acercó a la ayahuasca."),
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "Qué es, cómo actúa y cómo reducir riesgos."),
    ],
    "refs": [
        'dos Santos RG, Araujo DB, Sanches RF, Hallak JE. Unveiling ayahuasca psychopharmacology: the accomplishments of Jordi Riba (1968-2020). <em>Brazilian Journal of Psychiatry</em>. 2021;43:565-566. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8639014">https://pmc.ncbi.nlm.nih.gov/articles/PMC8639014</a>',
        'Virdi J. «Remembering Dr. Jordi Riba, ayahuasca research pioneer (1968–2020)». Chacruna. <a href="https://chacruna.net/?p=18947">https://chacruna.net/?p=18947</a> y <a href="https://www.bialabate.net/blog-archive/news/at-chacruna-remembering-dr-jordi-riba-ayahuasca-research-pioneer-1968-2020">https://www.bialabate.net/blog-archive/news/at-chacruna-remembering-dr-jordi-riba-ayahuasca-research-pioneer-1968-2020</a>',
        'ICEERS. «Jordi Riba». <a href="https://www.iceers.org/en/tag/jordi-riba/">https://www.iceers.org/en/tag/jordi-riba/</a>',
        'de la Fuente Revenga M. «The legacy of Jordi Riba, a pioneer of modern psychedelic research». Psychedelic Review. <a href="https://psychedelicreview.com/the-legacy-of-jordi-riba-a-pioneer-of-modern-psychedelic-research/">https://psychedelicreview.com/the-legacy-of-jordi-riba-a-pioneer-of-modern-psychedelic-research/</a>',
        'Beckley Foundation. «Collaboration with Dr Jordi Riba at the Sant Pau Institute of Biomedical Research». <a href="https://beckleyfoundation.org/science/collaborations/beckley-sant-pau-hospital-research-programme/">https://beckleyfoundation.org/science/collaborations/beckley-sant-pau-hospital-research-programme/</a>',
        'MAPS. «Pharmacological study of ayahuasca in healthy volunteers» (Barbanoj y Riba). <a href="https://maps.org/2003/05/09/pharmacological_study_of_ayahuasca_in_healthy_volunteers/">https://maps.org/2003/05/09/pharmacological_study_of_ayahuasca_in_healthy_volunteers/</a>',
        'Redacción Médica. «Un farmacólogo español, entre los 25 nombres del futuro para Rolling Stone». <a href="https://www.redaccionmedica.com/secciones/sanidad-hoy/un-farmacologo-espanol-entre-los-25-nombres-del-futuro-para-rolling-stone-3807">https://www.redaccionmedica.com/secciones/sanidad-hoy/un-farmacologo-espanol-entre-los-25-nombres-del-futuro-para-rolling-stone-3807</a>',
    ],
}

BOUSO = {
    "slug": "jose-carlos-bouso", "nombre": "José Carlos Bouso", "iniciales": "JB", "anio": 1970,
    "que": "el psicólogo y farmacólogo español de la investigación psicodélica",
    "tarjeta": "Psicólogo y farmacólogo. Pionero del MDMA en España e investigador de ICEERS.",
    "desc": ("José Carlos Bouso, psicólogo clínico y doctor en Farmacología, pionero de la investigación con MDMA "
             "y ayahuasca en España: su trayectoria y sus libros."),
    "alias": "Psicólogo clínico y farmacólogo (Madrid, 1970)",
    "entrada": ("Cuando casi nadie hablaba de usos terapéuticos de los psicodélicos, ya investigaba en Madrid el "
                "MDMA para el estrés postraumático. Hoy es una de las voces de referencia en español."),
    "tipo": "Ciencia",
    "nacio_iso": "1970", "lugar": "Madrid",
    "datos": [("Nació", "1970, Madrid"),
              ("Ámbito", "psicología clínica y farmacología"),
              ("Le debemos", "uno de los primeros ensayos con MDMA en Europa y <em>Medicina psiquedélica</em>")],
    "titulos": {"aportaciones": "Lo que investiga", "mirada": "Su mirada"},
    "claves": [
        ("Quién es", "Un psicólogo clínico madrileño, doctor en Farmacología, que ha investigado en la "
                     "Universidad Autónoma de Madrid, en Sant Pau y en el IMIM de Barcelona." + rr(1, 2)),
        ("Por qué importa", "Dirigió uno de los primeros estudios con MDMA para el estrés postraumático, en mujeres "
                            "que habían sufrido una agresión sexual." + rr(2, 3)),
        ("Hoy", "Fue director científico de ICEERS, donde coordinó estudios sobre cannabis, ayahuasca e "
                "ibogaína, y sigue colaborando con la fundación." + r(1)),
        ("Por dónde empezar", "<em>Medicina psiquedélica</em> (2025), en la Biblioteca."),
    ],
    "vida": f"""<p>José Carlos Bouso nació en Madrid en 1970.{r(2)} Es psicólogo clínico y doctor en Farmacología. Ha investigado en la Universidad Autónoma de Madrid, en el Instituto de Investigación Biomédica de Sant Pau y en el Instituto Hospital del Mar de Investigaciones Médicas (IMIM), en Barcelona.{r(1)}</p>
<p>Fue director científico de ICEERS y sigue colaborando con esta fundación. También es miembro del Medical Anthropology Research Center de la Universitat Rovira i Virgili y profesor visitante en la Facultad de Medicina de Ribeirão Preto (Universidad de São Paulo).{r(1)}</p>""",
    "aportaciones": f"""<h3>El MDMA y el estrés postraumático</h3>
<p>A comienzos de los años 2000 estudió en Madrid la seguridad y la eficacia de distintas dosis de MDMA, dentro de la psicoterapia, en mujeres con estrés postraumático crónico tras una agresión sexual.{rr(3, 4)}</p>
<h3>Ayahuasca, cannabis e ibogaína</h3>
<p>Ha estudiado los efectos a largo plazo del uso de ayahuasca en comunidades de España y Brasil, y ha coordinado estudios sobre los posibles beneficios del cannabis y la ibogaína.{rr(1, 3)}</p>
<h3>Divulgación</h3>
<p>En <em>Medicina psiquedélica</em> (2025) reúne la evidencia científica publicada sobre MDMA, LSD, ketamina y otras sustancias, pensando en pacientes, clínicos y curiosos.{r(5)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Bouso insiste en que el contexto importa tanto como la sustancia: un entorno responsable y bien preparado es lo que hace posible que una experiencia sea sanadora.{r(4)} Defiende una investigación rigurosa y una información honesta, lejos tanto del miedo como del entusiasmo sin matices.</p>""",
    "cronologia": [
        ("1970", "Nace en Madrid."),
        ("Años 2000", "Estudio con MDMA para el estrés postraumático en Madrid."),
        ("2013", "Coedita con Beatriz Caiuby Labate <em>Ayahuasca y salud</em>."),
        ("2025", "Publica <em>Medicina psiquedélica</em>."),
    ],
    "libros": [
        ("medicina-psiquedelica", "Su manual para pacientes, clínicos, usuarios y curiosos."),
        ("ayahuasca-y-salud", "Volumen colectivo que coeditó con Beatriz Caiuby Labate."),
        ("psilocibes-603", "Sobre las setas de psilocibina."),
        ("cannabis-medicinal-778", "Sobre el cannabis en medicina."),
    ],
    "relacion": [
        ("../jordi-riba/", "Jordi Riba", "Su colega en la investigación sobre la ayahuasca."),
        ("../../sustancias/mdma/", "Guía del MDMA", "La sustancia de sus primeros estudios."),
        ("../../investigacion-terapeutica/", "Investigación", "Qué se está investigando hoy y cómo participar."),
    ],
    "refs": [
        'ICEERS. «José Carlos Bouso». <a href="https://www.iceers.org/?p=996">https://www.iceers.org/?p=996</a> y <a href="https://www.iceers.org/en/tag/jose-carlos-bouso/">https://www.iceers.org/en/tag/jose-carlos-bouso/</a>',
        'Pareja P. «J.C. Bouso, investigador en psicodélicos» (entrevista). elDiario.es, 2 de mayo de 2026. <a href="https://www.eldiario.es/cultura/j-c-bouso-investigador-psicodelicos-paradoja-derecha-sea-apoyando-sustancias-cat_1_13184929.html">https://www.eldiario.es/cultura/j-c-bouso-investigador-psicodelicos-paradoja-derecha-sea-apoyando-sustancias-cat_1_13184929.html</a>',
        'SlidesLive. «José Carlos Bouso» (nota biográfica). <a href="https://slideslive.com/s/jose-carlos-bouso-4949?tab=about">https://slideslive.com/s/jose-carlos-bouso-4949?tab=about</a>',
        'Wikipedia (en inglés). «José Carlos Bouso» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Jos%C3%A9_Carlos_Bouso">https://en.wikipedia.org/wiki/José_Carlos_Bouso</a>',
        'El Español. «Bouso, el sabio de la terapia psicodélica» (20 de octubre de 2025). <a href="https://www.elespanol.com/ciencia/20251020/bouso-sabio-terapia-psicodelica-mdma-ilegal-cuesta-farmacia-igual-llegara/1003743974624_0.html">https://www.elespanol.com/ciencia/20251020/bouso-sabio-terapia-psicodelica-mdma-ilegal-cuesta-farmacia-igual-llegara/1003743974624_0.html</a>',
    ],
}

IRINEU = {
    "slug": "mestre-irineu", "nombre": "Mestre Irineu", "iniciales": "MI", "anio": 1890,
    "que": "el fundador del Santo Daime",
    "tarjeta": "Raimundo Irineu Serra. Fundó el Santo Daime en la Amazonía brasileña.",
    "desc": ("Mestre Irineu, Raimundo Irineu Serra, el nieto de esclavos que fundó el Santo Daime en Acre, la "
             "religión ayahuasquera más antigua de Brasil: su vida y legado."),
    "alias": "Raimundo Irineu Serra, fundador del Santo Daime (Maranhão, 1890 – Rio Branco, 1971)",
    "entrada": ("Un hombre negro, nieto de esclavos, llegó a la Amazonía para trabajar en el caucho. Allí "
                "conoció la ayahuasca y fundó el Santo Daime, una religión de himnos que hoy se celebra en "
                "muchos países."),
    "tipo": "Saber tradicional",
    "nacio_iso": "1890-12-15", "murio_iso": "1971-07-06", "lugar": "São Vicente Ferrer, Maranhão",
    "datos": [("Nació", "15 de diciembre de 1890 (la tradición daimista decía 1892), São Vicente Ferrer (Maranhão, Brasil)"),
              ("Murió", "6 de julio de 1971, Rio Branco (Acre)"),
              ("Ámbito", "religión y espiritualidad ayahuasquera"),
              ("Le debemos", "el Santo Daime y su himnario, <em>O Cruzeiro</em>")],
    "titulos": {"aportaciones": "Lo que fundó", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Raimundo Irineu Serra, nacido en Maranhão y nieto de esclavos, que emigró a la Amazonía "
                      "en 1912, en plena fiebre del caucho." + rr(1, 2)),
        ("Por qué importa", "Fundó en Rio Branco, en los años treinta, el Santo Daime, la religión ayahuasquera "
                            "más antigua de Brasil." + rr(1, 2)),
        ("Su legado", "Sus himnos, reunidos en <em>O Cruzeiro</em>, siguen siendo el centro de los rituales "
                      "daimistas." + r(5)),
        ("Por dónde empezar", "<em>Liquid Light</em>, de William Barnard, en la Biblioteca."),
    ],
    "vida": f"""<p>Raimundo Irineu Serra nació en São Vicente Ferrer (Maranhão), en el nordeste de Brasil, el 15 de diciembre de 1890, según su partida de bautismo; la tradición daimista situaba su nacimiento en 1892. Era nieto de esclavos y nació dos años después de la abolición de la esclavitud en Brasil.{rr(1, 2)}</p>
<p>En 1912, con unos veinte años, se fue a la Amazonía a trabajar en el caucho, como tantos nordestinos.{r(3)} Hacia 1914 tomó ayahuasca por primera vez en la frontera entre Brasil, Bolivia y Perú.{r(1)} En 1920 se instaló en Rio Branco (Acre) y entró en la guardia territorial, donde estuvo hasta 1932.{r(3)}</p>
<p>En 1945 sus compañeros consiguieron unas tierras y fundaron la comunidad de Alto Santo.{r(5)} Murió en Rio Branco el 6 de julio de 1971.{r(4)}</p>""",
    "aportaciones": f"""<h3>El Santo Daime</h3>
<p>Según el relato fundador, en la selva se le apareció una figura femenina que puso en la bebida su poder de curación y le concedió el don de sanar.{r(2)} En 1930 celebró en Rio Branco el primer «trabajo», el ritual del Santo Daime, y a comienzos de los años treinta ya se le conocía como Mestre Irineu.{r(1)} Él llamó a la bebida «Daime».{r(5)}</p>
<h3>Los himnos</h3>
<p>Recibía mensajes en forma de himnos sencillos, que se convirtieron en el corazón de la doctrina. Su himnario, <em>O Cruzeiro</em>, se canta entero en las fiestas principales, como Nochebuena.{r(5)}</p>
<h3>Una religión que creció</h3>
<p>Tras su muerte, algunos discípulos fundaron sus propias iglesias. La más conocida, la de Sebastião Mota de Melo, llevó el Santo Daime a otros países en los años noventa.{r(5)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER, desde fuera de la tradición daimista. No habla en su nombre.</em></p>
<p>Mestre Irineu unió el uso amazónico de la ayahuasca con el cristianismo popular, las tradiciones afrobrasileñas y el esoterismo de su tiempo. Su vida recuerda que la historia de la ayahuasca no es solo indígena ni solo occidental: también es la historia de un hombre negro y pobre que construyó una comunidad espiritual en la frontera amazónica. Desde la psicología transpersonal, el Santo Daime muestra el poder de la música y del grupo para sostener la experiencia.</p>""",
    "cronologia": [
        ("1890", "Nace en São Vicente Ferrer (Maranhão), el 15 de diciembre."),
        ("1912", "Emigra a la Amazonía para trabajar en el caucho."),
        ("Hacia 1914", "Toma ayahuasca por primera vez."),
        ("1920", "Se instala en Rio Branco y entra en la guardia territorial."),
        ("1930", "Primer ritual del Santo Daime en Rio Branco."),
        ("1945", "Fundación de la comunidad de Alto Santo."),
        ("1971", "Muere en Rio Branco, el 6 de julio."),
    ],
    "libros": [
        ("liquid-light-ayahuasca-spirituality-and-the-santo-daime-tradition-579", "Sobre la espiritualidad del Santo Daime."),
        ("ayahuasca-religions", "Una guía de las religiones ayahuasqueras."),
        ("o-uso-ritual-da-ayahuasca", "Volumen colectivo, en portugués, sobre los usos rituales de la ayahuasca."),
    ],
    "relacion": [
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "Qué es, cómo actúa y cómo reducir riesgos."),
        ("../../enciclopedia/ayahuasca/", "Ayahuasca en la Enciclopedia", "Su historia y sus usos tradicionales."),
        ("../pablo-amaringo/", "Pablo Amaringo", "Otro saber amazónico de la ayahuasca, el del vegetalismo."),
    ],
    "refs": [
        'World Religions and Spirituality Project. «Santo Daime timeline». <a href="https://wrldrels.org/?p=3309">https://wrldrels.org/?p=3309</a>',
        'Chacruna. «Mestre Irineu: a Black man who changed the history of ayahuasca». <a href="https://chacruna.net/?p=17982">https://chacruna.net/?p=17982</a>',
        'Goulart SL. A história do encontro do Mestre Irineu com a ayahuasca: mitos fundadores da religião do Santo Daime. NEIP. <a href="https://kodu.ut.ee/~hellex/aya/kirjandus/aya%20religioon/t_sandra_encontro.pdf">https://kodu.ut.ee/~hellex/aya/kirjandus/aya religioon/t_sandra_encontro.pdf</a>',
        'Jornal Grande Bahia. «6 de julho. Passagem para a vida espiritual do Mestre Raimundo Irineu Serra». <a href="https://jornalgrandebahia.com.br/?p=23691">https://jornalgrandebahia.com.br/?p=23691</a>',
        'Wikipedia (en inglés). «Mestre Irineu» y «Santo Daime» (fuentes secundarias). <a href="https://en.wikipedia.org/wiki/Mestre_Irineu">https://en.wikipedia.org/wiki/Mestre_Irineu</a>',
    ],
}

AMARINGO = {
    "slug": "pablo-amaringo", "nombre": "Pablo Amaringo", "iniciales": "PA", "anio": 1938,
    "que": "el vegetalista peruano que pintó las visiones de la ayahuasca",
    "tarjeta": "Vegetalista y pintor peruano. Fundó la escuela Usko-Ayar.",
    "desc": ("Pablo Amaringo, el vegetalista peruano que pintó las visiones de la ayahuasca y fundó una escuela "
             "de pintura gratuita en Pucallpa: su vida y su obra."),
    "alias": "Vegetalista y pintor (Puerto Libertad, Ucayali – 2009)",
    "entrada": ("Fue curandero vegetalista y después pintor. Sus cuadros, llenos de color y de seres de la "
                "selva, se han convertido en la imagen más conocida de las visiones de la ayahuasca."),
    "tipo": "Saber tradicional",
    "murio_iso": "2009-11-16", "lugar": "Puerto Libertad, Ucayali (Perú)",
    "datos": [("Nació", "en Puerto Libertad (Ucayali, Perú), en 1938 según unas fuentes y en 1943 según otras"),
              ("Murió", "16 de noviembre de 2009"),
              ("Ámbito", "vegetalismo y pintura visionaria"),
              ("Le debemos", "<em>Ayahuasca Visions</em> y la escuela Usko-Ayar")],
    "titulos": {"aportaciones": "Lo que hizo", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Pablo César Amaringo Shuña, un vegetalista de la Amazonía peruana que aprendió los "
                      "ícaros, los cantos de curación, y luego se dedicó a pintar." + rr(1, 2)),
        ("Por qué importa", "<em>Ayahuasca Visions</em> (1991), con Luis Eduardo Luna, dio a conocer en todo el "
                            "mundo su forma de pintar las visiones." + rr(2, 5)),
        ("Su legado", "En 1988 fundó en Pucallpa la Escuela de Pintura Amazónica Usko-Ayar, gratuita para "
                      "sus alumnos." + r(1)),
        ("Por dónde empezar", "<em>Ayahuasca Visions</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Pablo César Amaringo Shuña nació en Puerto Libertad, a orillas de un afluente del Ucayali, en la Amazonía peruana. Las fuentes no coinciden en el año: unas dicen 1938 y otras 1943. Fue el séptimo de trece hermanos de una familia muy pobre que acabó en Pucallpa, donde solo pudo ir dos años a la escuela.{rr(1, 2, 4)}</p>
<p>Tomó ayahuasca por primera vez a los diez años. Una grave enfermedad del corazón, que según contaba se curó con ayahuasca, le llevó a la vida de curandero: se hizo vegetalista y aprendió los ícaros, los cantos que, según su tradición, enseña la propia planta.{r(1)}</p>
<p>Practicó el vegetalismo en los años setenta y después se dedicó sobre todo a pintar y a enseñar.{r(3)} Hasta poco antes de morir pintó, dirigió su escuela y acompañó retiros de ayahuasca. Murió el 16 de noviembre de 2009, tras una larga enfermedad.{r(2)}</p>""",
    "aportaciones": f"""<h3>Pintar las visiones</h3>
<p>El antropólogo Luis Eduardo Luna y el etnobotánico Dennis McKenna lo conocieron en Pucallpa.{r(2)} Con Luna publicó <em>Ayahuasca Visions: The Religious Iconography of a Peruvian Shaman</em> (1991), donde cada cuadro va acompañado de sus explicaciones sobre los seres, los cantos y las plantas que aparecen.{r(5)}</p>
<h3>Usko-Ayar</h3>
<p>En junio de 1988 abrió en Pucallpa la Escuela de Pintura Amazónica Usko-Ayar («príncipe espiritual»), donde los jóvenes aprendían gratis a pintar la naturaleza amazónica.{rr(1, 2)} En 1992 recibió el premio Global 500 del Programa de las Naciones Unidas para el Medio Ambiente.{r(3)}</p>""",
    "mirada": f"""<p><em>Esta sección es una reflexión de APDER, desde fuera del vegetalismo. No habla en su nombre.</em></p>
<p>Los cuadros de Amaringo no son solo bellos: son mapas de un mundo en el que las plantas enseñan, los cantos curan y todo está vivo. Desde la psicología transpersonal y junguiana, su obra muestra cómo la experiencia visionaria toma la forma de los símbolos de una cultura. Su escuela recuerda además que ese saber puede transmitirse cuidando la selva y a quienes viven en ella.</p>""",
    "cronologia": [
        ("1938 o 1943", "Nace en Puerto Libertad (Ucayali, Perú)."),
        ("Hacia los diez años", "Toma ayahuasca por primera vez."),
        ("1988", "Funda la escuela Usko-Ayar en Pucallpa."),
        ("1991", "Publica con Luis Eduardo Luna <em>Ayahuasca Visions</em>."),
        ("1992", "Recibe el premio Global 500 de la ONU."),
        ("2009", "Muere el 16 de noviembre."),
    ],
    "libros": [
        ("ayahuasca-visions", "Sus cuadros explicados por él mismo, con Luis Eduardo Luna."),
        ("the-ayahuasca-visions-of-pablo-amaringo-589", "Una segunda colección de sus pinturas."),
    ],
    "relacion": [
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "Qué es, cómo actúa y cómo reducir riesgos."),
        ("../marlene-dobkin-de-rios/", "Marlene Dobkin de Rios", "La antropóloga que estudió el curanderismo con ayahuasca en Perú."),
        ("../terence-mckenna/", "Terence McKenna", "Su hermano Dennis conoció a Amaringo en Pucallpa."),
    ],
    "refs": [
        'Erowid. «Pablo Amaringo». <a href="https://cache.erowid.org/culture/characters/amaringo_pablo">https://cache.erowid.org/culture/characters/amaringo_pablo</a>',
        'Wikipedia (en inglés). «Pablo Amaringo» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Pablo_Amaringo">https://en.wikipedia.org/wiki/Pablo_Amaringo</a>',
        'Artprice. «Pablo Amaringo (1943-2009)». <a href="https://www.artprice.com/artist/238799/pablo-amaringo/biography">https://www.artprice.com/artist/238799/pablo-amaringo/biography</a>',
        'eGallery. «Pablo Cesar Amaringo Shuna». <a href="https://www.egallery.com/artists/?id=34">https://www.egallery.com/artists/?id=34</a>',
        'Luna LE, Amaringo P. <em>Ayahuasca Visions: The Religious Iconography of a Peruvian Shaman</em>. Berkeley: North Atlantic Books; 1991.',
    ],
}

DOBKIN = {
    "slug": "marlene-dobkin-de-rios", "nombre": "Marlene Dobkin de Rios", "iniciales": "MD", "anio": 1939,
    "que": "la antropóloga que estudió durante treinta años la ayahuasca en la Amazonía",
    "tarjeta": "Antropóloga médica. Treinta años de trabajo de campo en la Amazonía.",
    "desc": ("Marlene Dobkin de Rios, la antropóloga médica y psicoterapeuta que estudió durante treinta años "
             "el curanderismo con ayahuasca en Perú: su vida y sus libros."),
    "alias": "Antropóloga médica y psicoterapeuta (Nueva York, 1939 – Placentia, 2012)",
    "entrada": ("Antropóloga y psicoterapeuta, pasó casi treinta años estudiando cómo curan los ayahuasqueros "
                "de la Amazonía. También escribió con mirada crítica sobre el turismo de ayahuasca."),
    "tipo": "Ciencia",
    "nacio_iso": "1939-04-12", "murio_iso": "2012-11-10", "lugar": "Nueva York",
    "datos": [("Nació", "12 de abril de 1939, Nueva York"),
              ("Murió", "10 de noviembre de 2012, Placentia (California), a los 73 años"),
              ("Ámbito", "antropología médica y psicoterapia"),
              ("Le debemos", "<em>Visionary Vine</em> y <em>Amazon Healer</em>")],
    "titulos": {"aportaciones": "Lo que investigó", "mirada": "Su mirada"},
    "claves": [
        ("Quién fue", "Una antropóloga médica y psicoterapeuta estadounidense, profesora en la Universidad del "
                      "Estado de California en Fullerton." + rr(1, 2)),
        ("Por qué importa", "Su tesis y su libro <em>Visionary Vine</em> (1972) estudiaron cómo se cura con "
                            "ayahuasca en la Amazonía peruana; trabajó allí casi treinta años." + rr(2, 3)),
        ("Su mirada", "Explicó que, para el curandero, la ayahuasca no es un medicamento sino una forma de ver "
                      "la causa de la enfermedad." + r(3)),
        ("Por dónde empezar", "<em>Visionary Vine</em> y <em>Amazon Healer</em>, en la Biblioteca."),
    ],
    "vida": f"""<p>Marlene Dobkin nació en Nueva York el 12 de abril de 1939, en una familia judía de origen ucraniano.{r(2)} Estudió Psicología clínica en el Queens College (1959) y un máster en Antropología en la Universidad de Nueva York (1963). Se doctoró en la Universidad de California en Riverside con una tesis sobre el uso de plantas alucinógenas en la medicina popular de la Amazonía peruana.{r(2)}</p>
<p>Desde 1972 fue profesora de Antropología en la Universidad del Estado de California en Fullerton. Hizo trabajo de campo en la Amazonía peruana y brasileña durante casi treinta años.{r(2)} Murió el 10 de noviembre de 2012 en Placentia (California), a los 73 años, tras un tratamiento contra el cáncer.{rr(1, 2)}</p>""",
    "aportaciones": f"""<h3>La curación con ayahuasca</h3>
<p>En <em>Visionary Vine</em> (1972) y <em>Amazon Healer</em> (1992), la vida de un curandero urbano, describió cómo se cura con ayahuasca en los barrios de las ciudades amazónicas.{rr(1, 2)}</p>
<h3>Una mirada comparada</h3>
<p>En <em>The Wilderness of Mind</em> (1976) y <em>Hallucinogens: Cross-Cultural Perspectives</em> (1984) comparó el uso de plantas sagradas en distintas culturas. Con el psiquiatra Oscar Janiger escribió <em>LSD, Spirituality, and the Creative Process</em> (2003).{r(2)}</p>
<h3>Los jóvenes y la ayahuasca</h3>
<p>Entre finales de los noventa y comienzos de los 2000 dirigió la parte cualitativa de un estudio en Brasil sobre adolescentes que tomaban ayahuasca en la União do Vegetal.{rr(1, 2)}</p>""",
    "mirada": f"""<p><em>Esta sección resume sus ideas. No son hechos comprobados.</em></p>
<p>Dobkin de Rios insistía en que la ayahuasca, en manos del curandero, no es un remedio en el sentido occidental: le permite entrar en el terreno de las causas de la enfermedad, que para su cultura pueden ser sociales o mágicas, y actuar sobre ellas. Fue muy crítica con el turismo de ayahuasca y con quienes venden sesiones como «formación chamánica».{r(3)}</p>
<p>Desde la psicología humanista, su obra recuerda que la curación tiene siempre un marco cultural y relacional.</p>""",
    "cronologia": [
        ("1939", "Nace en Nueva York, el 12 de abril."),
        ("1963", "Máster en Antropología por la Universidad de Nueva York."),
        ("1972", "Se doctora en Riverside, es profesora en Fullerton y publica <em>Visionary Vine</em>."),
        ("1984", "Publica <em>Hallucinogens: Cross-Cultural Perspectives</em>."),
        ("1992", "Publica <em>Amazon Healer</em>."),
        ("2003", "Publica con Oscar Janiger <em>LSD, Spirituality, and the Creative Process</em>."),
        ("2012", "Muere en Placentia (California), el 10 de noviembre."),
    ],
    "libros": [
        ("visionary-vine", "Su estudio clásico sobre la curación con ayahuasca."),
        ("amazon-healer", "La vida de un curandero urbano."),
        ("hallucinogens-dobkin-de-rios", "Las plantas sagradas en distintas culturas."),
        ("lsd-spirituality-and-the-creative-process-439", "Con Oscar Janiger, sobre el LSD y la creatividad."),
        ("a-hallucinogenic-tea-laced-with-controversy-572", "Con Róger Rumrrill, sobre la ayahuasca en la Amazonía y en Estados Unidos."),
    ],
    "relacion": [
        ("../pablo-amaringo/", "Pablo Amaringo", "Un vegetalista de la misma Amazonía peruana."),
        ("../../sustancias/ayahuasca/", "Guía de la ayahuasca", "Qué es, cómo actúa y cómo reducir riesgos."),
        ("../josep-maria-fericgla/", "Josep Maria Fericgla", "Otro antropólogo de la ayahuasca."),
    ],
    "refs": [
        'Erowid. «Marlene Dobkin de Rios». <a href="https://erowid.org/culture/characters/dobkin_derios_marlene/">https://erowid.org/culture/characters/dobkin_derios_marlene/</a>',
        'Wikipedia (en inglés). «Marlene Dobkin de Rios» (fuente secundaria). <a href="https://en.wikipedia.org/wiki/Marlene_Dobkin_de_Rios">https://en.wikipedia.org/wiki/Marlene_Dobkin_de_Rios</a>',
        'Slovar Online. «Dobkin de Rios, Marlene» (diccionario de antropología). <a href="https://slovaronline.com/browse/90a53aa8-4814-342f-9268-b9af518a4f31/dobkin-de-rios-marlene">https://slovaronline.com/browse/90a53aa8-4814-342f-9268-b9af518a4f31/dobkin-de-rios-marlene</a>',
    ],
}
