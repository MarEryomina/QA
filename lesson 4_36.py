from selenium import webdriver
from selenium.webdriver.common.by import By

login = 'standard_user'
password = 'secret_sauce'
product = ''
price = 0
def Login():

    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    user_name.send_keys(login)
    print('Input login')
    password_input = driver.find_element(By.XPATH, '//input[@id="password"]')
    password_input.send_keys(password)
    print('Input password')
    btn_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    btn_login.click()
    print('Click button login')
    get_url = driver.current_url
    cur_url = 'https://www.saucedemo.com/inventory.html'
    assert get_url == cur_url
    print('url correct')

def add_item(name, count, button):
    item_name = driver.find_element(By.XPATH, name)
    global product
    product = item_name.text
    print(product)
    print('save item')
    item_price = driver.find_element(By.XPATH, count)
    global price
    price = float(item_price.text[1:])
    print('save price item')
    item_btn = driver.find_element(By.XPATH, button)
    item_btn.click()
    print('add item')

def Basket_check():
    btn_basket = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    btn_basket.click()
    print('click basket button')
    get_url = driver.current_url
    cur_url = 'https://www.saucedemo.com/cart.html'
    assert get_url == cur_url
    print('url coorect 2')
    checkout_btn = driver.find_element(By.XPATH, '//button[@class="btn btn_action btn_medium checkout_button "]')
    checkout_btn.click()
    print('click checkout button')

def date():
    first_name = input('Введите имя:')
    input_First_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    input_First_name.send_keys(first_name)
    print('input First name')
    last_name = input('введите фамилию:')
    input_Last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    input_Last_name.send_keys(last_name)
    print('input Last name')
    postal_code = input('Введите почтовый индекс:')
    input_postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    input_postal_code.send_keys(postal_code)
    print('input postal-code')
    btn_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
    btn_continue.click()
    print('click continue button')

def check_total(total_name,product,price):
    total_item_name = driver.find_element(By.XPATH, total_name).text
    assert total_item_name == product
    print('name item correct')
    total_price = price
    print(total_price)
    item_total = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]').text
    item_total = item_total[13:]
    assert total_price == float(item_total)
    print('price correct')

def Finish():
    finish_btn = driver.find_element(By.XPATH, '//button[@id="finish"]')
    finish_btn.click()
    print('finish button correct')
    get_url = driver.current_url
    cur_url = 'https://www.saucedemo.com/checkout-complete.html'
    assert get_url == cur_url
    print('congratulation!!!')
print('Добро пожаловать в интернет магазин!')
a = input('Введите номер товара:')
try:
    if a == '1':
        item = '//a[@id="item_4_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[1]'
        btn_item = '//button[@id="add-to-cart-sauce-labs-backpack"]'
        total_item_name_1 = '//a[@id="item_4_title_link"]'
    elif a == '2':
        item = '//a[@id="item_0_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[2]'
        btn_item = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
        total_item_name_1 = '//a[@id="item_0_title_link"]'
    elif a == '3':
        item = '//a[@id="item_1_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[3]'
        btn_item = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
        total_item_name_1 = '//a[@id="item_1_title_link"]'
    elif a == '4':
        item = '//a[@id="item_5_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[4]'
        btn_item = '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'
        total_item_name_1 = '//a[@id="item_5_title_link"]'
    elif a == '5':
        item = '//a[@id="item_2_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[5]'
        btn_item = '//button[@id="add-to-cart-sauce-labs-onesie"]'
        total_item_name_1 = '//a[@id="item_2_title_link"]'
    elif a == '6':
        item = '//a[@id="item_3_title_link"]'
        price_item = '(//div[@class="inventory_item_price"])[6]'
        btn_item = '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'
        total_item_name_1 = '//a[@id="item_3_title_link"]'
except:
    print('Товар не найден!')
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
Login()
add_item(item, price_item, btn_item)
Basket_check()
date()
check_total(item, product, price)
Finish()