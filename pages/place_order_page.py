from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    Locators for place order page
    """
    NAME= (By.XPATH,"//input[@id='name']")
    COUNTRY= (By.XPATH,"//input[@id='country']")
    CITY= (By.XPATH,"//input[@id='city']")
    CREDIT_CARD= (By.XPATH,"//input[@id='card']")
    MONTH= (By.XPATH,"//input[@id='month']")
    YEAR= (By.XPATH,"//input[@id='year']")
    PURCHASE_BTN = (By.XPATH,"//button[@onclick='purchaseOrder()']")

class PlaceOrderPage(BasePage):
    """
    PlaceOrderPage Object
    """
    def enter_name(self, name):
        self.type(Locators.NAME, name)
    def enter_country(self, country):
        self.type(Locators.COUNTRY, country)
    def enter_city(self, city):
        self.type(Locators.CITY, city)
    def enter_creditcard(self, creditcard):
        self.type(Locators.CREDIT_CARD, creditcard)
    def enter_month(self, month):
        self.type(Locators.MONTH, month)
    def enter_year(self, year):
        self.type(Locators.YEAR, year)
    def click_purchase_btn(self):
        self.click(Locators.PURCHASE_BTN)
    def get_error_alert(self):
        return self.get_alert_text()

