import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


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

    def test_OpenPage_CaptionPresented(self):
        caption = self.driver.find_element(By.CSS_SELECTOR, 'header h1')

        self.assertEqual('todos', caption.text)

    def test_AddTask_IncTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')

        self.assertEqual('1 Items left', counter.text)

    def test_AddTaskMarkCompleted_NothingLeftInTotalCounter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('action1')
        todo.send_keys(Keys.ENTER)

        toggle = self.driver.find_element(By.CSS_SELECTOR, '.toggle')
        toggle.click()

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')

        self.assertEqual('Nothing left', counter.text)

    def test_CreateATaskAndFilterCompleted_NoCompletedTasks(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('Task')
        todo.send_keys(Keys.ENTER)

        completed_tasks_button = self.driver.find_element(By.LINK_TEXT, "Completed")
        completed_tasks_button.click()

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(0, task_count)

    def test_CreateATaskMarkingItAsCompleted_CompletedTaskVisibleInCompletedFilter(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('Task')
        todo.send_keys(Keys.ENTER)

        task_completion_marker = self.driver.find_element(By.CSS_SELECTOR, "div.view > input")
        task_completion_marker.click()

        completed_tasks_button = self.driver.find_element(By.LINK_TEXT, "Completed")
        completed_tasks_button.click()

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(1, task_count)

    def test_CreateATaskMarkingItAsCompleted_ClearCompletedButtonVisibility(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('Task')
        todo.send_keys(Keys.ENTER)

        task_completion_marker = self.driver.find_element(By.CSS_SELECTOR, "div.view > input")
        task_completion_marker.click()

        clear_completed = self.driver.find_element(By.CSS_SELECTOR, '.clear-completed')

        self.assertEqual('Clear completed', clear_completed.text)

    def test_CreateATaskMarkingItAsCompletedAndClickTheClearCompletedButton_EmptyList(self):
        todo = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo.clear()
        todo.send_keys('Task\n')

        task_completion_marker = self.driver.find_element(By.CSS_SELECTOR, "div.view > input")
        task_completion_marker.click()

        clear_completed = self.driver.find_element(By.CSS_SELECTOR, '.clear-completed')
        clear_completed.click()

        task_count = len(self.driver.find_elements(By.CSS_SELECTOR, ".view"))

        self.assertEqual(0, task_count)

    def test_Create2TasksAndCompleteFirstAndPressClearCompleted_SecondTaskRemains(self):
        todo_first_task = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo_first_task.clear()
        todo_first_task.send_keys('action1\n')

        todo_second_task = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo_second_task.clear()
        todo_second_task.send_keys('Задача2\n')

        task_completion_marker = self.driver.find_element(By.CSS_SELECTOR, "div.view > input")
        task_completion_marker.click()

        clear_completed = self.driver.find_element(By.CSS_SELECTOR, '.clear-completed')
        clear_completed.click()

        task_list = self.driver.find_elements(By.CSS_SELECTOR, ".todo-list > li")
        self.assertEqual(1, len(task_list))
        self.assertEqual("Задача2", task_list[0].text)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('1 Items left', counter.text)

    def test_Create2TasksAndClickOnMarkAllButton_TasksCompletedCounterNothingLeft(self):
        todo_first_task = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo_first_task.clear()
        todo_first_task.send_keys('action1\n')

        todo_second_task = self.driver.find_element(By.CSS_SELECTOR, '.new-todo')
        todo_second_task.clear()
        todo_second_task.send_keys('Задача2\n')

        button_to_complete_all_tasks = self.driver.find_element(By.CSS_SELECTOR, ".toggle-all")
        button_to_complete_all_tasks.click()

        completed_tasks = self.driver.find_elements(By.CSS_SELECTOR, '.todo-list li.completed label')
        self.assertEqual(2, len(completed_tasks))

        time.sleep(1)
        task_color = completed_tasks[0].value_of_css_property('color')
        self.assertEqual("rgba(217, 217, 217, 1)", task_color)
        task_text_decoration = completed_tasks[0].value_of_css_property('text-decoration')
        self.assertEqual("line-through solid rgb(217, 217, 217)", task_text_decoration)

        task_color = completed_tasks[1].value_of_css_property('color')
        self.assertEqual("rgba(217, 217, 217, 1)", task_color)
        task_text_decoration = completed_tasks[1].value_of_css_property('text-decoration')
        self.assertEqual("line-through solid rgb(217, 217, 217)", task_text_decoration)

        counter = self.driver.find_element(By.CSS_SELECTOR, '.todo-count')
        self.assertEqual('Nothing left', counter.text)
