from tests.locators.calc_page_locators import CalcPageLocators
import logging


class CalcPage:
    def __init__(self, driver):
        super(CalcPage, self).__init__()
        self.driver = driver

    def calculator(self, op1, op2, operation):
        self.input_first_operand(op1)
        self.input_second_operand(op2)
        self.set_operation(operation)

    def input_first_operand(self, value):
        logging.info(f"entering '{value}' in first operand")
        first_operand = self.driver.find_element(*CalcPageLocators.first_operand)
        first_operand.clear()
        first_operand.send_keys(value)

    def input_second_operand(self, value):
        logging.info(f"entering '{value}' in second operand")
        second_operand = self.driver.find_element(*CalcPageLocators.second_operand)
        second_operand.clear()
        second_operand.send_keys(value)

    def set_operation(self, value):
        logging.info(f"entering '{value}' in operation")
        operation = self.driver.find_element(*CalcPageLocators.operation)
        operation_select = self.driver.find_elements(*CalcPageLocators.operation_selection)
        operation.click()
        if value == "+":
            option = operation_select[0]
        else:
            option = operation_select[1]
        option.click()

    def get_result(self):
        logging.info(f"result is shown")
        result = self.driver.find_element(*CalcPageLocators.result)
        return result.get_attribute("value")

    def click_calculator_button(self):
        login_button = self.driver.find_element(*CalcPageLocators.calculator_button)
        login_button.click()

    def get_caption_text(self):
        return self.driver.find_element(*CalcPageLocators.caption).text

    def get_labels_text(self):
        return self.driver.find_element(*CalcPageLocators.labels_calculator)
