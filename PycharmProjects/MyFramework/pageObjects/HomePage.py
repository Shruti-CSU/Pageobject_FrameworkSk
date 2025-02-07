from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    empradio = (By.ID, "inlineRadio1")
    submit = (By.XPATH, "//input[@value='Submit']")
    sucessmessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)  # * will deserialize tuple from shop object
        #driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getcheck(self):
        return self.driver.find_element(*HomePage.check)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def getradio(self):
        return self.driver.find_element(*HomePage.empradio)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsucessmessage(self):
        return self.driver.find_element(*HomePage.sucessmessage)










