import json

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

# English translation dictionary for titles, meanings, definitions, fadhilats
en_map = {
    1: {
        "title": "Prayer Upon Waking Up",
        "meaning": "All praise is due to Allah who brought us to life after our death, and to Him is the return.",
        "fadhilat": "Expressing gratitude to Allah for granting another day of life and acknowledging resurrection."
    },
    2: {
        "title": "Before Eating Prayer",
        "meaning": "O Allah, bless us in what You have provided us and protect us from the punishment of the Fire.",
        "fadhilat": "Seeking blessings in our sustenance and protection from Hellfire."
    },
    3: {
        "title": "Leaving Home Prayer",
        "meaning": "In the name of Allah, I place my trust in Allah; there is no might nor power except by Allah.",
        "fadhilat": "Seeking divine protection, guidance, and sufficiency when stepping out of the house."
    },
    4: {
        "title": "Entering Restroom Prayer",
        "meaning": "O Allah, I seek refuge in You from all male and female impure spirits (devils).",
        "fadhilat": "Protection from unclean places and invisible harm."
    },
    5: {
        "title": "After Eating Prayer",
        "meaning": "All praise is due to Allah who has fed us, provided us drink, and made us Muslims.",
        "fadhilat": "Gratitude for sustenance and Islam."
    },
    6: {
        "title": "Entering Home Prayer",
        "meaning": "In the name of Allah we enter, in the name of Allah we leave, and upon our Lord we rely.",
        "fadhilat": "Blessings and peace entering the household."
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
        "title": "Prayer for Both Parents",
        "meaning": "My Lord, have mercy upon them as they brought me up [when I was] small.",
        "fadhilat": "Filial piety and invoking divine mercy upon parents."
    },
    10: {
        "title": "Riding / Vehicle Prayer",
        "meaning": "Exalted is He who has subjected this to us, and we could not have otherwise subdued it. And indeed, to our Lord we will surely return.",
        "fadhilat": "Safety during travel and acknowledging Allah's sovereignty."
    },
    11: {
        "title": "Opening Supplication (Iftitah)",
        "meaning": "Allah is most great... Verily my prayer, my sacrifice, my living and my dying are for Allah, Lord of the worlds.",
        "fadhilat": "Establishing presence and sincerity at the start of prayer."
    },
    12: {
        "title": "Master of Istighfar (Sayyidul Istighfar)",
        "meaning": "O Allah, You are my Lord, there is no deity except You... I acknowledge Your favor upon me and I acknowledge my sin, so forgive me...",
        "fadhilat": "Guaranteed Paradise for whoever recites it with firm belief during day or night and dies."
    },
    13: {
        "title": "Prayer for Righteous Offspring & Family",
        "meaning": "Our Lord, grant us from among our wives and offspring comfort to our eyes and make us an example for the righteous.",
        "fadhilat": "Harmony in family and righteous progeny."
    },
    14: {
        "title": "Prayer to Thank Allah's Blessings",
        "meaning": "My Lord, enable me to be grateful for Your favor which You have bestowed upon me and upon my parents...",
        "fadhilat": "Continuous blessings through gratitude."
    },
    15: {
        "title": "Post-Prayer Dhikr & Supplications",
        "meaning": "O Allah, You are Peace and from You is peace... There is no deity except Allah alone, without partner...",
        "fadhilat": "Purification and elevated spiritual station after obligatory prayers."
    },
    16: {
        "title": "Prayer Upon Completing Al-Quran (Khatam)",
        "meaning": "O Allah, have mercy on me through the Magnificent Quran and make it for me a leader, light, guidance, and mercy...",
        "fadhilat": "Enormous barakah and acceptance upon finishing Quran recitation."
    },
    17: {
        "title": "Step 1: Takbiratul Ihram & Intention",
        "meaning": "Intention and opening takbir for prayer.",
        "definition": "The formal commencement of prayer."
    },
    18: {
        "title": "Step 2: Opening Supplication (Iftitah)",
        "meaning": "Opening supplication recited after Takbiratul Ihram."
    },
    19: {
        "title": "Step 3: Bowing (Ruku') Recitation",
        "meaning": "Glory is to my Lord, the Magnificent, and with His praise.",
        "definition": "Glorifying Allah in bowing position."
    },
    20: {
        "title": "Step 4: Rising from Ruku' (I'tidal)",
        "meaning": "Allah hears whoever praises Him. Our Lord, to You belongs all praise.",
        "definition": "Standing erect after ruku'."
    },
    21: {
        "title": "Step 5: Prostration (Sujud) Recitation",
        "meaning": "Glory is to my Lord, the Most High, and with His praise.",
        "definition": "The closest a servant is to Allah during prostration."
    },
    22: {
        "title": "Step 6: Sitting Between Two Prostrations",
        "meaning": "O Lord, forgive me, have mercy on me, guide me, enrich me, give me health, and pardon me.",
        "definition": "Supplication for complete well-being between prostrations."
    },
    23: {
        "title": "Step 7: First Tahiyyat (Tashahhud Awal)",
        "meaning": "Salutations, prayers, and good things belong to Allah. Peace be upon you, O Prophet...",
        "definition": "Attestation of faith in the middle of prayers with 3 or 4 rakaats."
    },
    24: {
        "title": "Step 8: Final Tahiyyat (Tashahhud Akhir)",
        "meaning": "Salutations, prayers, and good things belong to Allah... O Allah, send prayers upon Muhammad and upon the family of Muhammad...",
        "definition": "Final testimony and blessings upon Prophet Muhammad before salam."
    },
    25: {
        "title": "Step 9: Concluding Salam",
        "meaning": "Peace be upon you and the mercy of Allah.",
        "definition": "Concluding the prayer by turning the head right and left."
    },
    26: {
        "title": "Prayer for Healing & Recovery",
        "meaning": "O Allah, Lord of mankind, remove the affliction and heal, for You are the Healer. There is no cure except Your cure...",
        "fadhilat": "Prophetic healing and relief from illness."
    },
    27: {
        "title": "Intention for Subuh Prayer",
        "meaning": "I intend to pray the obligatory Subuh prayer of two rakaats facing the qibla, following the imam, for Allah the Almighty.",
        "definition": "Intention for Fajr/Subuh prayer."
    },
    28: {
        "title": "Intention for Zohor Prayer",
        "meaning": "I intend to pray the obligatory Zohor prayer of four rakaats...",
        "definition": "Intention for Dhuhr prayer."
    },
    29: {
        "title": "Intention for Asar Prayer",
        "meaning": "I intend to pray the obligatory Asar prayer of four rakaats...",
        "definition": "Intention for Asr prayer."
    },
    30: {
        "title": "Intention for Maghrib Prayer",
        "meaning": "I intend to pray the obligatory Maghrib prayer of three rakaats...",
        "definition": "Intention for Maghrib prayer."
    },
    31: {
        "title": "Intention for Isyak Prayer",
        "meaning": "I intend to pray the obligatory Isyak prayer of four rakaats...",
        "definition": "Intention for Isha prayer."
    },
    32: {
        "title": "Intention for Dhuha Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Dhuha prayer of two rakaats for Allah the Almighty.",
        "definition": "Sunnah prayer performed in the morning after sunrise."
    },
    33: {
        "title": "Intention for Tahajjud Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Tahajjud prayer of two rakaats for Allah the Almighty.",
        "definition": "Night vigil prayer performed after sleeping."
    },
    34: {
        "title": "Intention for Hajat Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Hajat prayer of two rakaats for Allah the Almighty.",
        "definition": "Prayer to seek Allah's help and fulfillment of needs."
    },
    35: {
        "title": "Intention for Witir Sunnah Prayer",
        "meaning": "I intend to pray the Sunnah Witir prayer of two/one rakaat for Allah the Almighty.",
        "definition": "Odd-numbered concluding night prayer."
    },
    36: {
        "title": "Intention for Rawatib Qobliyah Subuh",
        "meaning": "I intend to pray the Sunnah Qobliyah Subuh prayer before it...",
        "definition": "Rawatib sunnah prayer before Subuh."
    },
    37: {
        "title": "Intention for Rawatib Qobliyah Zohor",
        "meaning": "I intend to pray the Sunnah Qobliyah Zohor prayer before it...",
        "definition": "Rawatib sunnah prayer before Zohor."
    },
    38: {
        "title": "Intention for Rawatib Ba'diyah Zohor",
        "meaning": "I intend to pray the Sunnah Ba'diyah Zohor prayer after it...",
        "definition": "Rawatib sunnah prayer after Zohor."
    },
    39: {
        "title": "Intention for Rawatib Ba'diyah Maghrib",
        "meaning": "I intend to pray the Sunnah Ba'diyah Maghrib prayer after it...",
        "definition": "Rawatib sunnah prayer after Maghrib."
    },
    40: {
        "title": "Intention for Rawatib Ba'diyah Isyak",
        "meaning": "I intend to pray the Sunnah Ba'diyah Isyak prayer after it...",
        "definition": "Rawatib sunnah prayer after Isyak."
    },
    41: {
        "title": "Intention for Rawatib Qobliyah Asar",
        "meaning": "I intend to pray the Sunnah Qobliyah Asar prayer before it...",
        "definition": "Rawatib sunnah prayer before Asar."
    },
    42: {
        "title": "Intention for Rawatib Qobliyah Maghrib",
        "meaning": "I intend to pray the Sunnah Qobliyah Maghrib prayer before it...",
        "definition": "Rawatib sunnah prayer before Maghrib."
    },
    43: {
        "title": "Intention for Rawatib Qobliyah Isyak",
        "meaning": "I intend to pray the Sunnah Qobliyah Isyak prayer before it...",
        "definition": "Rawatib sunnah prayer before Isyak."
    },
    44: {
        "title": "Istikharah Prayer Supplication",
        "meaning": "O Allah, I seek Your guidance through Your knowledge, and Ability through Your power...",
        "fadhilat": "Guidance in making important life decisions."
    },
    45: {
        "title": "Prayer for Offspring (Prophet Zakaria a.s.)",
        "meaning": "My Lord, grant me from Yourself a good offspring. Indeed, You are the Hearer of supplication.",
        "fadhilat": "Seeking righteous children and divine grace."
    },
    46: {
        "title": "Intention for Friday (Jumaat) Prayer",
        "meaning": "I intend to pray the obligatory Jumaat prayer of two rakaats following the imam for Allah the Almighty.",
        "definition": "Congregational Friday prayer."
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
    if did in en_map:
        new_d['title'] = en_map[did].get('title', d['title'])
        new_d['meaning'] = en_map[did].get('meaning', d['meaning'])
        if 'definition' in d or 'definition' in en_map[did]:
            new_d['definition'] = en_map[did].get('definition', d.get('definition', ''))
        if 'fadhilat' in d or 'fadhilat' in en_map[did]:
            new_d['fadhilat'] = en_map[did].get('fadhilat', d.get('fadhilat', ''))
    en_duas.append(new_d)

with open('en-duas.json', 'w', encoding='utf-8') as f:
    json.dump(en_duas, f, ensure_ascii=False, indent=2)

print("Successfully generated en-duas.json with 48 translated entries!")
