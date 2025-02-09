# tests/test_calculator.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_exponentiate(self):
        self.assertEqual(self.calc.exponentiate(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(16), 4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_trigonometric(self):
        self.assertAlmostEqual(self.calc.sin(0), 0)
        self.assertAlmostEqual(self.calc.cos(0), 1)
        self.assertAlmostEqual(self.calc.tan(0), 0)

    def test_logs(self):
        self.assertAlmostEqual(self.calc.natural_log(1), 0)
        self.assertAlmostEqual(self.calc.log_base_10(10), 1)
        with self.assertRaises(ValueError):
            self.calc.natural_log(-1)
        with self.assertRaises(ValueError):
            self.calc.log_base_10(0)

    def test_memory(self):
        self.calc.store_to_memory(42)
        self.assertEqual(self.calc.recall_from_memory(), 42)
        self.calc.clear_memory()
        self.assertEqual(self.calc.recall_from_memory(), 0)


if __name__ == "__main__":
    unittest.main()