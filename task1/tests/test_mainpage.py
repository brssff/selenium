from ..helper import assert_element

BASE_URL = 'https://demo.opencart.com/'


def test_main_page(browser):
    browser.get(BASE_URL)
    assert_element('.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle', browser)
    assert_element('.form-control.input-lg', browser)
    assert_element('.swiper-wrapper', browser)
    assert_element('.fa.fa-phone', browser)
    assert_element('#logo', browser)
