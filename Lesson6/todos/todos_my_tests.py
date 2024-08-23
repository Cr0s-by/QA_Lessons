import unittest

from selenium import webdriver
from config_manager import ConfigManager
from pages.todos_page import TodosPage


class TodosMyTests(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        config = ConfigManager.get_config()

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

        self.driver.get(config.page_url)

        self.page = TodosPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

        super().tearDown()

    def test_CreateAnEmptyTask_TaskNotCreated(self):
        self.page.create_new_task("")

        task_count = len(self.page.get_task_list())
        self.assertEqual(0, task_count)

    def test_CreateATaskAndDeleteUsingTheButtonOnTheRight_TaskDeleted(self):
        self.page.create_new_task("action1")
        self.page.click_delete_button()

        task_count = len(self.page.get_task_list())
        self.assertEqual(0, task_count)

    def test_CreateATaskAndFilterActive_TaskInTheActiveFilterList(self):
        self.page.create_new_task("Task")
        self.page.click_filter_active_button()

        task_count = len(self.page.get_task_list())
        self.assertEqual(1, task_count)

    def test_CreateATaskAndEditingText_TaskTextChanged(self):
        self.page.create_new_task("action1")
        self.page.edit_task("action2")

        todo_list = self.page.get_task_list_text(0)

        self.assertEqual('action2', todo_list)
