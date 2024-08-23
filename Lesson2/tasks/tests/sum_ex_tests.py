import unittest

from src.sum_ex import sum_ex


class SumExTestCase(unittest.TestCase):
    def test_SumEx_Positive_True(self):
        numbers = ([1, 2, 3])

        validation_result = sum_ex(numbers)

        self.assertEqual(6, validation_result)

    def test_SumEx_SumOfPositiveAndNegativeNumbers_SumOutput(self):
        numbers = ([-2, -3, -4, 2, 3, 4])

        validation_result = sum_ex(numbers)

        self.assertEqual(0, validation_result)

    def test_SumEx_SumOfFloatingPointNumbers_SumOutput(self):
        numbers = ([-2.2, -3.3, -4.4, 2.2, 3.3, 4.4])

        validation_result = sum_ex(numbers)

        self.assertEqual(0, validation_result)

    def test_SumEx_SumWithWords_ErrorOutput(self):
        numbers = (["one", "zero", "five"])

        validation_result = sum_ex(numbers)

        with self.assertRaises(TypeError) as context:
            sum_ex(numbers)

        self.assertIn('Неверные данные', str(context.exception))

    def test_SumEx_SumSingleNumber_NoEnoughSummands(self):
        numbers = [1]

        with self.assertRaises(Exception) as context:
            sum_ex(numbers)

        self.assertEqual('Недостаточно слагаемых', str(context.exception))

    def test_SumEx_EmptyList_NoEnoughSummands(self):
        numbers = ([])

        with self.assertRaises(Exception) as context:
            sum_ex(numbers)

        self.assertEqual('Недостаточно слагаемых', str(context.exception))
