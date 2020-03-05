from selenium.webdriver.common.by import By
from lesson_7.pages.base_page import Page

class MainPage(Page):
    SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'input.nav-input[value="Go"]')


    def open(self):
        self.open_page('https://www.amazon.com')

    def search_product(self, text: str):
        self.input(text, *self.SEARCH_INPUT_LOCATOR)
        self.click(*self.SEARCH_BUTTON_LOCATOR)

