from pytest_bdd import scenarios, given, when, then
from selene.support.conditions import have, be

from tests.web.pages.home_page import HomePage

scenarios(
    '../features/home/002_validar_consulta.feature',
)


@given("que estou na tela inicial do marketplace")
def step_impl1(driver):
    HomePage(driver).driver.open('/')


@when("no campo de busca informar um parâmetro para consulta")
def step_impl2(driver):
    HomePage(driver).search('alcool em gel')


@then("é apresentado a quantidade dos produtos retornados")
def step_impl3(driver):
    home_page = HomePage(driver)
    home_page.txt_qty_products_found.wait_until(be.visible)
    home_page.txt_qty_products_found.should(have.text('produtos encontrados'))
    assert int(home_page.get_qty_products_returned()) > 0


@then("é apresentado os produtos de acordo com o critério buscado")
def step_impl4(driver):
    HomePage(driver).first_prod.should(be.visible)
