from selenium.webdriver.common.by import By
from Homework_week_8.pages.base_page import Page


class ResultsPage(Page):
    SEARCH_SELECT_RESULT = (By.CSS_SELECTOR, '.s-desktop-toolbar .a-color-base')

    def verify_department_header_result(self, expected_text: str):
        self.verify_elmnt_txt(expected_text, *self.SEARCH_SELECT_RESULT)
