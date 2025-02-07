from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

WNames = driver.window_handles
driver.switch_to.window(WNames[1])

UserName = driver.find_element(By.XPATH, "//a[@href='mailto:mentor@rahulshettyacademy.com']").text
driver.close()

driver.switch_to.window(WNames[0])

driver.find_element(By.ID, "username").send_keys(UserName)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
driver.find_element(By.ID, "signInBtn").click()

Exwait = WebDriverWait(driver, 10)
Exwait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))

print(driver.find_element(By.CLASS_NAME, "alert-danger").text)