"""Driver Factory"""
import argparse
import os

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def get_driver_config(url_base):
    args = get_args()
    if args.runenv == 'remote':
        driver = get_remote_chrome(args.ipenv)
    elif os.environ.get("RUN_ENV") == 'mobile':
        driver = get_mobile_chorme(args.ipenv)
    else:
        driver = get_local_chrome()
    browser.set_driver(driver)
    browser.config.base_url = url_base
    browser.config.browser_name = 'chrome'
    browser.config.timeout = 7
    browser.config.reports_folder = './reports'
    pytest.globalDict['_browser'] = driver
    return browser


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runenv", "-runenv", help="Run enviroment")
    parser.add_argument("--ipenv", "-ipenv", help="Run enviroment")
    args, unknown = parser.parse_known_args()
    return args


def get_local_chrome():
    return webdriver.Chrome(chrome_options=get_options_chrome())


def get_remote_chrome(ipenv):
    return webdriver.Remote(
        command_executor=f"http://{ipenv}:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
        options=get_options_chrome())


def get_mobile_chorme(ipenv):
    desired_cap = {
        "deviceName": "Galaxy S8",
        "platformName": "Android",
        "version": "9.0",
        "browserName": 'Chrome',
        "realDevice": 'true'
    }
    return webdriver.Remote(command_executor=F"http://{ipenv}:4444/wd/hub", desired_capabilities=desired_cap)


def get_options_chrome():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return options
