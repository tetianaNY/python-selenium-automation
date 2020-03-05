from selenium.webdriver.common.by import By
from Homework_week_7.pages.base_page import Page

class MainPage(Page):
    ORDERS_LOCATOR = (By.CSS_SELECTOR, '#nav-orders .nav-line-2')


    def open(self):
        self.open_page('https://www.amazon.com')

    def open_orders(self):
        self.click(*self.ORDERS_LOCATOR)




