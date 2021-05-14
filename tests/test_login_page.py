from ..helper import assert_element

URL = 'https://demo.opencart.com/index.php?route=account/login'


def test_login_page(browser,):
    browser.get(URL)
    assert_element('.breadcrumb', browser)
    assert_element('.btn.btn-primary[href]', browser)
    assert_element('.btn.btn-primary[type]', browser)
    assert_element('#column-right', browser)
    assert_element('#logo', browser)
    assert_element('#top', browser)
    assert_element('footer', browser)


def test_can_redirect_to_register_page(browser):
    browser.find_element_by_css_selector('.btn.btn-primary[href]').click()
    assert 'route=account/register' in browser.current_url
