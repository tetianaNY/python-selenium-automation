from selenium.webdriver.common.by import By
from lesson_7.pages.base_page import Page

class ResultsPage(Page):
    HEADER_GOODS_PAGE_LOCATOR = (By.XPATH,
                                 "//div[@id='search']//div[@class='a-section a-spacing-small a-spacing-top-small']//span[@class='a-color-state a-text-bold']")
    def verify_header_result(self, text):
        self.verify_element_text(text, *self.HEADER_GOODS_PAGE_LOCATOR)


