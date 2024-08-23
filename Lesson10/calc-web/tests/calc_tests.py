import unittest
import logging
import os
import allure
from datetime import datetime
from selenium import webdriver

from pages.calc_page import CalcPage
from pages.login_page import LoginPage


class CalcTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'
    screenshot_folder_path = './tests/screenshots/'

    def setUp(self) -> None:
        if not os.path.isdir(self.screenshot_folder_path):
            os.mkdir(self.screenshot_folder_path)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.page_url)

        self.calc_page = CalcPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.login_page.login("admin", 123)

    def tearDown(self) -> None:
        self.driver.quit()
        super().tearDown()

    def save_screenshot(self, name):
        name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + f'__{name}.png'
        logging.debug(f"saving screenshot {name}")
        self.driver.save_screenshot(self.screenshot_folder_path + name)
        allure.attach.file(source=self.screenshot_folder_path + name, attachment_type=allure.attachment_type.PNG)

    @allure.description("Calculator caption is shown")
    def test_OpenPage_CaptionPresented(self):
        logging.info('checking calc caption is shown')
        caption_text = self.calc_page.get_caption_text()
        self.assertEqual('Calculator', caption_text)

        self.save_screenshot("test_OpenPage_CaptionPresented")

    @allure.description("Calculator interface visible")
    def test_IsTheCalculatorInterfaceVisible_ElementsShown(self):
        logging.info('checking calc interface is shown')
        labels_text = self.calc_page.get_labels_text()
        self.assertTrue(labels_text.is_displayed())

        self.save_screenshot("test_OpenPage_CaptionPresented")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Calculation is correct result")
    def test_NumberAddition_CorrectResult(self):
        self.calc_page.calculator(3, 4, "+")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("7", result)

        self.save_screenshot("test_NumberAddition_CorrectResult")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Calculation is correct result")
    def test_NumberSubtraction_CorrectResult(self):
        self.calc_page.calculator(5, 6, "-")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("-1", result)

        self.save_screenshot("test_NumberSubtraction_CorrectResult")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Calculation is correct result")
    def test_OneOperand_EmptyResult(self):
        self.calc_page.calculator(5, "", "-")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("", result)

        self.save_screenshot("test_OneOperand_EmptyResult")
