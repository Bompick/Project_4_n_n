from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
from .pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, url)# initialitiationof of object belonging to MainPage
    page.open() #open of main page
    login_page = page.go_to_login_page() # go to login page->> variable = login page
    login_page = LoginPage(browser, browser.current_url) ## initialitiationof of object(variable) AS belonging to LoginPage wits it's atributes and metods and atributes and methods of Ancestors.!!!!CURENTURL!!!
    login_page.should_be_login_page()
   
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, url)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page = BasketPage(browser,browser.current_url)
    basket_page.no_goods_in_basket()
    basket_page.basket_is_empty_message()




    