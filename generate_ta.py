import json

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

cat_ta = {
    "Harian": "தினசரி",
    "Perlindungan": "பாதுகாப்பு",
    "Kesihatan": "சுகாதாரம்",
    "Ilmu": "கல்வி",
    "Wirid": "திக்ர்",
    "Istigfar": "இஸ்திக்பார்",
    "Majlis": "சபை",
    "Bacaan Solat": "தொழுகை ஓதுதல்கள்",
    "Niat Solat": "தொழுகை நிய்யத்",
    "Solat Fardu": "பர்ளு தொழுகை",
    "Solat Sunat": "சுன்னத் தொழுகை",
    "Rawatib": "ரவாதிப்",
    "Favorit": "விருப்பமானவை",
    "Sunat Amalan": "சுன்னத் அமல்கள்"
}

def translate_ta_cat(c):
    if isinstance(c, list):
        return [cat_ta.get(x, x) for x in c]
    return cat_ta.get(c, c)

ta_duas = []
for d in duas:
    new_d = d.copy()
    new_d['category'] = translate_ta_cat(d['category'])
    if d.get('source'):
        new_d['source'] = d['source'].replace('Sahih (Riwayat al-Bukhari & Muslim)', 'ஸஹீஹ் ஹதீஸ் ( புகாரி & முஸ்லிம்)').replace('Al-Quran', 'அல்குர்ஆன்')

    # Tamil translations for key titles/meanings
    did = d['id']
    if did == 1:
        new_d['title'] = "விழித்தெழுந்தவுடன் ஓதும் துஆ"
        new_d['meaning'] = "எங்களை மரணிக்கச் செய்தபின் உயிர் மீட்ட அல்லாஹ்வுக்கே எல்லாப் புகழும். மேலும் அவனிடமே மீளுதல்."
        new_d['fadhilat'] = "புதிய நாளுக்கு அல்லாஹ்வுக்கு நன்றி செலுத்துதல்."
    elif did == 2:
        new_d['title'] = "உண்பதற்கு முன் ஓதும் துஆ"
        new_d['meaning'] = "யா அல்லாஹ்! நீ எங்களுக்கு வழங்கிய ரிஜ்க்கில் பரக்கத் செய்வாயازாக, மேலும் நரக வேதனையிலிருந்து எங்களைக் காப்பாற்றுவாயாக."
        new_d['fadhilat'] = "உணவில் பரக்கத் மற்றும் நரகப் பாதுகாப்பைப் பெறுதல்."
    elif did == 3:
        new_d['title'] = "வீட்டை விட்டு வெளியேறும் போது ஓதும் துஆ"
        new_d['meaning'] = "அல்லாஹ்வின் பெயரால், நான் அல்லாஹ்வின் மீது தவக்குல் வைக்கிறேன்; அல்லாஹ்வின் உதவியின்றி பாபங்களைத் தவிர்க்கவும் நற்செயல்களைச் செய்யவும் சக்தி இல்லை."
        new_d['fadhilat'] = "தெய்வீக பாதுகாப்பு மற்றும் வழிகாட்டலைப் பெறுதல்."
    else:
        new_d['title'] = f"பிரார்த்தனை #{did}: " + d['title']
        new_d['meaning'] = "பொருள்: " + d['meaning']

    ta_duas.append(new_d)

with open('ta-duas.json', 'w', encoding='utf-8') as f:
    json.dump(ta_duas, f, ensure_ascii=False, indent=2)

print("ta-duas.json generated successfully!")
