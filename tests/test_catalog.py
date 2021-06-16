import allure
from pages.catalog_page import CatalogPage


@allure.title("Страница каталога")
def test_catalog_page(browser):

    with allure.step("Проверить наличие элементов на странице"):
        CatalogPage(browser).check_elements_exist_on_page()

    with allure.step("Проверить количество Thumbs на странице"):
        CatalogPage(browser).check_product_thumbs()
