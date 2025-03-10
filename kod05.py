# 1️⃣ Oddiy List Comprehension
# ⏩ Oddiy usul vs List Comprehension:

# # Oddiy usul (for loop)
sonlar = []
for i in range(10):
    sonlar.append(i**2)

# # List Comprehension
sonlar2 = [i**2 for i in range(10)]

print(sonlar)
print(sonlar2)

# 2️⃣ Shart bilan List Comprehension
# ⏩ Juft sonlarni ajratish:
juft_sonlar = [i for i in range(20) if i % 2 == 0]
print(juft_sonlar)

# ⏩ Toq sonlarni kvadratga oshirish:
toq_kvadrat = [i**2 for i in range(10) if i % 2 != 0]
print(toq_kvadrat)

# 3️⃣ if-else bilan List Comprehension
natija = ['juft' if i % 2 == 0 else 'toq' for i in range(10)]
print(natija)

# 4️⃣ Matn bilan ishlash
# ⏩ Harflarni katta harfga o‘tkazish:
soz = 'python'
katta = [harf.upper() for harf in soz]
print(katta)

# ⏩ Faqat unli harflarni ajratish:
soz = 'programming'
unli_harflar = [harf for harf in soz if harf in 'aeiou']
print(unli_harflar)

# 5️⃣ Ichma-ich List Comprehension
# ⏩ 2D ro‘yxat yaratish (matritsa):
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

# ⏩ Ikki ro‘yxatdan juftliklar yaratish:
raqamlar = [1, 2, 3]
harflar = ['A', 'B', 'C']

juftliklar = [(r, h) for r in raqamlar for h in harflar]
print(juftliklar)

# 6️⃣ Set va Dictionary Comprehension
# 🔹 Set comprehension (takrorlanuvchi elementlarni avtomatik olib tashlaydi):
sonlar = {i**2 for i in range(10)}
print(sonlar)

# 🔹 Dictionary comprehension (lug‘atlar yaratish):
raqam_dict = {x: x**2 for x in range(5)}
print(raqam_dict)

# 🎯 Amaliy misol: So‘z uzunliklarini hisoblash
sozlar = ['salom', 'dasturlash', 'python', 'hello']
uzunliklar = {soz: len(soz) for soz in sozlar}
print(uzunliklar)

# 🎉 Xulosa
# ✅ List Comprehension kodni qisqa va tushunarli qiladi.
# ✅ if, if-else, va ichki tsikllar bilan ham ishlaydi.
# ✅ Set va Dictionary comprehension ham shunga o‘xshash usulda ishlaydi.
# ✅ List comprehension tezroq ishlaydi va kamroq xotira sarflaydi.