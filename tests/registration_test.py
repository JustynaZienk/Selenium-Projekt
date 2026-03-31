from test_data.registration_data import RegistrationDataGenerator
from tests.base_test import BaseTest



class RegistrationTest(BaseTest):


    def setUp(self):
        super(). setUp()
        self.data= RegistrationDataGenerator()
        self.create_account_page = self.home_page.click_sign_up()



    def testNoUsername(self):

        self.create_account_page.enter_password(self.data.PASSWORD)
        self.create_account_page.click_signup()
        expected_error= "Please fill out Username and Password."
        actual_error = self.create_account_page.get_error_alert()
        self.assertEqual(expected_error, actual_error)

    def testNoPassword(self):

        self.create_account_page.enter_username(self.data.USERNAME)
        self.create_account_page.click_signup()
        expected_error= "Please fill out Username and Password."
        actual_error = self.create_account_page.get_error_alert()
        self.assertEqual(expected_error, actual_error)