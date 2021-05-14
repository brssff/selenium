"""
Задание 1.

1.1. Написать фикстуру для запуска разных браузеров (firefox, chrome, opera).
1.2. Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest.
1.3. По завершению работы тестов должно осуществляться закрытие браузера.
1.3. Написать тест, который открывает основную страницу opencart и проверяет что title соотсвествует ожидаемому.
1.4. Добавить опцию командной строки, которая указывает базовый URL opencart.
"""


def test_opencart(browser):
    browser.get('https://demo.opencart.com/')
    assert browser.title == 'Your Store'


# 1.4. Добавить опцию командной строки, которая указывает базовый URL opencart.
def test_base_url_param(browser, base_url):
    browser.get(base_url)
    assert browser.title
