import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    __driver = None

    @classmethod
    def setUpClass(cls):
        cls.__driver = webdriver.Chrome()
        cls.__driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.__driver.quit()

    @property
    def driver(self):
        return self.__driver
