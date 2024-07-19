from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('url', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    browser.get(link)

    log_in = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="ember459"]')))
    log_in.click()
    print('Нажата кнопка войти')

    email = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_email"]')))
    email.send_keys('eryomina.job@gmail.com')

    password = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="id_login_password"]')))
    password.send_keys('Maar159e')
    print('Введены емейл и пароль')
    btn_ok = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="sign-form__btn button_with-loader "]')))
    btn_ok.click()
    print('Нажата кнопка вход')
    field_text = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="ember-text-area ember-view textarea string-quiz__textarea"]')))
    field_text.send_keys(Keys.CONTROL + 'a')
    field_text.send_keys(Keys.DELETE)
    answer = math.log(int(time.time()))
    field_text.send_keys(answer)
    print('текст с ответом добавлен')
    time.sleep(1)
    btn_ans = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class ="submit-submission"]')))
    btn_ans.click()
    print('нажата кнопка ответить')
    time.sleep(1)
    correct_text = browser.find_element(By.XPATH, '//p[@class ="smart-hints__hint"]').text
    result = 'Correct!'
    assert correct_text == result

    browser.quit()
