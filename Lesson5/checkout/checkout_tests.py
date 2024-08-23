import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckoutTests(unittest.TestCase):
    page_url = 'https://getbootstrap.com/docs/4.4/examples/checkout/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_OpenPage_CaptionPresented(self):
        caption = self.driver.find_element(By.CSS_SELECTOR, '.py-5 h2')

        self.assertEqual('Checkout form', caption.text)

    def test_EmptyFirstNameAndCheckout_CheckoutFailedAndFirstNameMarked(self):
        first_name_input = self.driver.find_element(By.ID, 'firstName')
        first_name_input.clear()

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.btn-primary')
        continue_button.click()

        first_name_feedback = self.driver.find_element(By.CSS_SELECTOR, '#firstName + .invalid-feedback')

        self.assertEqual('block', first_name_feedback.value_of_css_property('display'))

    def test_FillFirstNameAndCheckout_FirstNameIsNotMarked(self):
        first_name_input = self.driver.find_element(By.ID, 'firstName')
        first_name_input.send_keys('Ivan')

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.btn-primary')
        continue_button.click()

        first_name_feedback = self.driver.find_element(By.CSS_SELECTOR, '#firstName + .invalid-feedback')

        self.assertEqual('none', first_name_feedback.value_of_css_property('display'))

