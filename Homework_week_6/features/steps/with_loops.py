from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLERS_LINK = (By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
HEADER = (By.CSS_SELECTOR, '#zg_tabs li')

PAGE_TEXT = (By.ID, 'zg_banner_text_wrapper')


@given('Amazon webpage')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')

@when('Click on best sellers')
def best_sellers(context):
    context.driver.find_element(*BEST_SELLERS_LINK).click()

@then('Click on each top link and verify that new pages open')
def verification(context):
    for i in range(len(context.driver.find_elements(*HEADER))):
        context.driver.find_elements(*HEADER)[i].click()
        context.wait.until(EC.visibility_of_element_located(PAGE_TEXT))
        assert context.driver.find_elements(*HEADER)[i].text in context.driver.find_element(*PAGE_TEXT).text



