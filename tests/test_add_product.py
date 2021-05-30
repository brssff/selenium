from tests.pages.admin_login_page import AdminLoginPage
from tests.pages.dashboard_page import DashboardPage


def test_add_product(browser):
    AdminLoginPage(browser).log_in()
    DashboardPage(browser).nav_to_products_page()
    DashboardPage(browser).add_new_product()
