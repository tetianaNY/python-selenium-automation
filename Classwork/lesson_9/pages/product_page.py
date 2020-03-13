from Classwork.lesson_9.pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductPage(Page):
    ADD_TO_CART_BUTTON_LOCATOR = (By.ID, 'add-to-cart-button')
    SIZE_TOOLTIP_LOCATOR = (By.ID, 'a-popover-content-1')

    def open_product_page(self, amazon_product):
        product_url = f'https://www.amazon.com/gp/product/{amazon_product}'
        self.open_page(product_url)

    def hover_over_button(self):
        self.hover_over_element(*self.ADD_TO_CART_BUTTON_LOCATOR)
        sleep(4)

    def verify_tooltip(self):
        self.wait_for_element_appear(self.SIZE_TOOLTIP_LOCATOR)

