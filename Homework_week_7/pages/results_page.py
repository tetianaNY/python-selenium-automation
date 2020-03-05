from selenium.webdriver.common.by import By
from Homework_week_7.pages.base_page import Page

class ResultsPage(Page):
    SIGN_IN_H1 = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMPTY_CART = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty')

    def verify_header_result(self, text):
        self.verify_elmnt_txt(text, *self.SIGN_IN_H1)

    def verify_empty_cart(self, text):
        self.verify_elmnt_txt(text, *self.EMPTY_CART)


