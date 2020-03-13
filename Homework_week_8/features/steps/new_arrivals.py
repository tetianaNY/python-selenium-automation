from behave import given, when, then


@given('Open amazon product {amazon_product} page')
def open_amazon_pp(context, amazon_product):
    context.app.product_page.open_product_page(amazon_product)


@when('Hover over New Arrivals')
def hover_over_button(context):
    context.app.product_page.hover_over_button()


@then('Verify user sees a deal')
def verify_user_sees_deal(context):
    context.app.product_page.verify_information()
