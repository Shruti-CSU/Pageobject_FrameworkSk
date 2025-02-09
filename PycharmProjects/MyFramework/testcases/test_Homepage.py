import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

import TestData.HomepageData
from TestData import HomepageData
from TestData.HomepageData import HomapageData
from pageObjects import ExcelDemo
from pageObjects.ExcelDemo import exceldemo
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import openpyxl


class TestHomepage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["name"])
        homepage.getname().send_keys(getData["name"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(getData["passcode"])
        homepage.getcheck().click()
        sel = Select(homepage.getgender())
        sel.select_by_visible_text("Male")
        homepage.getradio().click()
        homepage.getsubmit().click()

        alertText = homepage.getsucessmessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

        print(alertText)

    #@pytest.fixture(params=HomapageData.test_homepage_data)
    #def getData(self, request):
        #return request.param

    @pytest.fixture(params=[{"name": "shruti", "email": "s1@gmail.com", "passcode": "000"},
                          {"name": "sk", "email": "s2@gmail.com", "passcode": "111"}])
    def getData(self, request):
        return request.param

    #Error in below block
    @pytest.fixture(params=exceldemo.getTestData("TestCase2"))
    def getData(self, request):
        return request.param






