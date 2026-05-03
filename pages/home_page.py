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
        self.driver.find_element(By.TAG_NAME, "body").click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Locators.LOG_IN)
        )

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.LOG_IN)
        )

        element.click()
        return LoginPage(self.driver)

    def is_user_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.LOGGED_IN)).is_displayed()
        return True

    def click_phones(self):
        """
        Click phone button and displays available PHONES
        """
        wait = WebDriverWait(self.driver, 10)

        for i in range(5):
            try:
                phones = wait.until(EC.element_to_be_clickable(Locators.PHONES))
                phones.click()
                return PhonePage(self.driver)
            except StaleElementReferenceException:
                continue

        raise Exception("Unabale to click phone button")

    def click_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.CART)).click()
        return CartPage(self.driver)

    def click_product_store(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.PRODUCT_STORE_BTN)).click()

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(EC.title_is("STORE"))