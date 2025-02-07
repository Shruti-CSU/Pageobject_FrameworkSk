import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# this find.elements is pural which shows list of country
ListC = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(ListC))

# in entire list for loop will find exact county and make a click
for county in ListC:
    if county.text == "India":
        county.click()
        break

# this will print selected values of dropdown
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
