import json

with open("/data/data/com.termux/files/home/dua-app/duas.json", "r") as f:
    duas = json.load(f)

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

print(f"Total duas: {len(duas)}, en_duas: {len(en_duas)}")

malay_words = ["doa", "dan", "yang", "untuk", "dengan", "ampunilah", "Allah", "Ya Allah"]

issues = []

for d, en_d in zip(duas, en_duas):
    did = d['id']
    en_did = en_d.get('id')
    if did != en_did:
        issues.append(f"ID mismatch: {did} vs {en_did}")

    # Check title translation
    title_ms = d.get('title', '')
    title_en = en_d.get('title', '')
    if not title_en:
        issues.append(f"Missing title for ID {did}")
    elif title_en == title_ms and not title_en.startswith("Step"):
        issues.append(f"Untranslated title for ID {did}: {title_en}")

    # Check meaning translation
    meaning_ms = d.get('meaning', '')
    meaning_en = en_d.get('meaning', '')
    if not meaning_en:
        issues.append(f"Missing meaning for ID {did}")
    elif meaning_en == meaning_ms and len(meaning_ms) > 10:
        issues.append(f"Untranslated meaning for ID {did}: {meaning_en}")

print(f"Total issues found: {len(issues)}")
for iss in issues:
    print(iss)
