from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

List1 = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(List1))

# this is for checkbox
for checkbox in List1:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

print("Test ended for checkbox button with option 2")
# this is for radio button
List2 = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")

print(len(List2))

for radio in List2:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break

print("Test ended for radio button with option 3")

# this is for text box appernce once we click on box

# This assertion will validation that text box should be visible
assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()

# now after clicking on button text box will not visible
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# assert not use when condition intentionaly goes fail such as above case 