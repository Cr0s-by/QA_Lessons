import unittest
from src.sum_ex import sum_unless0


class SumUnless0TestCase(unittest.TestCase):
    def test_SumEx_Positive_True(self):
        numbers = ([1, 2, 3])

        validation_result = sum_unless0(numbers)

        self.assertEqual(6, validation_result)

    def test_SumEx_ZerAtTheBeginningOfTheList_ZeroOutput(self):
        numbers = ([0, 1, 2, 3, 4])

        validation_result = sum_unless0(numbers)

        self.assertEqual(0, validation_result)

    def test_SumEx_ZeroIsThirdOnTheList_TheSumOfTheFirstTwoNumbers(self):
        numbers = ([1, 2, 0, 4, 3])

        validation_result = sum_unless0(numbers)

        self.assertEqual(3, validation_result)

    def test_SumEx_ZerAtTheEndOfTheList_SumOfNumbersBeforeZero(self):
        numbers = ([-1, 1, 3, 2, 0])

        validation_result = sum_unless0(numbers)

        self.assertEqual(5, validation_result)

    def test_SumEx_SumOfFloatingPointNumbers_SumOfFloatingPointNumbers(self):
        numbers = ([-2.2, -3.3, -4.4, 2.2, 3.3, 4.4])

        validation_result = sum_unless0(numbers)

        self.assertEqual(0, validation_result)

    def test_SumEx_EmptyList_NotEnoughSummands(self):
        numbers = ([])

        with self.assertRaises(Exception) as context:
            sum_unless0(numbers)

        self.assertEqual('Недостаточно слагаемых', str(context.exception))

    def test_SumEx_SumSingleNumber_NotEnoughSummands(self):
        numbers = [1]

        with self.assertRaises(Exception) as context:
            sum_unless0(numbers)

        self.assertEqual('Недостаточно слагаемых', str(context.exception))

    def test_SumEx_SumWithWords_IncorrectData(self):
        numbers = (["one", "zero", "five"])

        validation_result = sum_unless0(numbers)

        with self.assertRaises(TypeError) as context:
            sum_unless0(numbers)

        self.assertIn('Неверные данные', str(context.exception))
