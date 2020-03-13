from behave import given, when, then


@given('Open amazon product {amazon_product} page')
def open_amazon_pp(context, amazon_product):
    context.app.product_page.open_product_page(amazon_product)


@when('Hover over Add to the Cart Button')
def hover_over_button(context):
    context.app.product_page.hover_over_button()


@then('Verify size tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_tooltip()
