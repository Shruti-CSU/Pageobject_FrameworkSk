from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)

ExpListVeggie = ['Cucumber - 1 Kg', 'Beetroot - 1 Kg', 'Beans - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
ActualListVeggie = []

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("be")
VeggieList = driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(VeggieList))

for Veggie in VeggieList:
    ActualListVeggie.append(Veggie.find_element(By.XPATH, "h4").text)
    Veggie.find_element(By.XPATH, "div/button").click()

assert ExpListVeggie == ActualListVeggie
print("List of serched veggies assertion is passed")

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

TotalAmount1 = driver.find_elements(By.XPATH, "//tr/td[5]/p")

# Comaparing total amount should be same as Total before discount
sum = 0
for Total1 in TotalAmount1:
    sum = sum + int(Total1.text)

print(sum)

WithDiscountA = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == WithDiscountA
print("Assertion for Amount matched before discount apply")

BefoDis = driver.find_element(By.CLASS_NAME, "discountPerc").text
print("{} {}".format("Before Discoutn %", BefoDis))

# Apply discount code

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

ExWait = WebDriverWait(driver, 10)
ExWait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# stored discount amount in float bcoz of decimal values and to compare with actual value

DiscountAppiedA = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
print(DiscountAppiedA)

AfterDis = driver.find_element(By.CLASS_NAME, "discountPerc").text
print("{} {}".format("After Discount %", AfterDis))

assert DiscountAppiedA < WithDiscountA
print("Passed assertion that actual amount should be less after applied discount")

assert AfterDis > BefoDis