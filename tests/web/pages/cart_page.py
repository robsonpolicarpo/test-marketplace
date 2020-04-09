from selene.api import s, ss
from selene.support.conditions import be

from tests.support.generic_page import GenericPage


class CartPage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.products = ss("//div[@class='BasketItem']")
        self.first_product = s("//div[@class='BasketItem']")

    def wait_product_visible(self):
        self.first_product.wait_until(be.visible)

    def get_title_product(self, item=0):
        self.wait_product_visible()
        title = self.products[item].s("./descendant::a[@class='BasketItemProduct-info-title']/p").text
        return title
