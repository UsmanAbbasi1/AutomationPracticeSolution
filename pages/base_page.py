from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        self.base_url = 'http://automationpractice.com/'
        # Make sure to add chromedriver path in 'PATH' env var
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
