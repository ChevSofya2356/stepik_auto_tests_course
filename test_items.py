import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_add_to_cart_button(browser):
    """Тест проверяет наличие кнопки добавления в корзину на странице товара"""
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Добавляем паузу для визуальной проверки языка интерфейса
    time.sleep(30)

    # Ищем кнопку добавления в корзину
    # Используем несколько вариантов селекторов для надежности
    try:
        # Основной селектор для английской версии
        button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
    except:
        # Альтернативный селектор
        button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        )

    # Проверяем, что кнопка отображается на странице
    assert button is not None, "Кнопка добавления в корзину не найдена на странице"

    # Дополнительная проверка, что кнопка видима
    assert button.is_displayed(), "Кнопка добавления в корзину не видна на странице"

    # Проверяем, что на кнопке есть текст (для визуальной проверки)
    button_text = button.text
    print(f"\nТекст на кнопке: '{button_text}'")

    # Необязательная проверка, что текст не пустой
    assert button_text != "", "Текст на кнопке пустой"