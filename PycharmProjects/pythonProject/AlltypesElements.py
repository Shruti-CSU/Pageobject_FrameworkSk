import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.implicitly_wait(2)

print(driver.find_element(By.XPATH, "//legend[text()='Radio Button Example']").text)
driver.find_element(By.XPATH, "//input[@value='radio3']").click()
assert driver.find_element(By.XPATH, "//input[@value='radio3']").is_selected()

print(driver.find_element(By.XPATH, "//legend[text()='Suggession Class Example']").text)
driver.find_element(By.ID, "autocomplete").send_keys("Uni")
CountyList = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item-wrapper")
print(len(CountyList))

for county in CountyList:
    if county.text == "United Arab Emirates":
        county.click()

# assert "United Arab Emirates" == Auto

print(driver.find_element(By.XPATH, "//legend[text()='Dropdown Example']").text)
driver.find_element(By.XPATH, "//option[@value='option2']").click()
assert driver.find_element(By.XPATH, "//option[@value='option2']").is_selected()

print(driver.find_element(By.XPATH, "//legend[text()='Checkbox Example']").text)
driver.find_element(By.ID, "checkBoxOption2").click()
assert driver.find_element(By.ID, "checkBoxOption2").is_selected()

print(driver.find_element(By.CLASS_NAME, "switch-tab").text)
driver.find_element(By.ID, "opentab").click()

NW = driver.window_handles
driver.switch_to.window(NW[1])
print(driver.title)
driver.close()

driver.switch_to.window(NW[0])
print(driver.title)

print(driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']").text)
driver.find_element(By.ID, "name").send_keys("Test")
driver.find_element(By.ID, "alertbtn").click()

A1 = driver.switch_to.alert
A1.accept()

print(driver.find_element(By.XPATH, "//legend[text()='Element Displayed Example']").text)
driver.find_element(By.ID, "hide-textbox").click()

driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.ID, "displayed-text").is_displayed()

print(driver.find_element(By.XPATH, "//legend[text()='Mouse Hover Example']").text)

# This will just hover on elements
hover1 = ActionChains(driver)
hover1.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#This will do right click on element
hover1.context_click(driver.find_element(By.LINK_TEXT, "Reload")).perform()

print("This is to scroll the page")
# window.scrollBy(0, 500) use this syntax in consol of browser to set scroll limit
# as the above syntax in javascript, will run this javas in python
driver.execute_script("window.scrollBy(0, 500);")  #add ; at the end as per js

# for screenshot
driver.get_screenshot_as_file("name.png")

# handle iframe
print(driver.find_element(By.XPATH, "//legend[text()='iFrame Example']").text)
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT, "Courses").click()
driver.switch_to.default_content()
driver.close()
