from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Найдено x: {x}")

    # 2. Вычисляем функцию
    y = calc(x)
    print(f"Ответ: {y}")

    # 3. Находим все элементы, с которыми будем работать
    input_answer = browser.find_element(By.ID, "answer")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    radiobutton = browser.find_element(By.ID, "robotsRule")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # 4. Прокручиваем страницу, чтобы всё было видно
    # Скроллим до кнопки, так как она обычно внизу
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Можно также сделать чуть более плавный скролл (необязательно)
    # browser.execute_script("window.scrollBy(0, 100);")

    # 5. Теперь взаимодействуем с элементами
    input_answer.send_keys(y)
    checkbox.click()
    radiobutton.click()
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Не забываем оставить пустую строку в конце файла