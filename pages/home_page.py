from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.create_account_page import CreateAccountPage
from pages.log_in_page import LoginPage
from pages.phone_page import PhonePage


class Locators:
    """
     Home Page elements locators
     """
    SIGN_UP = (By.ID, "signin2")
    LOG_IN = (By.ID, 'login2')
    LOGGED_IN = (By.ID, 'nameofuser')
    PHONES = (By.XPATH,"//a[contains(@onclick,'phone')]" )
    CART = (By.ID, "cartur")
    PRODUCT_STORE_BTN =(By.XPATH,'//a[@class="navbar-brand"]')
    CART_2BTN = (By.XPATH, "//a[@onclick='showcart()']")

class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_sign_up(self):
        """
        Click sign up button and displays SIGN UP pop-up window
        """

        self.click(Locators.SIGN_UP)
        return CreateAccountPage(self.driver)

    def click_log_in(self):
        """
        Click login button and displays LOGIN pop-up window
        """
        self.click_body()
        self.click(Locators.LOG_IN)

        return LoginPage(self.driver)

    def is_user_logged_in(self):
        """
        Check if user logged in
        """
        return self.is_visible(Locators.LOGGED_IN)

    def click_phones(self):
        """
        Click phone button and displays available PHONES
        """
        self.click(Locators.PHONES)
        return PhonePage(self.driver)


    def click_cart(self):
        self.click(Locators.CART)
        return CartPage(self.driver)

    def click_cart_btn(self):
        self.click(Locators.CART_2BTN)
        return CartPage(self.driver)
    def click_product_store(self):
        self.click(Locators.PRODUCT_STORE_BTN)

    def _verify_page(self):
        self.is_visible(Locators.SIGN_UP)