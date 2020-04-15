import re

from selene.api import s, ss
from selene.core.configuration import Config
from selene.support.conditions import be, have
from selenium.webdriver.common.keys import Keys

from tests.support.generic_page import GenericPage


class HomePage(GenericPage):

    def __init__(self, driver):
        super().__init__(driver)
        self._input_search = s("#inpHeaderSearch")
        self._container_search = s("//div[contains(@class, 'search-results-container')]")
        self.txt_qty_products_found = s("//div[@class='header-search']").s("./descendant::small")
        self._txt_products_not_found = s("//div[@class='nm-not-found-message1']")
        self.first_prod = s("//li[@class='product']")
        self._products = ss("//li[@class='product']")

    def search(self, term):
        self._input_search.type(term).type(Keys.ENTER)

    def wait_products_presented(self, timeout=20):
        self.first_prod.with_(Config(timeout=timeout)).wait_until(be.clickable)

    def get_qty_products_returned(self):
        self.txt_qty_products_found.should(be.visible)
        text = self.txt_qty_products_found.text
        text = re.search("[\d]+", text).group()
        return text

    def detail_product(self, item=0):
        self.wait_products_presented()
        prod_title = self._products[item].s("./descendant::*[@class='nm-product-name']").text
        self._products[item].click()
        return prod_title

    def get_prod_not_found_text(self):
        self._txt_products_not_found.with_(Config(timeout=15)).wait_until(be.visible)
        return self._txt_products_not_found
