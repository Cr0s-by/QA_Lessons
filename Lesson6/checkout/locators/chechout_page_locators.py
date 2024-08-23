from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    caption = (By.CSS_SELECTOR, '.py-5 h2')
    first_name_input = (By.ID, 'firstName')
    first_name_feedback = (By.CSS_SELECTOR, '#firstName + .invalid-feedback')
    continue_button = (By.CSS_SELECTOR, '.btn-primary')
