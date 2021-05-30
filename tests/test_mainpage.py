from tests.pages.main_page import MainPage


def test_main_page(browser):
    browser.get(MainPage.BASE_URL)
    browser.find_element(*MainPage.CART_BUTTON)
    browser.find_element(*MainPage.SEARCH_INPUT)
    browser.find_element(*MainPage.PHONE)
    browser.find_element(*MainPage.LOGO)
    assert len(browser.find_elements(*MainPage.SWIPERS)) == 2

"""
Научиться реализовывать PageObject шаблон в автотестах.

V Переписать уже имеющиеся тесты в проекте opencart на PageObject паттерн.

Добавить автотесты на следующие сценарии.
    Добавление нового товара в разделе администратора.
    Удаление товара из списка в разделе администартора.
    Регистрация нового пользователя в магазине опенкарта.
    Переключение валют из верхнего меню опенкарта.
"""