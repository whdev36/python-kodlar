# 📌 Lug‘atlar (dict) – Kalit-qiymat juftligi asosida saqlanadi

talaba = {
    'ism': 'Ali',
    'yosh': 22,
    'universitet': 'TATU'
}
print(talaba)

# 📌 Lug‘atdan qiymat olish
print(talaba['ism'])
print(talaba.get('yosh'))

# ✅ .get() usuli xatolikdan himoya qiladi:
print(talaba.get('kurs', 'Ma\'lumot topilmadi.'))

# 📌 Lug‘atga yangi element qo‘shish
talaba['kurs'] = 3
print(talaba)

# 📌 Lug‘atdan element o‘chirish
del talaba['yosh']
print(talaba)

# ✅ .pop() usuli ham elementni o‘chiradi:
talaba.pop('universitet')
print(talaba)

# 📌 Lug‘at bo‘ylab aylanib chiqish (for)
for kalit, qiymat in talaba.items():
    print(f'{kalit}: {qiymat}')

# 📌 Lug‘atdagi kalitlar (keys()) va qiymatlar (values())
print(talaba.keys())
print(talaba.values())

# 📌 Ichma-ich (nested) lug‘atlar
universitetlar = {
    'TATU': {'shahar': 'Toshkent', 'talabalar': 5000},
    'INHA': {'shahar': 'Toshkent', 'talabalar': 2000}
}
print(universitetlar['TATU']['shahar'])

# 🗂️ To‘plamlar (sets) – Takrorlanmas elementlar jamlanmasi
raqamlar = {1, 2, 3, 4, 5}
print(raqamlar)

# 📌 Takrorlanuvchi elementlar avtomatik olib tashlanadi
raqamlar = {1, 2, 2, 3, 4, 4, 5}
print(raqamlar)
# ✅ To‘plamda indeks yo‘q, shuning uchun raqamlar[0] xatolik keltirib chiqaradi!

# 📌 To‘plamga element qo‘shish (add()) va olib tashlash (remove(), discard())
raqamlar.add(6)
raqamlar.remove(3)  # Agar mavjud bo‘lmasa, xatolik chiqaradi
raqamlar.discard(10)  # Xatolik chiqarmaydi
print(raqamlar)

# 📌 To‘plamlar ustida amallar
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A & B)  # {3, 4}
print(A - B)  # {1, 2}
print(A ^ B)  # {1, 2, 5, 6}

# 🎯 Lug‘atlar va To‘plamlar amaliyotda
# 📌 1️⃣ So‘zlarni unikal qilish (set)
sozlar = ["kitob", "qalam", "kitob", "ruchka", "daftar", "qalam"]
unikal = set(sozlar)
print(unikal)  # {'kitob', 'qalam', 'ruchka', 'daftar'}

# 📌 2️⃣ So‘zlar tez-tez ishlatilishini lug‘atda sanash (dict)
matn = 'salom salom dunyo dunyo dunyo'
sozlar = matn.split()
hisob = {}

for soz in sozlar:
    hisob[soz] = hisob.get(soz, 0) + 1

print(hisob)

# 🎉 Xulosa
# ✅ Lug‘atlar (dict) → Kalit-qiymat juftligi asosida saqlanadi.
# ✅ To‘plamlar (set) → Takrorlanmaydigan va tartibsiz elementlar.
# ✅ Lug‘atlar mos keladigan kalit orqali tez ma’lumot olish uchun ishlatiladi.
# ✅ To‘plamlar duplikatlarni yo‘qotish va matematik amallar uchun foydali.