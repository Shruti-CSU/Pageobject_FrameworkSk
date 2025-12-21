import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Practice04 import Practice04
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("openbrowser")
class TestPracticeT4(BaseClass):

    def test_practice4(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 10)
        HoverButton = Practice04(self.driver)

        HoverButton.SkinCareHover().perform()
        HoverButton.SelectEyeB().click()
        HoverButton.SelectProduct().click()
        log.info("This is the selection of SubProduct")
        ProductPrice = HoverButton.TotalPrice().text
        assert "$89.00" in ProductPrice

        HoverButton.SelectSubProduct()
        log.info("This is the changes of product")
        Prices = HoverButton.TotalPrice().text
        assert "$38.00" in Prices
        log.info("This is the updated price of the product")




