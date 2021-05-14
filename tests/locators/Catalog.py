from selenium.webdriver.common.by import By


class Catalog:
    LOGO = (By.CSS_SELECTOR, '#logo')
    CATALOG_COLUMN = (By.CSS_SELECTOR, '#column-left')
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search')
    PRODUCT_THUMB = (By.CSS_SELECTOR, '.product-thumb')
    LIST_VIEW = (By.CSS_SELECTOR, '#list-view')
    GRID_VIEW = (By.CSS_SELECTOR, '#grid-view')
    SORT_BY = (By.CSS_SELECTOR, '#input-sort')
    SHOW_LIMIT = (By.CSS_SELECTOR, '#input-limit')
    FOOTER = (By.CSS_SELECTOR, 'footer .container')
