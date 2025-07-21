import time

from selenium import webdriver

from pageObjects.BillingPage import BillingPage
from pageObjects.RegisterPage import RegisterPage
from pageObjects.SelectProductPage import SelectProductPage
from pageObjects.SignupPage import SignupPage
from utilities.BaseClass import BaseClass




class TestTwo(BaseClass):

    def test_mye2e(self):
        log = self.getLogger()
        RegTest = RegisterPage(self.driver)
        SignupTest = SignupPage(self.driver)
        SelectProductTest = SelectProductPage(self.driver)
        BillingPageTest = BillingPage(self.driver)

        RegTest.AddEmail().send_keys("shrutik@gmail.com")
        RegTest.EnterB().click()

        log.info("Signup Sucessfully")

        SignupTest.firstname().send_keys("Shruti")
        SignupTest.lastname().send_keys("Soni")
        SignupTest.address().send_keys("1700 E 13th ST, 44114")
        SignupTest.email().send_keys("shrutik@gmail.com")
        SignupTest.phonenum().send_keys("216-456-6374")
        SignupTest.gender().click()
        #assert SignupTest.gender().click().selected()
        SignupTest.hobbies().click()
        SignupTest.skills().click()
        SignupTest.year().click()
        SignupTest.month().click()
        SignupTest.date().click()
        SignupTest.password().send_keys("Test@123")
        SignupTest.cpassword().send_keys("Test@123")
        SignupTest.submitbutton().click()
        SignupTest.refreshbutton().click()

        log.info("Register Sucessfully")

        SelectProductTest.linkclick().click()
        SelectProductTest.selectpro().click()
        SelectProductTest.addtocart().click()
        SelectProductTest.viewbasket().click()
        Tamount = SelectProductTest.total().text
        #assert "₹357.00" in Tamount
        SelectProductTest.cbasket().clear()
        SelectProductTest.addagain().send_keys("2")
        SelectProductTest.updatebasket().click()
        SelectProductTest.pagescroll()
        FinalAmount = SelectProductTest.finaltotal().text
        #assert "₹714.00" in FinalAmount

        time.sleep(3)
        BillingPageTest.checkoutc().click()
        BillingPageTest.bfirstn().send_keys("Shruti")
        BillingPageTest.blastn().send_keys("Soni")
        BillingPageTest.pagescroll()
        BillingPageTest.bemail().send_keys("shrutis1@gmail.com")
        BillingPageTest.bphone().send_keys("2164566378")
        BillingPageTest.badd1().send_keys("1700 E 13th ST")
        BillingPageTest.badd2().send_keys("APT E 22Q")
        BillingPageTest.bcity().send_keys("Cleveland")
        BillingPageTest.bpost().send_keys("365630")
        BillingPageTest.pagescroll()
        CheckTotal = BillingPageTest.btotal().text
        print(CheckTotal)
        #BillingPageTest.bpayment().click()
        BillingPageTest.pagescroll()
        BillingPageTest.border().click()
        time.sleep(3)
        FinalMsg = BillingPageTest.sucmsg().text
        assert "Thank you. Your order has been received." in FinalMsg
        print(FinalMsg)










