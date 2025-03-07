
# 1️⃣ Ro‘yxatlar (Lists) 📋
mevalar = ['olma', 'anor', 'banan', 'shaftoli']
sonlar = [10, 20, 30, 40]
aralash = ['salom', 3.14, 42, True]  # har xil turdagi ma'lumotlar bo'lishi mumkin

print(mevalar)
print(sonlar)
print(aralash)

# 2️⃣ List elementlariga murojaat qilish
mevalar = ['olma', 'anor', 'banan', 'shaftoli']
print(mevalar[0])    # olma
print(mevalar[-1])   # shaftoli
print(mevalar[1:3])  # ['anor', 'banan']

# 3️⃣ Listga element qo‘shish va o‘chirish
# 🟢 Yangi element qo‘shish
mevalar = ['olma', 'anor', 'banan', 'shaftoli']
mevalar.append('gilos')
mevalar.insert(2, 'uzum')
print(mevalar)

# 🔴 Elementni o‘chirish
mevalar.remove('banan')  # Qiymat bo'yicha o'chirish
print(mevalar)

mevalar.pop(1)           # Indeks bo'yicha olib tashlash
print(mevalar)

del mevalar[0]           # Indeks bo'yicha o'chirish
print(mevalar)

mevalar.clear()          # Hammasini o'chirish
print(mevalar)

# 4️⃣ List ustida amallar
# 🔄 Ro‘yxatni teskarisiga o‘girish
sonlar = [1, 2, 3, 4, 5]
sonlar.reverse()
print(sonlar)

# 🔢 Ro‘yxatni saralash
raqamlar = [9, 1, 8, 2, 7, 3, 6, 4, 5]
print(raqamlar)

raqamlar.sort()
print(raqamlar)

raqamlar.sort(reverse=True)
print(raqamlar)

# 5️⃣ Tuplar (Tuples) 🎭
ranglar = ('qizil', 'yashil', 'sariq')
sonlar = (1, 2, 3, 4, 5)
aralash = ('salom', 3.14, 42)

print(ranglar)
print(sonlar)
print(aralash)

print(ranglar[0])
print(sonlar[-1])
print(ranglar[1:])

# 7️⃣ Tuple va List o‘zaro o‘zgartirish
# Tuple -> List
tuple_data = (10, 20, 30)
list_data = list(tuple_data)  # Tuple-ni List-ga o'zgartirish
list_data.append(40)
print(list_data)

# List -> Tuple
list_data = ['a', 'b', 'c']
tuple_data = tuple(list_data)  # List-ni Tuple-ga o'zgartirish
print(tuple_data)

# 🎯 Amaliy misol: Foydalanuvchi ma’lumotlari
foydalanuvchi = ('Ali', 25, 'Toshkent')
ism, yosh, shahar = foydalanuvchi  # Tuple-dan o'zgaruvchilarga ajratish
print(f'{ism} {yosh} yoshda va {shahar} shahrida yashaydi.')

# 🎉 Xulosa
# ✅ List – o‘zgaruvchan, tez-tez o‘zgaruvchi ma’lumotlar uchun ishlatiladi.
# ✅ Tuple – o‘zgarmas, tez ishlaydi va xotirani kam ishlatadi.
# ✅ List va Tuple ustida turli operatsiyalar va metodlar mavjud.
# ✅ Tuple elementlarini o‘zgartirib bo‘lmaydi, lekin Listga o‘tkazib o‘zgartirish mumkin.