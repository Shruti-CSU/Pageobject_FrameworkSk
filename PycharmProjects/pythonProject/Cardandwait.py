import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# this implicite wait will apply in each case to wait for given time
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

VeggieList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(VeggieList))
count = len(VeggieList)

for cart in VeggieList:
    cart.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Validation a sum of total and total amount is eqaul or not

LTotal = driver.find_elements(By.XPATH, "//tr/td[5]/p")

sum = 0
for amount in LTotal:
    sum = sum + int(amount.text)  # we will be getting amount as string and we need int to sum so use int(str)

print(sum)

SubTotal = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == SubTotal

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# this explisite wait will apply for only one particular case

Exwait = WebDriverWait(driver,5)
Exwait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


# adding validation that after applying promocode Total discount sould be less than actual amount

print(sum)

# used float to store decimal values 
DiscountP = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

print(DiscountP)

assert sum > DiscountP