import pytest

BASE_URL = 'https://www.opencart.ru/'
CSS_SELECTORS = ['#button-demo', '.btn.button-green', '.suport__link', '.login', '#cart-total-img', '.header-logo']


@pytest.mark.parametrize('selector', CSS_SELECTORS)
def test_main_page(browser, selector):
    browser.get(BASE_URL)
    assert browser.find_element_by_css_selector(selector)
