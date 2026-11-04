import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

keys = set()
for d in en_duas:
    keys.update(d.keys())
print("Keys in en-duas.json:", keys)
