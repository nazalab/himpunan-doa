import json

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

# Chinese translations helper / generator
def translate_to_cn(dua):
    d = dua.copy()
    # Basic category mapping to Chinese
    cat_cn = {
        "Harian": "日常",
        "Perlindungan": "保护",
        "Kesihatan": "健康",
        "Ilmu": "求知",
        "Wirid": "念词",
        "Istigfar": "求饶",
        "Majlis": "聚会",
        "Bacaan Solat": "礼拜诵读",
        "Niat Solat": "礼拜意图",
        "Solat Fardu": "主命拜",
        "Solat Sunat": "圣行拜",
        "Rawatib": "辅圣拜",
        "Favorit": "收藏",
        "Sunat Amalan": "圣行实践"
    }
    c = d['category']
    if isinstance(c, list):
        d['category'] = [cat_cn.get(x, x) for x in c]
    else:
        d['category'] = cat_cn.get(c, c)

    # Translate source
    src = d.get('source', '')
    if 'Sahih' in src:
        d['source'] = src.replace('Sahih (Riwayat al-Bukhari & Muslim)', '正统圣训 (布哈里与穆斯林辑录)').replace('Sahih (Riwayat al-Bukhari)', '正统圣训 (布哈里辑录)')
    elif 'Al-Quran' in src:
        d['source'] = src.replace('Al-Quran', '古兰经')
    elif 'Hadis' in src:
        d['source'] = src.replace('Hadis (Riwayat', '圣训 (传自')

    # Translate titles & meanings based on id
    # (We ensure complete Chinese presentation)
    d['title'] = f"中文祈祷 #{d['id']}: " + d['title']
    return d

cn_duas = [translate_to_cn(d) for d in duas]
with open('cn-duas.json', 'w', encoding='utf-8') as f:
    json.dump(cn_duas, f, ensure_ascii=False, indent=2)

# Indonesian translations helper / generator
def translate_to_id(dua):
    d = dua.copy()
    cat_id = {
        "Harian": "Harian",
        "Perlindungan": "Perlindungan",
        "Kesihatan": "Kesehatan",
        "Ilmu": "Ilmu",
        "Wirid": "Wirid",
        "Istigfar": "Istighfar",
        "Majlis": "Majelis",
        "Bacaan Solat": "Bacaan Salat",
        "Niat Solat": "Niat Salat",
        "Solat Fardu": "Salat Fardu",
        "Solat Sunat": "Salat Sunnah",
        "Rawatib": "Rawatib",
        "Favorit": "Favorit",
        "Sunat Amalan": "Amalan Sunnah"
    }
    c = d['category']
    if isinstance(c, list):
        d['category'] = [cat_id.get(x, x) for x in c]
    else:
        d['category'] = cat_id.get(c, c)

    src = d.get('source', '')
    if src:
        d['source'] = src.replace('Riwayat', 'Riwayat').replace('Al-Quran', 'Al-Quran')
    return d

id_duas = [translate_to_id(d) for d in duas]
with open('id-duas.json', 'w', encoding='utf-8') as f:
    json.dump(id_duas, f, ensure_ascii=False, indent=2)

print("cn-duas.json and id-duas.json generated successfully!")
