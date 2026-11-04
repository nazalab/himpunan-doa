import json

with open("/data/data/com.termux/files/home/dua-app/duas.json", "r") as f:
    duas = json.load(f)

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

issues = []
print(f"Total duas: {len(duas)}, en_duas: {len(en_duas)}")

malay_keywords = ["dan", "yang", "untuk", "dengan", "allah", "ya allah", "ampunilah", "doa", "kesembuhan", "kesusahan"]

for i, (d, en_d) in enumerate(zip(duas, en_duas)):
    if d.get("id") != en_d.get("id"):
        issues.append(f"ID mismatch at index {i}: {d.get('id')} vs {en_d.get('id')}")

    for key in ["title", "translation", "benefit", "reference", "category"]:
        val_en = en_d.get(key, "")
        val_id = d.get(key, "")
        if not val_en:
            issues.append(f"Missing field {key} in en-dua id {d.get('id')}")

        # Check if en version has obvious Malay words or is identical to ID when it should be translated
        if key in ["translation", "benefit"] and val_en == val_id and len(val_id) > 10:
            issues.append(f"Potentially untranslated ({key}) in id {d.get('id')}: {val_en}")

print(f"Found {len(issues)} issues:")
for iss in issues:
    print(iss)

print("EN_DUAS_COUNT:", len(en_duas))
print("TOTAL_DUAS:", len(duas))
print("FULLY_TRANSLATED:", len(issues) == 0)
