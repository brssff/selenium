from selenium.webdriver.common.by import By
from .base_page import BasePage
import random


class DashboardPage(BasePage):

    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_SECTION = (By.PARTIAL_LINK_TEXT, "Products")
    ADD_BUTTON = (By.CSS_SELECTOR, ".fa.fa-plus")
    TRASH_BUTTON = (By.CSS_SELECTOR, ".fa.fa-trash-o")
    TABLE_CHECKBOX = (By.CSS_SELECTOR, "table.table-bordered.table-hover [type='checkbox']")
    WARNING_MSG = (By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")

    # навигация к странице с продуктами
    def nav_to_products_page(self):
        self.browser.find_element(*self.MENU_CATALOG).click()
        self.wait_element(self.PRODUCTS_SECTION)
        self.browser.find_element(*self.PRODUCTS_SECTION).click()

    # выбор случайного чекбокса (кроме общего) и удаление продукта
    def delete_random_product(self):
        checkboxes = len(self.browser.find_elements(*self.TABLE_CHECKBOX))
        self.browser.find_elements(*self.TABLE_CHECKBOX)[random.randint(1, checkboxes)].click()
        self.browser.find_element(*self.TRASH_BUTTON).click()
        self.browser.switch_to_alert().accept()
        assert self.browser.find_element(*self.WARNING_MSG)

    def add_new_product(self):
        pass
