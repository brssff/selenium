from .locators.admin_login_page import AdminLoginPage
from .locators.dashboard_page import DashboardPage


def test_add_product(browser):
    AdminLoginPage(browser).log_in()
    DashboardPage(browser).nav_to_products_page()
    DashboardPage(browser).add_new_product()

"""
    Регистрация нового пользователя в магазине опенкарта.
    Переключение валют из верхнего меню опенкарта.
"""
