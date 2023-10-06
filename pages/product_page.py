from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_click = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_click.click()

    def item_should_be_added_in_cart_message(self):
        added_to_basket_item_name = self.browser.find_element(By.CSS_SELECTOR, ".alertinner >strong")
        name2 = added_to_basket_item_name.text
        name_of_product = self.browser.find_element(By.TAG_NAME, "h1")
        name1 = name_of_product.text
        assert name1 == name2, "Имена продуктов не совпали"

    def price_should_be_equal(self):
        price_of_product = self.browser.find_element(By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
        price1 = price_of_product.text
        price_of_product_in_basket = self.browser.find_element(By.CSS_SELECTOR, ".alertinner > p > strong")
        price2 = price_of_product_in_basket.text
        assert price1 == price2, "Цены не совпали"
