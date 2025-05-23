from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").click()
title = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
assert title == "Sauce Labs Bolt T-Shirt"
print("Product details test passed.")
driver.quit()