import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from time import sleep


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        # sleep(3)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    sleep(2)
    page.should_be_login_page()


def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser, language):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_products_in_basket(language=language)



