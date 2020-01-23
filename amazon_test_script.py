from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

# open the url
driver.get('https://www.amazon.com')

search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_button = driver.find_element(By.XPATH, "//div[@id='nav-search']//input[@class='nav-input'][@value='Go']")
search.clear()
search.send_keys('lego')
sleep(1)
search_button.click()

assert 'lego' in driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-small a-spacing-top-small']//span[text()='\"lego\"']").text

driver.quit()


