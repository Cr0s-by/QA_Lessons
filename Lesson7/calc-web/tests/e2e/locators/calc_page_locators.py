from selenium.webdriver.common.by import By


class CalcPageLocators:
    caption = (By.CSS_SELECTOR, 'h3')
    labels_calculator = (By.CSS_SELECTOR, "label")
    first_operand = (By.ID, 'firstOperand')
    operation_selection = (By.CSS_SELECTOR, 'select>option')
    second_operand = (By.ID, 'secondOperand')
    calculator_button = (By.ID, 'submitCalc')
    result = (By.ID, 'result')
    operation = (By.ID, 'operation')
