from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'searchval')
SEARCH_BUTTON = (By.CSS_SELECTOR, '.banner-search-btn')
PRODUCT_LIST = (By.CSS_SELECTOR, '#product_listing .ag-item')
BUY_BUTTON = (By.ID, 'buyButton')
VIEW_CART = (By.CSS_SELECTOR, '.btn.btn-primary')
EMPTY_CART = (By.CSS_SELECTOR, '.emptyCartButton.btn.btn-mini.btn-ui.pull-right')
EMPTY_CART_CONFIRM = (By.CSS_SELECTOR, '.modal-footer .btn.btn-primary')

@given('Open Webstaurant store page')
def open_webpage(context):
    context.driver.get('https://www.webstaurantstore.com')

@when('Look for {querry}')
def looking_for_item(context, querry):
    webst_search = context.driver.find_element(*SEARCH_FIELD)
    webst_search.clear()
    webst_search.send_keys(querry)
    context.driver.find_element(*SEARCH_BUTTON).click()

@when('Check all result ensuring {q} its title')
def looking_for_something(context, q):
    context.products = context.driver.find_elements(*PRODUCT_LIST)
    for i in range(len(context.products)):
        assert q in context.products[i].text, f'Expected {q}, but didnt find it in item {i}, with text {context.products[i].text}'
@then('Add last item to the cart')
def add_last_item(context):
    context.driver.find_elements(*PRODUCT_LIST)[len(context.products)-1].click()
    context.driver.find_element(*BUY_BUTTON).click()
@then('Empty cart')
def empty_cart(context):
    context.wait.until(EC.element_to_be_clickable(VIEW_CART))
    context.driver.find_element(*VIEW_CART).click()
    context.driver.find_element(By.NAME, 'quantityButtonDown').click()
    context.driver.find_element(By.ID, 'update-cart').click()

    sleep(2)


