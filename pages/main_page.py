from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        self.go_to_element(*MainPageLocators.LOGIN_LINK)
        

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_age_of_the_pussyfoot (self):
        self.go_to_element(*MainPageLocators.pussyfoot)
    
    def go_to_all_products (self):
        self.go_to_element(*MainPageLocators.all_products_link)