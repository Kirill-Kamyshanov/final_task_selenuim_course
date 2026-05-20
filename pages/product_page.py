from pages.base_page import BasePage
from pages.locators import GoodPageLocators

class GoodPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*GoodPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        self.good_name = self.browser.find_element(*GoodPageLocators.GOOD_NAME).text
        self.good_price = self.browser.find_element(*GoodPageLocators.GOOD_PRICE).text


    def good_should_be_added(self):
        message = self.browser.find_element(*GoodPageLocators.RESULT_MESSAGE).text
        assert message, "Сообщение о добавлении товара не отображено"
        assert message == self.good_name + " has been added to your basket.", "Текст сообщения не совпадает с ожидаемым"
        assert self.good_price == self.browser.find_element(*GoodPageLocators.RESULT_PRICE).text, (
            "Цена в окне после добавления товара не совпадает с ожидаемой"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*GoodPageLocators.RESULT_MESSAGE), \
            "Сообщение об успехе отображается, но не должно"