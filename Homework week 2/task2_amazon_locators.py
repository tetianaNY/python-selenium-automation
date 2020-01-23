from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

# open the url
driver.get('https://www.amazon.com')
search_button = driver.find_element(By.XPATH, "//div[@id='nav-signin-tooltip']//a[@class='nav-action-button'][@data-nav-role='signin']")
sleep(2)
search_button.click()


# Amazon logo
search_logo = driver.find_element(By.XPATH, "//div[@id='a-page']//i[@class='a-icon a-icon-logo'][@role='img']")

# Email field
search_email = driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']//input[@type='email']")

# Continue button
search_continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")

# Need help link
search_need_h_link = driver.find_element(By.XPATH, "//div[@class='a-section']//span[@class='a-expander-prompt']")

# Forgot your password link
# Other issues with sign-in link
# "Create your Amazon account" button
search_create_account = driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Conditions of use link
search_conditions_of_use = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privace notice link
search_privace_notice = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")


driver.quit()
