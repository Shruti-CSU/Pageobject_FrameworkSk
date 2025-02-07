from selenium.webdriver.common.by import By


class ConfirmPage:

    CountyName = (By.ID, "country")
    SelectCountry = (By.LINK_TEXT, "India")
    CheckboxSelect = (By.CSS_SELECTOR, ".checkbox-primary")
    PurchaseClick = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    Success = (By.CLASS_NAME, "alert-success")


    def __init__(self, driver):
        self.driver = driver

    def EnterName(self):
        return self.driver.find_element(*ConfirmPage.CountyName)

    def SelectName(self):
        return self.driver.find_element(*ConfirmPage.SelectCountry)

    def ClickCheckbox(self):
        return self.driver.find_element(*ConfirmPage.CheckboxSelect)

    def ClickonPurchase(self):
        return self.driver.find_element(*ConfirmPage.PurchaseClick)

    def SuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.Success)