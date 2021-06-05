from pages.catalog_page import CatalogPage


def test_catalog_page(browser):

    CatalogPage(browser).check_elements_exist_on_page()
    CatalogPage(browser).check_product_thumbs()
