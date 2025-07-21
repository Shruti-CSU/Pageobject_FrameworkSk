from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    FirstName = (By.XPATH, "//input[@placeholder='First Name']")
    LastName = (By.XPATH, "//input[@placeholder='Last Name']")
    Address = (By.XPATH, "//textarea[@ng-model]")
    Email = (By.XPATH, "//input[@type='email']")
    PhoneNum = (By.XPATH, "//input[@type='tel']")
    Gender = (By.XPATH, "//input[@type='radio']")
    Hobbies = (By.ID, "checkbox2")
    Skills = (By.XPATH, "//select/option[@value='APIs']")
    Year = (By.XPATH, "//select/option[@value='1924']")
    Month = (By.XPATH, "//select/option[@value='May']")
    Date = (By.XPATH, "//select/option[@value='10']")
    Password = (By.ID, "firstpassword")
    CPassword = (By.ID, "secondpassword")
    SubmitB = (By.ID, "submitbtn")
    RefreshB = (By.ID, "Button1")

    def firstname(self):
        return self.driver.find_element(*SignupPage.FirstName)

    def lastname(self):
        return self.driver.find_element(*SignupPage.LastName)

    def address(self):
        return self.driver.find_element(*SignupPage.Address)

    def email(self):
        return self.driver.find_element(*SignupPage.Email)

    def phonenum(self):
        return self.driver.find_element(*SignupPage.PhoneNum)

    def gender(self):
        return self.driver.find_element(*SignupPage.Gender)

    def hobbies(self):
        return self.driver.find_element(*SignupPage.Hobbies)

    def skills(self):
        return self.driver.find_element(*SignupPage.Skills)

    def year(self):
        return self.driver.find_element(*SignupPage.Year)

    def month(self):
        return self.driver.find_element(*SignupPage.Month)

    def date(self):
        return self.driver.find_element(*SignupPage.Date)

    def password(self):
        return self.driver.find_element(*SignupPage.Password)

    def cpassword(self):
        return self.driver.find_element(*SignupPage.CPassword)

    def submitbutton(self):
        return self.driver.find_element(*SignupPage.SubmitB)

    def refreshbutton(self):
        return self.driver.find_element(*SignupPage.RefreshB)