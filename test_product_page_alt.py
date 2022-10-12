from .pages.product_page import ProductPage
import time
import pytest


def test_1(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, url)# initialitiation of of object belonging to class ProductPage
    product_page.open()
    product_page.should_not_be_success_message()
    product_page.add_to_basket()    
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_message()
    product_page.should_be_price_message()
    product_page.should_disappear()




