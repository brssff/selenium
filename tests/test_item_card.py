from pages.card_page import CardPage


def test_product_card(browser):
    CardPage(browser).check_elements_exist()
    CardPage(browser).add_to_cart()
