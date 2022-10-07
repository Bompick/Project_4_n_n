from .pages.product_page import ProductPage
import time

def test_1(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, url)# initialitiationof of object belonging to class ProductPage
    product_page.open()
    product_page.add_to_basket()    
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_message()
    product_page.should_be_price_message()
   


