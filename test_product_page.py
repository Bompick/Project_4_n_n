from .pages.product_page import ProductPage
import time
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.need_review 
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]) #to show parametrize. 9 from 10 links were deleted for review. 
def test_guest_can_add_product_to_basket(browser,link):
    url = f"{link}"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket()    
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket_message()
    product_page.should_be_price_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.no_goods_in_basket()
    basket_page.basket_is_empty_message()


@pytest.mark.user_2t
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, self.url)
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.login_page.register_new_user(email,password)
        self.login_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.add_to_basket()    
        product_page.should_be_add_to_basket_message()
        product_page.should_be_price_message()



