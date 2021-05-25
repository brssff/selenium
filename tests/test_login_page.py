from ..helper import assert_element
from .locators.login_page import LoginPage


def test_login_page(browser):
    browser.get(LoginPage.URL)
    assert_element(LoginPage.BREADCRUMBS[1], browser)
    assert_element(LoginPage.CONTINUE_BTN[1], browser)
    assert_element(LoginPage.LOGIN_BTN[1], browser)
    assert_element(LoginPage.RIGHT_COLUMN[1], browser)
    assert_element(LoginPage.LOGO[1], browser)
    assert_element(LoginPage.HEADER[1], browser)
    assert_element(LoginPage.FOOTER[1], browser)


def test_can_redirect_to_register_page(browser):
    browser.get(LoginPage.URL)
    browser.find_element(*LoginPage.CONTINUE_BTN).click()
    assert browser.title == 'Register Account'
