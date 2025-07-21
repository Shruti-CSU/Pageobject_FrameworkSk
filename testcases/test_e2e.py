# This is from video part 86
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import ExcelDemo
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class Testone(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        HomeTest = HomePage(self.driver)
        CheckoutTest = CheckoutPage(self.driver)
        ConfirmTest = ConfirmPage(self.driver)

        self.driver.implicitly_wait(4)
        HomeTest.shopItems().click()

        log.info("Getting all cart items")
        PList = CheckoutTest.GetProductList()
        log.info("This is final items")

        for phone in PList:
            phoneName = phone.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                phone.find_element(By.XPATH, "div/button").click()

                log.info("found blackberry and added in cart")

        CheckoutTest.ClickonCheckout().click()
        CheckoutTest.FinalCheckout().click()
        ConfirmTest.EnterName().send_keys("ind")

        self.waitforlinkpresence("India")
        
        ConfirmTest.SelectName().click()
        ConfirmTest.ClickCheckbox().click()
        ConfirmTest.ClickonPurchase().click()
        success = ConfirmTest.SuccessMessage().text

        assert "Success! Thank you!" in success

