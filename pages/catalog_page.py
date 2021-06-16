import allure
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@allure.suite("Страница каталога товаров")
class CatalogPage(BasePage):
    PATH = 'index.php?route=product/category&path=20'

    LOGO = (By.CSS_SELECTOR, '#logo')
    CATALOG_COLUMN = (By.CSS_SELECTOR, '#column-left')
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search')
    PRODUCT_THUMB = (By.CSS_SELECTOR, '.product-thumb')
    LIST_VIEW = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW = (By.CSS_SELECTOR, '#grid-view')
    SORT_BY = (By.CSS_SELECTOR, '#input-sort')
    SHOW_LIMIT = (By.CSS_SELECTOR, '#input-limit')
    FOOTER = (By.CSS_SELECTOR, 'footer .container')

    def check_elements_exist_on_page(self):
        browser = self.browser
        browser.open(self.PATH)
        browser.find_element(*self.LOGO)
        browser.find_element(*self.CATALOG_COLUMN)
        browser.find_element(*self.SEARCH_INPUT)
        browser.find_element(*self.LIST_VIEW)
        browser.find_element(*self.GRID_VIEW)
        browser.find_element(*self.SORT_BY)
        browser.find_element(*self.SHOW_LIMIT)
        browser.find_element(*self.FOOTER)

    def check_product_thumbs(self):
        logging.info("Checking if all product thumbs exist on page")
        product_thumbs = self.browser.find_elements(*CatalogPage.PRODUCT_THUMB)

        with allure.step("На странице 12 thumbnails"):
            assert len(product_thumbs) == 12, \
                f"Thumbs on page: {len(product_thumbs)}, but 12 expected"
