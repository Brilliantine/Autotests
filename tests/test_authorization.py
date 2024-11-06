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

appium_server_url = 'http://127.0.0.1:4723'

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.activate_app('ru.rzd.pass.debug')
    yield driver
    driver.quit()

def test_form_authorization(driver):
    sign_in_text_view = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ID, 'ru.rzd.pass.debug:id/sign_in_text_view')))
    assert sign_in_text_view.is_displayed()

    login_button = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="ru.rzd.pass.debug:id/sign_in_text_view"]')
    login_button.click()

    form_authorization = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ID, 'ru.rzd.pass.debug:id/sign_in_by_login_layout')))
    assert form_authorization.is_displayed()

    login_field = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Логин"]')
    login_field.clear()
    login_field.send_keys("prostotest123456789")

    password_field = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Пароль"]')
    password_field.send_keys("Qwerty123")

    login_button = driver.find_element(by=AppiumBy.ID,value='ru.rzd.pass.debug:id/avatar')
    login_button.click()
    time.sleep(1)
    avatar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ID, 'ru.rzd.pass.debug:id/avatar_image_view')))
    assert avatar.is_displayed()
