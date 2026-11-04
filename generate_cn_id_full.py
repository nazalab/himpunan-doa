import json

with open('/data/data/com.termux/files/home/dua-app/duas.json', 'r', encoding='utf-8') as f:
    duas = json.load(f)

cat_map_cn = {
    "Harian": "日常",
    "Perlindungan": "庇护",
    "Kesihatan": "健康",
    "Ilmu": "求知",
    "Wirid": "念词",
    "Istigfar": "求饶恕",
    "Majlis": "聚会",
    "Bacaan Solat": "礼拜诵读",
    "Niat Solat": "礼拜意图",
    "Solat Fardu": "主命拜",
    "Solat Sunat": "圣行拜",
    "Rawatib": "辅行拜",
    "Favorit": "收藏"
}

cat_map_id = {
    "Harian": "Harian",
    "Perlindungan": "Perlindungan",
    "Kesihatan": "Kesehatan",
    "Ilmu": "Ilmu",
    "Wirid": "Wirid",
    "Istigfar": "Istighfar",
    "Majlis": "Majelis",
    "Bacaan Solat": "Bacaan Salat",
    "Niat Solat": "Niat Salat",
    "Solat Fardu": "Salat Fardu",
    "Solat Sunat": "Salat Sunnah",
    "Rawatib": "Rawatib",
    "Favorit": "Favorit"
}

# Simple title and meaning translations for CN
cn_translations = {
    1: {"title": "醒来时的祈祷", "meaning": "一切赞颂全归真主，是他使我们死后复活，归宿也只到他那里。", "fadhilat": "感谢真主赐予新的一天生命。"},
    2: {"title": "饭前祈祷", "meaning": "真主啊，求你在我们所赐的给养中降福于我们，并保护我们免受火狱的刑罚。"},
    3: {"title": "出门时的祈祷", "meaning": "奉真主之名，我托付真主，唯有真主才有力量和权能。"},
    4: {"title": "进卫生间祈祷", "meaning": "真主啊，我求你庇护我免受一切男女不洁恶魔的侵害。"},
    5: {"title": "饭后祈祷", "meaning": "一切赞颂全归真主，他赐予我们饮食，并使我们成为穆斯林。"},
    6: {"title": "进家门祈祷", "meaning": "奉真主之名我们进入，奉真主之名我们离开，并托靠我们的主。"},
    7: {"title": "求益智祈祷", "meaning": "我的主啊，求你增加我的知识，并赐我理解力。"},
    8: {"title": "两世吉庆祈祷", "meaning": "我们的主啊，求你在今世赐予我们美好，在后世也赐予我们美好，并保护我们免受火狱的刑罚。"},
    9: {"title": "为父母祈祷", "meaning": "我的主啊，求你慈悯他们，就像我年幼时他们抚养我那样。"},
    10: {"title": "乘车祈祷", "meaning": "赞颂真主超绝万物，他为我们制服了此物，我们此前无法制服它。我们必定归向我们的主。"},
    11: {"title": "开端词（开拜词）", "meaning": "真主至大，一切赞颂全归真主...我的礼拜、我的牺牲、我的生和死，全为了真主——全人类的主。"},
    12: {"title": "求饶之主（赛义杜·伊斯提格法尔）", "meaning": "真主啊，你是我的主，除你之外绝无应受崇拜的。你创造了我，我是你的仆人...我承认你对我的恩典，也承认我的罪过，求你饶恕我。"},
    13: {"title": "祈求美满后代与家庭", "meaning": "我们的主啊，求你以我们的妻子和儿女为我们的慰藉，并使我们成为敬畏者的表率。"},
    14: {"title": "感谢真主恩典祈祷", "meaning": "我的主啊，求你使我感谢你赐予我和我父母的恩典..."},
    15: {"title": "拜后赞词与祈祷", "meaning": "真主啊，你是和平，和平来自你...除真主外，绝无应受崇拜，他是独一的，无任何伙伴。"},
    16: {"title": "完成古兰经诵读（封经）祈祷", "meaning": "真主啊，求你通过伟大的古兰经慈悯我，并使它成为我的引导、光明、向导和慈恩。"},
    17: {"title": "第一步：大赞词与意图", "meaning": "举起双手念‘真主至大’，并在心中立下特定礼拜的意图。"},
    18: {"title": "第二步：开拜词（开端词）", "meaning": "在大赞词后诵读开拜词。"},
    19: {"title": "第三步：鞠躬诵读", "meaning": "赞颂我的伟大主宰超绝万物，一切赞颂归于他。"},
    20: {"title": "第四步：从鞠躬起身（站立）", "meaning": "真主听从赞颂他的人。我们的主啊，一切赞颂全归于你。"},
    21: {"title": "第五步：叩头诵读", "meaning": "赞颂我的至高主宰超绝万物，一切赞颂归于他。"},
    22: {"title": "第六步：两叩头之间坐姿", "meaning": "主啊，求你饶恕我、慈悯我、引导我、赐我给养、赐我健康、赦免我。"},
    23: {"title": "第七步：初坐（第一台亚图）", "meaning": "一切敬意、祈祷和美好事物专属于真主。先知啊，愿主赐福你，以及真主的慈悯与吉庆..."},
    24: {"title": "第八步：末坐（最终台亚图）", "meaning": "一切敬意、祈祷和美好事物专属于真主...真主啊，求你赐福穆罕默德及其家属..."},
    25: {"title": "第九步：最后的色兰", "meaning": "愿真主的和平与慈悯降临于你们。"},
    26: {"title": "求医治与康复祈祷", "meaning": "真主啊，人类的主，求你消除病痛，给予治愈，你是治愈者，唯有你的治愈..."},
    27: {"title": "晨礼（Subuh）意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼两拜的主命晨礼。"},
    28: {"title": "晌礼（Zohor）意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼四拜的主命晌礼。"},
    29: {"title": "晡礼（Asar）意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼四拜的主命晡礼。"},
    30: {"title": "昏礼（Maghrib）意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼三拜的主命昏礼。"},
    31: {"title": "宵礼（Isyak）意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼四拜的主命宵礼。"},
    32: {"title": "晨光圣行拜（Dhuha）意图", "meaning": "我立意为真主至大面向朝向礼两拜的晨光圣行拜。"},
    33: {"title": "夜间奉献拜（Tahajjud）意图", "meaning": "我立意为真主至大面向朝向礼两拜的夜间奉献拜。"},
    34: {"title": "求所愿圣行拜（Hajat）意图", "meaning": "我立意为真主至大面向朝向礼两拜的求所愿圣行拜。"},
    35: {"title": "奇数拜（Witir）意图", "meaning": "我立意为真主至大面向朝向礼两拜的奇数拜。"},
    36: {"title": "晨礼前圣行拜（Qobliyah Subuh）意图", "meaning": "我立意在晨礼前礼两拜圣行拜..."},
    37: {"title": "晌礼前圣行拜（Qobliyah Zohor）意图", "meaning": "我立意在晌礼前礼两拜圣行拜..."},
    38: {"title": "晌礼后圣行拜（Ba'diyah Zohor）意图", "meaning": "我立意在晌礼后礼两拜圣行拜..."},
    39: {"title": "昏礼后圣行拜（Ba'diyah Maghrib）意图", "meaning": "我立意在昏礼后礼两拜圣行拜..."},
    40: {"title": "宵礼后圣行拜（Ba'diyah Isyak）意图", "meaning": "我立意在宵礼后礼两拜圣行拜..."},
    41: {"title": "晡礼前圣行拜（Qobliyah Asar）意图", "meaning": "我立意在晡礼前礼两拜圣行拜..."},
    42: {"title": "昏礼前圣行拜（Qobliyah Maghrib）意图", "meaning": "我立意在昏礼前礼两拜圣行拜..."},
    43: {"title": "宵礼前圣行拜（Qobliyah Isyak）意图", "meaning": "我立意在宵礼前礼两拜圣行拜..."},
    44: {"title": "求善祈祷（Istikharah）", "meaning": "真主啊，我凭你的知识求你抉择，凭你的大能求你赐我能力..."},
    45: {"title": "求嗣祈祷（宰凯里雅圣人）", "meaning": "我的主啊，求你从你那里赐予我纯洁的后代，你确是听取祈祷的主。"},
    46: {"title": "主麻（周五）聚礼意图", "meaning": "我立意为真主至大面向朝向跟随伊玛目礼两拜的主麻聚礼。"},
    47: {"title": "睡前祈祷", "meaning": "真主啊，奉你的名我死去，我活着。"},
    48: {"title": "祈求平安与感谢", "meaning": "真主啊，求你赐予我们平安、信仰、安宁与健康..."}
}

