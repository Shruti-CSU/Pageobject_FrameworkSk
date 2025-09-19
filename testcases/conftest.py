import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
# To run in specific browser you need to run command like py.test --browser_name firefox

# Practice Test 1
@pytest.fixture(scope="class")
def invokebrowser(request):

    browser_name = request.config.getoption("browser_name") # This will get the value  of browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":  #elif means else if
        driver = webdriver.Firefox()
    elif browser_name == "IE":  # elif means else if
        print("IE driver code")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

# Practice Test 2
@pytest.fixture(scope="class")
def lunchbrowser(request):

    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Index.html")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

# Practice Test 3
@pytest.fixture(scope="class")
def PracticeTest1(request):

    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Index.html")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()