# Tried to use different ways to find locators

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

# open the url
driver.get('https://www.amazon.com')
sleep(2)
search_button = driver.find_element(By.CSS_SELECTOR, "div.nav-signin-tooltip-footer a.nav-a")
search_button.click()
sleep(2)

# Amazon logo
search_logo = driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-medium.a-text-center i.a-icon.a-icon-logo")

# "Create account" title
search_create_account_title = driver.find_element(By.CSS_SELECTOR, "div.a-box-inner h1.a-spacing-small")
assert 'Create account' in driver.find_element(By.CSS_SELECTOR, "div.a-box-inner h1.a-spacing-small").text

# Your name field
search_your_name_field = driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12.auth-autofocus.auth-required-field.auth-contact-verification-request-info")

# E-mail field
search_email_field = driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password field
search_password_field = driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password check field
search_password_check_field = driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# "Create your Amazon account" button
search_create_account = driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions of use link
search_conditions_of_use = driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy notice link
search_privacy_notice = driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Sign-in link
search_sign_in = driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")

driver.quit()
