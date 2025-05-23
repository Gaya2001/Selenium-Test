from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("✅ Logged in successfully")
time.sleep(2)

# Wait for products to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))


# Open sidebar menu
driver.find_element(By.ID, "react-burger-menu-btn").click()
print("📂 Sidebar menu opened")
time.sleep(2)

# Click About link
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "about_sidebar_link")))
driver.find_element(By.ID, "about_sidebar_link").click()
print("🔗 Clicked on 'About' link")
time.sleep(3)

# Wait until redirected
WebDriverWait(driver, 10).until(lambda d: "sauce" in d.current_url.lower())
print("🌐 Redirected to:", driver.current_url)

# Verify URL
assert "saucelabs.com" in driver.current_url, "❌ Redirection failed"
print("✅ About page redirection test passed!")

# Final pause to observe
time.sleep(3)
driver.quit()
