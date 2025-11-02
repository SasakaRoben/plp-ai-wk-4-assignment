from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Test valid credentials
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_pass")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(2)
assert "Dashboard" in driver.title

# Test invalid credentials
driver.get("https://example.com/login")
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "loginBtn").click()
time.sleep(2)
assert "Invalid" in driver.page_source

driver.quit()
