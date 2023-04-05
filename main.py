import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromdriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://www.saucedemo.com")
sleep(5)
search = driver.find_element(By.ID, "user-name")
search.send_keys("standard_user")
search = driver.find_element(By.ID, "password")
search.send_keys("secret_sauce")
search = driver.find_element(By.ID, "login-button").click()
print("Login Successful!")
sleep(2)

search = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
search = driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
sleep(2)
search = driver.find_element(By.ID, "checkout").click()
sleep(2)
search = driver.find_element(By.ID, "first-name")
search.send_keys("Anees")
search = driver.find_element(By.ID, "last-name")
search.send_keys("Mufti")
search = driver.find_element(By.ID, "postal-code")
search.send_keys("123456")
sleep(2)
search = driver.find_element(By.ID, "continue").click()
sleep(2)
search = driver.find_element(By.ID, "finish").click()
sleep(2)
search = driver.find_element(By.ID, "back-to-products").click()
sleep(2)
print("Purchase Complete!")