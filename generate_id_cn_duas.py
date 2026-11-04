import json
import time
from deep_translator import MyMemoryTranslator

with open('duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

cat_map_id = {
    "Harian": "Harian",
    "Perlindungan": "Perlindungan",
    "Kesihatan": "Kesehatan",
    "Ilmu": "Ilmu",
    "Wirid": "Wirid",
    "Istigfar": "Istighfar",
    "Majlis": "Majelis",
    "Bacaan Solat": "Bacaan Salat",
    "Niat Solat": "Niat Salat",
    "Solat Fardu": "Salat Fardhu",
    "Solat Sunat": "Salat Sunnah",
    "Rawatib": "Rawatib",
    "Favorit": "Favorit"
}

cat_map_cn = {
    "Harian": "日常",
    "Perlindungan": "庇护",
    "Kesihatan": "健康",
    "Ilmu": "求知",
    "Wirid": "念词",
    "Istigfar": "求饶恕",
    "Majlis": "聚会",
    "Bacaan Solat": "礼拜诵读",
    "Niat Solat": "礼拜意图",
    "Solat Fardu": "主命拜",
    "Solat Sunat": "圣行拜",
    "Rawatib": "辅行拜",
    "Favorit": "收藏"
}

def translate_cat(c, mapping):
    if isinstance(c, list):
        return [mapping.get(x, x) for x in c]
    return mapping.get(c, c)

translator_id = MyMemoryTranslator(source="malay", target="indonesian")
translator_cn = MyMemoryTranslator(source="malay", target="chinese simplified")

id_duas = []
cn_duas = []

for idx, dua in enumerate(duas):
    print(f"Processing Dua {dua['id']}: {dua['title']}")

    # Indonesian
    d_id = dua.copy()
    d_id["category"] = translate_cat(dua["category"], cat_map_id)
    time.sleep(0.3)
    try:
        d_id["title"] = translator_id.translate(dua["title"])
    except Exception as e:
        print(f"Error translating title ID: {e}")
    time.sleep(0.3)
    try:
        d_id["meaning"] = translator_id.translate(dua["meaning"])
    except Exception as e:
        print(f"Error translating meaning ID: {e}")
    if "source" in dua and dua["source"]:
        time.sleep(0.3)
        try:
            d_id["source"] = translator_id.translate(dua["source"])
        except Exception:
            pass
    if "fadhilat" in dua and dua["fadhilat"]:
        time.sleep(0.3)
        try:
            d_id["fadhilat"] = translator_id.translate(dua["fadhilat"])
        except Exception:
            pass
    if "definition" in dua and dua["definition"]:
        time.sleep(0.3)
        try:
            d_id["definition"] = translator_id.translate(dua["definition"])
        except Exception:
            pass
    id_duas.append(d_id)

    # Chinese
    d_cn = dua.copy()
    d_cn["category"] = translate_cat(dua["category"], cat_map_cn)
    time.sleep(0.3)
    try:
        d_cn["title"] = translator_cn.translate(dua["title"])
    except Exception as e:
        print(f"Error translating title CN: {e}")
    time.sleep(0.3)
    try:
        d_cn["meaning"] = translator_cn.translate(dua["meaning"])
    except Exception as e:
        print(f"Error translating meaning CN: {e}")
    if "source" in dua and dua["source"]:
        time.sleep(0.3)
        try:
            d_cn["source"] = translator_cn.translate(dua["source"])
        except Exception:
            pass
    if "fadhilat" in dua and dua["fadhilat"]:
        time.sleep(0.3)
        try:
            d_cn["fadhilat"] = translator_cn.translate(dua["fadhilat"])
        except Exception:
            pass
    if "definition" in dua and dua["definition"]:
        time.sleep(0.3)
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
