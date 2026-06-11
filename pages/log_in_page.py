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
        """
        Enter username
        """
        self.type(Locators.USERNAME, username)

    def enter_password(self, password):
        """
        Enter password
        """
        self.type(Locators.PASSWORD, password)

    def click_login_btn(self):
        """
        Click login button
        """
        self.click(Locators.LOGIN_BTN)

    def get_error_alert(self):
        """
        Get alert text
        """
        return self.get_alert_text()

    def click_login_alert(self):
        """
        Accept alert
        """
        self.accept_alert()

    def _verify_page(self):
        """
        Verify login button is visible
        """
        self.is_visible(Locators.LOGIN_BTN)


