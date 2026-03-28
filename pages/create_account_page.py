from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.PASSWORD))
        self.driver.find_element(*Locators.USERNAME).send_keys(username)
    def enter_password(self, password):
        """
        enter password
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.PASSWORD))
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_signup(self):
        self.driver.find_element(*Locators.SIGN_UP).click()


    def get_error_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text



