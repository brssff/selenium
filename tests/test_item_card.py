import allure
from pages.card_page import CardPage


@allure.title("Добавление нового продукта в корзину")
@allure.description("Проверяем наличие элементов на странице и добавляем продукт в корзину")
def test_product_card(browser):
    CardPage(browser).check_elements_exist()
    CardPage(browser).add_to_cart()
