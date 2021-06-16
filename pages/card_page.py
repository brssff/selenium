import allure
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@allure.suite("Страница карточки товара")
class CardPage(BasePage):
    PATH = 'index.php?route=product/product&path=57&product_id=49'
    LOGO = (By.CSS_SELECTOR, '#logo')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, '#button-cart')
    THUMBNAILS = (By.CSS_SELECTOR, '.col-sm-8 .thumbnails')
    HEADER = (By.CSS_SELECTOR, '#top')
    FOOTER = (By.CSS_SELECTOR, 'footer .container')
    SUCCESS_MSG = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

    @allure.step("Проверить наличие элементов на странице")
    def check_elements_exist(self):
        logging.info("Checking elements exist")
        browser = self.browser
        browser.open(self.PATH)
        browser.find_element(*CardPage.LOGO)
        browser.find_element(*CardPage.HEADER)
        browser.find_element(*CardPage.QUANTITY)
        browser.find_element(*CardPage.THUMBNAILS)
        browser.find_element(*CardPage.FOOTER)
        logging.info("All elements exist")

    @allure.step("Добавить товар в корзину")
    def add_to_cart(self):
        # добавить товар в корзину и получить сообщение об успешном действии
        logging.info("Adding an item to cart")
        self.browser.find_element(*CardPage.ADD_TO_CART).click()
        self.wait_element(self.SUCCESS_MSG, timeout=2)
