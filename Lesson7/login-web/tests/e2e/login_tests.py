import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.greeting_page import GreetingPage


class LoginTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.login_page = LoginPage(self.driver)
        self.greeting_page = GreetingPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def test_InvalidUser_ErrorMessageShown(self):
        self.login_page.set_username('fake-user')
        self.login_page.set_password('fake-password')
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_user_name_error_message_shown())

    def test_ValidUser_GreetingShown(self):
        self.login_page.set_username('admin')
        self.login_page.set_password('123')
        self.login_page.click_login_button()

        greeting_text = self.greeting_page.get_greeting_text()
        self.assertEqual('Welcome, admin!', greeting_text)

