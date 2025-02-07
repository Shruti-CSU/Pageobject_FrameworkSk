import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")  # define scope="class" will run the test once before class
def invokeBrowser(request):
    driver = webdriver.Chrome()
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--ignore-certificate-errors')
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

