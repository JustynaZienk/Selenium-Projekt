from test_data.registration_data import RegistrationDataGenerator

class TestRegistration:

    def test_no_username(self, create_account_page):
        data = RegistrationDataGenerator()

        create_account_page.enter_password(data.PASSWORD)
        create_account_page.click_signup()
        expected_error= "Please fill out Username and Password."
        actual_error = create_account_page.get_error_alert()
        assert expected_error == actual_error

    def test_no_password(self,create_account_page):
        data = RegistrationDataGenerator()
        create_account_page.enter_username(data.USERNAME)
        create_account_page.click_signup()
        expected_error= "Please fill out Username and Password."
        actual_error = create_account_page.get_error_alert()
        assert expected_error == actual_error