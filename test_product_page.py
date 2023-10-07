import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = MainPage(browser, link)
    product = ProductPage(browser, link)
    page.open()
    product.add_to_basket()
    page.solve_quiz_and_get_code()
    product.item_should_be_added_in_cart_message()
    product.price_should_be_equal()
