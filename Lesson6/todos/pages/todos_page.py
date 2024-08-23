from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.todos_page_locators import TodosPageLocators


class TodosPage:
    def __init__(self, driver):
        self.driver = driver

    def get_caption_text(self):
        return self.driver.find_element(*TodosPageLocators.caption).text

    def create_new_task(self, value):
        todo = self.driver.find_element(*TodosPageLocators.todos_input)
        todo.clear()
        todo.send_keys(value)
        todo.send_keys(Keys.ENTER)

    def get_counter_text(self):
        return self.driver.find_element(*TodosPageLocators.counter).text

    def complete_task(self):
        toggle = self.driver.find_element(*TodosPageLocators.toggle_button)
        toggle.click()

    def click_filter_completed_button(self):
        completed_tasks_button = self.driver.find_element(*TodosPageLocators.filter_completed_button)
        completed_tasks_button.click()

    def click_filter_active_button(self):
        completed_tasks_button = self.driver.find_element(*TodosPageLocators.filter_active_button)
        completed_tasks_button.click()

    def get_task_list(self):
        return self.driver.find_elements(*TodosPageLocators.label_task)

    def get_task_list_text(self, number):
        task = self.driver.find_elements(*TodosPageLocators.label_task)
        return task[number].text

    def get_clear_completed_text(self):
        return self.driver.find_element(*TodosPageLocators.clear_completed_button).text

    def click_clear_completed_button(self):
        clear_completed_button = self.driver.find_element(*TodosPageLocators.clear_completed_button)
        clear_completed_button.click()

    def click_button_to_complete_all_tasks(self):
        button_to_complete_all_tasks = self.driver.find_element(*TodosPageLocators.button_to_complete_all_tasks)
        button_to_complete_all_tasks.click()

    def is_task_color_gray(self, number):
        completed_tasks = self.driver.find_elements(*TodosPageLocators.completed_label_task)
        return completed_tasks[number].value_of_css_property('color') == "rgba(217, 217, 217, 1)"

    def is_task_crossed_out(self, number):
        completed_tasks = self.driver.find_elements(*TodosPageLocators.completed_label_task)
        return completed_tasks[number].value_of_css_property(
            'text-decoration') == "line-through solid rgb(217, 217, 217)"

    def click_delete_button(self):
        delete_button = self.driver.find_element(*TodosPageLocators.delete_button)
        task = self.driver.find_element(*TodosPageLocators.label_task)
        actions = ActionChains(self.driver)
        actions.move_to_element(task).perform()
        delete_button.click()

    def edit_task(self, value):
        task = self.driver.find_element(*TodosPageLocators.label_task)
        actions = ActionChains(self.driver)
        actions.move_to_element(task)
        actions.double_click(task)
        actions.click().send_keys(Keys.DELETE + value)
        actions.send_keys(Keys.ENTER).perform()
