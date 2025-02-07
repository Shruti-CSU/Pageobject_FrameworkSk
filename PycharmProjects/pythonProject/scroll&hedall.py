from selenium import webdriver

driver = webdriver.Chrome()

# THis is to run chrome in backgroud without visibility
Obj1 = webdriver.ChromeOptions()
Obj1.add_argument("headless")

# This is to ignore ssl certificate error

Obj1.add_argument("--ignore-certificate-errors")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# this will scroll the window by 500 and for this in chrome browser in console write window.scrollby(0, value)
driver.execute_script("window.scrollBy(0, 500);")

# to take a screenshot of last previous execure screen
driver.get_screenshot_as_file("screen1.png")