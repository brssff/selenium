from selenium.webdriver.common.by import By


class MainPage:

    BASE_URL = 'https://demo.opencart.com/'

    CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')
    SEARCH_INPUT = (By.CSS_SELECTOR, '.form-control.input-lg')
    PHONE = (By.CSS_SELECTOR, '.fa.fa-phone')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SWIPERS = (By.CSS_SELECTOR, '.swiper-wrapper')
