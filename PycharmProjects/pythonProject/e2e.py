# This is from video part 66

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(4)
driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

PList = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for phone in PList:
    phoneName = phone.find_element(By.XPATH, "div/h4/a").text
    if phoneName == "Blackberry":
        phone.find_element(By.XPATH, "div/button").click()

# * in xpath will allow any one class to reach to the element
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
success = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in success