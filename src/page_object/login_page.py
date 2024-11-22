import allure
from src.locators.login_page_locators import LocatorsLogin
from src.page_object.base_page import BasePage


class LoginPage(BasePage):

    title_login = (LocatorsLogin.TITLE_LOGIN)
    recovery_link = (LocatorsLogin.RECOVERY_LINK)
    field_email = (LocatorsLogin.FIELD_EMAIL)
    field_password = (LocatorsLogin.FIELD_PASSWORD)
    button_login = (LocatorsLogin.BUTTON_LOGIN)

    @allure.step("Ожидаем появления заголовка 'Вход'")
    def wait_title_login(self):
        self.def_visibility_of_element_located(self.title_login)
    
    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recovery_link(self):
        self.def_visibility_of_element_located(self.recovery_link).click()
    
    @allure.step("Ввести почту в поле 'Email'")
    def input_email(self, email):
        self.def_visibility_of_element_located(self.field_email).send_keys(email)
    
    @allure.step("Ввести пароль в поле 'Пароль'")
    def input_password(self, password):
        self.def_visibility_of_element_located(self.field_password).send_keys(password)
        
    @allure.step("Клик по кнопке 'Войти'")
    def click_input_button(self):
        self.def_element_to_be_clickable(self.button_login).click()
