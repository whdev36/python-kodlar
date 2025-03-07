# 🔢 Operatorlar (Arifmetik, Mantiqiy, Solishtirish) ➕➖

# 1️⃣ Arifmetik Operatorlar
a = 10
b = 3

print(a + b)  # Natija: 13
print(a - b)  # Natija: 7
print(a * b)  # Natija: 30
print(a / b)  # Natija: 3.3333333333333335
print(a // b) # Natija: 3
print(a % b)  # Natija: 1
print(a ** b) # Natija: 1000 (10 darajasi 3)

# 2️⃣ Solishtirish Operatorlari
x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= 10)  # True
print(y <= 5)  # True

# 3️⃣ Mantiqiy Operatorlar
a = True
b = False

print(a and b) # False (Ikkalasi ham True bo'lishi kerak)
print(a or b)  # True  (Kamida bittasi True bo'lsa yetarli)
print(not b)   # True  (Teskarisini qaytaradi)

# 👀 Real hayotiy misol:

yomgir_yogayaptimi = True
soyabon_bormi = False

if yomgir_yogayaptimi and not soyabon_bormi:
    print('Siz ho‘l bo‘lasiz! ☔️')

# 🎯 Bonus: O‘zgaruvchiga qiymat beruvchi operatorlar (Assignment Operators)
x = 10
x += 5   # x = x + 5
print(x) # natija: 15

y = 20
y //= 3   # y = y // 3
print(y)  # natija: 6

# 🎉 Xulosa
# -> Arifmetik operatorlar: Qo‘shish, ayirish, bo‘lish va h.k.
# -> Solishtirish operatorlari: Qiymatlarni taqqoslash uchun.
# -> Mantiqiy operatorlar: and, or, not bilan shartlarni tekshirish.
# -> Qiymat beruvchi operatorlar: +=, -=, *=, va h.k.