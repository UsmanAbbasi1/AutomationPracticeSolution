from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.base_url = 'http://automationpractice.com/'
        self.driver = driver
