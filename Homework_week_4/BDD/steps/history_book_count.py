from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT_CS = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON_CS = (By.CSS_SELECTOR, '.nav-input')
BOOKS_SEARCH_RESULT = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-fixed-height')

@when('Input {search_t}')
def search_input_enter(context, search_t):
    amazon_search = context.driver.find_element(*SEARCH_INPUT_CS)
    amazon_search.clear()
    amazon_search.send_keys(search_t)
    sleep(1)

@when('Search history books')
def search_button_click(context):
    amazon_button = context.driver.find_element(*SEARCH_BUTTON_CS)
    amazon_button.click()
    sleep(1)

# 1:49:11 lesson 4 find_elements
@then('Count result')
def count_result(context):
    result_list = context.driver.find_elements(*BOOKS_SEARCH_RESULT)
    print(len(result_list))

