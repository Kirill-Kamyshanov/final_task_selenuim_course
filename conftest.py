import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    """Регистрация опции --language для локализации сайта"""
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Язык интерфейса сайта"
    )

@pytest.fixture
def language(request: pytest.FixtureRequest) -> str:
    """Возвращает переданное значение опции --language"""
    return request.config.getoption("--language").lower()


@pytest.fixture
def browser(language: str):
    """Инициализация объекта браузера. Для каждого теста объект уникальный.
    Локаль зависит от опции --language. Без явной передачи опции интерфейс по-умолчанию на русском языке
    """
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    browser.quit()