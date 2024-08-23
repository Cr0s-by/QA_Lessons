import logging

from tests.locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        super(LoginPage, self).__init__()
        self.driver = driver

    def set_username(self, value):
        logging.info(f"entering '{value}' in username field")
        username = self.driver.find_element(*LoginPageLocators.username_input)
        username.clear()
        username.send_keys(value)

    def set_password(self, value):
        logging.info(f"entering '{value}' in password field")
        password = self.driver.find_element(*LoginPageLocators.password_input)
        password.clear()
        password.send_keys(value)

    def click_login_button(self):
        logging.info("clicking on 'Sign in' button")
        login_button = self.driver.find_element(*LoginPageLocators.login_button)
        login_button.click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def is_username_error_message_shown(self):
        user_name_error_message = self.driver.find_element(*LoginPageLocators.username_error_message)
        return user_name_error_message.value_of_css_property('display') == 'block'

    def get_username_error_text(self):
        return self.driver.find_element(*LoginPageLocators.username_error_message).text

    def get_caption_text(self):
        return self.driver.find_element(*LoginPageLocators.caption).text

    def get_label_username(self):
        return self.driver.find_element(*LoginPageLocators.label_username).text

    def get_label_password(self):
        return self.driver.find_element(*LoginPageLocators.label_password).text
