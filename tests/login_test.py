from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from pages.home_page import HomePage
from test_data.registration_data import RegistrationDataGenerator
from tests.base_test import BaseTest


class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.create_account_page = self.home_page.click_sign_up()

    def testWrongPassword(self):
        self.create_account_page.enter_username(self.data.USERNAME)
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.click_signup()
        self.create_account_page.click_signup_alert()
        self.log_in_page = self.home_page.click_log_in()
        self.log_in_page.enter_username(self.data.USERNAME)
        self.log_in_page.click_login_btn()
        sleep(3)
        expected_error = "Please fill out Username and Password."
        actual_error = self.log_in_page.get_error_alert()
        self.assertEqual(expected_error, actual_error)

    def test_user_logged_in_successfully(self):

        self.create_account_page.enter_username(self.data.USERNAME)
        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.click_signup()
        self.create_account_page.click_signup_alert()
        self.log_in_page = self.home_page.click_log_in()
        self.log_in_page.enter_username(self.data.USERNAME)
        self.log_in_page.enter_password(self.data.PASSWORD)
        self.log_in_page.click_login_btn()
        sleep(4)
        self.assertTrue(self.home_page.is_user_logged_in())





