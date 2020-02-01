from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_LOCATOR = (By.CSS_SELECTOR, '#nav-cart')
CART_EMPTY_LOCATOR = (By.CSS_SELECTOR, '.sc-empty-cart-header')

@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Search cart on the website and click')
def search_input_enter(context):
    amazon_cart = context.driver.find_element(*CART_LOCATOR)
    amazon_cart.click()
    sleep(4)

@then('Check {cart} on the page')
def check_goods_page(context, cart):
    assert cart in context.driver.find_element(*CART_EMPTY_LOCATOR).text
