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

if __name__ == "__main__":
    unittest.main()