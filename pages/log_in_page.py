from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Locators:
    """
    Locators for login page
    """
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")
    LOGIN_BTN= (By.XPATH, "//button[@onclick='logIn()']")
    LOGIN_WINDOW=(By.ID, "logInModal")

class LoginPage(BasePage):
    """
    Login Page object
    """

    def enter_username(self, username):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.USERNAME))

        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.PASSWORD))
        element.clear()
        element.send_keys(password)

    def click_login_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BTN)
        )
        element.click()


    def get_error_alert(self):
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text

    def click_login_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
    def _verify_page(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BTN))


