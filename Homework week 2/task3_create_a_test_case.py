from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)


# open the url
# no help button on amazon.com
# driver.get('https://www.amazon.com')
# sleep(2)
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.XPATH, "//div[@class='a-row']//input[@type='search']")
search.clear()
search.send_keys('cancel order')
driver.find_element(By.XPATH, "//div[@class='a-column a-span2 a-span-last']//input[@class='a-button-input']").click()

assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='a-box a-spacing-extra-large a-color-offset-background answer-box']").text

driver.quit()
