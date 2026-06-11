
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    """
    Locators for Nokia Lumia 1520 Page
    """
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
class NokiaLumia1520(BasePage):
    """
    Nokia Lumia S6 Page Object
    """
    def click_add_to_cart(self):
        self.click(Locators.ADD_TO_CART)

    def click_product_added_alert(self):
        self.accept_alert()