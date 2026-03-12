import pytest
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket():
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    
    # Получаем информацию о товаре до добавления
    product_name = page.get_product_name()
    product_price = page.get_product_price()
    
    # Добавляем товар в корзину
    page.add_product_to_basket()
    
    # Решаем математическое выражение и получаем проверочный код
    page.solve_quiz_and_get_code()
    
    # Проверяем сообщение о добавлении товара
    page.should_be_success_message_with_product_name(product_name)
    
    # Проверяем стоимость корзины
    page.should_be_basket_total_equal_product_price(product_price)
