from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

DEAL_OF_THE_DAY = (By.CSS_SELECTOR, '#navSwmHoliday .nav-imageHref')
BLOG_LINK_LOCATOR = (By.XPATH, "//div[@id='main-content']//a[text()='Learn more on our blog']")
AMAZON_LINK = (By.CSS_SELECTOR, '.ArticlePage-hat .GatewayMenu')

AMAZON_DEVICES_FIRST = (By.ID, 'dealImage')
CART_BUTTON = (By.ID, 'add-to-cart-button')
POPUP_CLOSE = (By.CSS_SELECTOR, '.a-icon-close')
SERVICE_PLAN = (By.ID, 'siNoCoverage-announce')
SEE_DETAIL_OPTION = (By.CSS_SELECTOR, '.a-list-item .a-link-normal')

WARRANTY_WINDOW1 = (By.ID, 'a-popover-content-8')
WW1_CLOSE = (By.ID, 'siNoCoverage-announce')
WARRANTY_WINDOW2 = (By.ID, 'attach-warranty-pane')
WW2_CLOSE = (By.ID, 'attachSiNoCoverage-announce')

CART_LOCATOR = (By.CSS_SELECTOR, '#nav-cart')
CART_1ITEM_LOCATOR = (By.ID, 'sc-subtotal-label-activecart')

@given('Open Amazon page and store it')
def open_page(context):
    context.driver.get('https://www.amazon.com')
    context.init_window = context.driver.current_window_handle

@when('Click to the blog link, switch windows, and click to the amazon link')
def blog_link_and_new_page_open(context):
    blog = context.driver.find_element(*BLOG_LINK_LOCATOR)
    blog.click()
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[1])
    # Так как нет товаров в блоге, кликаем на ссылку на основной сайт амазона и открывается 3-е окно
    amazon2 = context.driver.find_element(*AMAZON_LINK)
    amazon2.click()
    context.driver.close()
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[1])

@when('Open deal of the day, choose first item')
def deal_of_the_day(context):
    context.driver.find_element(*DEAL_OF_THE_DAY).click()
    context.driver.find_element(*AMAZON_DEVICES_FIRST).click()

# Здесь обработка 2-х различных вариантов "Deal of the day" с "add to cart button" и "see datail"
# если попадутся еще, нужно будет добавить
@then('Add goods to the cart')
def add_to_the_cart(context):
    # Проверка наличия кнонки добавить в корзину или 'See details'
    if len(context.driver.find_elements(*CART_BUTTON)) < 1:
        context.driver.find_element(*SEE_DETAIL_OPTION).click()
    context.wait.until(EC.element_to_be_clickable(CART_BUTTON))
    context.driver.find_element(*CART_BUTTON).click()
    # определение вылетающих окон с гарантиями
    WW1 = context.driver.find_elements(*WARRANTY_WINDOW1)
    WW2 = context.driver.find_elements(*WARRANTY_WINDOW2)
    # закрываем окна с предложением дополнительной гарантии, если они вылетели
    if len(WW1) > 0:
        context.driver.find_element(*WW1_CLOSE).click()
    elif len(WW2) > 0:
        context.driver.find_element(*WW2_CLOSE).click()

@then('Switch back to original')
def switch_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.all_windows[0])
    context.driver.refresh()



@then('Check goods in he cart')
def check_goods_in_yhe_cart(context):
    amazon_cart = context.driver.find_element(*CART_LOCATOR)
    amazon_cart.click()
    assert 'Subtotal (1 item):' in context.driver.find_element(*CART_1ITEM_LOCATOR).text








