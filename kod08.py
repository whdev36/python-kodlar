# 📌 1. Lug‘atga yangi element qo‘shish
talaba = {'ism': 'Ali', 'yosh': 22}
talaba['universitet'] = 'TATU'
print(talaba)

# 📌 2. Lug‘atdagi qiymatni o‘zgartirish
talaba['yosh'] = 23
print(talaba)

# 📌 3. update() bilan bir nechta element qo‘shish va yangilash
talaba.update({'yosh': 24, 'kurs': 4})
print(talaba)

# 📌 4. Lug‘atdan element o‘chirish (del, pop(), popitem())
# ✅ del usuli – Elementni kaliti bo‘yicha o‘chirish
del talaba['universitet']
print(talaba)

# ✅ pop() usuli – Elementni o‘chirish va qiymatini qaytarish
yosh = talaba.pop('yosh')
print(yosh)
print(talaba)

# ✅ popitem() usuli – Lug‘atdagi oxirgi elementni o‘chirish
oxirgi = talaba.popitem()
print(oxirgi)
print(talaba)

# 📌 5. Lug‘atni tozalash (clear())
talaba.clear()
print(talaba)

