from .locators.admin_login_page import AdminLoginPage


def test_admin_login_page(browser):
    page = AdminLoginPage(browser=browser)
    page.open(page.URL)
    page.log_in()
