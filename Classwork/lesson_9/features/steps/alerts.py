from behave import given, when, then


@given('Open Amazon main page')
def open_page(context):
    context.app.main_page.open_p()


@when('Alert is open')
def hover_over_button(context):
    context.app.alerts.create_alert()


@then('We can close Alert')
def verify_tooltip_shown(context):
    context.app.alerts.close_alert()


@when('Confirm is open')
def hover_over_button(context):
    context.app.alerts.create_confirm()
