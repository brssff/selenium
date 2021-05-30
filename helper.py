from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# удобный метод с встроенным явным ожиданием
def assert_element(locator: tuple, driver, timeout=1):
    try:
        # пытаемся дождаться видимости элемента за timeout секунд
        WebDriverWait(driver, timeout, poll_frequency=0.3).until(
            EC.visibility_of_element_located(locator))
    except TimeoutException:
        # Выбрасываем AssertionError
        raise AssertionError(f"Did not wait for an element: {locator}")
