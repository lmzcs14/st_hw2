import unittest

from calculator import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
    def test_sub(self):
        calc = Calculator()
        result = calc.sub(2, 3)
        self.assertEqual(result, -1)  
    def test_mult(self):
        calc = Calculator()
        result = calc.mult(2, 3)
        self.assertEqual(result, 6)
    def test_div(self):
        calc = Calculator()
        result = calc.div(3, 2)
        self.assertEqual(result, 1)
    def test_div_0(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.div(3, 0)
    def test_mod(self):
        calc = Calculator()
        result = calc.mod(7, 3)
        self.assertEqual(result, 1)
    def test_mod_negative(self):
        calc = Calculator()
        result = calc.mod(-7, 3)
        self.assertEqual(result, 2)  # result takes the sign of the divisor
    def test_mod_0(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.mod(3, 0)
    def test_power(self):
        calc = Calculator()
        result = calc.power(2, 3)
        self.assertEqual(result, 8)
    def test_power_0_0(self):
        calc = Calculator()
        result = calc.power(0, 0)
        self.assertEqual(result, 1)  # 0^0 is defined as 1
    def test_power_negative(self):
        calc = Calculator()
        result = calc.power(2, -1)
        self.assertEqual(result, 0.5)

if __name__ == "__main__":
    unittest.main()