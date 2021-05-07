import pytest
import os
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/develop/selenium/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--base_url", action="store", help="opencart base url", default='https://www.opencart.ru')


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    maximized = request.config.getoption('--maximized')

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(options=options, executable_path=f"{DRIVERS}/chromedriver")

    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.headless = headless

        driver = webdriver.Firefox(options=options, executable_path=f"{DRIVERS}/geckodriver")

    elif browser == 'opera':
        options = OperaOptions()
        if headless:
            raise ValueError('Cant run Opera with headless mode')

        driver = webdriver.Opera(options=options, executable_path=f"{DRIVERS}/operadriver")

    else:
        raise ValueError(f"Passed driver not supported: \'{browser}\'")

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption("base_url")
