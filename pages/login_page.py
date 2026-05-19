from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        """Проверка открытия страницы логина"""
        assert "login" in self.browser.current_url, "Страница логин не открыта"

    def should_be_login_form(self):
        """Проверка наличия формы авторизации на странице"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма авторизации не отображена"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не отображена"
