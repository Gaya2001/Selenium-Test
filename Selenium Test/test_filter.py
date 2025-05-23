from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait to let the page load
time.sleep(2)

# Wait for inventory items to appear
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

# Select "Name (Z to A)" from sort dropdown
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_visible_text("Name (Z to A)")

# Get list of product names
product_names = [elem.text for elem in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

# Check if names are sorted Z to A
assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z to A"
print("Product sorting (Z to A) passed.")

# Pause to see result
time.sleep(3)
driver.quit()
