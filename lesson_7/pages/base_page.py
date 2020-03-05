class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def verify_element_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, f"Expected {expected_text}, but got {actual_text}."





