import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'ru.rzd.pass.debug',
    'appActivity': 'ru.rzd.app.common.gui.MainActivity',
    'appWaitActivity': 'ru.rzd.*',
    'noReset': True
}

appium_sever_url = 'http://127.0.0.1:4723'
