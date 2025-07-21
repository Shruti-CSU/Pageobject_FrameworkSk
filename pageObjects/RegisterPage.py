from selenium.webdriver.common.by import By

class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    EmailAdd = (By.ID, "email")
    EnterClick = (By.ID, "enterimg")

    def AddEmail(self):
        return self.driver.find_element(*RegisterPage.EmailAdd)

    def EnterB(self):
        return  self.driver.find_element(*RegisterPage.EnterClick)



