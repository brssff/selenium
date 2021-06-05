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

    def check_elements_exist(self):
        self.browser.open(LoginPage.PATH)
        self.wait_element(LoginPage.BREADCRUMBS)
        self.wait_element(LoginPage.CONTINUE_BTN)
        self.wait_element(LoginPage.LOGIN_BTN)
        self.wait_element(LoginPage.RIGHT_COLUMN)
        self.wait_element(LoginPage.LOGO)
        self.wait_element(LoginPage.HEADER)
        self.wait_element(LoginPage.FOOTER)

    def redirect_to_register_page(self):
        self.browser.open(self.PATH)
        self.browser.find_element(*self.CONTINUE_BTN).click()
        assert self.browser.title == 'Register Account'
