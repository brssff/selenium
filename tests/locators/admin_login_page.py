from selenium.webdriver.common.by import By


class AdminLoginPage:
    URL = 'https://demo.opencart.com/admin/'

    LOGO = (By.CSS_SELECTOR, '#header-logo')
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.help-block')
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn.btn-primary')
    FOOTER = (By.CSS_SELECTOR, '#footer')

    # def wait_for_open(self, browser):
    #     browser.get(self.URL)
    # def log_in(self, browser):
    #     browser.get(self.URL)
    #     browser.find_element(self.LOGIN_BTN).click()
    #     return self


