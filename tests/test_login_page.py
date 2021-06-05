from pages.login_page import LoginPage


def test_login_page_has_all_elements(browser):
    LoginPage(browser).check_elements_exist()


def test_can_redirect_to_register_page(browser):
    LoginPage(browser).redirect_to_register_page()
