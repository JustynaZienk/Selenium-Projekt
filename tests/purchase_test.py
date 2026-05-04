import time
from time import sleep

from selenium.webdriver.common import alert
from selenium.webdriver.support.wait import WebDriverWait

import test_data.place_order_data
from test_data.products_in_cart import Products, Prices
from test_data.registration_data import RegistrationDataGenerator
from tests.base_test import BaseTest
from ddt import ddt, data, unpack

@ddt
class PurchaseTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = RegistrationDataGenerator()
        self.product_name= Products()
        self.product_price = Prices()

    def testAddedOneItemToCart(self):
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
        self.samsung_galaxy_s6_page=self.phone_page.click_samsung_galaxyS6()
        self.samsung_galaxy_s6_page.click_add_to_cart()
        self.samsung_galaxy_s6_page.click_product_added_alert()
        self.cart_page=self.home_page.click_cart()
        expected_result=self.product_name.SINGLE_PRODUCT_IN_CART[0]
        actual_result= self.cart_page.get_product_names()
        self.assertIn(expected_result, actual_result)

    def testOneItemPrice(self):
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
        self.samsung_galaxy_s6_page = self.phone_page.click_samsung_galaxyS6()
        self.samsung_galaxy_s6_page.click_add_to_cart()
        self.samsung_galaxy_s6_page.click_product_added_alert()
        self.cart_page = self.home_page.click_cart()
        expected_result=self.product_price.SAMSUNG_GALAXY_S6_PRICE[0]
        actual_result= self.cart_page.get_product_prices()
        self.assertIn(expected_result, actual_result)

    def testAddedTwoItemToCart(self):
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
        self.samsung_galaxy_s6_page = self.phone_page.click_samsung_galaxyS6()
        self.samsung_galaxy_s6_page.click_add_to_cart()
        self.samsung_galaxy_s6_page.click_product_added_alert()
        self.home_page.click_product_store()
        self.nokia_lumia_1520=self.phone_page.click_nokia_lumia_1520()
        self.nokia_lumia_1520.click_add_to_cart()
        self.nokia_lumia_1520.click_product_added_alert()
        self.cart_page = self.home_page.click_cart()
        expected_result = self.product_name.TWO_PRODUCTS_IN_CART
        actual_result = self.cart_page.get_product_names()
        self.assertEqual(sorted(expected_result), sorted(actual_result))

    def testTotalPriceTwoItems(self):
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
        self.samsung_galaxy_s6_page = self.phone_page.click_samsung_galaxyS6()
        self.samsung_galaxy_s6_page.click_add_to_cart()
        self.samsung_galaxy_s6_page.click_product_added_alert()
        self.home_page.click_product_store()
        self.nokia_lumia_1520 = self.phone_page.click_nokia_lumia_1520()
        self.nokia_lumia_1520.click_add_to_cart()
        self.nokia_lumia_1520.click_product_added_alert()
        self.cart_page = self.home_page.click_cart()
        expected_result = self.product_price.TOTAL_PRICE_SAM_NOK
        actual_result = self.cart_page.get_total_price()
        self.assertEqual(expected_result,actual_result)


    @data(*test_data.place_order_data.get_csv_data("test_data/orderData.csv"))
    @unpack
    def testPlaceOrder(self, scenario,name, country, city, creditcard, month, year):
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
        self.samsung_galaxy_s6_page = self.phone_page.click_samsung_galaxyS6()
        self.samsung_galaxy_s6_page.click_add_to_cart()
        self.samsung_galaxy_s6_page.click_product_added_alert()
        self.cart_page = self.home_page.click_cart()
        self.place_order_page=self.cart_page.click_place_order()
        #ddt
        self.place_order_page.enter_name(name)
        self.place_order_page.enter_country(country)
        self.place_order_page.enter_city(city)
        self.place_order_page.enter_creditcard(creditcard)
        self.place_order_page.enter_month(month)
        self.place_order_page.enter_year(year)
        sleep(3)
        self.place_order_page.click_purchase_btn()

        expected_error = "Please fill out Name and Creditcard."
        actual_error= self.place_order_page.get_error_alert()


        if scenario == "NoNameInPlaceOrder":
            self.assertEqual(expected_error,actual_error)
        elif scenario == "NoCreditcardInPlaceOrder":
            self.assertEqual(expected_error,actual_error)
        elif scenario == "ValidUser":
            self.assertIsNone(actual_error)




