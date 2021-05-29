from selenium.webdriver.common.by import By
from .base_page import BasePage


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
        self.open(self.URL)
        self.browser.find_element(*self.USERNAME).clear()
        self.browser.find_element(*self.USERNAME).send_keys("demo")
        self.browser.find_element(*self.PASSWORD).clear()
        self.browser.find_element(*self.PASSWORD).send_keys("demo")
        self.browser.find_element(*self.LOGIN_BTN).click()
        assert self.browser.title == 'Dashboard'
        assert 'user_token' in self.browser.current_url
