from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Fill login details
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait to let the page load
time.sleep(2)

# Check result (optional assertion)
if "inventory.html" in driver.current_url:
    print("✅ TC01: Login successful ")

time.sleep(10)

# Close the browser
driver.quit()