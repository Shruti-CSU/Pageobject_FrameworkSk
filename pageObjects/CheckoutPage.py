from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    ProductList = (By.XPATH, "//div[@class='card h-100']")
    CheckoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    Checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def GetProductList(self):
        return self.driver.find_elements(*CheckoutPage.ProductList)

    def ClickonCheckout(self):
        return self.driver.find_element(*CheckoutPage.CheckoutButton)

    def FinalCheckout(self):
        return self.driver.find_element(*CheckoutPage.Checkout)


