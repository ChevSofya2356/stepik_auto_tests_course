from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления зашифрованного текста ссылки
def get_secret_link_text():
    return str(math.ceil(math.pow(math.pi, math.e) * 10000))

link = "http://suninjuly.github.io/find_link_text"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычисляем текст ссылки
    secret_text = get_secret_link_text()
    print(f"Ищем ссылку с текстом: {secret_text}")

    # Находим ссылку по точному тексту и кликаем по ней
    secret_link = browser.find_element(By.LINK_TEXT, secret_text)
    secret_link.click()

    # --- Заполняем форму на новой странице ---
    # Даем странице немного времени на загрузку
    time.sleep(1)

    # Ищем первое поле (имя) по тегу 'input' (как в прошлом задании)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    # Ищем второе поле (фамилия) по атрибуту name='last_name'
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    # Ищем третье поле (город) по классу 'city'
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    # Ищем четвёртое поле (страна) по ID 'country'
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Ищем кнопку отправки по CSS-селектору 'button.btn'
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Не забываем оставить пустую строку в конце файла
