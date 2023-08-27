import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime
import time
from allure_commons.types import AttachmentType


def handle_element(driver, selector, value=0):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    if value:
        element.send_keys(value)
    else:
        element.click()


def get_items_as_number(driver, selector):
    element = driver.find_element(By.CSS_SELECTOR, selector).text
    return float(element.replace("$", ""))

def capture_a_screenshot_and_save_it(driver):
    # Capture a screenshot and save it if the assertion fails
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('screenshots/screenshot-%s.png' % now)
    #print("Test failed! Screenshot saved at:", 'allure_report/screenshot-%s.png' % now)