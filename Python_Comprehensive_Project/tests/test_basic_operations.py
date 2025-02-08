# tests/test_basic_operations.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import unittest
from src.basic_operations import add, subtract, multiply, divide

class TestBasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()