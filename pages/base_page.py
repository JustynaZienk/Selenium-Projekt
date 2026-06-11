from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base Page Object for each page
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self._verify_page()

    def find(self, locator):
        """
        Find element by locator
        """
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator):
        """
        Find all elements by locator
        """
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
    def find_all_del_btn(self,locator):
        """
        Find all delete buttons by locator
        """
        return self.driver.find_elements(*locator)
    def click(self, locator):
        """
        Click element by locator
        """

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text):
        """
        Type element by locator
        """
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get text from locator
        """
        return self.wait.until(EC.visibility_of_element_located(locator).text)

    def get_alert_text(self):
        """
        Handle alert and return its text
        """
        try:
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return "None"

    def is_visible(self, locator):
        """
        Check if element is visible
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def accept_alert(self):
        """
        Accept alert
        """
        self.wait.until(EC.alert_is_present()).accept()

    def click_body(self):
        self.driver.find_element(By.TAG_NAME, "body").click()

    def _verify_page(self):
        # site autotest
        return