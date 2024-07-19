from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REG_FORM = (By.XPATH, '//form[@id="register_form"]')
    TITLE_BOOK = (By.XPATH, '//h1')
    BOOK_PRICE = (By.XPATH, '(//p[@class="price_color"])[1]')
    SUCCESS_MESSAGE = (By.XPATH, '(//div[@class="alert alert-safe alert-noicon alert-success  fade in"])[1]')
