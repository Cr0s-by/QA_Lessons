from tests.e2e.locators.greeting_page_locators import GreetingPageLocators


class GreetingPage:
    def __init__(self, driver):
        super(GreetingPage, self).__init__()
        self.driver = driver

    def get_greeting_text(self):
        return self.driver.find_element(*GreetingPageLocators.greeting_value).text
