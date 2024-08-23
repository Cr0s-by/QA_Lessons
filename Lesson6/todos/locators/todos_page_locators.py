from selenium.webdriver.common.by import By


class TodosPageLocators:
    caption = (By.CSS_SELECTOR, 'header h1')
    todos_input = (By.CSS_SELECTOR, '.new-todo')
    counter = (By.CSS_SELECTOR, '.todo-count')
    toggle_button = (By.CSS_SELECTOR, '.toggle')
    filter_completed_button = (By.LINK_TEXT, "Completed")
    filter_active_button = (By.LINK_TEXT, "Active")
    clear_completed_button = (By.CSS_SELECTOR, '.clear-completed')
    button_to_complete_all_tasks = (By.CSS_SELECTOR, ".toggle-all")
    delete_button = (By.CSS_SELECTOR, '.destroy')
    completed_label_task = (By.CSS_SELECTOR, '.todo-list li.completed label')
    label_task = (By.CSS_SELECTOR, '.view > label')
