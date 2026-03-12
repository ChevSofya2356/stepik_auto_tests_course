from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим элементы с числами и получаем из них текст
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # 2. Вычисляем сумму
    sum_result = num1 + num2
    print(f"Число 1: {num1}, Число 2: {num2}, Сумма: {sum_result}")

    # 3. Работаем с выпадающим списком
    # Находим сам элемент select
    select_element = browser.find_element(By.ID, "dropdown")
    # Создаём объект Select для работы с ним
    select = Select(select_element)

    # Выбираем опцию по видимому тексту (нашему числу)
    # ВАЖНО: преобразуем число в строку, так как select ищет именно строку
    select.select_by_visible_text(str(sum_result))

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

# Не забываем оставить пустую строку в конце файла
