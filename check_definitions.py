import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

for d in en_duas:
    print(f"ID {d.get('id')}: definition={d.get('definition')}, fadhilat={d.get('fadhilat')}")
