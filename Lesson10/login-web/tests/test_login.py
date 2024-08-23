import logging
import os
from datetime import datetime

import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.greeting_page import GreetingPage


class TestLogin:
    page_url = 'http://127.0.0.1:7000/'

    def setup_method(self) -> None:
        if not os.path.isdir('./tests/screenshots'):
            os.mkdir('./tests/screenshots')

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.login_page = LoginPage(self.driver)
        self.greeting_page = GreetingPage(self.driver)

    def teardown_method(self):
        self.driver.close()

    def save_screenshot(self, name):
        path = './tests/screenshots/'
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f'saving screenshot {name}')
        self.driver.save_screenshot(path + name)
        allure.attach.file(source=path + name, attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Login with invalid credentials and check that username error message is shown')
    def test_InvalidUser_ErrorMessageShown(self):
        logging.info('trying to log in as invalid user')
        self.login_page.log_in('fake-user', 'fake-password')

        logging.info('checking that error message is shown')
        assert True == self.login_page.is_user_name_error_message_shown()

        self.save_screenshot('test_InvalidUser_ErrorMessageShown')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Login as admin with valid password and check that correct greeting message is shown')
    def test_ValidUser_GreetingShown(self):
        logging.info('trying to log in as valid user')
        self.login_page.log_in('admin', '123')

        logging.info('checking greeting message')
        greeting_text = self.greeting_page.get_greeting_text()
        assert 'Welcome, admin!' == greeting_text

        self.save_screenshot('test_ValidUser_GreetingShown')
