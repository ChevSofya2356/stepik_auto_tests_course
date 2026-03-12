from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, чтобы вызвать confirm
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Переключаемся на всплывающее окно confirm и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. Теперь мы на новой странице. Решаем капчу для роботов
    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено x: {x}")

    # Вычисляем ответ
    y = calc(x)
    print(f"Ответ: {y}")

    # Вводим ответ в поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Не забываем оставить пустую строку в конце файла