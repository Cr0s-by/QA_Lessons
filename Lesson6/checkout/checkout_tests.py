import unittest

from selenium import webdriver

from config_manager import ConfigManager
from pages.checkout_page import CheckoutPage


class CheckoutTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)
        self.driver.get(config.page_url)

        self.page = CheckoutPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_OpenPage_CaptionPresented(self):
        caption_text = self.page.get_caption_text()

        self.assertEqual('Checkout form', caption_text)

    def test_EmptyFirstNameAndCheckout_CheckoutFailedAndFirstNameMarked(self):
        self.page.clear_first_name()
        self.page.click_continue()

        is_error_visible = self.page.is_first_name_error_visible()
        self.assertTrue(is_error_visible)

    def test_FillFirstNameAndCheckout_FirstNameIsNotMarked(self):
        self.page.set_first_name('Ivan')
        self.page.click_continue()

        is_error_visible = self.page.is_first_name_error_visible()
        self.assertFalse(is_error_visible)
