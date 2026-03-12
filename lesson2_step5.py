from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент с числом x по ID
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено x: {x}")

    # Вычисляем ответ
    y = calc(x)
    print(f"Ответ: {y}")

    # Вводим ответ в поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()