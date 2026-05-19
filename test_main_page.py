import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from time import sleep


link = "http://selenium1py.pythonanywhere.com/"

# @pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    # sleep(3)

# @pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_3(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    sleep(2)
    page.should_be_login_page()

