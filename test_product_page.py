from faker import Faker
import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

good_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
faker = Faker()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """проверка, что нет сообщения об успехе с помощью is_not_element_present"""
    page = ProductPage(browser, good_link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()



def test_guest_cant_see_success_message(browser):
    """проверка, что нет сообщения об успехе с помощью is_not_element_present"""
    page = ProductPage(browser, good_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('num',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]
                         )
def test_guest_can_add_product_to_basket(browser, num):
    """Проверка добавления товара в корзину для анрега"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.good_should_be_added()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Проверка, что нет сообщения об успехе с помощью is_disappeared"""
    page = ProductPage(browser, good_link)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """Проверка отображения ссылки логина для анрега"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Проверка перехода на страницу для анрега"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, language):
    """Проверка отсутствия товаров в корзине для анрега"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_products_in_basket(language=language)


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Регистрирует тестового юзера. Использует уникальные случайно сгенерированные данные"""
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        test_email = faker.email()
        test_password = faker.password()

        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(test_email, test_password)
        page.should_be_authorized_user()



    def test_user_cant_see_success_message(self, browser):
        """Проверяет, что сообщение об успехе не отображается при переходе на страницу продукта"""
        page = ProductPage(browser, good_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Проверка добавления товара в корзину для авторизованного юзера"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.good_should_be_added()
