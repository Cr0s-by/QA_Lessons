import unittest

from math_lib import add, sub, mul, div


class MathTestCase(unittest.TestCase):

    def test_Add_Positives_ValidPositive(self):
        # arrange
        x1 = 2
        x2 = 3

        # act
        result = add(x1, x2)

        # assert
        self.assertEqual(5, result)

    def test_Add_Negatives_ValidNegative(self):
        # arrange
        x1 = -2
        x2 = -3

        # act
        result = add(x1, x2)

        # assert
        self.assertEqual(-5, result)

    def test_Sub_X1LessX2_ValidNegative(self):
        # arrange
        x1 = 2
        x2 = 3

        # act
        result = sub(x1, x2)

        # assert
        self.assertEqual(-1, result)

    def test_Mul_Positives_ValidPositive(self):
        # arrange
        x1 = 2
        x2 = 3

        # act
        result = mul(x1, x2)

        # assert
        self.assertEqual(6, result)

    def test_Div_Positives_ValidPositive(self):
        # arrange
        x1 = 6
        x2 = 3

        # act
        result = div(x1, x2)

        # assert
        self.assertEqual(2, result)

    def test_Div_ByZero_RaiseException(self):
        # arrange
        x1 = 6
        x2 = 0

        # act
        with self.assertRaises(Exception) as context:
            div(x1, x2)
