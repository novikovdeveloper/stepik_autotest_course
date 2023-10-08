from pages.base_page import BasePage
from pages.locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине есть товары, должна быть пуста"

    def is_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY),\
            "Не появилось сообщение, что корзина пуста"