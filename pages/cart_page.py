import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.place_order_page import PlaceOrderPage


class Locators:
    """
    Locators for CartPage
    """
    PRODUCT_NAME =(By.XPATH,"//tr/td[2]")
    PRODUCT_PRICE =(By.XPATH,"//td[3]")
    PLACE_ORDER_BTN= (By.XPATH,"//button[@class='btn btn-success']")
    CART_BTN= (By.ID,"cartur")
class CartPage(BasePage):
    """
    Page object for CartPage
    """
    def get_product_names(self):
        products=self.find_all(Locators.PRODUCT_NAME)
        return [product.text for product in products]
    def get_product_prices(self):
        prices=self.find_all(Locators.PRODUCT_PRICE)
        return [int(price.text) for price in prices]

    def get_total_price(self):
        return sum(self.get_product_prices())

    def click_place_order(self):
        self.click(Locators.PLACE_ORDER_BTN)
        return PlaceOrderPage(self.driver)
    def click_cart_btn(self):
        self.click(Locators.CART_BTN)






