from multiprocessing import Pool
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()         # метод добавления в корзину

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
   
    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented" 
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ADDED), "Added Product name is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED).text
        assert product_name == message_product_name, "No product name in the message"
    
    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Price  is not presented"
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_ADEED), " Added Price  is not presented"
        price_value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_value_added = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADEED).text
        assert price_value == price_value_added, 'price in basket is not correct'



      