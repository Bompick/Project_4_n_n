from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, url)# initialitiationof of object belonging to MainPage
    page.open() #open of main page
    login_page = page.go_to_login_page() # go to login page->> variable = login page
    login_page = LoginPage(browser, browser.current_url) ## initialitiationof of object(variable) AS belonging to LoginPage wits it's atributes and metods and atributes and methods of Ancestors.!!!!CURENTURL!!!
    login_page.should_be_login_page()
   



    