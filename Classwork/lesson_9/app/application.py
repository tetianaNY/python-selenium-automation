from Classwork.lesson_9.pages.main_page import MainPage
from Classwork.lesson_9.pages.product_page import ProductPage
from Classwork.lesson_9.pages.results_page import ResultsPage
from Classwork.lesson_9.pages.login_page import LoginPage
from Classwork.lesson_9.pages.cart_page import CartPage
from Classwork.lesson_9.pages.hamburger_menu_page import HamburgerMenuPage
from Classwork.lesson_9.pages.alerts import Alerts


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.hamburger_menu_page = HamburgerMenuPage(self.driver)
        self.alerts = Alerts(self.driver)
