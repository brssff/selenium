from allure import description, title
from pages.login_page import LoginPage


@title("Проверка всех элементов на странице")
@description("Проверяем страницу логина на наличие всех элементов")
def test_login_page_has_all_elements(browser):
    LoginPage(browser).check_elements_exist()


@title("Переход на страницу регистрации")
@description("Проверяем возможность перехода на страницу регистрации")
def test_can_redirect_to_register_page(browser):
    LoginPage(browser).nav_to_register_page()
