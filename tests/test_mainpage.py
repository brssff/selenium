from pages.main_page import MainPage


def test_main_page(browser):
    MainPage(browser).check_elements_exist()


# поочередное переключение валюты + проверка их верного отображения
def test_change_currencies(browser):
    MainPage(browser).select_pound().select_usd().select_euro()
