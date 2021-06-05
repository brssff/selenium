from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.form-control.input-lg')
    PHONE = (By.CSS_SELECTOR, '.fa.fa-phone')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SWIPERS = (By.CSS_SELECTOR, '.swiper-wrapper')

    # внезапно это не селектор, а кнопка
    CURRENCY_SELECTOR = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    EUR = (By.CSS_SELECTOR, '.currency-select.btn.btn-link.btn-block[name="EUR"]')
    GBP = (By.CSS_SELECTOR, '.currency-select.btn.btn-link.btn-block[name="GBP"]')
    USD = (By.CSS_SELECTOR, '.currency-select.btn.btn-link.btn-block[name="USD"]')
    CURRENCY_STATE = (By.TAG_NAME, 'strong')

    def check_elements_exist(self):
        self.browser.find_element(*MainPage.CART_BUTTON)
        self.browser.find_element(*MainPage.SEARCH_INPUT)
        self.browser.find_element(*MainPage.PHONE)
        self.browser.find_element(*MainPage.LOGO)

    def count_swipers(self):
        assert len(self.browser.find_elements(*MainPage.SWIPERS)) == 2

    def check_currencies(self):
        self.browser.find_element(*self.CURRENCY_SELECTOR).click()

    def select_pound(self):
        self.check_currencies()
        self.browser.find_element(*self.EUR).click()
        assert self.browser.find_element(*self.CURRENCY_STATE).text == '€'
        return self

    def select_euro(self):
        self.check_currencies()
        self.browser.find_element(*self.GBP).click()
        assert self.browser.find_element(*self.CURRENCY_STATE).text == '£'
        return self

    def select_usd(self):
        self.check_currencies()
        self.browser.find_element(*self.USD).click()
        assert self.browser.find_element(*self.CURRENCY_STATE).text == '$'
        return self
