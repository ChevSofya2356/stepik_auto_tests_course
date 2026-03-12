import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список URL-адресов уроков
urls = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

# Данные для авторизации (замените на свои)
login = 'cevakinasona@gmail.com'  # ВАШ ЛОГИН
password = 'S1256s1256~'  # ВАШ ПАРОЛЬ


@pytest.fixture(scope="function")
def browser():
    """Фикстура для браузера"""
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', urls)
def test_stepik_login_and_answer(browser, url):
    """Тест авторизации и отправки ответа на Stepik"""

    # Открываем страницу
    browser.get(url)

    # Ждем и нажимаем кнопку авторизации
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.navbar__auth_login'))
    ).click()

    # Вводим логин и пароль
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(login)
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(password)

    # Нажимаем кнопку "Войти"
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ждем успешной авторизации (ждем появления аватарки пользователя)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.navbar__profile'))
    )

    # Небольшая пауза для полной загрузки страницы после авторизации
    time.sleep(3)

    # Вычисляем правильный ответ
    answer = math.log(int(time.time()))

    # Находим поле для ввода ответа (ждем его появления)
    # Обратите внимание: селектор может отличаться на разных страницах, но обычно это textarea
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.ember-text-area'))
    )

    # Очищаем поле и вводим ответ
    textarea.clear()
    textarea.send_keys(str(answer))

    # Находим и нажимаем кнопку отправки
    browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()

    # Ждем появления фидбека
    feedback_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
    )

    # Получаем текст фидбека
    feedback_text = feedback_element.text

    # Проверяем, что фидбек равен "Correct!"
    # Если не равен - тест упадет и покажет текст из фидбека (это и есть кусочек послания)
    assert feedback_text == 'Correct!', f'Получен текст: "{feedback_text}" вместо "Correct!"'


if __name__ == "__main__":
    pytest.main()