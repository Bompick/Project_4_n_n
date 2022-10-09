from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_FORM = (By.ID,'register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR,'li[class="active"]')
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, '[class="alertinner "] strong')
    BOOK_PRICE = (By.CSS_SELECTOR,".product_main .price_color")
    BOOK_PRICE_ADEED = (By.CSS_SELECTOR,'.alert-info p strong')

