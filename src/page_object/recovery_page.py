import allure
from src.locators.recovery_page_locators import LocatorsRecovery
from src.page_object.base_page import BasePage


class RecoveryPage(BasePage):

    field_email = (LocatorsRecovery.FIELD_EMAIL)
    recover_button = (LocatorsRecovery.RECOVER_BUTTON)
    
    @allure.step("Вводим почту в поле 'Email' ")
    def input_email(self, email):
        self.def_visibility_of_element_located(self.field_email).send_keys(email)

    @allure.step("Нажимаем кнопку 'Восстановить'")
    def click_recover_button(self):
        self.def_element_to_be_clickable(self.recover_button).click()
