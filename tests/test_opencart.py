def test_opencart(browser):
    browser.get('https://demo.opencart.com/')
    assert browser.title == 'Your Store'
