from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_elmnt_txt(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'



