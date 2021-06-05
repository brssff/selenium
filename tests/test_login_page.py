from pages.login_page import LoginPage
from helper import assert_element


def test_login_page(browser):
    browser.open(LoginPage.PATH)
    assert_element(LoginPage.BREADCRUMBS, browser)
    assert_element(LoginPage.CONTINUE_BTN, browser)
    assert_element(LoginPage.LOGIN_BTN, browser)
    assert_element(LoginPage.RIGHT_COLUMN, browser)
    assert_element(LoginPage.LOGO, browser)
    assert_element(LoginPage.HEADER, browser)
    assert_element(LoginPage.FOOTER, browser)


def test_can_redirect_to_register_page(browser):
    browser.open(LoginPage.PATH)
    browser.find_element(*LoginPage.CONTINUE_BTN).click()
    assert browser.title == 'Register Account'
