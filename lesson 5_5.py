from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time

logins = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
password = 'secret_sauce'
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

class login_page():
    def __init__(self, driver):
        self.driver = driver
    def entrance(self, login_name, login_password):

        user_name = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_name)
        print('Input login')
        time.sleep(1)
        password = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(login_password)
        print('input password')
        time.sleep(1)
        btn_login = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        btn_login.click()
        print('Click button login')

        get_url = self.driver.current_url
        cur_url = 'https://www.saucedemo.com/inventory.html'
        assert get_url == cur_url
        print('url correct')
    def clean_input(self):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(Keys.CONTROL +'a')
        user_name.send_keys(Keys.DELETE)
        print('login clean')
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(Keys.CONTROL + 'a')
        password.send_keys(Keys.DELETE)
        print('password clean')
for i in logins:
    try:
        user = login_page(driver)
        user.entrance(i, password)
        button_out = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
        button_out.click()
        logout = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
        logout.click()
        print('logout!')
        user.clean_input()
        time.sleep(3)

    except:
        print('Вход не выполнен! Неверный логин', i)
        user.clean_input()
        time.sleep(3)
'''P.S. Зачем снимать блокировку после ввода данных второго пользователя? Работает просто очищение полей.'''