import unittest

from src.email_validator import validate_email


class EmailValidatorTestCase(unittest.TestCase):
    def test_ValidateEmail_Positive_True(self):
        email = 'petr@gmail.com'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_InvalidCharacterAtInName_NotValid(self):
        email = "petri@vanov@gmail.com"

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_NotFullEmail_IncorrectInput(self):
        email = 'test@rambler'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_EmptyInputEmail_NoData(self):
        email = ''

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_UsingThePlusSymbolInTheDomain_InvalidCharacterInTheDomain(self):
        email = 'adress@plus+plus.com'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)

    def test_ValidateEmail_EmailWithValidCharacters_ValidCharactersUsed(self):
        email = 'Plus+Minus-Dash_Point.@super-.c-o.m'

        validation_result = validate_email(email)

        self.assertTrue(validation_result)
