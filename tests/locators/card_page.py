from selenium.webdriver.common.by import By


class CardPage:
    LOGO = (By.CSS_SELECTOR, '#logo')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, '#button-cart')
    THUMBNAILS = (By.CSS_SELECTOR, '.col-sm-8 .thumbnails')
    HEADER = (By.CSS_SELECTOR, '#top')
    FOOTER = (By.CSS_SELECTOR, 'footer .container')
