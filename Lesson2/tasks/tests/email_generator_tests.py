import unittest

from src.email_generator import generate_email


class EmailGeneratorTestCase(unittest.TestCase):
    def test_GenerateEmail_Positive_True(self):
        user_name = "Petr"
        domain = "rambler.ru"

        validation_result = generate_email(user_name, domain)

        self.assertEqual("Petr@rambler.ru", validation_result)

    def test_GenerateEmail_PointInName_ValidName(self):
        user_name = "Petr.Ivanov"
        domain = "gmail.com"

        validation_result = generate_email(user_name, domain)

        self.assertEqual("Petr.Ivanov@gmail.com", validation_result)

    def test_GenerateEmail_NonReplaceableCharacterEMInTheName_TheEMSymbolHasNotBeenReplaced(self):
        user_name = "Petr.Ivanov!!"
        domain = "gmail.com"

        validation_result = generate_email(user_name, domain)

        self.assertEqual("Petr.Ivanov__@gmail.com", validation_result)

    def test_GenerateEmail_ReplaceableSymbols_TheCharactersHaveBeenReplaced(self):
        user_name = "Petr.Ivanov@#$%^&*()"
        domain = "gmail.com"

        validation_result = generate_email(user_name, domain)

        self.assertEqual("Petr.Ivanov_________@gmail.com", validation_result)

    def test_GenerateEmail_InvalidCharactersInLocalPart_TheCharactersHaveBeenReplaced(self):
        user_name = "Petr!№;:?/\|-+="
        domain = "gmail.com"

        validation_result = generate_email(user_name, domain)

        self.assertEqual("Petr___________@gmail.com", validation_result)
