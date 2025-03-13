# 📌 1. Modul nima?

import matematika

print(matematika.kvadrat(5))
print(matematika.kub(3))

# 📥 2. Modulni turli usullar bilan chaqirish
# 1️⃣ Oddiy import yordamida chaqirish

import matematika
print(matematika.kvadrat(4))


# 2️⃣ Modul ichidan faqat kerakli funksiyalarni import qilish
from matematika import kvadrat, kub
print(kvadrat(6))
print(kub(2))

# 3️⃣ Modulni boshqa nom bilan import qilish (as)
import matematika as m
print(m.kvadrat(7))

# 4️⃣ Hammasini import qilish (*)
from matematika import *
print(kub(5))

# 📂 3. Paket (package) nima?
from mka.algebra import kvadrat
from mka.geometria import aylana_yuzi

print(kvadrat(4))
print(aylana_yuzi(3))

# 📚 4. Standart kutubxona modullari
import math
print(math.sqrt(25))
print(math.pi)

# 🚀 5. pip yordamida tashqi modullarni o‘rnatish
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.json())