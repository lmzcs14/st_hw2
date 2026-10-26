import random
import unittest
from calculator import Calculator

# Property-based tests: instead of checking fixed answers like add(2, 3) == 5,
# each test checks a rule that must hold for ANY inputs, on 1000 random pairs.

TRIALS = 1000

def rand_int():
    return random.randint(-1000, 1000)

def rand_nonzero():
    b = 0
    while b == 0:
        b = rand_int()
    return b

class TestCalculatorProperties(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sub_undoes_add(self):
        # Metamorphic: (a + b) - b == a
        for _ in range(TRIALS):
            a, b = rand_int(), rand_int()
            self.assertEqual(self.calc.sub(self.calc.add(a, b), b), a, f"a={a}, b={b}")

    def test_add_commutative(self):
        # a + b == b + a
        for _ in range(TRIALS):
            a, b = rand_int(), rand_int()
            self.assertEqual(self.calc.add(a, b), self.calc.add(b, a), f"a={a}, b={b}")

    def test_mult_commutative(self):
        # a * b == b * a
        for _ in range(TRIALS):
            a, b = rand_int(), rand_int()
            self.assertEqual(self.calc.mult(a, b), self.calc.mult(b, a), f"a={a}, b={b}")

    def test_div_undoes_mult(self):
        # Metamorphic: (a * b) / b == a, for b != 0
        for _ in range(TRIALS):
            a, b = rand_int(), rand_nonzero()
            self.assertEqual(self.calc.div(self.calc.mult(a, b), b), a, f"a={a}, b={b}")

    def test_div_floors(self):
        # Floor division: the remainder a - div(a, b) * b must be in [0, b) for b > 0.
        # This catches truncating division (e.g. int(a / b)) on negative a,
        # which the Q1 test div(3, 2) == 1 cannot distinguish.
        for _ in range(TRIALS):
            a, b = rand_int(), random.randint(1, 1000)
            remainder = a - self.calc.div(a, b) * b
            self.assertTrue(0 <= remainder < b, f"a={a}, b={b}, remainder={remainder}")

if __name__ == "__main__":
    unittest.main()
