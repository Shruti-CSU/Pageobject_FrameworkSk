import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# ID, Name, Classname, XPath, Cssselector, linktext are types of locators

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "name").send_keys("Shruti")
driver.find_element(By.NAME, "email").send_keys("shruti@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()


# Xpath syntax -> //tagname[@attributes='value'] -> //input[@value='Submit']
# CSS syntax -> tagname[attributes='value'], #id, .classname

driver.find_element(By.XPATH, "//input[@value='Submit']").click()

# Radio button selection
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Drop down selection
Dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
Dropdown.select_by_visible_text("Female")
Dropdown.select_by_index(1)

SuccessMessage = driver.find_element(By.CLASS_NAME, "alert ").text
print(SuccessMessage)
assert "Success!" in SuccessMessage

driver.find_element(By.CLASS_NAME, "ng-pristine").send_keys("Hello")
driver.find_element(By.XPATH, "//input[@type='text']").clear()


time.sleep(2)
driver.close()