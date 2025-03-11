# 📌 1. Faylni ochish (open())
fayl = open('data.txt', 'r')
print(fayl)

# 📌 2. Fayldan o‘qish (read(), readline(), readlines())
# ✅ read() — Butun faylni o‘qish
malumot = fayl.read()  # Barcha matnlarni o'qish
print(malumot)

# ✅ readlines() — Barcha qatorlarni ro‘yxat sifatida o‘qish
qatorlar = fayl.readlines()
print(qatorlar)

# ✅ readline() — Faylni qatorma-qator o‘qish
bininchi_qator = fayl.readline()
print(bininchi_qator)

# 📌 3. Faylga yozish (write())
# ✅ Faylga yozish ("w") — mavjud ma'lumotlarni o‘chirib, yangisini yozadi:
fayl = open('data.txt', 'w')
fayl.write('yangi matn!\n')
fayl.write('bu yangi fayl.\n')
# fayl.close()

# 📌 4. Faylga qo‘shimcha yozish ("a")
# ✅ "a" — mavjud faylga yangi ma'lumot qo‘shadi:
fayl = open('data.txt', 'a')
fayl.write('bu qo\'shimcha matn.\n')
# fayl.close()

# 📌 5. Kontekst menejeri (with open())
# ✅ with open() yordamida faylni ochish va avtomatik yopish mumkin:
with open('data.txt', 'r') as fayl:
    malumot = fayl.read()
    print(malumot)
# Fayl avtomatik ravishda yopiladi