from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

# open the url
driver.get('https://www.amazon.com')
sleep(2)
search_button = driver.find_element(By.XPATH, "//div[@id='nav-tools']//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
search_button.click()

# Sign in page present with a Sign in button
search_email = driver.find_element(By.XPATH, "//div[@class='a-row a-spacing-base']//input[@type='email']")
search_continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")

driver.close()