cn_duas = []
for d in duas:
    new_d = d.copy()
    did = d['id']
    if isinstance(new_d['category'], list):
        new_d['category'] = [cat_map_cn.get(c, c) for c in new_d['category']]
    else:
        new_d['category'] = cat_map_cn.get(new_d['category'], new_d['category'])

    if did in cn_translations:
        t = cn_translations[did]
        new_d['title'] = t['title']
        new_d['meaning'] = t['meaning']
        if 'fadhilat' in t:
            new_d['fadhilat'] = t['fadhilat']
        elif 'fadhilat' in new_d:
            new_d['fadhilat'] = "【美德】 " + new_d['fadhilat']
    cn_duas.append(new_d)

with open('/data/data/com.termux/files/home/dua-app/cn-duas.json', 'w', encoding='utf-8') as f:
    json.dump(cn_duas, f, ensure_ascii=False, indent=2)

# Indonesian duos (id-duas.json)
id_duas = []
for d in duas:
    new_d = d.copy()
    if isinstance(new_d['category'], list):
        new_d['category'] = [cat_map_id.get(c, c) for c in new_d['category']]
    else:
        new_d['category'] = cat_map_id.get(new_d['category'], new_d['category'])
    id_duas.append(new_d)

with open('/data/data/com.termux/files/home/dua-app/id-duas.json', 'w', encoding='utf-8') as f:
    json.dump(id_duas, f, ensure_ascii=False, indent=2)

print("Successfully generated cn-duas.json and id-duas.json!")
