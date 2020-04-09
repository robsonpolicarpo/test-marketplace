from selene.support.conditions import have

from tests.web.pages.cart_page import CartPage
from tests.web.pages.home_page import HomePage
from tests.web.pages.product_detail_page import ProductDetailPage


def test_search_not_found(driver):
    home_page = HomePage(driver)
    home_page.search('productnotfound')
    home_page.get_prod_not_found_text().should(have.text('não encontrou resultado algum :('))


def test_verify_product_in_cart(driver):
    home_page = HomePage(driver)
    home_page.search('alcool em gel')
    home_page.txt_qty_products_found.should(have.text('produtos encontrados'))
    assert int(home_page.get_qty_products_returned()) > 0
    prod_selected = home_page.detail_product()
    ProductDetailPage(driver).add_to_cart()
    prod_title_in_cart = CartPage(driver).get_title_product()
    assert prod_selected == prod_title_in_cart
