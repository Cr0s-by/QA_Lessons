import logging
import os
import unittest
import allure
from datetime import datetime

from selenium import webdriver

from pages.calc_page import CalcPage
from pages.login_page import LoginPage


class LoginTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'
    screenshot_folder_path = './tests/screenshots/'

    def setUp(self) -> None:
        if not os.path.isdir(self.screenshot_folder_path):
            os.mkdir(self.screenshot_folder_path)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.login_page = LoginPage(self.driver)
        self.calc_page = CalcPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def save_screenshot(self, name):
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f"saving screenshot {name}")
        self.driver.save_screenshot(self.screenshot_folder_path + name)
        allure.attach.file(source=self.screenshot_folder_path + name, attachment_type=allure.attachment_type.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Login as invalid user and checking error message")
    def test_InvalidUser_ErrorMessageShown(self):
        logging.info('trying to log in as invalid user')
        self.login_page.login("fake-user", "fake-user")

        logging.info('checking that error message is shown')
        self.assertTrue(self.login_page.is_username_error_message_shown())
        error_message_text = self.login_page.get_username_error_text()
        self.assertEqual('Invalid user name', error_message_text)

        self.save_screenshot("test_InvalidUser_ErrorMessageShown")

    def test_ValidUser_CalcShown(self):
        logging.info('trying to log in as valid user')
        self.login_page.login("admin", "123")

        logging.info('checking calc caption is shown')
        calc_text = self.calc_page.get_caption_text()
        self.assertEqual('Calculator', calc_text)

        self.save_screenshot("ValidUser_CalcShown")

    def test_OpenPage_CaptionPresented(self):
        logging.info('checking login caption is shown')
        caption_text = self.login_page.get_caption_text()

        self.assertEqual('Please sign in', caption_text)

        self.save_screenshot("test_OpenPage_CaptionPresented")

    def test_OpenPage_LabelsVisible(self):
        logging.info('checking label username is shown')
        label_username = self.login_page.get_label_username()
        self.assertEqual('User name', label_username)
        logging.info('checking label password is shown')
        label_password = self.login_page.get_label_password()
        self.assertEqual('Password', label_password)

        self.save_screenshot("test_OpenPage_LabelsVisible")
