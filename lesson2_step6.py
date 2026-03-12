from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим элемент-картинку (сундук)
    # Подходящий селектор для картинки с сокровищами
    treasure_element = browser.find_element(By.ID, "treasure")

    # 2. Получаем значение атрибута valuex
    x_value = treasure_element.get_attribute("valuex")
    print(f"Найденное значение x (из атрибута): {x_value}")

    # 3. Преобразуем в число и вычисляем функцию
    x = int(x_value)
    y = calc(x)
    print(f"Вычисленный ответ: {y}")

    # 4. Вводим ответ в текстовое поле (id="answer")
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot" (id="robotCheckbox")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!" (id="robotsRule")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 7. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Не забываем оставить пустую строку в конце файла