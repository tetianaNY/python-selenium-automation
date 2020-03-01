from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

BLOG_LINK_LOCATOR = (By.XPATH, "//div[@id='main-content']//a[text()='Learn more on our blog']")

@given('Open Amzon page')
def open_main_page(context):
    context.driver.get('https://www.amazon.com')


@when('Store original window')
def store_init_window(context):
    context.init_window = context.driver.current_window_handle
    # print(context.init_window)

@when('Click to blog link')
def click_to_blog_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog_link.click()
    context.wait.until(EC.number_of_windows_to_be(2))
    context.all_windows = context.driver.window_handles
    # print(all_windows)

@when('Switch to the newly opened window')
def switch_to_the_new_window(context):
    context.driver.switch_to.window(context.all_windows[1])
    sleep(5)

@then('Check this page has {expected_url}')
def page_check(context, expected_url):
    assert expected_url in context.driver.current_url
    # print(context.driver.current_url)

@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    # new_window = context.driver.current_window_handle
    # new_window.close()
    context.driver.close()
    context.driver.switch_to.window(context.all_windows[0])



