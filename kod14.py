import json

# 📥 JSON ma'lumotlarini Python lug‘atiga aylantirish (json.loads())

talaba = {
    'ism': 'Dilnoza',
    'yosh': 22,
    'kurs': 3,
    'fanlar': ['Matematika', 'Fizika', 'Dasturlash']
}

json_talaba = json.dumps(talaba, indent=4)
print(json_talaba)

# 📂 JSON faylni o‘qish (json.load())

with open('malumot.json', 'r') as fayl:
    data = json.load(fayl)

print(data)

# 📂 JSON faylga yozish (json.dump())

talaba = {
    'ism': 'Bobur',
    'yosh': 24,
    'kurs': 4,
    'fanlar': ['Kompyuter tarmoqlari', 'Kiberxavfsizlik']
}

with open('talaba.json', 'w') as fayl:
    json.dump(talaba, fayl, indent=4)

print('JSON fayl yaratildi!')

# 🎭 JSON’da maxsus parametrlar
malumot = {'b': 2, 'a': 1, 'c': 3}
json_str = json.dumps(malumot, indent=2, sort_keys=True)
print(json_str)