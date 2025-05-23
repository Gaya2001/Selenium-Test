from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Wait a bit before logging in
time.sleep(1)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("✅ Logged in")
time.sleep(2)

# Wait for main inventory page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

# Open sidebar
driver.find_element(By.ID, "react-burger-menu-btn").click()
print("📂 Sidebar opened")
time.sleep(2)

# Click logout
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
driver.find_element(By.ID, "logout_sidebar_link").click()
print("🚪 Clicked logout")
time.sleep(2)

# Wait for login button to appear again
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
print("✅ Successfully logged out")

# Final pause before closing
time.sleep(3)
driver.quit()
