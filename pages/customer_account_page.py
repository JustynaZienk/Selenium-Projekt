from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class Locators:
    """Locators for customer account page"""
    PHONES_BTN = (By.XPATH, "//a[@onclick= 'byCat('phone')']")

class CustomerAccountPage(BasePage):
    """
    Customer account object
    """

    def add_item_to_cart(self):
        """
        Add item to cart
        """
        self.driver.find_element(*Locators.PHONES).click()