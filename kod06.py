# 1️⃣ for tsikli

# 📌 Oddiy for tsikli
for i in range(5):
    print(i)

# 📌 Ro‘yxat ustida for tsikli
mevalar = ['olma', 'banan', 'uzum']
for meva in mevalar:
    print(f'Men {meva}ni yaxshi ko\'raman!!!')

# 📌 for va range(start, stop, step)
for i in  range(2, 10, 2):
    print(i)

# 📌 for va enumerate()
ismlar = ['Ali', 'Vali', 'Hasan']
for index, ism in enumerate(ismlar):
    print(f'{index}: {ism}')

# 📌 for va zip()
ismlar = ['Ali', 'Vali', 'Hasan']
yoshlar = [20, 22, 25]

for ism, yosh in zip(ismlar, yoshlar):
    print(f'{ism} {yosh} yoshda.')

# 2️⃣ while tsikli
# 📌 Oddiy while tsikli
son = 0
while son < 5:
    print(f'Son: {son}')
    son += 1

# 📌 Foydalanuvchidan kiritish olish
javob = ''
while javob.lower() != 'stop':
    javob = input('Biror so\'z yozing (chiqish uchun \'stop\'): ')

# 3️⃣ break va continue

# 📌 break (to‘xtatish)
for i in range(10):
    if i == 5:
        break
    print(i)

# continue (keyingi iteratsiyaga o‘tish)
for i in range(5):
    if i == 2:
        continue
    print(i)

# 4️⃣ else bloki bilan for va while
# 📌 for bilan else
for i in range(3):
    print(i)
else:
    print('Tsikl tugadi.')

# 📌 while bilan else
son = 0
while son < 3:
    print(son)
    son += 1
else:
    print('While tsikli tugadi.')

# 5️⃣ Ichma-ich (nested) tsikllar
for i in range(3):
    for j in range(3):
        print(f'{i}, {j}')

# 🎯 Amaliy misol: Foydalanuvchidan PIN kod kiritish
togri_pin = '1234'
kiritish = ''

while kiritish != togri_pin:
    kiritish = input('PIN kodni kiriting: ')
print('To\'g\'ri PIN kiritildi!')

# 🎉 Xulosa
# ✅ for → Iteratsiya uchun.
# ✅ while → Shart bajarilmaguncha takrorlanadi.
# ✅ break → Tsiklni to‘xtatadi.
# ✅ continue → Bir iteratsiyani o‘tkazib yuboradi.
# ✅ else → Tsikl muvaffaqiyatli tugasa ishlaydi.
# ✅ Ichma-ich (nested) tsikllar murakkab jarayonlar uchun ishlatiladi.