from ..helper import assert_element
from .locators.Catalog import Catalog
URL = 'https://demo.opencart.com/index.php?route=product/category&path=20'


def test_catalog(browser):
    browser.get(URL)
    browser.find_element(*Catalog.LOGO)
    browser.find_element(*Catalog.CATALOG_COLUMN)
    browser.find_element(*Catalog.SEARCH_INPUT)
    browser.find_element(*Catalog.LIST_VIEW)
    browser.find_element(*Catalog.GRID_VIEW)
    browser.find_element(*Catalog.SORT_BY)
    browser.find_element(*Catalog.SHOW_LIMIT)
    browser.find_element(*Catalog.FOOTER)
    assert_element(Catalog.FOOTER[1], browser, timeout=2)

    product_thumbs = browser.find_elements(*Catalog.PRODUCT_THUMB)
    assert len(product_thumbs) == 12, f"Thumbs on page: {len(product_thumbs)}, but 12 expected"
