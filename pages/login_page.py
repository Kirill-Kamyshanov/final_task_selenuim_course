from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Проверка отображения страницы логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        """Регистрация нового юзера"""
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_url(self):
        """Проверка открытия страницы логина"""
        assert "login" in self.browser.current_url, "Страница логин не открыта"

    def should_be_login_form(self):
        """Проверка наличия формы авторизации на странице"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма авторизации не отображена"

    def should_be_register_form(self):
        """Проверка наличия формы регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не отображена"
