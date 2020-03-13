from selenium.webdriver.common.by import By
from Homework_week_8.pages.base_page import Page
from selenium.webdriver.support.select import Select


class MainPage(Page):
    SEARCH_INPUT_LOCATOR = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON_LOCATOR = (By.CSS_SELECTOR, 'input.nav-input[type="submit"]')
    ORDERS_BUTTON_LOCATOR = (By.ID, 'nav-orders')
    CART_BUTTON_LOCATOR = (By.ID, 'nav-cart')
    HAMBURGER_MENU_BUTTON_LOCATOR = (By.ID, 'nav-hamburger-menu')
    SELECT_DEPARTMENTS_LOCATOR = (By.ID, 'searchDropdownBox')


    def open_p(self):
        self.open_page('https://www.amazon.com')

    def search_product(self, text: str):
        self.input(text, *self.SEARCH_INPUT_LOCATOR)
        self.click(*self.SEARCH_ICON_LOCATOR)

    def open_amazon_orders(self):
        self.click(*self.ORDERS_BUTTON_LOCATOR)

    def open_amazon_cart(self):
        self.click(*self.CART_BUTTON_LOCATOR)

    def open_amazon_hamburger_menu(self):
        self.click(*self.HAMBURGER_MENU_BUTTON_LOCATOR)

    def select_search_category(self, option):
        selected = Select(self.find_element(*self.SELECT_DEPARTMENTS_LOCATOR))
        selected.select_by_visible_text(option)








