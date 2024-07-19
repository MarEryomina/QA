from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import datetime

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)

date = datetime.date.today() + datetime.timedelta(days=10)
print('future_date:', date)

input_date = driver.find_element(By.XPATH, '//input[@id ="datePickerMonthYearInput"]')
input_date.send_keys(Keys.CONTROL + 'a')
input_date.send_keys(Keys.DELETE)
input_date.send_keys(str(date))
print('input future date')