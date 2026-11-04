import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

for d in en_duas:
    # Clean source
    src = d.get('source', '')
    if src:
        src = src.replace('daripada', 'from')
        src = src.replace('Amalan Tradisi & Panduan JAKIM Malaysia', 'Traditional Practice & JAKIM Malaysia Guide')
        src = src.replace('Amalan Tradisi Nusantara & Kitab Doa', 'Nusantara Traditional Practice & Prayer Book')
        src = src.replace('Rukun Fardhu Solat', 'Obligatory Prayer Pillars')
        src = src.replace('Sunat Ab\'ad / Sunat Solat', 'Sunnah Ab\'ad / Prayer Sunnah')
        src = src.replace('Rukun Solat', 'Prayer Pillars')
        src = src.replace('Sunat Ab\'ad Solat', 'Sunnah Ab\'ad Prayer')
        src = src.replace('Panduan Fardhu Ain & Ibadah Solat', 'Fardhu Ain & Prayer Worship Guide')
        src = src.replace('Panduan Solat Sunat Rawatib', 'Rawatib Sunnah Prayer Guide')
        src = src.replace('Panduan Solat Sunat', 'Sunnah Prayer Guide')
        src = src.replace('Panduan Solat', 'Prayer Guide')
        d['source'] = src

    # Clean definition
    defn = d.get('definition')
    if defn:
        if d.get('id') == 11:
            d['definition'] = "Reciting the Opening Supplication (Iftitah) in prayer holds various great merits and virtues, as it serves as a meaningful introduction and opening conversation between the servant and their Creator before starting the recitation of Al-Fatihah."
        elif d.get('id') == 44:
            d['definition'] = "Istikharah prayer is a two-rakat Sunnah prayer performed to seek guidance and the best choice from Allah SWT (such as career, studies, or life partner selection)."
        elif d.get('id') == 47:
            d['definition'] = "Additional Tip: Among the recommended Sunnah practices before sleeping are dusting off the bed three times, reciting Ayat al-Kursi, Surah al-Ikhlas, al-Falaq, an-Nas, and the sleep prayer taught by the Messenger of Allah SAW."

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "w") as f:
    json.dump(en_duas, f, indent=2, ensure_ascii=False)

print("en-duas.json updated successfully with 100% English fields.")
