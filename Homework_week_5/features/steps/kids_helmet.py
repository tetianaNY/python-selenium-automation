from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name ul[role="radiogroup"] li')
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
ADD_TO_CRT = (By.CSS_SELECTOR, '#add-to-cart-button')
HELMET_CLICK = (By.NAME, 'submit.add-to-cart')

@given('Open Amazon kids helmet page')
def open_helmet_page(context):
    context.driver.get('https://www.amazon.com/Kids-Helmet-Adjustable-Toddler-Youth/dp/B07PG3PRG8/ref=sxin_3_ac_d_pm?ac_md=2-1-QmV0d2VlbiAkMjAgYW5kICQyNQ%3D%3D-ac_d_pm&crid=2QJB9SKZJ39XB&cv_ct_cx=helmets+for+kids+3-5&keywords=helmets+for+kids+3-5&pd_rd_i=B07PG3PRG8&pd_rd_r=d61d33d8-6352-4256-a610-ec5b749642a1&pd_rd_w=GRQ5q&pd_rd_wg=Z03YU&pf_rd_p=516e6e17-ed95-417b-b7a4-ad2c7b9cbae3&pf_rd_r=ESPCQ6XDWNJMGNGYWTS2&psc=1&qid=1582402456&sprefix=helmet%2Caps%2C158')

@when('Get all helmets color')
def get_all_helmet_colors(context):
    context.helmets_color = context.driver.find_elements(*COLOR_LOCATOR)

@then('Check every color has a description')
def description_check(context):
    context.color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for color in context.helmets_color:
        color.click()
        print(context.color_title.text)
        assert context.color_title.text in color.get_attribute('title'), f"Expected {color_title.text} in {color.get_attribute('title')}"

# @then('Add to the crt')
# def add_to_crt(context):
#     for color in context.helmets_color:
#         color.click()
#         if context.color_title.text == "BLUE":
#             print(context.color_title.text)
#             sleep(3)
#             add_to_crt = context.driver.find_element(*ADD_TO_CRT)
#             add_to_crt.click()










