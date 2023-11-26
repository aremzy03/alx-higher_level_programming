#!/usr/bin/python3
"""A unittest module
"""
import unittest


max_integer = __import__("6-max_integer").max_integer


class MaxIntegerTest(unittest.TestCase):
    """tests the max_integer module

    Args:
        unittest (_type_): _description_
    """

    def test_int(self):
        """Checks if it works if a a list of ints is passed
        """
        self.assertEqual(max_integer([1, 434, 566, 4, 492]), 566)
        self.assertEqual(max_integer([232, -32, 2, 1000000]), 1000000)

    def test_str(self):
        """Tests when a string is passed
        """
        self.assertEqual(max_integer("yoo"), "y")
        self.assertEqual(max_integer("I am Abdulmalik"), "u")

    def test_none(self):
        """Tests when nothing is passed
        """
        self.assertIsNone(max_integer(""))
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())
