from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT_CS = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON_CS = (By.CSS_SELECTOR, '.nav-input')
BOOKS_SEARCH_RESULT = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-fixed-height')
FIRST_BOOK_PRICE_LOCATOR = (By.CSS_SELECTOR, '.a-price-whole')
FIRST_BOOK = (By.CSS_SELECTOR, '.s-no-hover')
ADD_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')

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

@then('Add first book to the cart if price more than {price} dollars')
def add_to_cart(context, price):
    first_book_price = context.driver.find_element(*FIRST_BOOK_PRICE_LOCATOR).text
    if int(first_book_price) > int(price):
        first_book_button = context.driver.find_element(*FIRST_BOOK)
        first_book_button.click()
        sleep(1)
        add_button = context.driver.find_element(*ADD_CART_BUTTON)
        add_button.click()
        sleep(4)
    else:
        print('The first book price is not more than', price, 'dollars.')





