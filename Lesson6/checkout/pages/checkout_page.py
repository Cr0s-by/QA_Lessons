from locators.chechout_page_locators import CheckoutPageLocators


class CheckoutPage:
    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def get_caption_text(self):
        return self.driver.find_element(*CheckoutPageLocators.caption).text

    def clear_first_name(self):
        first_name_input = self.driver.find_element(*CheckoutPageLocators.first_name_input)
        first_name_input.clear()

    def click_continue(self):
        continue_button = self.driver.find_element(*CheckoutPageLocators.continue_button)
        continue_button.click()

    def is_first_name_error_visible(self):
        first_name_feedback = self.driver.find_element(*CheckoutPageLocators.first_name_feedback)
        return first_name_feedback.value_of_css_property('display') == 'block'

    def set_first_name(self, value):
        first_name_input = self.driver.find_element(*CheckoutPageLocators.first_name_input)
        first_name_input.send_keys(value)
