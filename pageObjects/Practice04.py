import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Practice04:

    def __init__(self, driver):
        self.driver = driver

    SKincareH = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=43']")
    EyeC = (By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=product/category&path=43_47']")
    EyeProduct = (By.XPATH, "//a[@title='Absolue Eye Precious Cells']")
    ProductList = (By.XPATH, "//a[@class='productname']")
    PPrice = (By.XPATH, "//span[@class='total-price']")

    def SkinCareHover(self):
        SkinHover = ActionChains(self.driver)
        hover01 = self.driver.find_element(*Practice04.SKincareH)
        return SkinHover.move_to_element(hover01)

    def SelectEyeB(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable(self.EyeC))

    def SelectProduct(self):
        return self.driver.find_element(*Practice04.EyeProduct)

    def SelectSubProduct(self):
        PList = self.driver.find_elements(*Practice04.ProductList)
        print(PList)
        for product in PList:
            if product.text == "Total Moisture Facial Cream":
                product.click()
                break
        return

    def TotalPrice(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located(Practice04.PPrice)
        )















