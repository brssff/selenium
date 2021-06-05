from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_element(self, locator: tuple, timeout=2):
        try:
            return WebDriverWait(self.browser, timeout, poll_frequency=0.3).until(
                EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Cant find element {locator} for {timeout} seconds")

    def clear_n_paste(self, locator: tuple, value):
        try:
            self.browser.find_element(*locator).clear()
            self.browser.find_element(*locator).send_keys(value)
        except NoSuchElementException:
            raise AssertionError(f"Cant find element {locator}")
