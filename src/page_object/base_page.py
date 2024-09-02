import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators.base_page_locators import LocatorsBase


class BasePage:
    button_account = (LocatorsBase.BUTTON_PERSONAL_AC)
    button_constructor = (LocatorsBase.BUTTON_CONSTRUCTOR)
    button_tape_orders = (LocatorsBase.BUTTON_TAPE_ORDERS)

    def __init__(self,  driver: Chrome | Firefox):
        self.driver = driver

    @allure.step("Клик по кнопке 'Личных кабинет' на главной странице")
    def click_on_the_account_button(self, time=5):
        WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(self.button_account)).click()
        
    @allure.step("Клик по кнопке 'Конструктор' на главной странице")
    def click_on_the_constructor(self, time=5):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(self.button_constructor)).click()
        
    @allure.step("Клик по кнопке 'Лента заказов' на главной странице")
    def click_on_the_tape_orders(self,  time=5):
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(self.button_tape_orders)).click()
    
    def def_visibility_of_element_located(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator))
    
    def def_invisibility_of_element_located(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator))
        
    def def_element_to_be_clickable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator))
    
    def def_invisibility_of_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element(locator))
    
    def def_text_to_be_present_in_element(self, locator, number, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.text_to_be_present_in_element(locator, number))
    
    def def_url_contains(self, url, time=5):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url))
