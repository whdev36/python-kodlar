# 🎯 O‘zgaruvchilar (Variables)

meva = 'olma'  # Matnli qiymat
yosh = 20  # Butun son
narx = 15.5  # O'nlik son
issiqmi = True  # Mantiqiy qiymat (True/False)

# Har doim o‘zgaruvchilarni tushunarli nomlashga harakat qiling, aks holda kod tushunarsiz bo‘lib qoladi! 😅
x = 'olma'
y = 20
z = 15.5
a = True  # Shunchaki tushunarsiz kod! ❌

# Keling, ularni kodda sinab ko‘ramiz! 🚀

# Matn (String)
ism = 'Ali'
print('Mening ismim:', ism)

# Butun son (Integer)
yosh = 22
print('Mening yoshim:', yosh)

# O‘nlik son (Float)
narx = 99.99
print('Maxsulot narxi:', narx, 'so‘m')

# Mantiqiy qiymat (Boolean)
dars_bor = True
print('Bugun dars bormi?', dars_bor)

# Ro‘yxat (List)
mevalar = ['Olma', 'Banan', 'Shaftoli']
print('Mening sevimli mevalarim:', mevalar)

# # Lug‘at (Dictionary)
talaba = {'ism': 'Ali', 'yosh': 22, 'kurs': 2}
print('Talabaning yoshi:', talaba['yosh'])

# 🛠 Ma’lumot turini aniqlash

son = 42
print(type(son))

matn = 'Salom'
print(type(matn))

raqam = 3.14
print(type(raqam))

haqiqat = True
print(type(haqiqat))

# 🔄 Ma’lumot turlarini o‘zgartirish (Type Conversion)

# Sonni matnga aylantirish
son = 10
matn = str(son)
print(matn, type(matn))

# Matnni songa aylantirish
raqam = '25'
butun_son = int(raqam)
print(butun_son, type(butun_son))

# Matndan o'nlik songa o'tkazish
float_son = float('3.14')
print(float_son, type(float_son))

# 🎉 Xulosa
# -> O‘zgaruvchilar – ma’lumotlarni saqlash uchun ishlatiladi.
# -> Ma’lumot turlari – har xil turdagi ma’lumotlarni ifodalash uchun kerak.
# -> type() funksiyasi – o‘zgaruvchining turini aniqlaydi.
# -> Type conversion – ma’lumot turlarini o‘zgartirish imkonini beradi.
