import unittest

from app.services.GreetingService import GreetingService


class GreetingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.greeting_service = GreetingService()

    def test_Get_LatinSymbols_GreetingGenerated(self):
        user_name = 'admin'
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)

    def test_Get_NameWithSpace_GreetingGenerated(self):
        user_name = 'super admin'
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)

    def test_Get_Numbers_GreetingGenerated(self):
        user_name = '0123456789'
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)

    def test_Get_CyrillicSymbols_GreetingGenerated(self):
        user_name = 'Админ'
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)

    def test_Get_SpecialSymbols_GreetingGenerated(self):
        user_name = '!@#$%^*()_+=-<>./?,\|"'
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)

    def test_Get_empty_GreetingGenerated(self):
        user_name = ''
        greeting = self.greeting_service.get(user_name)
        self.assertEqual('Welcome, ' + user_name + '!', greeting)
