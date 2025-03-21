# 🔹 1. unittest kutubxonasi
# 📌 Oddiy funksiya uchun test yozish

import unittest

# 🎯 Test qilinadigan funksiya
def add(x, y):
    return x + y

# 🧪 Test klassi
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertNotEqual(add(2, 2), 5)

# # 🏃 Testlarni ishga tushirish
# if __name__ == '__main__':
#     unittest.main()

# 🔹 2. pytest kutubxonasi
# 📌 Oddiy funksiya uchun test yozish
def add(x, y):
    return x + y

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(2, 2) != 5


# 📌 pytest yordamida klasslar bilan test yozish
import pytest

def divide(x, y):
    if y == 0:
        raise ValueError('📌 pytest yordamida klasslar bilan test yozish')
    return x / y

class TestMathOperations:
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)