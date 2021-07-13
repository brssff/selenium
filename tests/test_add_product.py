import allure
from pages.admin_login_page import AdminLoginPage
from pages.dashboard_page import DashboardPage


@allure.title("Добавление нового продукта")
@allure.description("Логин в админку, переход на страницу продуктов, добавление нового продукта")
def test_add_product(browser):
    AdminLoginPage(browser).log_in()
    DashboardPage(browser).nav_to_products_page()
    DashboardPage(browser).add_new_product()
