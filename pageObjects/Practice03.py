

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities import BaseClass


class Practice03:

    def __init__(self, driver):
        self.driver = driver

    SkipSign = (By.ID, "btn2")
    HoverClick = (By.XPATH, "//a[@href='SwitchTo.html']")
    AlertClick = (By.XPATH, "//a[@href='Alerts.html']")
    DisplayButton = (By.CSS_SELECTOR, ".btn-danger")
    AlertOk = (By.ID, "OKTab")
    AlertCancelButton = (By.XPATH, "//button[@class='btn btn-primary']")
    CancelTab = (By.XPATH, "//a[@href='#CancelTab']")
    CancelM = (By.ID, "demo")
    TextButton = (By.XPATH, "//a[@href='#Textbox']")
    TextB1Click = (By.XPATH, "//button[@class='btn btn-info']")
    Sucessmsg = (By.ID, "demo1")

    def SkipButton(self):
        return self.driver.find_element(*Practice03.SkipSign)
    def HoverEle(self):
        hover1 = ActionChains(self.driver)
        element = self.driver.find_element(*Practice03.HoverClick)
        return hover1.move_to_element(element)

    def AlertEle(self):
        return self.driver.find_element(*Practice03.AlertClick)

    def WaitforEle(self):
        W1 = WebDriverWait(self.driver, 10)
        W1.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".btn-danger")))

    def ButtonClick(self):
        return self.driver.find_element(*Practice03.DisplayButton)

    def Alertpop(self):
        alert = self.driver.switch_to.alert
        return alert

    def AlerttoCancel(self):
        return self.driver.find_element(*Practice03.CancelTab)

    def CancelMsg(self):
        return self.driver.find_element(*Practice03.CancelM)

    def AlertCBClick(self):
        return self.driver.find_element(*Practice03.AlertCancelButton)

    def TaxtBClick(self):
        return self.driver.find_element(*Practice03.TextButton)

    def TextBC1(self):
        return self.driver.find_element(*Practice03.TextB1Click)

    def FinalMsg(self):
        return self.driver.find_element(*Practice03.Sucessmsg)






