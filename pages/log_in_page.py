from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Locators:
    """
    Locators for login page
    """
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BTN= (By.XPATH, "//button[@onclick='logIn()']")

class LoginPage(BasePage):
    """
    Login Page object
    """

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BTN))

        self.driver.find_element(*Locators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*Locators.LOGIN_BTN).click()

    def get_error_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

    def click_login_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
    def _verify_page(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BTN))


