from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    """Функция для тестирования регистрации на переданной ссылке"""
    browser = None
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля, используя УНИКАЛЬНЫЕ селекторы

        # 1. Первое обязательное поле: Имя (используем уникальный класс)
        # На первой странице это .first_block .first, на второй такого класса нет
        input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input_first_name.send_keys("Ivan")

        # 2. Второе обязательное поле: Фамилия (уникальный класс)
        input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input_last_name.send_keys("Petrov")

        # 3. Третье обязательное поле: Email (уникальный класс)
        input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input_email.send_keys("ivan.petrov@example.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждём загрузки страницы с результатом
        time.sleep(1)

        # Ищем элемент с приветственным текстом
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Возвращаем текст для проверки в основной программе
        return welcome_text

    finally:
        if browser:
            browser.quit()

# --- Основная часть программы ---
if __name__ == "__main__":
    # Тест на старой странице (ДОЛЖЕН ПРОХОДИТЬ)
    link1 = "http://suninjuly.github.io/registration1.html"
    print("Тестируем первую страницу (должна пройти):")
    result1 = test_registration(link1)
    if result1 and "Congratulations" in result1:
        print(f"УСПЕХ! Найден текст: {result1}\n")
    else:
        print(f"ОШИБКА на первой странице! Текст: {result1}\n")

    # Тест на новой странице (ДОЛЖЕН ПАДАТЬ с NoSuchElementException)
    link2 = "http://suninjuly.github.io/registration2.html"
    print("Тестируем вторую страницу (должна упасть с ошибкой):")
    try:
        result2 = test_registration(link2)
        # Если код дошел до этой строки, значит элемент БЫЛ найден и тест НЕ заметил баг
        print(f"ТЕСТ ПРОШЁЛ, ХОТЯ ДОЛЖЕН БЫЛ УПАСТЬ! Текст: {result2}")
    except Exception as e:
        # Ожидаем, что тест упадёт именно с NoSuchElementException
        if "NoSuchElementException" in str(e):
            print(f"УСПЕХ! Тест упал с ожидаемой ошибкой: {type(e).__name__}")
        else:
            print(f"Тест упал с другой ошибкой: {type(e).__name__} - {e}")

    # Даём время посмотреть результаты перед закрытием окон
    time.sleep(2)