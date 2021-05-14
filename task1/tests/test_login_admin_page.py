from ..helper import assert_element

URL = 'https://demo.opencart.com/admin/'


def test_login_admin_page(browser):
    browser.get(URL)

    assert_element('#header-logo', browser)
    assert_element('#input-username', browser)
    assert_element('#input-password', browser)
    assert_element('.help-block', browser)
    assert_element('.btn.btn-primary', browser)
    assert_element('#footer', browser)


def test_ability_to_log_in(browser):
    browser.get(URL)
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    assert 'user_token' in browser.current_url
    assert browser.title == 'Dashboard'
    assert_element('.fa.fa-sign-out', browser)
