from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_INPUT_CS = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON_CS = (By.CSS_SELECTOR, '.nav-input')
BEST_SELLER = (By.CSS_SELECTOR, '.a-badge-text')


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')

@when('Search {search}')
def search_books(context, search):
    amazon_search = context.driver.find_element(*SEARCH_INPUT_CS)
    amazon_search.clear()
    amazon_search.send_keys(search)
    amazon_button = context.driver.find_element(*SEARCH_BUTTON_CS)
    amazon_button.click()

@then('Counting best sellers')
def best_sellers(context):
    count = 0
    context.best_sellers = context.driver.find_elements(*BEST_SELLER)
    for best_seller in context.best_sellers:
        # print(best_seller.text)
        if best_seller.text == 'Best Seller':
            count += 1
    print(f"Best sellers = {count}")





