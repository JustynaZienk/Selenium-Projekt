
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class Locators:
    """
    CreateAccountPage locators
    """

    USERNAME = (By.ID, "sign-username")
    PASSWORD = (By.ID, "sign-password")
    SIGN_UP = (By.XPATH, "//button[@onclick= 'register()']")
class CreateAccountPage(BasePage):
    """
    Sign up pop_up window object
    """


    def enter_username(self, username):
        """
        enter username
        """
        self.type(Locators.USERNAME, username)
    def enter_password(self, password):
        """
        enter password
        """
        self.type(Locators.PASSWORD, password)
    def click_signup(self):
        self.click(Locators.SIGN_UP)


    def get_error_alert(self):
        return self.get_alert_text()

    def click_signup_alert(self):
        self.accept_alert()

    def _verify_page(self):
        """
        Check if sing up page exists
        """
        self.is_visible(Locators.SIGN_UP)


