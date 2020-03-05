from behave import given, when, then


# @given('Open Amzo page')
# def open_head_page(context):
#     context.app.main_page.open()

@when('Click on cart icon')
def open_cart(context):
    context.app.main_page.open_cart()

@then('Verify {expected_result} text present')
def verify(context, expected_result):
    context.app.results_page.verify_empty_cart(expected_result)

