class BasePageLocators:
    LOGIN_LINK = ("css selector", "#login_link")
    LOGIN_LINK_INVALID = ("css selector", "#login_link_inc")
    USER_ICON = ("css selector", ".icon-user")

    BASKET_BUTTON = ("xpath", '//a[@class="btn btn-default"]')
    ITEMS_TO_BUY_IN_BASKET = ("css selector", '[class="col-sm-6 h3"]')
    EMPTY_BASKET_MESSAGE = ("css selector", '#content_inner')

class MainPageLocators:
    LOGIN_LINK = ("css selector", "#login_link")


class LoginPageLocators:
    LOGIN_FORM = ("css selector", "form#login_form")
    REGISTER_FORM = ("css selector", "form#register_form")

    EMAIL_ADDRESS_FIELD = ("css selector", "#id_registration-email")
    PASSWORD_FIELD = ("css selector", "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = ("css selector", "#id_registration-password2")
    REGISTER_BUTTON = ("css selector", '[name="registration_submit"]')



class GoodPageLocators:
    ADD_TO_BASKET_BUTTON = ("xpath", '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    GOOD_NAME = ("css selector", "#content_inner h1")
    GOOD_PRICE = ("css selector", ".product_main  .price_color")

    RESULT_PRICE = ("css selector", "div.alertinner p strong")
    RESULT_GOOD_NAME = ("xpath", '(//div[@class="alertinner "]/strong)[1]')
    RESULT_MESSAGE = ("xpath", '(//div[@class="alertinner "])[1]')