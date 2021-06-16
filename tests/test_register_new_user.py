from allure import description, title
from pages.login_page import LoginPage
from pages.register_account_page import RegisterAccount


@title("Регистрация нового пользователя")
@description("Переходим на страницу регистрации и создаем нового пользователя")
def test_register_new_user(browser):
    LoginPage(browser).nav_to_register_page()
    RegisterAccount(browser).fill_inputs_and_register()
