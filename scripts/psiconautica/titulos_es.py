# -*- coding: utf-8 -*-
"""Títulos en español de las páginas de Psiconáutica, para que se parezcan a los de PsychonautWiki.

Regla (la aplica titulo() en generar.py):
1. Si el título original es una sigla o un nombre con cifras (LSD, MDMA, 2C-B, 4-AcO-DMT), se usa tal cual.
2. Si está en este diccionario, se usa la traducción. Los nombres científicos van en latín, como en la wiki.
3. Si no, se usa el título que ya tenía la página, sin artículo delante («La manía» → «Manía»)."""
import re

TITULOS = {
    "Alpha-GPC": "Alfa-GPC", "Amanita muscaria": "Amanita muscaria", "Amanita pantherina": "Amanita pantherina",
    "Anadenanthera peregrina": "Anadenanthera peregrina", "Argyreia nervosa": "Argyreia nervosa",
    "Banisteriopsis caapi": "Banisteriopsis caapi", "Calea ternifolia": "Calea ternifolia", "Datura": "Datura",
    "Datura (botany)": "Datura (botánica)", "Echinopsis lageniformis": "Echinopsis lageniformis",
    "Echinopsis pachanoi": "Echinopsis pachanoi", "Entada rheedii": "Entada rheedii",
    "Hyoscyamus niger (botany)": "Hyoscyamus niger (botánica)", "Ipomoea tricolor": "Ipomoea tricolor",
    "Lophophora diffusa": "Lophophora diffusa", "Lophophora fricii": "Lophophora fricii",
    "Lophophora williamsii": "Lophophora williamsii", "Mandragora": "Mandrágora",
    "Mandragora officinarum (botany)": "Mandragora officinarum (botánica)", "Mimosa tenuiflora": "Mimosa tenuiflora",
    "Kratom": "Kratom", "Blue lotus": "Loto azul", "Peganum harmala": "Peganum harmala",
    "Phalaris aquatica (botany)": "Phalaris aquatica (botánica)", "PiHKAL": "PiHKAL", "Psilocybe cubensis": "Psilocybe cubensis",
    "Psilocybe cyanescens": "Psilocybe cyanescens", "Psilocybe mexicana": "Psilocybe mexicana",
    "Psilocybe subaeruginosa": "Psilocybe subaeruginosa", "Psychotria viridis": "Psychotria viridis",
    "Salvia divinorum": "Salvia divinorum", "Tabernanthe iboga (botany)": "Tabernanthe iboga (botánica)",
    "Prolintane": "Prolintano", "Mescaline": "Mescalina", "Methylone": "Metilona", "Ethylone": "Etilona",
    "Escaline": "Escalina", "Allylescaline": "Alilescalina", "Psilocin": "Psilocina", "Methallylescaline": "Metalilescalina",
    "Proscaline": "Proscalina", "Aborting trips": "Cómo cortar un viaje", "Phenibut": "Fenibut", "Adrafinil": "Adrafinilo",
    "Beta-Carboline": "Beta-carbolina", "Alcohols": "Alcoholes", "All day awareness": "Conciencia durante todo el día",
    "Alprazolam": "Alprazolam", "Alternative use of alcohols": "Usos alternativos de los alcoholes", "Amnesia": "Amnesia",
    "Aniracetam": "Aniracetam", "Antagonist": "Antagonista", "Anticholinergic": "Anticolinérgico", "Aporphine": "Aporfina",
    "Atropa belladonna": "Atropa belladonna", "Bad vibes": "Malas vibraciones", "Beta-Endorphin": "Beta-endorfina",
    "Bibliography of Alexander Shulgin": "Bibliografía de Alexander Shulgin", "Breathing techniques": "Técnicas de respiración",
    "Bromazepam": "Bromazepam", "Bromo-DragonFLY": "Bromo-DragonFLY", "Bufotenin": "Bufotenina", "Cannabidiol": "Cannabidiol",
    "Cannabis": "Cannabis", "Cannabis (botany)": "Cannabis (botánica)", "Carisoprodol": "Carisoprodol", "Changa": "Changa",
    "Clonazepam": "Clonazepam", "Clonazolam": "Clonazolam", "Coca": "Coca", "Cocaine": "Cocaína",
    "Coffea (botany)": "Coffea (botánica)", "Cognitive depressions": "Depresiones cognitivas",
    "Cognitive effects - Psychedelics": "Efectos cognitivos de los psicodélicos", "Cold turkey": "Abandono brusco («mono»)",
    "Coluracetam": "Coluracetam", "Comparison of psychoactive alcohols in alcoholic drinks": "Alcoholes psicoactivos en las bebidas alcohólicas",
    "Conversion of CBD to THC by heat": "Conversión de CBD en THC por calor",
    "Conversion of CBD to THC with zeolite": "Conversión de CBD en THC con zeolita", "Cortisol": "Cortisol", "Creatine": "Creatina",
    "Dangerous combinations": "Combinaciones peligrosas", "Déjà vu": "Déjà vu", "Delirium tremens": "Delirium tremens",
    "Deschloroetizolam": "Descloroetizolam", "Desmanthus illinoensis (botany)": "Desmanthus illinoensis (botánica)",
    "Diazepam": "Diazepam", "Dichloropane": "Dicloropano", "Diclazepam": "Diclazepam", "Diet": "Alimentación", "Doxepin": "Doxepina",
    "Echinopsis peruviana": "Echinopsis peruviana", "Efavirenz": "Efavirenz", "Ephedra sinica (botany)": "Ephedra sinica (botánica)",
    "Etizolam": "Etizolam", "Experience index": "Índice de experiencias", "F-Phenibut": "F-fenibut", "Fermented water": "Agua fermentada",
    "Flualprazolam": "Flualprazolam", "Flubromazepam": "Flubromazepam", "Flubromazolam": "Flubromazolam",
    "Flunitrazepam": "Flunitrazepam", "Flunitrazolam": "Flunitrazolam", "Food Of The Gods (book)": "El manjar de los dioses (libro)",
    "Fractal": "Fractal", "Good vibes": "Buenas vibraciones", "Grayanotoxin": "Grayanotoxina", "Haloperidol": "Haloperidol",
    "Hydromorphone": "Hidromorfona", "K-Opioid receptor agonist": "Agonista del receptor opioide kappa", "Kambo": "Kambó",
    "Kava": "Kava", "Ketamine": "Ketamina", "List of adjustable spectrum LED lights": "Luces led de espectro regulable",
    "List of bufotoxins": "Lista de bufotoxinas", "List of entheogens": "Lista de enteógenos",
    "List of non-hallucinogenic substances used in rituals": "Sustancias no alucinógenas usadas en rituales",
    "List of pharmaceuticals": "Lista de fármacos", "List of polysubstance combinations": "Lista de combinaciones de varias sustancias",
    "List of psychoactive substances derived from artificial fungi biotransformation": "Sustancias psicoactivas obtenidas por biotransformación con hongos",
    "List of psychoactive substances to avoid": "Sustancias psicoactivas que conviene evitar",
    "List of psychoactive substances, and precursor chemicals, produced by GMOs derived from genetically modified organisms": "Sustancias psicoactivas y precursores producidos por organismos modificados genéticamente",
    "List/substances-drafts": "Borradores de sustancias", "Loperamide": "Loperamida", "Lorazepam": "Lorazepam",
    "Lormetazepam": "Lormetazepam", "Main Page": "Portada de PsychonautWiki", "Methaqualone": "Metacualona",
    "Methcathinone": "Metcatinona", "Methiopropamine": "Metiopropamina", "Methoxphenidine": "Metoxfenidina",
    "Methylnaphthidate": "Metilnaftidato", "MDxx": "MDxx", "Metizolam": "Metizolam", "Mexedrone": "Mexedrona",
    "Midazolam": "Midazolam", "Modafinil": "Modafinilo", "Modulator": "Modulador", "N-Methylbisfluoromodafinil": "N-metilbisfluoromodafinilo",
    "MiPLA": "MiPLA", "MiPT": "MiPT", "Network": "Red de recursos", "Neurotoxicity": "Neurotoxicidad", "Monoamine": "Monoamina",
    "Nicotiana (botany)": "Nicotiana (botánica)", "Nifoxipam": "Nifoxipam", "Nitrazepam": "Nitrazepam",
    "Nymphaea caerulea": "Nymphaea caerulea", "O-Desmethyltramadol": "O-desmetiltramadol", "Omberacetam": "Omberacetam",
    "Oxiracetam": "Oxiracetam", "Oxymorphone": "Oximorfona", "Panaeolus cyanescens": "Panaeolus cyanescens", "Paranoia": "Paranoia",
    "Pentobarbital": "Pentobarbital", "Phalaris (botany)": "Phalaris (botánica)", "Phenobarbital": "Fenobarbital",
    "Phenylpiracetam": "Fenilpiracetam", "Piracetam": "Piracetam", "Pramiracetam": "Pramiracetam", "Prochlorperazine": "Proclorperazina",
    "Psychedelic": "Psicodélico", "Psychedelic cacti": "Cactus psicodélicos", "Psychedelic therapy": "Terapia psicodélica",
    "Psychoactive acacias": "Acacias psicoactivas", "Psychonaut media index": "Índice de medios psiconautas", "Quetiapine": "Quetiapina",
    "Receptor": "Receptor", "Rilmazolam": "Rilmazolam", "Salvinorin B methoxymethyl ether": "Éter metoximetílico de salvinorina B",
    "Schmidt sting pain index": "Índice de dolor por picadura de Schmidt", "Scientific information": "Información científica",
    "Secobarbital": "Secobarbital", "Soma": "Soma", "Spokespeople": "Portavoces", "Subjective effect index": "Índice de efectos subjetivos",
    "Tabernaemontana undulata (botany)": "Tabernaemontana undulata (botánica)", "Tapentadol": "Tapentadol", "Temazepam": "Temazepam",
    "Tetrahydrocannabinol": "Tetrahidrocannabinol", "Tetrahydrocannabutol": "Tetrahidrocannabutol", "Tramadol": "Tramadol",
    "Trippy vibes": "Vibraciones psicodélicas", "Tripsitting index": "Índice de acompañamiento", "Turbina corymbosa (botany)": "Turbina corymbosa (botánica)",
    "Tutorial index": "Índice de tutoriales", "Tyrosine": "Tirosina", "Visual effects - Psychedelics": "Efectos visuales de los psicodélicos",
    "Yoga Nidra": "Yoga nidra", "Zolpidem": "Zolpidem", "Oneironautics": "Onironáutica",
    # nombres con artículo o con cifras que conviene dejar como en la wiki aunque la regla general los cambie
    "Trip sitter": "Acompañante (trip sitter)",
}
FIJOS = {"Psilocybin mushrooms": "Setas de psilocibina", "Set and setting": "Set y setting", "Bad trip": "Mal viaje",
         "Unity and interconnectedness": "Unidad e interconexión", "Ayahuasca": "Ayahuasca"}


