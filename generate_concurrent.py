import json
from concurrent.futures import ThreadPoolExecutor, as_completed
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

def trans(text, target):
    if not text or not isinstance(text, str):
        return text
    try:
        return MyMemoryTranslator(source="english", target=target).translate(text) or text
    except Exception:
        return text

id_duas = []
cn_duas = []

print("Generating Indonesian and Chinese duas concurrently...")

for dua in en_duas:
    d_id = dua.copy()
    d_cn = dua.copy()

    d_id["category"] = translate_cat(dua["category"], cat_map_id)
    d_cn["category"] = translate_cat(dua["category"], cat_map_cn)

    fields_to_trans = ["title", "meaning", "source", "fadhilat", "definition"]

    def process_field(field):
        if field in dua and dua[field]:
            val = dua[field]
            val_id = trans(val, "indonesian")
            val_cn = trans(val, "chinese simplified")
            return field, val_id, val_cn
        return field, None, None

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_field, f) for f in fields_to_trans if f in dua and dua[f]]
        for future in as_completed(futures):
            field, val_id, val_cn = future.result()
            if val_id:
                d_id[field] = val_id
            if val_cn:
                d_cn[field] = val_cn

    id_duas.append(d_id)
    cn_duas.append(d_cn)
    print(f"Processed dua ID {dua['id']}")

with open('/data/data/com.termux/files/home/dua-app/id-duas.json', 'w', encoding='utf-8') as f:
    json.dump(id_duas, f, ensure_ascii=False, indent=2)

with open('/data/data/com.termux/files/home/dua-app/cn-duas.json', 'w', encoding='utf-8') as f:
    json.dump(cn_duas, f, ensure_ascii=False, indent=2)

print("Successfully generated id-duas.json and cn-duas.json!")
