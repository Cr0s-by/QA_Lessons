import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TodosTests(unittest.TestCase):
    page_url = 'https://todo.qa.apps.itschool.pro/#/'

    def setUp(self) -> None:
        super().setUp()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        self.driver = webdriver.Chrome(options=options)

        self.driver.get(self.page_url)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_CreateAnEmptyTask_TaskNotCreated(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys(Keys.ENTER)

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(0, task_count)

    def test_CreateATaskAndDeleteUsingTheButtonOnTheRight_TaskDeleted(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1\n')

        delete_button = self.driver.find_element(By.CSS_SELECTOR, '.destroy')
        task = self.driver.find_element(By.CSS_SELECTOR, '.view > label')
        actions = ActionChains(self.driver)
        actions.move_to_element(task).perform()
        delete_button.click()

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(0, task_count)

    def test_CreateATaskAndFilterActive_TaskInTheActiveFilterList(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('Task\n')

        completed_tasks_button = self.driver.find_element(By.LINK_TEXT, "Active")
        completed_tasks_button.click()

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(1, task_count)

    def test_CreateATaskAndEditingText_TaskTextChanged(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1\n')

        task = self.driver.find_element(By.CSS_SELECTOR, '.view>label')
        actions = ActionChains(self.driver)
        actions.move_to_element(task)
        actions.double_click(task)
        actions.send_keys(Keys.BACKSPACE + '2\n').perform()

        todo_list = self.driver.find_element(By.CSS_SELECTOR, 'ul.todo-list')

        self.assertEqual('action2', todo_list.text)