# Títulos que salían repetidos (26-11-2026): cada página con el suyo.
TITULOS.update({"Delusion": "Idea delirante", "LSA adducts": "Aductos de LSA", "DXM & DPH": "DXM y DPH"})
TITULOS.update({"Papaver somniferum": "Papaver somniferum (adormidera)", "Shulgin Rating Scale": "Escala de Shulgin",
                "Shadow people": "Figuras de sombra", "8A Geometry - Perceived exposure to semantic concept network": "Geometría 8A"})

def es_codigo(original):
    """Siglas y nombres con cifras: se dejan como en la wiki (LSD, MDMA, 2C-B, 4-AcO-DMT, 25x-NBOMe…)."""
    return bool(re.search(r"\d", original)) or bool(re.fullmatch(r"[A-Z][A-Za-z]?[A-Z][A-Za-z\-]{0,8}", original)) and sum(c.isupper() for c in original) >= 2


def titulo(original, actual):
    if original in FIJOS:
        return FIJOS[original]
    if original in TITULOS:
        return TITULOS[original]
    if es_codigo(original):
        return original
    t = re.sub(r"'{2,}", "", actual or original).strip()
    t = re.sub(r"^(El|La|Los|Las|Un|Una)\s+(?=\S)", "", t)
    return t[:1].upper() + t[1:]
