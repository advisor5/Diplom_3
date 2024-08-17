import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators.reset_page_locators import LocatorsReset
from src.data.constants import Url


class ResetPage:

    botton_eye = (LocatorsReset.BUTTON_EYE)
    field_new_pass = (LocatorsReset.FIELD_NEW_PASS)

    def __init__(self,  driver: Chrome | Firefox):
        self.driver = driver

    @allure.step("Ожидаем загрузку страницы Сброса пароля")
    def wait_reset_page(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains(Url.URL_RESSET_PASS))

    @allure.step("Нажимаем на кнопку 'глаз' пароль")
    def click_eye_botton(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.botton_eye)).click()
    
    @allure.step("Получает значение атрибута 'class' у поля - Пароль ")
    def get_class_field(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.field_new_pass)).get_attribute("class")
