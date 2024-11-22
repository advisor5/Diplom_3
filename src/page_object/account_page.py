import allure
from src.locators.account_locators import LocatorsAccount
from src.page_object.base_page import BasePage


class AccountPage(BasePage):
    
    title_profile = (LocatorsAccount.TITLE_PROFILE)
    field_login = (LocatorsAccount.FIELD_LOGIN)
    history_order = (LocatorsAccount.HISTORY_ORDER)
    button_exit = (LocatorsAccount.BUTTON_EXIT)
    last_order_in_list = (LocatorsAccount.LAST_ORDER_IN_LIST)

    @allure.step("Ожидаем появления заголовка 'Профиль'")
    def wait_title_profile(self):
        self.def_visibility_of_element_located(self.title_profile)
    
    @allure.step("Получает значение поля 'Логин'")
    def get_login_field_text(self):
        return self.def_visibility_of_element_located(self.field_login).get_attribute('value')
    
    @allure.step("Кликаем по пункту 'История заказов'")
    def click_history_order(self):
        self.def_element_to_be_clickable(self.history_order).click()
    
    @allure.step("Кликаем по пункту 'Выход'")
    def click_button_exit(self):
        self.def_visibility_of_element_located(self.button_exit).click()
        
    @allure.step("Получает номер последнего заказа в истории заказов")
    def get_last_order_in_list(self):
        return self.def_visibility_of_element_located(self.last_order_in_list).text
    