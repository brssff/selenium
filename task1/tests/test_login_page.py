import pytest
from ..helper import assert_element

URL = 'https://demo.opencart.com/index.php?route=account/login'
CSS_SELECTORS = ['.breadcrumb', '.btn.btn-primary[href]', '.btn.btn-primary[type]',
                 '#column-right', '#logo', '#top', 'footer']


@pytest.mark.parametrize('selectors', CSS_SELECTORS)
def test_login_page(browser, selectors):
    browser.get(URL)
    assert_element(selectors, browser)


def test_can_redirect_to_register_page(browser):
    browser.find_element_by_css_selector('.btn.btn-primary[href]').click()
    assert 'route=account/register' in browser.current_url
