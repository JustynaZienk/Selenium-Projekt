from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    Locators for phone page
    """
    SAMSUNG_GALAXY_S6=(By.LINK_TEXT, "Samsung galaxy s6")

class PhonePage(BasePage):
    """
    Phone Page Object
    """
    def click_samsung_galaxyS6(self):
        self.driver.find_element(*Locators.SAMSUNG_GALAXY_S6).click()