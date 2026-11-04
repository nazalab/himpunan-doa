import json

with open("/data/data/com.termux/files/home/dua-app/en-duas.json", "r") as f:
    en_duas = json.load(f)

for d in en_duas:
    print(f"--- ID {d.get('id')} ---")
    print(f"Title: {d.get('title')}")
    print(f"Category: {d.get('category')}")
    print(f"Source: {d.get('source')}")
    print(f"Definition: {d.get('definition')}")
    print(f"Fadhilat: {d.get('fadhilat')}")
    print(f"Meaning: {d.get('meaning')}")
