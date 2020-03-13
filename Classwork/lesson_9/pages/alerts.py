from selenium.webdriver.common.by import By
from Classwork.lesson_9.pages.base_page import Page


class Alerts(Page):
    def create_alert(self):
        self.driver.execute_script('window.alert(\'Hello world\')')

    def create_prompt(self):
        self.driver.execute_script('window.prompt(\"Hello world!!!\")')

    def create_confirm(self):
        self.driver.execute_script('window.confirm(\"Hello world\")')

    def close_alert(self):
        alert = self.wait_until_alert_is_present()
        alert.accept()

    def close_prompt(self):
        alert = self.wait_until_alert_is_present()
        alert.send_keys('Selenium')
        alert.accept()

    def close_confirm(self):
        alert = self.wait_until_alert_is_present()
        print(alert.text)
        alert.dismiss()





