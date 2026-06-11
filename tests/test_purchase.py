

import pytest
import test_data.place_order_data



class TestPurchase:

    def test_one_item_in_cart(self,cart_with_item):


        cart_page = cart_with_item.click_cart()

        names = cart_page.get_product_names()

        assert "Samsung galaxy s6" in names



    def test_one_item_price(self,cart_with_item):
        cart_page = cart_with_item.click_cart()
        prices=cart_page.get_product_prices()

        expected_result=360

        assert expected_result in prices

    def test_two_items_in_cart(self, cart_with_two_items):


        cart_page = cart_with_two_items.click_cart()

        names = cart_page.get_product_names()

        assert "Samsung galaxy s6" in names
        assert "Nokia lumia 1520" in names

    def test_total_price_two_items(self, cart_with_two_items):


        cart_page = cart_with_two_items.click_cart()


        prices = cart_page.get_product_prices()


        assert sum(prices) == cart_page.get_total_price()



    @pytest.mark.parametrize(
        "scenario,name,country,city,creditcard,month,year,expected_error",
        test_data.place_order_data.get_csv_data("test_data/orderData.csv")
    )
    def testPlaceOrder(self, cart_with_item,scenario,name, country, city, creditcard, month, year,expected_error):

        cart_page = cart_with_item.click_cart()
        place_order_page=cart_page.click_place_order()

        place_order_page.enter_name(name)
        place_order_page.enter_country(country)
        place_order_page.enter_city(city)
        place_order_page.enter_creditcard(creditcard)
        place_order_page.enter_month(month)
        place_order_page.enter_year(year)

        place_order_page.click_purchase_btn()


        actual_error= place_order_page.get_error_alert()


        assert expected_error == actual_error




