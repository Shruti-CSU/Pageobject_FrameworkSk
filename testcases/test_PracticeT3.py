import time

from pageObjects.Practice03 import Practice03
from utilities.BaseClass import BaseClass


class TestPracticeT3(BaseClass):

    def test_practice03A(self):
        log = self.getLogger()

        SkipTest = Practice03(self.driver)
        HoverTest = Practice03(self.driver)

        SkipTest.SkipButton().click()
        HoverTest.HoverEle().perform()
        HoverTest.AlertEle().click()
        HoverTest.WaitforEle()
        HoverTest.ButtonClick().click()
        HoverTest.Alertpop().accept()
        HoverTest.AlerttoCancel().click()
        HoverTest.AlertCBClick().click()
        time.sleep(2)
        HoverTest.Alertpop().dismiss()
        print(HoverTest.CancelMsg().text)
        HoverTest.TaxtBClick().click()
        HoverTest.TextBC1().click()
        HoverTest.Alertpop().send_keys("Hello")
        time.sleep(2)
        HoverTest.Alertpop().accept()
        print(HoverTest.FinalMsg().text)




