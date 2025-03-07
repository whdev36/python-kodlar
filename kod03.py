# 1️⃣ Funksiya yaratish (def)
def salom_ber():
    print("Assalomu alaykum! 😊")

salom_ber()  # Funksiyani chaqirish

# 2️⃣ Parametrlar (argumentlar)
def salom_ber(ism):
    print(f'Salom, {ism}! 😊')

salom_ber('Aziz')  # Parametr yuborish
salom_ber('Laylo') # Parametr yuborish

# 3️⃣ Bir nechta parametrlar
def info(ism, yosh):
    print(f"{ism} {yosh} yoshda.")

info("Bekzod", 25)
info("Nilufar", 21)

# 4️⃣ Standart parametr qiymati (default)
def salom_ber(ism="Do'st"):
    print(f'Salom, {ism}! 😊')

salom_ber()  # Argument berilmagan
salom_ber('Madina')  # Argument berilgan

# 5️⃣ Funksiya natija (return) qaytarishi
def kvadrat(x):
    return x * x  # Natija qaytariladi

son = 5
natija = kvadrat(son)
print(f'{son} ning kvadrati: {natija}')

# 6️⃣ Cheksiz (*args) parametrlar
def yigindi(*sonlar):
    return sum(sonlar)

print(yigindi(2, 3, 4))  # 9
print(yigindi(10, 20, 30, 40))  # 100

# 7️⃣ Kalit so‘zli argumentlar (kwargs)
def info(**malumot):
    for kalit, qiymat in malumot.items():
        print(f'{kalit}: {qiymat}')

info(ism='Ali', yosh=22, shahar='Toshkent')

# 🎯 Amaliy misol: Kalkulyator
def kalkulyator(a, b, amal):
    if amal == '+':
        return a + b
    elif amal == '-':
        return a - b
    elif amal == '*':
        return a * b
    elif amal == '/':
        return a / b if b != 0 else '0 ga bo\'lish mumkin emas!'
    else:
        return 'Noto\'g\'ri amal!'
    
print(kalkulyator(10, 5, '+'))
print(kalkulyator(8, 2, '/'))

# 🎉 Xulosa
# ✅ Funksiya – kodni modulli va qayta ishlatiladigan qiladi.
# ✅ Parametrlar funksiyaga qiymat yuborish imkonini beradi.
# ✅ return natijani qaytaradi va undan boshqa joyda foydalanish mumkin.
# ✅ *args va `kwargs`** – moslashuvchan funksiyalar yaratishga yordam beradi.