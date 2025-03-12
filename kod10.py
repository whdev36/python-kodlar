# 📌 1. try-except yordamida xatolarni ushlash
try:
    # Xatoga sabab bo'lishi mumkin bo'lgan kod
    x = 10 / 0
except:
    # Xato yuz berganda shu qism bajariladi
    print('Xatolik yuz berdi!')

# 📌 2. Aniq xatolarni ushlash
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Nolga bo\'lish mumkin emas!')

# 📌 3. Bir nechta xatolarni ushlash
try:
    son = int(input('Son kiriting: '))
    natija = 10 / son
except ZeroDivisionError:
    print('Nolga bo\'lish mumkin emas!')
except ValueError:
    print('Faqat raqam kiriting!')

# 📌 4. else va finally bloklari
# ✅ else → Agar xato bo‘lmasa, bajariladi.
# ✅ finally → Har qanday holatda ham bajariladi (xato bo‘lsa ham, bo‘lmasa ham).
try:
    x = 5 / 1
except ZeroDivisionError:
    print('Nolga bo\'lish mumkin emas!')
else:
    print('Hammasi joyida, natija:', x)
finally:
    print('Dastur tugadi.')

# 📌 5. Exception orqali har qanday xatoni ushlash
try:
    x = int('salom')
except Exception as e:
    print('Xatolik:', e)