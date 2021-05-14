from ..helper import assert_element
from .locators.CardPage import CardPage

URL = 'https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49'


def test_product_card(browser):
    browser.get(URL)
    browser.find_element(*CardPage.LOGO)
    browser.find_element(*CardPage.HEADER)
    browser.find_element(*CardPage.QUANTITY)
    browser.find_element(*CardPage.THUMBNAILS)
    browser.find_element(*CardPage.FOOTER)

    # добавить товар в корзину и получить сообщение об успешном действии
    browser.find_element(*CardPage.ADD_TO_CART).click()
    assert_element('.alert.alert-success.alert-dismissible', browser, timeout=2)
