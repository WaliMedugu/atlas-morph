"""
ATLAS-MORPH: Expanded Multilingual Benchmark Evaluation Dataset (60 Prompts)
=============================================================================
Curated benchmark corpus covering Yorùbá, Hausa, Igbo, and English
spanning Healthcare, Agriculture, Governance, Technology, Legal, and Dialogue.
"""

from typing import List, Dict

BENCHMARK_CORPUS: List[Dict[str, str]] = [
    # ==========================================
    # --- YORÙBÁ DATASET (Tonal diacritics & subdots) ---
    # ==========================================
    {"lang": "yor", "category": "healthcare", "text": "Àrùn ibà jẹ́ àìsàn tí ẹ̀fọn máa ń tàn kálẹ̀ nígbà tí ó bá bu ènìyàn jẹ ní alẹ́."},
    {"lang": "yor", "category": "healthcare", "text": "Ọmọdé gbọdọ̀ gba gbogbo abẹ́rẹ́ àjẹsára ní àkókò tó yẹ láti dènà àìsàn ikọ́-ọfe."},
    {"lang": "yor", "category": "healthcare", "text": "Ṣé oogun yìí kò ní pa ọmọdé lára tí ó bá mu ú nígbà tí ara rẹ̀ bá gbóná?"},
    {"lang": "yor", "category": "agriculture", "text": "Àgbẹ̀ gbọdọ̀ tọ́jú ilẹ̀ dáadáa kí wọ́n tó gbin àgbàdo àti ẹ̀wà ní àsìkò òjò."},
    {"lang": "yor", "category": "agriculture", "text": "Àwọn kòkòrò amúnikúnlẹ̀ ń ba oko kòkó jẹ́, ó sì yẹ kí a lo oògùn tó tọ́ láti pa wọ́n."},
    {"lang": "yor", "category": "agriculture", "text": "Ìmọ̀ ẹ̀rọ tuntun ti mú kí iṣẹ́ àgbẹ̀ rọrùn púpọ̀ fún àwọn àgbẹ̀ kéékèèké ní orílẹ̀-èdè wa."},
    {"lang": "yor", "category": "governance", "text": "Ìjọba àpapọ̀ ti kéde ètò tuntun láti ran àwọn ọ̀dọ́ lọ́wọ́ nínú ìmọ̀ ẹ̀rọ àti iṣẹ́ ọnà."},
    {"lang": "yor", "category": "governance", "text": "Àwọn aṣojú ìjọba gbọdọ̀ jẹ́ olóòótọ́ sí àwọn ènìyàn tí wọ́n dìbò yàn wọ́n sí ipò àṣẹ."},
    {"lang": "yor", "category": "technology", "text": "Ọgbọ́n àtọwọ́dáwọ́ AI yìí yóò mú kí kọ̀ǹpútà mọ èdè Yorùbá dáradára láìsí ìṣòro."},
    {"lang": "yor", "category": "technology", "text": "Ìṣirò orí ẹ̀rọ ayélujára ń tẹ̀síwájú ní kíákíá pẹ̀lú ìrànwọ́ àwọn onímọ̀ sáyẹ́ǹsì."},
    {"lang": "yor", "category": "legal_civic", "text": "Òfin orílẹ̀-èdè Nàìjíríà fún gbogbo ọmọ orílẹ̀-èdè ní ẹ̀tọ́ láti sọ èrò ọkàn rẹ̀ ní fàlàlà."},
    {"lang": "yor", "category": "daily_dialogue", "text": "Ẹ káàárọ̀ o gbogbo ilé, báwo ni ọjọ́ kẹrin ọ̀sẹ̀ yìí ṣe ń lọ fún yín?"},
    {"lang": "yor", "category": "daily_dialogue", "text": "Ẹ ṣé púpọ̀ fún ìrànwọ́ tí ẹ ṣe fún mi ní àná, inú mi dùn gidigidi."},
    {"lang": "yor", "category": "education", "text": "Ẹ̀kọ́ kíkà jẹ́ ọ̀nà pàtàkì tí ó ń ṣí ìlẹ̀kùn ọjọ́ ọ̀la rere fún àwọn ọmọ wa."},
    {"lang": "yor", "category": "commerce", "text": "Ọjà kò tíì rọrùn púpọ̀ lónìí nítorí iye owó epo bẹntiroolu tí ó ga sókè."},

    # ==========================================
    # --- HAUSA DATASET (Hooked glottals & tone orthography) ---
    # ==========================================
    {"lang": "hau", "category": "healthcare", "text": "Zazzabin cizon sauro yana daya daga cikin cututtukan da ke damun mutane a lokacin damina."},
    {"lang": "hau", "category": "healthcare", "text": "Wajibi ne iyaye su kai yara asibiti don karbar allurar riga-kafi a kan kari."},
    {"lang": "hau", "category": "healthcare", "text": "Wannan maganin zai taimaka wajen rage zazzabin cizon sauro ga kananan yara."},
    {"lang": "hau", "category": "agriculture", "text": "Manoma su tabbatar sun yi amfani da ingantaccen takin zamani wajen noman masara da gero."},
    {"lang": "hau", "category": "agriculture", "text": "Ƙungiyar manoma ta shawarci jama'a game da kiyaye amfanin gona daga fari da kwari."},
    {"lang": "hau", "category": "agriculture", "text": "Nomin rani yana taimakawa wajen samar da wadataccen abinci a lokacin sanyi."},
    {"lang": "hau", "category": "governance", "text": "Gwamnatin tarayya ta kaddamar da sabon shirin tallafawa matasa a fannin fasahar zamani."},
    {"lang": "hau", "category": "governance", "text": "Ɓangaren shari'a yana bukatar garambawul don tabbatar da adalci ga kowa a cikin al'umma."},
    {"lang": "hau", "category": "technology", "text": "Wannan fasaha ta basirar na'ura za ta taimaka wajen bunkasa harsunan Afirka a duniya."},
    {"lang": "hau", "category": "technology", "text": "Kwamfuta mai amfani da fasahar AI za ta iya fahimtar yaren Hausa cikin sauki."},
    {"lang": "hau", "category": "legal_civic", "text": "Tsarin mulkin Najeriya ya ba kowane dan kasa 'yancin fadar albarkacin bakinsa."},
    {"lang": "hau", "category": "daily_dialogue", "text": "Ina kwana lafiya lau, yaya aiki da kuma kokarin yau da kullum?"},
    {"lang": "hau", "category": "daily_dialogue", "text": "Barka da yamma, fatan kowa ya dawo gida lafiya daga wurin sana'a."},
    {"lang": "hau", "category": "education", "text": "Ilimi shi ne ginshikin ci gaban kowace al'umma a fadin duniyar nan."},
    {"lang": "hau", "category": "commerce", "text": "Kasuwancin zamani na intanet yana samun karbuwa sosai a tsakanin matasa."},

    # ==========================================
    # --- IGBO DATASET (Sub-dots & vowel harmony) ---
    # ==========================================
    {"lang": "ibo", "category": "healthcare", "text": "Ọrịa anwụnta bụ ajọ ọrịa na-enye ndị mmadụ nsogbu karịsịa n'oge udu mmiri."},
    {"lang": "ibo", "category": "healthcare", "text": "Nne na nna kwesịrị ịkpọrọ nwa ha gaa ụlọ ọgwụ ma ọ bụrụ na ahụ ọkụ dị ukwuu."},
    {"lang": "ibo", "category": "healthcare", "text": "Ịṅụ ọgwụ n'ụzọ ziri ezi na-enyere aka igbochi nsogbu ahụike dị iche iche."},
    {"lang": "ibo", "category": "agriculture", "text": "Ndị ọrụ ugbo kwesịrị ịhọrọ ezigbo mkpụrụ osisi tupu ha akụọ ọka na ji n'ubi ha."},
    {"lang": "ibo", "category": "agriculture", "text": "Ọrụ ugbo na-enye aka n'ịkwalite nri na nchekwa obodo n'oge ọkọchị."},
    {"lang": "ibo", "category": "agriculture", "text": "Iji nri fatịlaịza mee ihe n'ụzọ kwesịrị ekwesị na-eme ka ala mịa ezigbo mkpụrụ."},
    {"lang": "ibo", "category": "governance", "text": "Gọọmenti etiti amalitela atụmatụ ọhụrụ iji kwado ndị ntorobịa n'ọrụ aka na teknụzụ."},
    {"lang": "ibo", "category": "governance", "text": "Ndị ndu obodo kwesịrị ịtụgharị uche n'ịrụ ọrụ maka ọdịmma nke ndị ha na-achị."},
    {"lang": "ibo", "category": "technology", "text": "Teknụzụ ọgụgụ isi a ga-eme ka kọmputa nwee ike ịghọta asụsụ Igbo nke ọma."},
    {"lang": "ibo", "category": "technology", "text": "Mmepe nke ngwa ntanetị na-eme ka nkwukọrịta dị mfe n'etiti ndị mmadụ."},
    {"lang": "ibo", "category": "legal_civic", "text": "Iwu obodo nyere onye ọ bụla ikike ibi ndụ n'udo na ịchọ ezi ọganihu."},
    {"lang": "ibo", "category": "daily_dialogue", "text": "Ụtụtụ ọma ndị be anyị, kedu ka ụbọchị taa si aga n'ebe unu nọ?"},
    {"lang": "ibo", "category": "daily_dialogue", "text": "Daalụ nke ukwuu maka enyemaka ị nyere m ụnyaahụ, obi dị m ụtọ nke ukwuu."},
    {"lang": "ibo", "category": "education", "text": "Mmụta na agụmakwụkwọ bụ isi ihe na-eweta mmepe n'obodo anyị."},
    {"lang": "ibo", "category": "commerce", "text": "Ahịa taa dị mma n'ihi na ndị ahịa bịara n'ọtụtụ iji zụta ngwongwo."},

    # ==========================================
    # --- ENGLISH CONTROL DATASET ---
    # ==========================================
    {"lang": "eng", "category": "healthcare", "text": "Malaria is a preventable illness spread by mosquitoes during the rainy season."},
    {"lang": "eng", "category": "healthcare", "text": "Children should receive essential immunizations on schedule to prevent infectious diseases."},
    {"lang": "eng", "category": "healthcare", "text": "Clinical diagnostic accuracy is critical when treating severe pediatric respiratory illness."},
    {"lang": "eng", "category": "agriculture", "text": "Smallholder farmers should treat soil adequately before planting maize and beans."},
    {"lang": "eng", "category": "agriculture", "text": "Modern irrigation systems allow rural farmers to cultivate crops throughout the dry season."},
    {"lang": "eng", "category": "agriculture", "text": "Agricultural extension workers provide vital guidance on pest control and crop rotation."},
    {"lang": "eng", "category": "governance", "text": "The Federal Government launched a new initiative supporting youth in technology."},
    {"lang": "eng", "category": "governance", "text": "Transparent public expenditure tracking reinforces community trust in national programs."},
    {"lang": "eng", "category": "technology", "text": "This artificial intelligence model enables computers to understand Nigerian languages."},
    {"lang": "eng", "category": "technology", "text": "High performance inference acceleration enables models to run on affordable edge hardware."},
    {"lang": "eng", "category": "legal_civic", "text": "The constitution guarantees fundamental human rights and freedom of expression for all citizens."},
    {"lang": "eng", "category": "daily_dialogue", "text": "Good morning everyone, how is your work and daily activities progressing today?"},
    {"lang": "eng", "category": "daily_dialogue", "text": "Thank you very much for your kind assistance yesterday, I truly appreciate your support."},
    {"lang": "eng", "category": "education", "text": "Quality education is the foundation for socioeconomic empowerment and national progress."},
    {"lang": "eng", "category": "commerce", "text": "Digital retail commerce is expanding rapidly across urban and peri-urban centers in Nigeria."},
]
