# https://github.com/hayden-lakh/lab11-HL-TZ
# Partner 1: Hayden Lakhiani
# Partner 2: Tianxiang Zhai

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
         # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 7), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4, 9), 36)
        self.assertEqual(mul(7, -3), -21)
        self.assertEqual(mul(-2, -1), 2)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(9, 81), 9)
        self.assertAlmostEqual(div(12, 3), 0.25)
        self.assertAlmostEqual(div(-1, 2), -2)
        self.assertAlmostEqual(div(2, -1), -0.5)
        self.assertAlmostEqual(div(-6, -30), 5)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 81), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-4, 10)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(3, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(3, -4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(256), 16)

if __name__ == "__main__":
    unittest.main()
