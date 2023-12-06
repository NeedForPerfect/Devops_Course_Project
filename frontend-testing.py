import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chromeDriver = webdriver.Chrome()
chromeDriver.get('http://localhost:4200')
chromeDriver.implicitly_wait(1)


editFirstUserBtn = chromeDriver.find_element(By.ID, value="edit-btn-1")
editFirstUserBtn.click()

editUserInput = chromeDriver.find_element(By.ID, value="edit-user-input")
time.sleep(1)
print('First User Input value IS - ', editUserInput.get_attribute('value'))

chromeDriver.quit()