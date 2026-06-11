

import pytest
from selenium import webdriver

from pages.home_page import HomePage
from test_data.login_data import LoginData

BASE_URL = "https://demoblaze.com/"
@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver   

    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def create_account_page(driver):
    home_page = HomePage(driver)
    return home_page.click_sign_up()


@pytest.fixture
def logged_in_user(home_page):
    log_in_page = home_page.click_log_in()

    log_in_page.enter_username(LoginData.USERNAME)
    log_in_page.enter_password(LoginData.PASSWORD)
    log_in_page.click_login_btn()
    home_page.is_user_logged_in()
    return home_page

@pytest.fixture
def cart_with_item(logged_in_user):

    phone = logged_in_user.click_phones()
    samsung = phone.click_samsung_galaxyS6()

    samsung.click_add_to_cart()
    samsung.click_product_added_alert()

    yield logged_in_user





@pytest.fixture
def cart_with_two_items(logged_in_user):
    phone = logged_in_user.click_phones()
    samsung = phone.click_samsung_galaxyS6()

    samsung.click_add_to_cart()
    samsung.click_product_added_alert()
    logged_in_user.click_product_store()
    nokia= phone.click_nokia_lumia_1520()
    nokia.click_add_to_cart()
    nokia.click_product_added_alert()

    yield logged_in_user





