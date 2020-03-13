from behave import given, when, then


@given('Open Amzn main page')
def open_amazon_main(context):
    context.app.main_page.open_p()


@when('Select {option} options')
def hover_over_button(context, option):
    context.app.main_page.select_search_category(option)


@when('Looking for {search}')
def search(context, search):
    context.app.main_page.search_product(search)


@then('Our searching will be in {category} category')
def verify_tooltip_shown(context, category):
    context.app.results_page.verify_department_header_result(category)