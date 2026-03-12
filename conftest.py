import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавляем опцию --language в командную строку pytest"""
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language: es, fr, en, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера с указанным языком"""
    # Получаем параметр language из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем опции браузера для указанного языка
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    # Создаем экземпляр браузера
    browser = webdriver.Chrome(options=options)

    # Неявное ожидание для стабильности тестов
    browser.implicitly_wait(5)

    # Возвращаем браузер для использования в тесте
    yield browser

    # Закрываем браузер после теста
    browser.quit()