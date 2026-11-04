import json

with open("/data/data/com.termux/files/home/dua-app/duas.json", "r") as f:
    duas = json.load(f)

for d in duas:
    if d.get('definition') or d.get('fadhilat'):
        print(f"ID {d.get('id')}: definition={d.get('definition')}, fadhilat={d.get('fadhilat')}")
