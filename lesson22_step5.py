from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    # Поле "First name"
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Ivan")

    # Поле "Last name"
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Petrov")

    # Поле "Email"
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("ivan.petrov@example.com")

    # 2. Подготавливаем файл для загрузки
    # Создаём временный текстовый файл в той же папке, где лежит скрипт
    # Получаем путь к директории текущего скрипта
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Создаём имя файла и полный путь к нему
    file_name = "bio.txt"
    file_path = os.path.join(current_dir, file_name)

    # Записываем что-то в файл (он может быть и пустым)
    with open(file_path, 'w') as file:
        file.write("This is my short bio.")

    print(f"Файл создан: {file_path}")

    # 3. Загружаем файл
    # Находим элемент input с типом file
    file_input = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # Отправляем путь к файлу в этот элемент
    file_input.send_keys(file_path)

    # 4. Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер
    browser.quit()

    # Можно добавить удаление временного файла (необязательно)
    # if os.path.exists(file_path):
    #     os.remove(file_path)

# Не забываем оставить пустую строку в конце файла