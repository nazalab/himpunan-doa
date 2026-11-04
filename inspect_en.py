import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

for d in en_duas:
    print(f"ID {d.get('id')}:")
    print(f"  title: {d.get('title')}")
    print(f"  category: {d.get('category')}")
    print(f"  source: {d.get('source')}")
    print(f"  fadhilat: {d.get('fadhilat')}")
    print(f"  meaning: {d.get('meaning')[:50]}...")
