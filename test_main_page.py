from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        login = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        login.should_be_login_page(browser)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.skip
def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#registration_link")
    login_link.click()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    basket = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket.basket_is_empty()
    basket.is_empty_basket_message()
