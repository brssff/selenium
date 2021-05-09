from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# удобный метод с встроенным явным ожиданием
def assert_element(selector, driver, timeout=1):
    try:
        # пытаемся дождаться видимости элемента за timeout секунд
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        # Перехватываем исключение и атачим скриншот
        driver.save_screenshot("{}.png".format(driver.session_id))
        # Выбрасываем AssertionError
        raise AssertionError(f"Не дождался видимости элемента: {selector}")
