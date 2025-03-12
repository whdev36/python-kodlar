# 🔹 Dekoratorlar – funksiyalarga qo‘shimcha imkoniyat qo‘shish usuli.
# 🔹 Lambda funksiyalar – bir qatorlik, anonim funksiyalar.

# 🌀 Lambda funksiyalar
# lambda argument: ifoda

# ✅ Oddiy lambda misoli
kvadrat = lambda x: x ** 2
print(kvadrat(5))

# ✅ Lambda funksiyada bir nechta argumentlar
kopaytirish = lambda a, b: a * b
print(kopaytirish(4, 5))

# ✅ map(), filter(), sorted() bilan lambda

# 🔹 map() – Har bir elementga funksiya qo‘llash
raqamlar = [1, 2, 3, 4, 5]
kvadratlar = list(map(lambda x: x ** 2, raqamlar))
print(kvadratlar)

# 🔹 filter() – Shart bo‘yicha elementlarni ajratish
sonlar = [10, 21, 30, 41, 50]
juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft_sonlar)

# 🔹 sorted() – Tartanlanish bo‘yicha saralash
talabalar = [('Ali', 85), ('Bobur', 92), ('Dilnoza', 78)]
saralangan = sorted(talabalar, key=lambda x: x[1], reverse=True)
print(saralangan)

# 🎭 Dekoratorlar
def salom_dekorator(funk):
    def qadoqlangan_funk():
        print('Assalomu alaykum!')
        funk()
        print('Xayr!')
    return qadoqlangan_funk

@salom_dekorator
def salom_ber():
    print('Men oddiy funksiya.')

salom_ber()

# ✅ Parametrli dekorator
def kopaytiruvchi(n):
    def dekorator(funk):
        def qadoqlangan(*args):
            natija = funk(*args)
            return natija * n
        return qadoqlangan
    return dekorator

@kopaytiruvchi(3)
def son_qaytar(x):
    return x

print(son_qaytar(5))

# ✅ Bir nechta dekoratorlar
def dekorator1(funk):
    def qadoqlangan():
        print('Dekorator 1 ishladi.')
        funk()
    return qadoqlangan

def dekorator2(funk):
    def qadoqlangan():
        print('Dekorator 2 ishladi.')
        funk()
    return qadoqlangan

@dekorator1
@dekorator2
def funksiya():
    print('Asosiy funksiya!')

funksiya()