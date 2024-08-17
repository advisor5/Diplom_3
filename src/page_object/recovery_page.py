import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.locators.recovery_page_locators import LocatorsRecovery


class RecoveryPage:

    field_email = (LocatorsRecovery.FIELD_EMAIL)
    recover_button = (LocatorsRecovery.RECOVER_BUTTON)

    def __init__(self,  driver: Chrome | Firefox):
        self.driver = driver
    
    @allure.step("Вводим почту в поле 'Email' ")
    def input_email(self, email):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.field_email)).send_keys(email)

    @allure.step("Нажимаем кнопку 'Восстановить'")
    def click_recover_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.recover_button)).click()
