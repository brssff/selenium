from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from faker import Faker


class RegisterAccount(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "[type='checkbox']")
    CONTINUE = (By.CSS_SELECTOR, ".btn.btn-primary")

    def fill_inputs_and_register(self):
        faker = Faker()
        self.clear_n_paste(self.FIRST_NAME, "Ivan")
        self.clear_n_paste(self.LAST_NAME, "Snow")
        # если часто будут падать тесты с повторяющимся email, можно timestamp привязать
        self.clear_n_paste(self.EMAIL, faker.email())
        self.clear_n_paste(self.TELEPHONE, "+79990001117")
        self.clear_n_paste(self.PASSWORD, "Ww777111999")
        self.clear_n_paste(self.PASSWORD_CONFIRM, "Ww777111999")
        self.browser.find_element(*self.AGREE_CHECKBOX).click()
        self.browser.find_element(*self.CONTINUE).click()
        # TODO: как будет время, изменить на проверку через успешный логаут, а не тайтл
        assert self.browser.title == 'Your Account Has Been Created!'
