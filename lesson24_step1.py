from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ожидаем, когда цена станет равной $100
    # Используем явное ожидание до 12 секунд, проверяя наличие текста "$100" в элементе с id="price"
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Как только цена стала $100, нажимаем кнопку "Book"
    button_book = browser.find_element(By.ID, "book")
    button_book.click()

    # 3. Решаем математическую задачу на новой странице
    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем ответ
    y = calc(x)

    # Вводим ответ
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    browser.quit()