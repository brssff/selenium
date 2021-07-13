import allure
from pages.admin_login_page import AdminLoginPage
from pages.dashboard_page import DashboardPage


@allure.title("Удаление продукта из каталога")
@allure.description("Логинимся и удаляем случайный продукт из каталога")
def test_delete_product(browser):
    AdminLoginPage(browser).log_in()
    DashboardPage(browser).nav_to_products_page()
    DashboardPage(browser).delete_random_product()
