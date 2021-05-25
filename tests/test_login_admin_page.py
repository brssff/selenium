from ..helper import assert_element
from .locators.AdminLoginPage import AdminLoginPage


def test_admin_login_page(browser):
    browser.get(AdminLoginPage.URL)

    assert_element(AdminLoginPage.LOGO[1], browser)
    assert_element(AdminLoginPage.USERNAME[1], browser)
    assert_element(AdminLoginPage.PASSWORD[1], browser)
    browser.find_element(*AdminLoginPage.FORGOT_PASSWORD)
    browser.find_element(*AdminLoginPage.LOGIN_BTN)
    assert_element(AdminLoginPage.FOOTER[1], browser)


def test_log_in(browser):
    browser.get(AdminLoginPage.URL)
    browser.find_element(*AdminLoginPage.LOGIN_BTN).click()
    assert 'user_token' in browser.current_url
    assert browser.title == 'Dashboard'
