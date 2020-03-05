from behave import given, when, then


@given('Open Amzo page')
def open_head_page(context):
    context.app.main_page.open()

@when('Click Amazon Orders link')
def click_order_link(context):
    context.app.main_page.open_orders()

@then('Verify {expected_text} page is opened')
def verify(context, expected_text):
    context.app.results_page.verify_header_result(expected_text)


