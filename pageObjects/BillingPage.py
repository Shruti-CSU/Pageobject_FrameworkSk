from selenium.webdriver.common.by import By


class BillingPage:

    def __init__(self, driver):
        self.driver = driver

    CheckoutC = (By.XPATH, "//a[@href='https://practice.automationtesting.in/checkout/']")
    BFirstN = (By.ID, "billing_first_name")
    BLastN = (By.XPATH, "//input[@name='billing_last_name']")
    BEmail = (By.XPATH, "//input[@name='billing_email']")
    BPhone = (By.ID, "billing_phone")
    BAdd1 = (By.ID, "billing_address_1")
    BAdd2 = (By.ID, "billing_address_2")
    BCity = (By.ID, "billing_city")
    BPost = (By.ID, "billing_postcode")
    BTotal = (By.XPATH, "//tr[@class='order-total']")
    BPayment = (By.XPATH, "//input[@id='payment_method_cod']")
    BOrder = (By.ID, "place_order")
    SucMsg = (By.XPATH, "//p[@class='woocommerce-thankyou-order-received']")

    def checkoutc(self):
        return self.driver.find_element(*BillingPage.CheckoutC)

    def bfirstn(self):
        return self.driver.find_element(*BillingPage.BFirstN)

    def blastn(self):
        return self.driver.find_element(*BillingPage.BLastN)

    def pagescroll(self):
        return self.driver.execute_script("window.scrollBy(0, 500);")

    def bemail(self):
        return self.driver.find_element(*BillingPage.BEmail)

    def bphone(self):
        return self.driver.find_element(*BillingPage.BPhone)

    def badd1(self):
        return self.driver.find_element(*BillingPage.BAdd1)

    def badd2(self):
        return self.driver.find_element(*BillingPage.BAdd2)

    def bcity(self):
        return self.driver.find_element(*BillingPage.BCity)

    def bpost(self):
        return self.driver.find_element(*BillingPage.BPost)

    def btotal(self):
        return self.driver.find_element(*BillingPage.BTotal)

    def bpayment(self):
        return self.driver.find_element(*BillingPage.BPayment)

    def border(self):
        return self.driver.find_element(*BillingPage.BOrder)

    def sucmsg(self):
        return self.driver.find_element(*BillingPage.SucMsg)