from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage


class Locators:
    """
     Home Page elements locators
     """
    SIGN_UP = (By.ID, "signin2")
class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_sign_up(self):
        """
        Click sign up button and displays SIGN UP pop-up window
        """

        self.driver.find_element(*Locators.SIGN_UP).click()
        return CreateAccountPage(self.driver)