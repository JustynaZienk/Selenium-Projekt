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
        self.driver.find_element(*Locators.NAME).send_keys(name)
    def enter_country(self, country):
        self.driver.find_element(*Locators.COUNTRY).send_keys(country)
    def enter_city(self, city):
        self.driver.find_element(*Locators.CITY).send_keys(city)
    def enter_creditcard(self, creditcard):
        self.driver.find_element(*Locators.CREDIT_CARD).click()
    def enter_month(self, month):
        self.driver.find_element(*Locators.MONTH).send_keys(month)
    def enter_year(self, year):
        self.driver.find_element(*Locators.YEAR).send_keys(year)
    def click_purchase_btn(self):
        self.driver.find_element(*Locators.PURCHASE_BTN).click()
    def get_error_alert(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

