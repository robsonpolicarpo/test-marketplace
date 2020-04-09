import shutil
from collections import defaultdict
from pathlib import Path

import pytest
from selene.support.shared import browser

from tests.support.driver_factory import get_driver_config

URL_BASE = 'https://www.magazineluiza.com.br'


@pytest.fixture(scope='session')
def context():
    """Context object to store data to be passed between steps"""
    return {}


@pytest.fixture(scope="session")
def driver():
    browser = get_driver_config(URL_BASE)
    yield browser
    try:
        pytest.globalDict = None
        browser.quit()
    except Exception as exc:
        print('Error in close browser')
        pass


def pytest_runtest_call(item):
    if item.name != 'test_cn01_consultar_pedido_com_sucesso':
        browser.open('/')


def pytest_configure(config):
    if Path('./reports').exists():
        shutil.rmtree(Path('./reports/').absolute())
    Path('./reports/allure').mkdir(parents=True, exist_ok=True)
    Path('./reports/json').mkdir(parents=True, exist_ok=True)
    pytest.globalDict = defaultdict()
    pytest.globalDict.update({'scenarios_run': {}})
    pass


def pytest_bdd_before_scenario(request, feature, scenario):
    """Called before scenario is executed."""


def pytest_bdd_after_scenario(request, feature, scenario):
    """Called after scenario is executed."""
    add_scenario_to_run(request, scenario)


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute."""
    scenario.exception = exception
    scenario.failed = True
    flag = False
    for scenario_step in scenario.steps:
        scenario_step.failed = None if flag else False
        if scenario_step == step:
            scenario_step.exception = exception
            scenario_step.failed = True
            flag = True
    driver = pytest.globalDict['_browser']
    try:
        scenario.attach(driver.get_screenshot_as_base64(), media_type='image/png')
    except:
        pass
    if request.config.option.export_results == 'true':
        add_scenario_to_run(request, scenario)


def add_scenario_to_run(request, scenario):
    scenario.data_set = {}
    for key, value in request.node.funcargs.items():
        if key in scenario.params:
            scenario.data_set.update({key: value})

    suite_name = scenario.feature.name.split(' - ')[0]
    if suite_name not in pytest.globalDict['scenarios_run']:
        pytest.globalDict['scenarios_run'][suite_name] = []
    pytest.globalDict['scenarios_run'][suite_name].append(scenario.name)
    # deepcopy(scenario)
