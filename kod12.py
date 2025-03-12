# Obyektga yo‘naltirilgan dasturlash (OOP) ning 3 asosiy tamoyili:
# 1️⃣ Inkapsulyatsiya (Encapsulation) – ma’lumotlarni yashirish va himoyalash.
# 2️⃣ Meros olish (Inheritance) – bitta klass xususiyatlarini boshqa klassga berish.
# 3️⃣ Polimorfizm (Polymorphism) – bir xil nomdagi metodlarning turlicha ishlashi.

# 🔐 1. Inkapsulyatsiya (Encapsulation)
class BankHisob:
    def __init__(self, ism, balans):
        self.ism = ism
        self.__balans = balans  # Yashirilgan o'zgaruvchi

    def balansni_ol(self):
        return self.__balans  # Himoylangan balansni olish usuli
    
    def pul_qosh(self, summa):
        if summa > 0:
            self.__balans += summa
            return f'Hisob to\'ldirildi: {summa} so\'m. ' \
            f'Yangi balans: {self.__balans} so\'m'
        return 'Xatolik: Summani noto\'g\'ri kiritdingiz!'
    
    def pul_yech(self, summa):
        if 0 < summa <= self.__balans:
            self.__balans -= summa
            return f'Balansdan {summa} so\'m yechildi.' \
            f'Yangi balans: {self.__balans} so\'m.'
        return 'Xatolik: Maqblag\' yetarli emas yoki noto\'g\'ri summa!'
    
# Obyekt yaratamiz
hisob = BankHisob('Ali', 50000)

print(hisob.balansni_ol())    # ✅ 50000
print(hisob.pul_qosh(15000))  # ✅ Hisob to‘ldirildi...
print(hisob.pul_yech(30000))  # ✅ Balansdan yechildi...

# ✅ Inkapsulyatsiyaning afzalliklari:
# ✔️ Ma’lumotlarga ruxsatsiz kirishni oldini oladi.
# ✔️ Xavfsizlikni oshiradi.
# ✔️ Klass ichidagi ma’lumotlarni boshqarish imkonini beradi.

# 🛠️ 2. Meros olish (Inheritance)
# ✅ Meros olish misoli
class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi

    def ovoz(self):
        return 'Noma\'lum ovoz'
    
# Meros oluvchi klass
class It(Hayvon):
    def ovoz(self):
        return 'Vov-vov'  # Overriding
    
class Pishak(Hayvon):
    def ovoz(self):
        return 'Miyov!'
    
# Obyektlar yaratamiz!
it = It('Rex')
pishak = Pishak('Tom')

print(it.nomi, ":", it.ovoz())
print(pishak.nomi, ":", pishak.ovoz())

# ✅ Meros olishning afzalliklari:
# ✔️ Kodni qayta yozishning oldini oladi.
# ✔️ Ota klassdagi kodni boshqa klasslarda ham ishlatish mumkin.

# 🎭 3. Polimorfizm (Polymorphism)
class Qush:
    def ovoz(self):
        return 'Chirillash'
    
class Sigir:
    def ovoz(self):
        return 'Mo\'-mo\''
    
class It:
    def ovoz(self):
        return 'Vov-vov'
    
# Har xil hayvonlar uchun bir xil metodni ishlatish
def hayvon_ovoz(hayvon):
    print(hayvon.ovoz())

qush = Qush()
it = It()
sigir = Sigir()

hayvon_ovoz(qush)
hayvon_ovoz(sigir)
hayvon_ovoz(it)

# ✅ Polimorfizmning afzalliklari:
# ✔️ Kodni moslashuvchan qiladi.
# ✔️ Turli obyektlarni bitta metod orqali boshqarish imkonini beradi.