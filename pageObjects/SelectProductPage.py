from selenium.webdriver.common.by import By


class SelectProductPage:

    def __init__(self, driver):
        self.driver = driver

    LinkClick = (By.XPATH, "//a[@href='http://practice.automationtesting.in/']")
    SelectPro = (By.XPATH, "//a[@href='https://practice.automationtesting.in/product/mastering-javascript/']")
    AddToCart = (By.XPATH, "//button[@type='submit']")
    ViewBasket = (By.XPATH, "//a[@class='button wc-forward']")
    Total = (By.XPATH, "//tr[@class='order-total']")
    CBasket = (By.XPATH, "//input[@inputmode='numeric']")
    AddAgain = (By.XPATH, "//input[@inputmode='numeric']")
    UpdateBasket = (By.XPATH, "//input[@name='update_cart']")
    FinalTotal = (By.XPATH, "//tr[@class='order-total']")

    def linkclick(self):
        return self.driver.find_element(*SelectProductPage.LinkClick)

    def selectpro(self):
        return self.driver.find_element(*SelectProductPage.SelectPro)

    def addtocart(self):
        return self.driver.find_element(*SelectProductPage.AddToCart)

    def viewbasket(self):
        return self.driver.find_element(*SelectProductPage.ViewBasket)

    def total(self):
        return self.driver.find_element(*SelectProductPage.Total)

    def cbasket(self):
        return self.driver.find_element(*SelectProductPage.CBasket)

    def addagain(self):
        return self.driver.find_element(*SelectProductPage.AddAgain)

    def updatebasket(self):
        return self.driver.find_element(*SelectProductPage.UpdateBasket)

    def pagescroll(self):
        return self.driver.execute_script("window.scrollBy(0, 500);")

    def finaltotal(self):
        return self.driver.find_element(*SelectProductPage.FinalTotal)
