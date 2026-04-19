from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.nokia_lumia_1520 import NokiaLumia1520
from pages.samsung_galaxy_s6_page import SamsungGalaxyS6


class Locators:
    """
    Locators for phone page
    """
    SAMSUNG_GALAXY_S6=(By.LINK_TEXT, "Samsung galaxy s6")
    NOKIA_LUMIA_1520= (By.LINK_TEXT, "Nokia lumia 1520")
class PhonePage(BasePage):
    """
    Phone Page Object
    """
    def click_samsung_galaxyS6(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.SAMSUNG_GALAXY_S6)).click()
        return SamsungGalaxyS6(self.driver)
    def click_nokia_lumia_1520(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.NOKIA_LUMIA_1520)).click()
        return NokiaLumia1520(self.driver)