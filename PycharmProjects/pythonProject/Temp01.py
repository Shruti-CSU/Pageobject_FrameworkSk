from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()

d.get("https://rahulshettyacademy.com/client/auth/register")

d.find_element(By.CLASS_NAME, "login-wrapper-footer-text").click()