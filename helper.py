from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime


# удобный метод с встроенным явным ожиданием
def assert_element(locator, driver, timeout=1):
    try:
        # пытаемся дождаться видимости элемента за timeout секунд
        WebDriverWait(driver, timeout, poll_frequency=0.3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
    except TimeoutException:
        # Перехватываем исключение и атачим скриншот с именем = timestamp
        driver.save_screenshot(f"{datetime.timestamp(datetime.now())}.png")
        # Выбрасываем AssertionError
        raise AssertionError(f"Did not wait for an element: {locator}")
