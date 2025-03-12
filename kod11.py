# 📌 1. Klass va obyektlar
# ✅ Klass yaratish
class Avtomabil:
    def __init__(self, model, rang, yil):  # Konstruktor
        self.model = model
        self.rang = rang
        self.yil = yil

    def info(self):
        return f'{self.model} {self.rang} rangda, {self.yil}-yil.'
    
# ✅ Obyekt yaratish
mashina1 = Avtomabil('Tesla Model S', 'qora', 2023)
print(mashina1.info())

# 📌 2. Inkapsulyatsiya (Encapsulation)
class BankHisob:
    def __init__(self, ism, balans):
        self.ism = ism
        self.__balans = balans  # Himoyalanga o'zgaruvchi (__ bilan boshlanadi)

    def balansni_ol(self):
        return self.__balans  # Faqat shu metod orqali olish mumkin
    
hisob = BankHisob('Ali', 1000)
print(hisob.balansni_ol())  # ✅ 1000
# print(hisob.__balans)  # ❌ Xatolik beradi

# 📌 3. Meros olish (Inheritance)
class Transport:
    def __init__(self, nomi, tezligi):
        self.nomi = nomi
        self.tezligi = tezligi

    def info(self):
        return f'{self.nomi} {self.tezligi} km/soat tezlikda yuradi.'
    
class Avtomabil(Transport):
    def __init__(self, nomi, tezligi, turi):
        super().__init__(nomi, tezligi)  # Super klassdan meros olish

avto = Avtomabil('BMW', 220, 'Sedan')
print(avto.info())

# Har xil klasslar bir xil metodlarni har xil tarzda amalga oshirishi mumkin.
class Qush:
    def ovoz(self):
        return 'Chivillash'
    
class It:
    def ovoz(self):
        return 'Vov-vov'
    
def hayvon_ovoz(hayvon):
    print(hayvon.ovoz())

qush = Qush()
it = It()

hayvon_ovoz(qush)  # ✅ Chirillash
hayvon_ovoz(it)    # ✅ Vov-vov

# 📌 5. Statik metod (@staticmethod)
class Matematika:
    @staticmethod
    def kvadrat(x):
        return x * x
print(Matematika.kvadrat(5))  # ✅ 25

# 📌 6. Dunder metodlar (Special Methods)
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def __str__(self):  # print() ishlatilganda chaqiriladi
        return f'{self.nomi} - {self.muallif}'
    
kitob = Kitob('Python Asoslari', 'Ali Valiev')
print(kitob)