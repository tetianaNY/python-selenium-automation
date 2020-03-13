from Classwork.lesson_9.pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class ProductPage(Page):
    ADD_TO_CART_BUTTON_LOCATOR = (By.ID, 'add-to-cart-button')
    FLYOUT_MENU_LOCATOR = (By.XPATH, "//div[@class='mega-menu']//h3[text()='Women']")
    NEW_ARRIVALS_LOCATOR = (By.CSS_SELECTOR, '.nav-hasArrow[tabindex="67"]')

    def open_product_page(self, amazon_product):
        product_url = f'https://www.amazon.com/gp/product/{amazon_product}'
        self.open_page(product_url)

    def hover_over_button(self):
        self.hover_over_element(*self.NEW_ARRIVALS_LOCATOR)

    def verify_information(self):
        self.wait_for_element_appear(self.FLYOUT_MENU_LOCATOR)
