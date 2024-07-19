from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

driver.maximize_window()

login = 'standard_user'
password = 'secret_sauce'

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

item_1_name = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
product_1 = item_1_name.text
print(product_1)
print('save item 1')
item_1_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
price1 = float(item_1_price.text[1:])

print('save price item 1')
item_btn = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
item_btn.click()
print('add item 1')

item_2_name = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
product_2 = item_2_name.text
print(product_2)
print('save item 2')
item_2_price = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]')
price2 = float(item_2_price.text[1:])
print('save price item 2')
item_btn = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
item_btn.click()
print('add item 2')

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


input_First_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
input_First_name.send_keys('Marina')
print('input First name')
input_Last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
input_Last_name.send_keys('Eryomina')
print('input Last name')
input_postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
input_postal_code.send_keys('614000')
print('input postal-code')
btn_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
btn_continue.click()
print('click continue button')

total_item_name_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text
total_item_name_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]').text
assert total_item_name_1 == product_1
print('name item1 correct')
assert total_item_name_2 == product_2
print('name item2 correct')
total_price = price1+price2
print(total_price)
item_total = driver.find_element(By.XPATH, '//div[@class="summary_subtotal_label"]').text
item_total = item_total[13:]
assert total_price == float(item_total)
print('price correct')

finish_btn = driver.find_element(By.XPATH, '//button[@id="finish"]')
finish_btn.click()
print('finish button correct')

get_url = driver.current_url
cur_url = 'https://www.saucedemo.com/checkout-complete.html'
assert get_url == cur_url
print('congratulation!!!')