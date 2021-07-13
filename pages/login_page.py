import allure
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@allure.suite("Страница логина пользователя")
class LoginPage(BasePage):
    PATH = 'index.php?route=account/login'

    LOGO = (By.CSS_SELECTOR, '#logo')
    HEADER = (By.CSS_SELECTOR, '#top')
    FOOTER = (By.CSS_SELECTOR, 'footer')
    BREADCRUMBS = (By.CSS_SELECTOR, '.breadcrumb')
    CONTINUE_BTN = (By.CSS_SELECTOR, '.btn.btn-primary[href]')
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn.btn-primary[type]')
    RIGHT_COLUMN = (By.CSS_SELECTOR, '#column-right')

    @allure.step("Перейти на страницу регистрации")
    def nav_to_register_page(self):
        logging.info("Navigating to register page")
        self.browser.open(self.PATH)

        with allure.step("Кликнуть кнопку Continue"):
            self.browser.find_element(*self.CONTINUE_BTN).click()

    @allure.title("Проверка наличия всех элементов на странице")
    def check_elements_exist(self):
        self.browser.open(LoginPage.PATH)
        logging.info("Starting wait for all elements exist on: {}".format(self.browser.current_url))
        self.wait_element(LoginPage.BREADCRUMBS)
        self.wait_element(LoginPage.CONTINUE_BTN)
        self.wait_element(LoginPage.LOGIN_BTN)
        self.wait_element(LoginPage.RIGHT_COLUMN)
        self.wait_element(LoginPage.LOGO)
        self.wait_element(LoginPage.HEADER)
        self.wait_element(LoginPage.FOOTER)
        logging.info("All elements exist on: {}".format(self.browser.current_url))
