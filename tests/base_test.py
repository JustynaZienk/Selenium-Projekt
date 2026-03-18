import unittest
from time import sleep

from selenium import webdriver


class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        sleep(3)

    def tearDown(self):
        self.driver.quit()
