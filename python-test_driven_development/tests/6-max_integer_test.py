#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer"""

    def test_max_integer(self):
        """Test the function max_integer with a list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([100, 50, 150]), 150)
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test the function max_integer with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test the function max_integer with a list containing a single element"""
        self.assertEqual(max_integer([10]), 10)

    def test_floats(self):
        """Test the function max_integer with floats in the list"""
        self.assertEqual(max_integer([1.5, 2.2, 3.3, 0.4]), 3.3)

    def test_mixed_integers_floats(self):
        """Test the function max_integer with a list containing both integers and floats"""
        self.assertEqual(max_integer([1.5, 3, 2, 5.2]), 5.2)

if __name__ == "__main__":
    unittest.main()
