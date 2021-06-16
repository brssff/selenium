import pytest
import os
import logging
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/develop/selenium_prj/drivers")
SCREENSHOTS = os.path.expanduser("~/develop/selenium_prj/screenshots")
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.expanduser('~/develop/selenium_prj/logs/selenium.log'),
    format='%(asctime)s %(levelname)s %(filename)s %(message)s'
)


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run headless")
    #parser.addoption("--executor", "-E", default="127.0.0.1")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--url", default='https://demo.opencart.com/')
    parser.addoption("--timeout", type=int, default=2)


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')
    url = request.config.getoption("--url")
    timeout = request.config.getoption("--timeout")

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

    def fin():
        # driver.save_screenshot(f"{SCREENSHOTS}/{str(datetime.timestamp(datetime.now()))}.png")
        logging.info("Teardown: quit browser..")
        driver.quit()

    request.addfinalizer(fin)

    def open_url(path=""):
        return driver.get(url + path)

    driver.maximize_window()

    driver.open = open_url
    driver.open()
    driver.timeout = timeout

    return driver
