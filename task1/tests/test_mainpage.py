import pytest
from ..helper import assert_element

BASE_URL = 'https://demo.opencart.com/'
CSS_SELECTORS = ['.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle', '.form-control.input-lg',
                 '.swiper-wrapper', '.fa.fa-phone', '#logo']


@pytest.mark.parametrize('selector', CSS_SELECTORS)
def test_main_page(browser, selector):
    browser.get(BASE_URL)
    assert_element(selector, browser)
