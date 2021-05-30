from ..helper import assert_element
from .pages.catalog_page import CatalogPage


def test_catalog_page(browser):
    browser.get(CatalogPage.URL)
    browser.find_element(*CatalogPage.LOGO)
    browser.find_element(*CatalogPage.CATALOG_COLUMN)
    browser.find_element(*CatalogPage.SEARCH_INPUT)
    browser.find_element(*CatalogPage.LIST_VIEW)
    browser.find_element(*CatalogPage.GRID_VIEW)
    browser.find_element(*CatalogPage.SORT_BY)
    browser.find_element(*CatalogPage.SHOW_LIMIT)
    browser.find_element(*CatalogPage.FOOTER)
    assert_element(CatalogPage.FOOTER, browser, timeout=2)

    product_thumbs = browser.find_elements(*CatalogPage.PRODUCT_THUMB)
    assert len(product_thumbs) == 12, f"Thumbs on page: {len(product_thumbs)}, but 12 expected"
