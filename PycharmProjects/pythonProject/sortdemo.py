from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

ExpectedList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//a[text()='Top Deals']").click()

Wname = driver.window_handles
driver.switch_to.window(Wname[1])

# once we click on llist from browser it will show sorted list
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#now we will collect sorted list in list which is sorted by browser
VeggiesList = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggie in VeggiesList:
    ExpectedList.append(veggie.text)

# will again store sorted list in one variable to compare

OriginalList = ExpectedList.copy()

# Now sort this list
ExpectedList.sort()

assert OriginalList == ExpectedList


