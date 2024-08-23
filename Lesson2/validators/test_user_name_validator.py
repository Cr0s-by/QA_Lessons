import unittest

from user_name_validator import validate


class UserNameValidatorTestCase(unittest.TestCase):
    def test_validate_shotName_False(self):
        name = 'john'

        result = validate(name)

        self.assertFalse(result)

    def test_validate_longName_False(self):
        name = 'john-winston'

        result = validate(name)

        self.assertFalse(result)

    def test_validate_containsAtSymbol_False(self):
        name = 'john@doe'

        result = validate(name)

        self.assertFalse(result)

    def test_validate_validName_True(self):
        name = 'john-doe'

        result = validate(name)

        self.assertTrue(result)
