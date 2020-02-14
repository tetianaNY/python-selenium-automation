from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_CS = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON_CS = (By.CSS_SELECTOR, '.nav-input')
SEARCH_RESULT_ITEM = (By.CSS_SELECTOR, '.s-result-list.s-search-results .s-result-item .a-text-normal')
ADD_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
CHECK_CART_BUTTON = (By.CSS_SELECTOR, '#hlb-view-cart-announce')
ITEM_IN_THE_CART = (By.CSS_SELECTOR, '#sc-subtotal-label-activecart')


@given('Open Amazon website')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@when('Search input and fill {search_t}')
def search_input_enter(context, search_t):
    amazon_search = context.driver.find_element(*SEARCH_INPUT_CS)
    amazon_search.clear()
    amazon_search.send_keys(search_t)
    sleep(1)

@when('Click a search button')
def search_button_click(context):
    amazon_button = context.driver.find_element(*SEARCH_BUTTON_CS)
    amazon_button.click()
    sleep(1)

@when('Choose the first item')
def item_click(context):
    item_header = context.driver.find_element(*SEARCH_RESULT_ITEM)
    item_header.click()
    sleep(1)

@when('Add good to cart')
def adding_random_item_to_cart(context):
    add_button = context.driver.find_element(*ADD_CART_BUTTON)
    add_button.click()
    sleep(1)

@when('Click cart icon')
def cart_open(context):
    check_cart_button = context.driver.find_element(*CHECK_CART_BUTTON)
    check_cart_button.click()
    sleep(1)

@then('Check {item} in the cart')
def check_item_in_the_cart(context, item):
    assert item in context.driver.find_element(*ITEM_IN_THE_CART).text





