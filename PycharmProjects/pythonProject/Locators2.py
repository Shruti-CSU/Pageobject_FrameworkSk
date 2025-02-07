import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome()

driver1.get("https://rahulshettyacademy.com/client")
driver1.find_element(By.XPATH, "//p[@class='login-wrapper-footer-text']").click()
driver1.find_element(By.ID, "firstName").send_keys("shruti")
driver1.find_element(By.CSS_SELECTOR, "#lastName").send_keys("patel")
driver1.find_element(By.ID, "userEmail").send_keys("shruti+3@gmail.com")
driver1.find_element(By.CSS_SELECTOR, "#userMobile").send_keys("9874565412")
driver1.find_element(By.ID, "userPassword").send_keys("Test@1234")
driver1.find_element(By.ID, "confirmPassword").send_keys("Test@1234")
driver1.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver1.find_element(By.ID, "login").click()  # will click on Register button
driver1.find_element(By.LINK_TEXT, "Login here").click() #will click on login here button
driver1.find_element(By.ID, "login").send_keys("shruti+1@gmail.com")
driver1.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("Test@1234")
driver1.find_element(By.ID, "login").click()

time.sleep(2)