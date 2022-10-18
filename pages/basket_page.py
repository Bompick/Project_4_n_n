from  .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_GOODS), \
            "Item is added, but should not be"
        

    def basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "\"empty basket message\" is not presented "



       



