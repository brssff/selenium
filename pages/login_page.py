from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = 'index.php?route=account/login'

    LOGO = (By.CSS_SELECTOR, '#logo')
    HEADER = (By.CSS_SELECTOR, '#top')
    FOOTER = (By.CSS_SELECTOR, 'footer')
    BREADCRUMBS = (By.CSS_SELECTOR, '.breadcrumb')
    CONTINUE_BTN = (By.CSS_SELECTOR, '.btn.btn-primary[href]')
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn.btn-primary[type]')
    RIGHT_COLUMN = (By.CSS_SELECTOR, '#column-right')

    def nav_to_register_page(self):
        self.browser.open(self.PATH)
        self.browser.find_element(*self.CONTINUE_BTN).click()
