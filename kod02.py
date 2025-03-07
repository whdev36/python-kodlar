# 1️⃣ if-else shart operatori
yosh = 18

if yosh >= 18:
    print('Siz voyaga yetgansiz! ✅')
else:
    print('Siz hali voyaga yetmagansiz! ❌')

# 2️⃣ if-elif-else operatori
ball = 85

if ball >= 90:
    print('Sizning bahoingiz: A 🎯')
elif ball >= 80:
    print('Sizning bahoingiz: B 👍')
elif ball >= 70:
    print('Sizning bahoingiz: B 👍')
else:
    print('Siz imtihondan o\'tmadingiz 😢')

# 3️⃣ if ichida if (nested if)
ob_havo = "yomg'irli"
issiqmi = False

if ob_havo == 'yomg\'irli':
    if issiqmi:
        print('Soyabon va futbolka oling! ☔👕')
    else:
        print('Soyabon va kurtka oling! ☔🧥')
else:
    print('Soyabon va kurtka oling! ☔🧥')

# 4️⃣ match-case (Python 3.10+)
baho = ''

match baho:
    case 'a':
        print('Ajoyib! 🎉')
    case 'b':
        print('Yaxshi! 👍')
    case 'c':
        print('Qoniqarli! 🙂')
    case _:
        print('Siz qayta topshirishingiz kerak! 😢')

# 🎯 Amaliy misol: ATM tizimi
komanda = input('Amalni tanlang: (1 - Naqd pul olish, 2 - Balansni ko\'rish, 3 - Chiqish): ')

match komanda:
    case '1':
        print('Karta ichidan pul olinmoqda... 💸')
    case '2':
        print('Balansingiz: 1 500 000 so‘m 💰')
    case '3':
        print('Siz tizimdan chiqdingiz. 👋')
    case _:
        print('Noto‘g‘ri buyruq! ❌')

# 🎉 Xulosa
# ✅ if-else – Shartni tekshiradi va mos kelgan kodni bajaradi.
# ✅ elif – Qo‘shimcha shartlarni tekshirish uchun ishlatiladi.
# ✅ Ichma-ich if – Bir shart ichida boshqa shartlarni tekshirish imkonini beradi.
# ✅ match-case – Ko‘p shartli holatlarni yanada osonroq yozish uchun ishlatiladi.
