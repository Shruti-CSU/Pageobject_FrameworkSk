from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("Shruti")
driver.find_element(By.XPATH, "//input[@value='Alert']").click()

A1 = driver.switch_to.alert
alertText = A1.text
print(alertText)

assert "Shruti" in alertText # This assertion check Shruti word in alert popup
A1.accept()  # use to click on ok from alert popup
# A1.dismiss()  user to click on cancel from alert popup