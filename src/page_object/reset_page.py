import allure
from src.locators.reset_page_locators import LocatorsReset
from src.data.constants import Url
from src.page_object.base_page import BasePage


class ResetPage(BasePage):

    botton_eye = (LocatorsReset.BUTTON_EYE)
    field_new_pass = (LocatorsReset.FIELD_NEW_PASS)

    @allure.step("Ожидаем загрузку страницы Сброса пароля")
    def wait_reset_page(self):
        self.def_url_contains(Url.URL_RESSET_PASS)

    @allure.step("Нажимаем на кнопку 'глаз' пароль")
    def click_eye_botton(self):
        self.def_visibility_of_element_located(self.botton_eye).click()
    
    @allure.step("Получает значение атрибута 'class' у поля - Пароль ")
    def get_class_field(self):
        return self.def_visibility_of_element_located(self.field_new_pass).get_attribute("class")
