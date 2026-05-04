import unittest
from time import sleep

from selenium import webdriver

from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
