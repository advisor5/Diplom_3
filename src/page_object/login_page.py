import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators.login_page_locators import LocatorsLogin


class LoginPage:

    title_login = (LocatorsLogin.TITLE_LOGIN)
    recovery_link = (LocatorsLogin.RECOVERY_LINK)
    field_email = (LocatorsLogin.FIELD_EMAIL)
    field_password = (LocatorsLogin.FIELD_PASSWORD)
    button_login = (LocatorsLogin.BUTTON_LOGIN)

    def __init__(self,  driver: Chrome | Firefox):
        self.driver = driver

    @allure.step("Ожидаем появления заголовка 'Вход'")
    def wait_title_login(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.title_login))
    
    @allure.step("Клик по ссылке 'Восстановить пароль'")
    def click_recovery_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.recovery_link)).click()
    
    @allure.step("Ввести почту в поле 'Email'")
    def input_email(self, email):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.field_email)).send_keys(email)
    
    @allure.step("Ввести пароль в поле 'Пароль'")
    def input_password(self, password):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.field_password)).send_keys(password)
        
    @allure.step("Клик по кнопке 'Войти'")
    def click_input_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_login)).click()
