import pytest

URL = 'https://www.opencart.ru/index.php?route=account/login'
CSS_SELECTORS = ['.breadcrumb.blog', '.btn.btn-primary[href]', '.btn.btn-primary[type]',
                 '.list-group .list__group-item:nth-child(3)', '.header-logo', '.login__main .grn:nth-child(2)']


@pytest.mark.parametrize('selectors', CSS_SELECTORS,
                         ids=['Breadcrumbs', 'Continue', 'Login', 'Forgot pass', 'Logo', 'How to install'])
def test_login_page(browser, selectors):
    browser.get(URL)
    assert selectors
