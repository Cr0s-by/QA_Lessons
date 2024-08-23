import unittest

from selenium import webdriver

from pages.calc_page import CalcPage
from pages.login_page import LoginPage


class CalcTests(unittest.TestCase):
    page_url = 'http://127.0.0.1:7000/'

    def setUp(self) -> None:
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

    def test_OpenPage_CaptionPresented(self):
        caption_text = self.calc_page.get_caption_text()
        self.assertEqual('Calculator', caption_text)

    def test_IsTheCalculatorInterfaceVisible_ElementsShown(self):
        labels_text = self.calc_page.get_labels_text()
        self.assertTrue(labels_text.is_displayed())

    def test_NumberAddition_CorrectResult(self):
        self.calc_page.input_first_operand(3)
        self.calc_page.input_second_operand(4)
        self.calc_page.set_operation("+")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("7", result)

    def test_NumberSubtraction_CorrectResult(self):
        self.calc_page.input_first_operand(5)
        self.calc_page.input_second_operand(6)
        self.calc_page.set_operation("-")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("-1", result)

    def test_OneOperand_EmptyResult(self):
        self.calc_page.input_first_operand(5)
        self.calc_page.input_second_operand("")
        self.calc_page.set_operation("+")

        self.calc_page.click_calculator_button()

        result = self.calc_page.get_result()
        self.assertEqual("", result)
