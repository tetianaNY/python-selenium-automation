from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LC = (By.XPATH, "//div[@class='a-row']//input[@type='search']")
SEARCH_BUTTON_LC = (By.XPATH, "//div[@class='a-column a-span2 a-span-last']//input[@class='a-button-input']")
HEADER_GOODS_PAGE_LC = (By.CSS_SELECTOR, "p.a-color-secondary b")

@given('Open Amazon help')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search input enter {search_t}')
def search_input_enter(context, search_t):
    amazon_search = context.driver.find_element(*SEARCH_INPUT_LC)
    amazon_search.clear()
    amazon_search.send_keys(search_t)
    sleep(4)

@when('Click on search')
def click_search(context):
    amazon_button = context.driver.find_element(*SEARCH_BUTTON_LC)
    amazon_button.click()
    sleep(2)

@then('Find {search_t} on the page')
def check_goods_page(context, search_t):
    assert 'Cancel Order' in context.driver.find_element(*HEADER_GOODS_PAGE_LC).text
