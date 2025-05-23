from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add to cart
driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']//button").click()

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Verify item in cart
item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
assert "Sauce Labs Backpack" in item
print("✅ TC02: Item added to cart successfully")

time.sleep(10)

driver.quit()
