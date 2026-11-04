import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

for d in en_duas:
    print(f"ID {d.get('id')}:")
    print(f"  Source: {d.get('source')}")
    print(f"  Category: {d.get('category')}")
