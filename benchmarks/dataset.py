"""
ATLAS-MORPH: Multilingual Benchmark Evaluation Dataset
======================================================
Curated benchmark corpus covering Yorùbá, Hausa, Igbo, and English
spanning news, health advisories, governance, agricultural advice, and daily dialogue.
"""

from typing import List, Dict

BENCHMARK_CORPUS: List[Dict[str, str]] = [
    # --- YORÙBÁ DATASET (Tonal diacritics & subdots) ---
    {
        "lang": "yor",
        "category": "healthcare",
        "text": "Àrùn ibà jẹ́ àìsàn tí ẹ̀fọn máa ń tàn kálẹ̀ nígbà tí ó bá bu ènìyàn jẹ ní alẹ́.",
    },
    {
        "lang": "yor",
        "category": "agriculture",
        "text": "Àgbẹ̀ gbọdọ̀ tọ́jú ilẹ̀ dáadáa kí wọ́n tó gbin àgbàdo àti ẹ̀wà ní àsìkò òjò.",
    },
    {
        "lang": "yor",
        "category": "governance",
        "text": "Ìjọba àpapọ̀ ti kéde ètò tuntun láti ran àwọn ọ̀dọ́ lọ́wọ́ nínú ìmọ̀ ẹ̀rọ àti iṣẹ́ ọnà.",
    },
    {
        "lang": "yor",
        "category": "technology",
        "text": "Ọgbọ́n àtọwọ́dáwọ́ AI yìí yóò mú kí kọ̀ǹpútà mọ èdè Yorùbá dáradára láìsí ìṣòro.",
    },
    {
        "lang": "yor",
        "category": "daily_dialogue",
        "text": "Ẹ káàárọ̀ o gbogbo ilé, báwo ni ọjọ́ kẹrin ọ̀sẹ̀ yìí ṣe ń lọ fún yín?",
    },

    # --- HAUSA DATASET (Hooked glottals & tone orthography) ---
    {
        "lang": "hau",
        "category": "healthcare",
        "text": "Zazzabin cizon sauro yana daya daga cikin cututtukan da ke damun mutane a lokacin damina.",
    },
    {
        "lang": "hau",
        "category": "agriculture",
        "text": "Manoma su tabbatar sun yi amfani da ingantaccen takin zamani wajen noman masara da gero.",
    },
    {
        "lang": "hau",
        "category": "governance",
        "text": "Gwamnatin tarayya ta kaddamar da sabon shirin tallafawa matasa a fannin fasahar zamani.",
    },
    {
        "lang": "hau",
        "category": "technology",
        "text": "Wannan fasaha ta basirar na'ura za ta taimaka wajen bunkasa harsunan Afirka a duniya.",
    },
    {
        "lang": "hau",
        "category": "daily_dialogue",
        "text": "Ina kwana lafiya lau, yaya aiki da kuma kokarin yau da kullum?",
    },

    # --- IGBO DATASET (Sub-dots & vowel harmony) ---
    {
        "lang": "ibo",
        "category": "healthcare",
        "text": "Ọrịa anwụnta bụ ajọ ọrịa na-enye ndị mmadụ nsogbu karịsịa n'oge udu mmiri.",
    },
    {
        "lang": "ibo",
        "category": "agriculture",
        "text": "Ndị ọrụ ugbo kwesịrị ịhọrọ ezigbo mkpụrụ osisi tupu ha akụọ ọka na ji n'ubi ha.",
    },
    {
        "lang": "ibo",
        "category": "governance",
        "text": "Gọọmenti etiti amalitela atụmatụ ọhụrụ iji kwado ndị ntorobịa n'ọrụ aka na teknụzụ.",
    },
    {
        "lang": "ibo",
        "category": "technology",
        "text": "Teknụzụ ọgụgụ isi a ga-eme ka kọmputa nwee ike ịghọta asụsụ Igbo nke ọma.",
    },
    {
        "lang": "ibo",
        "category": "daily_dialogue",
        "text": "Ụtụtụ ọma ndị be anyị, kedu ka ụbọchị taa si aga n'ebe unu nọ?",
    },

    # --- ENGLISH CONTROL DATASET ---
    {
        "lang": "eng",
        "category": "healthcare",
        "text": "Malaria is a preventable illness spread by mosquitoes during the rainy season.",
    },
    {
        "lang": "eng",
        "category": "agriculture",
        "text": "Smallholder farmers should treat soil adequately before planting maize and beans.",
    },
    {
        "lang": "eng",
        "category": "governance",
        "text": "The Federal Government launched a new initiative supporting youth in technology.",
    },
    {
        "lang": "eng",
        "category": "technology",
        "text": "This artificial intelligence model enables computers to understand Nigerian languages.",
    },
    {
        "lang": "eng",
        "category": "daily_dialogue",
        "text": "Good morning everyone, how is your work and daily activities progressing today?",
    },
]
