import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class TestBrowserLanguage:
    def test_find_cart_button(self, browser):
        browser.get(link)
        add_to_card_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert add_to_card_button is not None, "button not found on page"
