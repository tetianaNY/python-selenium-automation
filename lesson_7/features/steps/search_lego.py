from behave import given, when, then

@given('Open Amazon main page')
def open_amazon_page(context):
    context.app.main_page.open()

@when('Search input fill {search_text}')
def search_input_fill(context, search_text):
    context.app.main_page.search_product(search_text)


@then('Assert {expected_text} in header on the page')
def check_header_goods_page(context, expected_text):
    context.app.results_page.verify_header_result(expected_text)
