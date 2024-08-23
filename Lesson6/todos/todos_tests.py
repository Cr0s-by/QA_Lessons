import unittest
import time

from selenium import webdriver
from config_manager import ConfigManager
from pages.todos_page import TodosPage


class TodosTests(unittest.TestCase):

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

    def test_OpenPage_CaptionPresented(self):
        caption_text = self.page.get_caption_text()

        self.assertEqual('todos', caption_text)

    def test_AddTask_IncTotalCounter(self):
        self.page.create_new_task("action1")

        counter_text = self.page.get_counter_text()
        self.assertEqual('1 Items left', counter_text)

    def test_AddTaskMarkCompleted_NothingLeftInTotalCounter(self):
        self.page.create_new_task("action1")
        self.page.complete_task()

        counter_text = self.page.get_counter_text()
        self.assertEqual('Nothing left', counter_text)

    def test_CreateATaskAndFilterCompleted_NoCompletedTasks(self):
        self.page.create_new_task("action1")
        self.page.click_filter_completed_button()

        task_count = len(self.page.get_task_list())
        self.assertEqual(0, task_count)

    def test_CreateATaskMarkingItAsCompleted_CompletedTaskVisibleInCompletedFilter(self):
        self.page.create_new_task("action1")
        self.page.complete_task()
        self.page.click_filter_completed_button()

        task_count = len(self.page.get_task_list())
        self.assertEqual(1, task_count)

    def test_CreateATaskMarkingItAsCompleted_ClearCompletedButtonVisibility(self):
        self.page.create_new_task("action1")
        self.page.complete_task()

        clear_completed_text = self.page.get_clear_completed_text()
        self.assertEqual('Clear completed', clear_completed_text)

    def test_CreateATaskMarkingItAsCompletedAndClickTheClearCompletedButton_EmptyList(self):
        self.page.create_new_task("Task")
        self.page.complete_task()
        self.page.click_clear_completed_button()

        task_count = len(self.page.get_task_list())
        self.assertEqual(0, task_count)

    def test_Create2TasksAndCompleteFirstAndPressClearCompleted_SecondTaskRemains(self):
        self.page.create_new_task("action1")
        self.page.create_new_task("Задача2")
        self.page.complete_task()
        self.page.click_clear_completed_button()

        task_list = self.page.get_task_list()
        self.assertEqual(1, len(task_list))
        self.assertEqual("Задача2", task_list[0].text)

        counter_text = self.page.get_counter_text()
        self.assertEqual('1 Items left', counter_text)

    def test_Create2TasksAndClickOnMarkAllButton_TasksCompletedCounterNothingLeft(self):
        self.page.create_new_task("action1")
        self.page.create_new_task("Задача2")
        self.page.click_button_to_complete_all_tasks()

        task_count = len(self.page.get_task_list())
        self.assertEqual(2, task_count)

        time.sleep(1)
        is_task_color = self.page.is_task_color_gray(0)
        self.assertTrue(is_task_color)
        is_task_decoration = self.page.is_task_crossed_out(0)
        self.assertTrue(is_task_decoration)

        is_task_color = self.page.is_task_color_gray(1)
        self.assertTrue(is_task_color)
        is_task_decoration = self.page.is_task_crossed_out(1)
        self.assertTrue(is_task_decoration)

        counter_text = self.page.get_counter_text()
        self.assertEqual('Nothing left', counter_text)
