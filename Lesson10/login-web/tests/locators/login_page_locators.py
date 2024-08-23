from selenium.webdriver.common.by import By


class LoginPageLocators:
    username_input = (By.ID, 'userName')
    password_input = (By.ID, 'password')
    login_button = (By.ID, 'signIn')
    username_error_message = (By.CSS_SELECTOR, '#userName + #invalidUserName')
