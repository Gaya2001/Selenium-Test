from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login-button").click()

time.sleep(1)
error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
assert "Username and password do not match" in error
print("✅ TC04: Invalid login shows proper error")

time.sleep(10)

driver.quit()
