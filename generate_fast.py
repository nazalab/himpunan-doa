import json
import time
from deep_translator import MyMemoryTranslator

with open('en-duas.json', 'r', encoding='utf-8') as f:
    en_duas = json.load(f)

cat_map_id = {
    "Daily": "Harian",
    "Protection": "Perlindungan",
    "Health": "Kesehatan",
    "Knowledge": "Ilmu",
    "Wird": "Wirid",
    "Istighfar": "Istighfar",
    "Gathering": "Majelis",
    "Prayer Recitations": "Bacaan Salat",
    "Prayer Intentions": "Niat Salat",
    "Obligatory Prayer": "Salat Fardhu",
    "Sunnah Prayer": "Salat Sunnah",
    "Rawatib Sunnah": "Rawatib",
    "Favorites": "Favorit"
}

cat_map_cn = {
    "Daily": "日常",
    "Protection": "庇护",
    "Health": "健康",
    "Knowledge": "求知",
    "Wird": "念词",
    "Istighfar": "求饶恕",
    "Gathering": "聚会",
    "Prayer Recitations": "礼拜诵读",
    "Prayer Intentions": "礼拜意图",
    "Obligatory Prayer": "主命拜",
    "Sunnah Prayer": "圣行拜",
    "Rawatib Sunnah": "辅行拜",
    "Favorites": "收藏"
}

def translate_cat(c, mapping):
    if isinstance(c, list):
        return [mapping.get(x, x) for x in c]
    return mapping.get(c, c)

translator_id = MyMemoryTranslator(source="english", target="indonesian")
translator_cn = MyMemoryTranslator(source="english", target="chinese simplified")

id_duas = []
cn_duas = []

for idx, dua in enumerate(en_duas):
    print(f"Processing Dua {dua['id']}: {dua['title']}")

    # Indonesian
    d_id = dua.copy()
    d_id["category"] = translate_cat(dua["category"], cat_map_id)
    time.sleep(0.15)
    try:
        d_id["title"] = translator_id.translate(dua["title"])
    except Exception:
        pass
    time.sleep(0.15)
    try:
        d_id["meaning"] = translator_id.translate(dua["meaning"])
    except Exception:
        pass
    if "fadhilat" in dua and dua["fadhilat"]:
        time.sleep(0.15)
        try:
            d_id["fadhilat"] = translator_id.translate(dua["fadhilat"])
        except Exception:
            pass
    if "definition" in dua and dua["definition"]:
        time.sleep(0.15)
        try:
            d_id["definition"] = translator_id.translate(dua["definition"])
        except Exception:
            pass
    id_duas.append(d_id)

    # Chinese
    d_cn = dua.copy()
    d_cn["category"] = translate_cat(dua["category"], cat_map_cn)
    time.sleep(0.15)
    try:
        d_cn["title"] = translator_cn.translate(dua["title"])
    except Exception:
        pass
    time.sleep(0.15)
    try:
        d_cn["meaning"] = translator_cn.translate(dua["meaning"])
    except Exception:
        pass
    if "fadhilat" in dua and dua["fadhilat"]:
        time.sleep(0.15)
        try:
            d_cn["fadhilat"] = translator_cn.translate(dua["fadhilat"])
        except Exception:
            pass
    if "definition" in dua and dua["definition"]:
        time.sleep(0.15)
        try:
            d_cn["definition"] = translator_cn.translate(dua["definition"])
        except Exception:
            pass
    cn_duas.append(d_cn)

with open('/data/data/com.termux/files/home/dua-app/id-duas.json', 'w', encoding='utf-8') as f:
    json.dump(id_duas, f, ensure_ascii=False, indent=2)

with open('/data/data/com.termux/files/home/dua-app/cn-duas.json', 'w', encoding='utf-8') as f:
    json.dump(cn_duas, f, ensure_ascii=False, indent=2)

print("Successfully generated id-duas.json and cn-duas.json!")
