import pytest

from ..helper import assert_element

URL = 'https://demo.opencart.com/admin/'
CSS_SELECTORS = ['#header-logo', '#input-username', '#input-password', '.help-block', '.btn.btn-primary', '#footer']


@pytest.mark.parametrize('selector', CSS_SELECTORS)
def test_login_admin_page(browser, selector):
    browser.get(URL)
    assert_element(selector, browser)


def test_ability_to_log_in(browser):
    browser.get(URL)
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    assert 'user_token' in browser.current_url
    assert browser.title == 'Dashboard'
    assert_element('.fa.fa-sign-out', browser)
