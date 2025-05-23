from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

assert driver.find_element(By.ID, "user-name").is_displayed()
assert driver.find_element(By.ID, "password").is_displayed()
assert driver.find_element(By.ID, "login-button").is_displayed()

print("✅ TC03: All UI elements are visible and enabled")

time.sleep(10)

driver.quit()
