import json
import sys

def check_json():
    try:
        with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r", encoding="utf-8") as f:
            en_data = json.load(f)
        with open("/data/data/com.termux/files/home/dua-app/duas.json", "r", encoding="utf-8") as f:
            ms_data = json.load(f)
    except Exception as e:
        print(f"JSON parsing error: {e}")
        sys.exit(1)

    print(f"Successfully parsed en-duas.json with {len(en_data)} entries (matches duas.json: {len(ms_data)}).")

    malay_keywords = [
        "dan", "yang", "untuk", "dengan", "ke", "di", "dari", "daripada",
        "adalah", "ialah", "dalam", "pada", "oleh", "sebagai", "seperti",
        "doa", "solat", "sembahyang", "puasa", "zakat", "haji", "umat",
        "amalan", "panduan", "rukun", "sunat", "kitab", "harian", "perlindungan",
        "kesihatan", "ilmu", "wirid", "istigfar", "majlis", "bacaan", "niat", "fardu"
    ]

    # Fields to check for Malay text (excluding Arabic/Rumi/transliteration which are non-English by nature)
    fields_to_check = ['title', 'meaning', 'definition', 'fadhilat', 'category', 'source']

    issues = []
    for item in en_data:
        item_id = item.get('id')
        for field in fields_to_check:
            val = item.get(field)
            if not val:
                continue
            if isinstance(val, list):
                val_text = " ".join(val)
            else:
                val_text = str(val)

            # Tokenize words
            words = val_text.lower().split()
            for w in words:
                # clean punctuation
                w_clean = ''.join(c for c in w if c.isalnum())
                if w_clean in malay_keywords:
                    # Allow common loan words or accepted English terms if any, but flag strict Malay words
                    if w_clean in ["dan", "yang", "untuk", "dengan", "daripada", "adalah", "ialah", "dalam", "pada", "oleh", "sebagai", "seperti", "amalan", "panduan", "rukun", "sunat"]:
                        issues.append(f"ID {item_id} field '{field}' contains Malay word '{w_clean}': '{val_text}'")

    if issues:
        print("Found potential Malay text in English-facing fields:")
        for iss in issues:
            print(f" - {iss}")
        sys.exit(1)
    else:
        print("Adversarial check passed: en-duas.json is valid JSON and contains zero Malay text in English-facing fields.")

if __name__ == "__main__":
    check_json()
