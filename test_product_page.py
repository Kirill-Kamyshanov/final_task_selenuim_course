import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from time import sleep
from pages.locators import GoodPageLocators
from pages.product_page import GoodPage

good_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.skip
@pytest.mark.parametrize('num',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
                         )
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = GoodPage(browser, link)
    page.open()
    page.add_to_basket()
    page.good_should_be_added()
    sleep(4)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """проверка, что нет сообщения об успехе с помощью is_not_element_present"""
    page = GoodPage(browser, good_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
    # page.is_not_element_present(*GoodPageLocators.RESULT_MESSAGE)
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    """проверка, что нет сообщения об успехе с помощью is_not_element_present"""
    page = GoodPage(browser, good_link)
    page.open()
    page.should_not_be_success_message()



def test_message_disappeared_after_adding_product_to_basket(browser):
    """Проверка, что нет сообщения об успехе с помощью is_disappeared"""
    page = GoodPage(browser, good_link)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()
