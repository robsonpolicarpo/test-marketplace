from selene.api import s

from tests.support.generic_page import GenericPage


class ProductDetailPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)
        self._btn_add_to_cart = s("//*[text()='Adicionar à sacola']/ancestor::button")

    def add_to_cart(self):
        self._btn_add_to_cart.click()
