from selenium.webdriver.common.by import By

from lesson4.pages.base_bage import BasePage
from lesson4.pages.locators import LoginPageLocators


class ProductPageLocators:
    pass


class ProductPage(BasePage):
    def add_basket(self):
        button = self.browser.find_element(By.XPATH, '//button[@class = "btn btn-lg btn-primary btn-add-to-basket"]')
        button.click()
    def check_title(self):
        assert self.browser.find_element(*LoginPageLocators.TITLE_BOOK).text == self.browser.find_element(By.XPATH,'(// strong)[4]').text, 'title book is not found'
    def check_price(self):
        assert self.browser.find_element(*LoginPageLocators.BOOK_PRICE).text == self.browser.find_element(By.XPATH,'(// strong)[6]').text, 'price so bad'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*LoginPageLocators.SUCCESS_MESSAGE), \
            "Увидел искомый элемент - упал. Не появился: успех, тест зеленый"

    def should_success_message(self):
        assert self.is_disappeared(*LoginPageLocators.SUCCESS_MESSAGE), \
            "Ждал до тех пор, пока элемент не исчезнет"