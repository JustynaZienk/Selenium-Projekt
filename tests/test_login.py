
from test_data.login_data import LoginData


class TestLogin:


    def test_wrong_password(self,home_page):

        log_in_page = home_page.click_log_in()
        log_in_page.enter_username(LoginData.USERNAME)
        log_in_page.click_login_btn()
        expected_error = "Please fill out Username and Password."
        actual_error = log_in_page.get_error_alert()
        assert expected_error in actual_error

    def test_logged_successfully(self,home_page):

        log_in_page = home_page.click_log_in()
        log_in_page.enter_username(LoginData.USERNAME)
        log_in_page.enter_password(LoginData.PASSWORD)
        log_in_page.click_login_btn()

        assert home_page.is_user_logged_in()





