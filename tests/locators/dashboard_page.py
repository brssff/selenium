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
    SAVE_BUTTON = (By.CSS_SELECTOR, ".fa.fa-save")
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name1")
    DESCRIPTION_TEXT_AREA = (By.CSS_SELECTOR, ".note-editable.panel-body")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")

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

    # добавление нового продукта
    def add_new_product(self):
        self.browser.find_element(*self.ADD_BUTTON).click()
        self.wait_element(self.SAVE_BUTTON)
        self.browser.find_element(*self.INPUT_NAME).clear()
        self.browser.find_element(*self.INPUT_NAME).send_keys('Test product')
        self.browser.find_element(*self.DESCRIPTION_TEXT_AREA).send_keys('Test text')
        self.browser.find_element(*self.META_TAG_TITLE_INPUT).send_keys('test-tag')
        self.browser.find_element(*self.SAVE_BUTTON).click()
        self.wait_element(self.WARNING_MSG)
