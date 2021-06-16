import allure, allure
from pages.main_page import MainPage


@allure.description("Проверка наличия всех элементов")
def test_main_page(browser):
    MainPage(browser).check_elements_exist()


# поочередное переключение валюты + проверка их верного отображения
@allure.title("Переключение валют")
@allure.description("Выполняем поочередное переключение всех доступных валют")
def test_change_currencies(browser):
    MainPage(browser).select_pound().select_usd().select_euro()
