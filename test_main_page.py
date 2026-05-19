from time import sleep

class TestHomework:
    def test_add_to_cart_button_is_displayed(self, browser):
        """Проверка наличия на странице товара кнопки добавления в корзину"""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

        browser.get(link)
        sleep(3)
        add_to_cart_button = browser.find_element("xpath", '(//button[@type="submit"])[2]')
        assert add_to_cart_button.is_displayed(), "Кнопка добавления в корзину не отображена"

