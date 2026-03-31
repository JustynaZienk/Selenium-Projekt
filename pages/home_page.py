from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.create_account_page import CreateAccountPage
from pages.log_in_page import LoginPage


class Locators:
    """
     Home Page elements locators
     """
    SIGN_UP = (By.ID, "signin2")
    LOG_IN = (By.ID, 'login2')
    LOGGED_IN = (By.ID, 'nameofuser')
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

    def click_log_in(self):
        """
        Click log in button and displays LOGIN pop-up window

        """
        self.driver.find_element(*Locators.LOG_IN).click()
        return LoginPage(self.driver)

    def is_user_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGGED_IN)).is_displayed()
        return True

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.title_is("STORE"))