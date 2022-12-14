from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')

class LoginPageLocators():
    LOGIN_FORM = (By.ID,'login_form')
    REGISTER_FORM = (By.ID,'register_form')
    EMAILL_ADRESS_FIELD = (By.ID,'id_registration-email')
    PASSWORD_FIELD = (By.ID,'id_registration-password1')
    CONFIRM_PASSWORD_FIELD = (By.ID,'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR,'button[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR,'li[class="active"]')
    PRODUCT_NAME_ADDED = (By.CSS_SELECTOR, '[class="alertinner "] strong')
    BOOK_PRICE = (By.CSS_SELECTOR,".product_main .price_color")
    BOOK_PRICE_ADEED = (By.CSS_SELECTOR,'.alert-info p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.content")
    ADDED_GOODS = (By.CSS_SELECTOR, ".basket-items")
