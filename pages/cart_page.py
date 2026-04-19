from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Locators:
    """
    Locators for CartPage
    """
    PRODUCT_NAME =(By.XPATH,"//td[2]")
    PRODUCT_PRICE =(By.XPATH,"//td[3]")
class CartPage(BasePage):
    """
    Page object for CartPage
    """
    def get_product_names(self):
        products=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(Locators.PRODUCT_NAME))
        return [product.text for product in products]
    def get_product_prices(self):
        prices=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(Locators.PRODUCT_PRICE))
        return [int(price.text) for price in prices]