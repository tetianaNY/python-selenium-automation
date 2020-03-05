from behave import given, when, then
from time import sleep

@when('Click on hamburger menu')
def humburger_menu(context):
    context.app.main_page.open_hamburger_menu()

@when('Click on Amazon Music menu item')
def hamburger_music_submenu(context):
    context.app.main_page.open_hamburger_submenu()
    sleep(3)

@then('{expected} menu items are present')
def six_menu_items(context, expected):
    context.app.results_page.verify_six_menu_items(expected)