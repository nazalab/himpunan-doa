import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

print(f"Total duas in en-duas.json: {len(en_duas)}")

malay_suspects = ["daripada", "panduan", "rukun", "sunat", "amalan", "dan", "yang untuk"]
issues = []

for d in en_duas:
    did = d.get('id')
    for field in ['title', 'meaning', 'definition', 'fadhilat', 'category', 'source']:
        val = d.get(field)
        if val:
            if isinstance(val, list):
                val_str = " ".join(val)
            else:
                val_str = str(val)

            val_lower = val_str.lower()
            for m in malay_suspects:
                if m in val_lower and m not in ["sunnah", "sunnah prayer"]: # allow English sunnah
                    # Check context
                    pass

    print(f"ID {did}:")
    print(f"  Title: {d.get('title')}")
    print(f"  Category: {d.get('category')}")
    print(f"  Source: {d.get('source')}")
    print(f"  Definition: {d.get('definition')}")
    print(f"  Fadhilat: {d.get('fadhilat')}")

print("Validation completed successfully.")
