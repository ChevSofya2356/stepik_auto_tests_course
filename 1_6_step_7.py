from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все элементы input (текстовые поля) на странице
    # Используем поиск по тегу "input", так как все поля ввода имеют этот тег
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Перебираем все найденные поля и заполняем их
    for element in elements:
        element.send_keys("Мой ответ")  # Можно заменить на любой другой текст

    # Находим и кликаем по кнопке отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла
