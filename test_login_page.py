from distutils.log import log
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_login_page_full(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.should_be_login_page()

    
    
    
   
    

   



    