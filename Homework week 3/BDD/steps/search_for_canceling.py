from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.XPATH, "//div[@class='a-row']//input[@type='search']")
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//div[@class='a-column a-span2 a-span-last']//input[@class='a-button-input']")
HEADER_GOODS_PAGE_LOCATOR = (By.XPATH, "//div[@class='a-box a-spacing-extra-large a-color-offset-background answer-box']")

@given('Open Amazon help')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search input enter {search_text}')
def search_input_enter(context, search_text):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys(search_text)
    sleep(4)

@when('Click on search')
def click_search(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()
    sleep(2)

@then('Assert {search_text} on the page')
def check_goods_page(context, search_text):
    assert search_text in context.driver.find_element(*HEADER_GOODS_PAGE_LOCATOR).text
