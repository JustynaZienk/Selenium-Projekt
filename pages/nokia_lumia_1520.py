
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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.ADD_TO_CART)).click()

    def click_product_added_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()