import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        """Тест для первой страницы (должен проходить)"""
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            # Заполняем обязательные поля
            input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input_first_name.send_keys("Ivan")

            input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input_last_name.send_keys("Petrov")

            input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input_email.send_keys("ivan.petrov@example.com")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Ждём загрузки
            time.sleep(1)

            # Проверяем результат
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            browser.quit()

    def test_registration2(self):
        """Тест для второй страницы (должен упасть с ошибкой)"""
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            # Заполняем обязательные поля
            input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input_first_name.send_keys("Ivan")

            input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input_last_name.send_keys("Petrov")

            input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input_email.send_keys("ivan.petrov@example.com")

            # Отправляем форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Ждём загрузки
            time.sleep(1)

            # Проверяем результат
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()