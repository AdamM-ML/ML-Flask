import unittest
from quadratic import MathOps.staticmethod

'''class TestQuadratic(unittest.TestCase):
    def test_invalid_type(self):
        self.assertTrue(type(quadratic_function("no", 4, 54) == str))
'''

class TestQuadratic(unittest.TestCase):
    def test_invalid_types(self):
        self.assertRaises(TypeError, quadratic_function, "", "", "")
