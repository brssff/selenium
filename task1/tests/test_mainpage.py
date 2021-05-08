import pytest

BASE_URL = 'https://demo.opencart.com/'
CSS_SELECTORS = ['.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle', '.form-control.input-lg',
                 '.swiper-wrapper', '.fa.fa-phone', '#logo']


@pytest.mark.parametrize('selector', CSS_SELECTORS)
def test_main_page(browser, selector):
    browser.get(BASE_URL)
    assert browser.find_element_by_css_selector(selector)
