import pytest
import unittest

import calc_functions as calc_functions

class CalcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc_functions.add(2, 4), 6)


    def test_subtract(self):
        self.assertEqual(calc_functions.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(calc_functions.multiply(2, 2), 4)


    def test_divide(self):
        self.assertEqual(calc_functions.divide(6, 3), 2)
        self.assertEqual(calc_functions.divide(5, 0), None)
