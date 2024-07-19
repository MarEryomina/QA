from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

def test_find_button_(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    browser.maximize_window()
    time.sleep(10)

    button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-default"]')))
    amount = []
    amount.append(button)
    assert len(amount)>0