import json

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

cat_map = {
    "Harian": "Daily",
    "Perlindungan": "Protection",
    "Kesihatan": "Health",
    "Ilmu": "Knowledge",
    "Wirid": "Wird",
    "Istigfar": "Istighfar",
    "Majlis": "Gathering",
    "Bacaan Solat": "Prayer Recitations",
    "Niat Solat": "Prayer Intentions",
    "Solat Fardu": "Obligatory Prayer",
    "Solat Sunat": "Sunnah Prayer",
    "Rawatib": "Rawatib Sunnah",
    "Favorit": "Favorites",
    "Sunat Amalan": "Sunnah Practices"
}

def translate_cat(c):
    if isinstance(c, list):
        return [cat_map.get(x, x) for x in c]
    return cat_map.get(c, c)

translations_db = {
    1: {
        "title": "Prayer Upon Waking Up",
        "meaning": "All praise is due to Allah who brought us to life after our death, and to Him is the return.",
        "fadhilat": "Expressing gratitude to Allah for granting another day of life and acknowledging resurrection."
    },
    2: {
        "title": "Prayer Before Eating",
        "meaning": "O Allah, bless us in what You have provided us and protect us from the punishment of the Fire.",
        "fadhilat": "Seeking blessings in our sustenance and protection from Hellfire."
    },
    3: {
        "title": "Prayer When Leaving Home",
        "meaning": "In the name of Allah, I place my trust in Allah; there is no might nor power except by Allah.",
        "fadhilat": "Seeking divine protection, guidance, and sufficiency when stepping out of the house."
    },
    4: {
        "title": "Prayer When Entering Restroom",
        "meaning": "O Allah, I seek refuge in You from all male and female impure spirits (devils).",
        "fadhilat": "Seeking protection from unclean places and invisible harm."
    },
    5: {
        "title": "Prayer After Eating",
        "meaning": "All praise is due to Allah who has fed us, provided us drink, and made us Muslims.",
        "fadhilat": "Gratitude for sustenance and Islam."
    },
    6: {
        "title": "Prayer When Entering Home",
        "meaning": "In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we rely.",
        "fadhilat": "Bringing blessings, peace, and angelic presence into the household."
    },
    7: {
        "title": "Prayer for Beneficial Knowledge",
        "meaning": "O my Lord, increase me in knowledge and grant me understanding.",
        "fadhilat": "Increase in wisdom, knowledge, and spiritual clarity."
    },
    8: {
        "title": "Prayer for Good in This World & Hereafter",
        "meaning": "Our Lord, give us in this world that which is good and in the Hereafter that which is good, and protect us from the punishment of the Fire.",
        "fadhilat": "Comprehensive dua covering worldly success and ultimate salvation."
    },
    9: {
        "title": "Prayer for Parents",
        "meaning": "My Lord, have mercy upon them as they brought me up when I was small.",
        "fadhilat": "Filial piety and invoking divine mercy upon parents."
    },
    10: {
        "title": "Prayer When Riding a Vehicle",
        "meaning": "Exalted is He who has subjected this to us, and we could not have otherwise subdued it. And indeed, to our Lord we will surely return.",
        "fadhilat": "Safety during travel and acknowledging Allah's sovereignty."
    },
    11: {
        "title": "Opening Supplication (Iftitah)",
        "meaning": "Allah is most great with all greatness, and all praise is for Allah in abundance... Verily my prayer, my sacrifice, my living and my dying are for Allah, Lord of the worlds.",
        "fadhilat": "Establishing presence, sincerity, and glorification at the start of prayer."
    },
    12: {
        "title": "Master of Istighfar (Sayyidul Istighfar)",
        "meaning": "O Allah, You are my Lord, there is no deity except You. You created me and I am Your servant... I acknowledge Your favor upon me and I acknowledge my sin, so forgive me.",
        "fadhilat": "Whoever recites it during the day with firm belief and dies before evening is from the people of Paradise."
    },
    13: {
        "title": "Prayer for Righteous Offspring & Family",
        "meaning": "Our Lord, grant us from among our wives and offspring comfort to our eyes and make us an example for the righteous.",
        "fadhilat": "Harmony in family and righteous progeny."
    },
    14: {
        "title": "Prayer to Thank Allah's Blessings",
        "meaning": "My Lord, enable me to be grateful for Your favor which You have bestowed upon me and upon my parents...",
        "fadhilat": "Continuous blessings through gratitude and righteous actions."
    },
    15: {
        "title": "Post-Prayer Dhikr & Supplications",
        "meaning": "O Allah, You are Peace and from You is peace... There is no deity except Allah alone, without partner...",
        "fadhilat": "Purification, remembrance, and elevated spiritual station after obligatory prayers."
    },
    16: {
        "title": "Prayer Upon Completing Al-Quran (Khatam)",
        "meaning": "O Allah, have mercy on me through the Magnificent Quran and make it for me a leader, light, guidance, and mercy...",
        "fadhilat": "Enormous barakah, divine mercy, and acceptance upon finishing Quran recitation."
    },
    17: {
        "title": "Step 1: Takbiratul Ihram & Intention",
        "meaning": "Raising hands and saying 'Allahu Akbar' while making intention in the heart for the specific prayer.",
        "definition": "The formal commencement of prayer."
    },
    18: {
        "title": "Step 2: Opening Supplication (Iftitah)",
        "meaning": "Reciting the opening supplication after Takbiratul Ihram.",
        "definition": "Sunnah supplication recited at the beginning of prayer."
    },
    19: {
        "title": "Step 3: Bowing (Ruku') Recitation",
        "meaning": "Glory is to my Lord, the Magnificent, and with His praise.",
        "definition": "Glorifying Allah in bowing position with back straight."
    },
    20: {
        "title": "Step 4: Rising from Ruku' (I'tidal)",
        "meaning": "Allah hears whoever praises Him. Our Lord, to You belongs all praise.",
        "definition": "Standing erect after ruku' with poise."
    },
    21: {
        "title": "Step 5: Prostration (Sujud) Recitation",
        "meaning": "Glory is to my Lord, the Most High, and with His praise.",
        "definition": "The closest a servant is to Allah during prostration touching forehead and nose to the ground."
    },
    22: {
        "title": "Step 6: Sitting Between Two Prostrations",
        "meaning": "O Lord, forgive me, have mercy on me, guide me, enrich me, give me health, and pardon me.",
        "definition": "Supplication for complete well-being and forgiveness between the two prostrations."
    },
    23: {
        "title": "Step 7: First Tahiyyat (Tashahhud Awal)",
        "meaning": "Salutations, prayers, and good things belong to Allah. Peace be upon you, O Prophet, and the mercy of Allah and His blessings...",
        "definition": "Attestation of faith in the middle of prayers containing 3 or 4 rakaats."
    },
    24: {
        "title": "Step 8: Final Tahiyyat (Tashahhud Akhir)",
        "meaning": "Salutations, prayers, and good things belong to Allah... O Allah, send prayers upon Muhammad and upon the family of Muhammad...",
        "definition": "Final testimony and blessings upon Prophet Muhammad and Prophet Ibrahim before salam."
    },
    25: {
        "title": "Step 9: Concluding Salam",
        "meaning": "Peace be upon you and the mercy of Allah.",
        "definition": "Concluding the prayer officially by turning the head right and left."
    },
    26: {
        "title": "Prayer for Healing & Recovery",
        "meaning": "O Allah, Lord of mankind, remove the affliction and heal, for You are the Healer. There is no cure except Your cure...",
        "fadhilat": "Prophetic healing, comfort, and relief from illness."
    },
    27: {
        "title": "Intention for Subuh Prayer",
        "meaning": "I intend to pray the obligatory Subuh prayer of two rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Fajr/Subuh prayer."
    },
    28: {
        "title": "Intention for Zohor Prayer",
        "meaning": "I intend to pray the obligatory Zohor prayer of four rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Dhuhr prayer."
    },
    29: {
        "title": "Intention for Asar Prayer",
        "meaning": "I intend to pray the obligatory Asar prayer of four rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Asr prayer."
    },
    30: {
        "title": "Intention for Maghrib Prayer",
        "meaning": "I intend to pray the obligatory Maghrib prayer of three rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Maghrib prayer."
    },
    31: {
        "title": "Intention for Isyak Prayer",
        "meaning": "I intend to pray the obligatory Isyak prayer of four rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Isha prayer."
    },
    32: {
        "title": "Intention for Dhuha Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Dhuha prayer of two rakaats facing the qibla, for Allah the Almighty.",
        "definition": "Sunnah prayer performed in the morning after sunrise."
    },
    33: {
        "title": "Intention for Tahajjud Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Tahajjud prayer of two rakaats facing the qibla, for Allah the Almighty.",
        "definition": "Night vigil prayer performed after sleeping."
    },
    34: {
        "title": "Intention for Hajat Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Hajat prayer of two rakaats facing the qibla, for Allah the Almighty.",
        "definition": "Prayer to seek Allah's help and fulfillment of needs."
    },
    35: {
        "title": "Intention for Witir Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Witir prayer of two rakaats facing the qibla, for Allah the Almighty.",
        "definition": "Odd-numbered concluding night prayer."
    },
    36: {
        "title": "Intention for Rawatib Qobliyah Subuh",
        "meaning": "I intend to pray the Sunnah Qobliyah Subuh prayer of two rakaats before Subuh...",
        "definition": "Sunnah Rawatib prayer performed before Subuh prayer."
    },
    37: {
        "title": "Intention for Rawatib Qobliyah Zohor",
        "meaning": "I intend to pray the Sunnah Qobliyah Zohor prayer of two rakaats before Zohor...",
        "definition": "Sunnah Rawatib prayer performed before Zohor prayer."
    },
    38: {
        "title": "Intention for Rawatib Ba'diyah Zohor",
        "meaning": "I intend to pray the Sunnah Ba'diyah Zohor prayer of two rakaats after Zohor...",
        "definition": "Sunnah Rawatib prayer performed after Zohor prayer."
    },
    39: {
        "title": "Intention for Rawatib Ba'diyah Maghrib",
        "meaning": "I intend to pray the Sunnah Ba'diyah Maghrib prayer of two rakaats after Maghrib...",
        "definition": "Sunnah Rawatib prayer performed after Maghrib prayer."
    },
    40: {
        "title": "Intention for Rawatib Ba'diyah Isyak",
        "meaning": "I intend to pray the Sunnah Ba'diyah Isyak prayer of two rakaats after Isyak...",
        "definition": "Sunnah Rawatib prayer performed after Isyak prayer."
    },
    41: {
        "title": "Intention for Rawatib Qobliyah Asar",
        "meaning": "I intend to pray the Sunnah Qobliyah Asar prayer of two rakaats before Asar...",
        "definition": "Sunnah Rawatib prayer performed before Asar prayer."
    },
    42: {
        "title": "Intention for Rawatib Qobliyah Maghrib",
        "meaning": "I intend to pray the Sunnah Qobliyah Maghrib prayer of two rakaats before Maghrib...",
        "definition": "Sunnah Rawatib prayer performed before Maghrib prayer."
    },
    43: {
        "title": "Intention for Rawatib Qobliyah Isyak",
        "meaning": "I intend to pray the Sunnah Qobliyah Isyak prayer of two rakaats before Isyak...",
        "definition": "Sunnah Rawatib prayer performed before Isyak prayer."
    },
    44: {
        "title": "Istikharah Prayer Supplication",
        "meaning": "O Allah, I seek Your guidance through Your knowledge, and Ability through Your power...",
        "fadhilat": "Seeking divine guidance and ease in making important life decisions."
    },
    45: {
        "title": "Prayer for Offspring (Prophet Zakaria a.s.)",
        "meaning": "My Lord, grant me from Yourself a good offspring. Indeed, You are the Hearer of supplication.",
        "fadhilat": "Seeking righteous children and divine grace."
    },
    46: {
        "title": "Intention for Friday (Jumaat) Prayer",
        "meaning": "I intend to pray the obligatory Jumaat prayer of two rakaats following the imam, for Allah the Almighty.",
        "definition": "Congregational Friday prayer replacing Zohor."
    },
    47: {
        "title": "Prayer Before Sleeping",
        "meaning": "In Your name, O Allah, I die and I live.",
        "fadhilat": "Placing oneself in Allah's protection before sleep."
    },
    48: {
        "title": "Prayer for Peace & Gratitude",
        "meaning": "O Allah, grant us safety, faith, peace, and well-being...",
        "fadhilat": "Divine peace, security, and stability."
    }
}

en_duas = []
for d in duas:
    new_d = d.copy()
    did = d['id']
    new_d['category'] = translate_cat(d['category'])

    # Translate source strings if present
    src = d.get('source', '')
    if src:
        src = src.replace('Riwayat', 'Narrated by').replace('Al-Quran', 'Quran').replace('Daripada', 'from')
    new_d['source'] = src

    if did in translations_db:
        td = translations_db[did]
        new_d['title'] = td.get('title', d['title'])
        new_d['meaning'] = td.get('meaning', d['meaning'])
        if 'definition' in d or 'definition' in td:
            new_d['definition'] = td.get('definition', d.get('definition', ''))
        if 'fadhilat' in d or 'fadhilat' in td:
            new_d['fadhilat'] = td.get('fadhilat', d.get('fadhilat', ''))

    en_duas.append(new_d)

with open('en-duas.json', 'w', encoding='utf-8') as f:
    json.dump(en_duas, f, ensure_ascii=False, indent=2)

print("en-duas.json fully translated and updated successfully!")
