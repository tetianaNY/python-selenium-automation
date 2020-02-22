# Sam

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver, timeout=10)

driver.get('https://www.google.com')
driver.implicitly_wait(5)



search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

driver.find_element(By.NAME, 'btnK').click()

assert 'Dress' in driver.find_element(By.XPATH, '//div[contains(@class, "commercial-unit-desktop-top")]').text
assert 'Dress' in driver.find_element(By.XPATH, '//div[@class="g"]').text

driver.quit()


