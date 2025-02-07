import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("invokeBrowser")
class Testone(BaseClass):

    def test_e2e01(self):

        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

        PList = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for phone in PList:
            phoneName = phone.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                phone.find_element(By.XPATH, "div/button").click()

        # * in xpath will allow any one class to reach to the element
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in success