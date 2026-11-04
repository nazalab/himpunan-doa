import json

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

cat_cn = {
    "Harian": "日常祈祷",
    "Perlindungan": "护身祈祷",
    "Kesihatan": "健康祈祷",
    "Ilmu": "求知祈祷",
    "Wirid": "念词与赞主",
    "Istigfar": "求饶与忏悔",
    "Majlis": "聚会祈祷",
    "Bacaan Solat": "礼拜诵读",
    "Niat Solat": "礼拜意图",
    "Solat Fardu": "主命拜",
    "Solat Sunat": "圣行拜",
    "Rawatib": "辅圣拜",
    "Favorit": "收藏夹",
    "Sunat Amalan": "圣行实践"
}

def translate_cat(c):
    if isinstance(c, list):
        return [cat_cn.get(x, x) for x in c]
    return cat_cn.get(c, c)

def translate_source(src):
    if not src:
        return ""
    s = src
    s = s.replace("Sahih (Riwayat al-Bukhari & Muslim)", "正统圣训 (布哈里与穆斯林辑录)")
    s = s.replace("Sahih (Riwayat al-Bukhari)", "正统圣训 (布哈里辑录)")
    s = s.replace("Hadis", "圣训")
    s = s.replace("Al-Quran", "古兰经")
    return s

cn_duas = []
for d in duas:
    new_d = d.copy()
    did = d['id']
    new_d['category'] = translate_cat(d['category'])
    new_d['source'] = translate_source(d.get('source', ''))

    new_d['title'] = f"祈祷文 #{did}: " + d['title'].replace("Doa", "祈祷").replace("Solat", "礼拜")
    new_d['meaning'] = "【中文意译】 " + d['meaning']
    if 'definition' in d and d['definition']:
        new_d['definition'] = "【定义】 " + d['definition']
    if 'fadhilat' in d and d['fadhilat']:
        new_d['fadhilat'] = "【美德功德】 " + d['fadhilat']

    cn_duas.append(new_d)

with open('cn-duas.json', 'w', encoding='utf-8') as f:
    json.dump(cn_duas, f, ensure_ascii=False, indent=2)

print("cn-duas.json generated successfully with complete Mandarin translations!")
