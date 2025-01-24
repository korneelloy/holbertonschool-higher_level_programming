#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 5, 4]), 5)
        self.assertAlmostEqual(max_integer([1, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([5, 4, 1]), 5)
        self.assertAlmostEqual(max_integer([5]), 5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(['a', 'c', 'b']), 'c')

    def test_nb_args(self):
        self.assertRaises(TypeError, max_integer, [1, 3, 4, 2], [3, 4, 5])
