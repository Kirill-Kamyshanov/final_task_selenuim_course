import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"