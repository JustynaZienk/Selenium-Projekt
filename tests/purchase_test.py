from selenium.webdriver.support.wait import WebDriverWait

from test_data.registration_data import RegistrationDataGenerator
from tests.base_test import BaseTest


class PurchaseTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()

    def testAddedItemToCart(self):
        self.create_account_page = self.home_page.click_sign_up()
        self.create_account_page.enter_username(self.data.USERNAME)
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.click_signup()
        self.create_account_page.click_signup_alert()
        self.log_in_page = self.home_page.click_log_in()
        self.log_in_page.enter_username(self.data.USERNAME)
        self.log_in_page.enter_password(self.data.PASSWORD)
        self.log_in_page.click_login_btn()
        self.phone_page = self.home_page.click_phones()
        self.phone_page.click_samsung_galaxyS6()
