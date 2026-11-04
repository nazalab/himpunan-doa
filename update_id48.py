import json

with open('en-duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

for d in duas:
    if d['id'] == 48:
        d['meaning'] = (
            "In the name of Allah, the Most Gracious, the Most Merciful.\n\n"
            "O Allah, indeed we ask You for preservation, and we entrust to You our religion, our selves, our families, our children, our possessions, and everything that You have bestowed upon us.\n\n"
            "O Allah, make us and them always remain under Your protection, Your safety, and Your care from every rebellious Satan, every arrogant and stubborn person, every person with an evil glance (envy/jealousy), every wrongdoer, and from the evil of every evil being. Indeed, You have power over all things.\n\n"
            "O Allah, adorn us with health and safety, establish our stance with piety and steadfastness, and protect us from matters that bring about regret. Indeed, You are the Hearer of prayers.\n\n"
            "O Allah, forgive our sins, the sins of our parents, our children, those who walk alongside us, our brothers and sisters in faith, our companions, whoever loves us for Your sake, and whoever has ever done good to us.\n\n"
            "And forgive all believing men and believing women, Muslim men and Muslim women, O Lord of the worlds.\n\n"
            "May Allah shower His mercy and blessings upon our master Prophet Muhammad, and upon his family and companions. Bestow upon us the perfection of following in his footsteps, both outwardly and inwardly, in a state of health and well-being, by Your mercy, O Most Merciful of the merciful.\n\n"
            "And may Allah bestow His blessings and peace upon His servant and Messenger, Prophet Muhammad, as well as his family and companions."
        )
        break

with open('en-duas.json', 'w', encoding='utf-8') as f:
    json.dump(duas, f, ensure_ascii=False, indent=2)

print("ID 48 meaning updated successfully in en-duas.json!")
