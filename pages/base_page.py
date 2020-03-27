from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.base_url = 'http://automationpractice.com/'
        self.driver = driver
