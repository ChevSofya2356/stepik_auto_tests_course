from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем первое поле (имя) по тегу 'input'
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
    # Увеличим время до 30 секунд, чтобы вы успели скопировать ответ
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
