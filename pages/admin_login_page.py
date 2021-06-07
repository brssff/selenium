import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    URL = 'https://demo.opencart.com/admin/'

    LOGO = (By.CSS_SELECTOR, '#header-logo')
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.help-block')
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn.btn-primary')
    FOOTER = (By.CSS_SELECTOR, '#footer')

    def open(self, url):
        return self.browser.get(url)

    def log_in(self):
        logging.info("Opening page: {}".format(self.URL))
        self.open(self.URL)
        logging.info("Inputting credentials for user")
        self.browser.find_element(*self.USERNAME).clear()
        self.browser.find_element(*self.USERNAME).send_keys("demo")
        self.browser.find_element(*self.PASSWORD).clear()
        self.browser.find_element(*self.PASSWORD).send_keys("demo")
        self.browser.find_element(*self.LOGIN_BTN).click()
        logging.info("Checking if log in was success")
        assert self.browser.title == 'Dashboard'
        assert 'user_token' in self.browser.current_url
        logging.info("Login success")
