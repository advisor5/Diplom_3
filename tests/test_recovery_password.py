import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox

from src.data.constants import Url, UserData, PageData
from src.page_object.base_page import BasePage
from src.page_object.main_page import MainPage
from src.page_object.login_page import LoginPage
from src.page_object.reset_page import ResetPage
from src.page_object.recovery_page import RecoveryPage


class TestRecovery:

    email = UserData.EMAIL

    @allure.title(
        "Тест перехода на страницу восстановления пароля по кнопке 'Восстановить пароль'"
    )
    @allure.description("Проверяем текущий URL с URL страницы восстановления пароля")
    def test_click_the_recovery_password_button_open_recovery_page(
        self, 
        driver: Chrome | Firefox,
        base_page: BasePage,
        main_page: MainPage,
        login_page: LoginPage
    ):
        main_page.wait_title_collect_burger()
        base_page.click_on_the_account_button()
        login_page.click_recovery_link()

        actually_value = driver.current_url
        expected_value = Url.URL_RECOVERY_PASS
        assert actually_value == expected_value

    @allure.title("Тест перехода на страницу сброса пароля")
    @allure.description(
        "Проверяем, что после ввода почты и клика по кнопке 'Восстановить' открывается страницы сброса пароля"
    )
    def test_click_the_recovery_button_open_reset_page(
        self,
        driver: Chrome | Firefox,
        base_page: BasePage,
        login_page: LoginPage,
        recovery_page: RecoveryPage,
        reset_page: ResetPage
    ):

        base_page.click_on_the_account_button()
        login_page.click_recovery_link()
        recovery_page.input_email(self.email)
        recovery_page.click_recover_button()
        reset_page.wait_reset_page()

        actually_value = driver.current_url
        expected_value = Url.URL_RESSET_PASS
        assert actually_value == expected_value

    @allure.title("Тест активации подсветки поля ввода нового пароля")
    @allure.description(
        "Проверяем: клик по кнопке показать/скрыть пароль \
    на странице восстановления пароля делает поле активным — подсвечивает его"
    )
    def test_click_eye_botton_activate_field_pass(
        self,
        base_page: BasePage,
        login_page: LoginPage,
        recovery_page: RecoveryPage,
        reset_page: ResetPage
    ):

        base_page.click_on_the_account_button()
        login_page.click_recovery_link()
        recovery_page.input_email(self.email)
        recovery_page.click_recover_button()
        reset_page.wait_reset_page()
        reset_page.click_eye_botton()

        actually_value = reset_page.get_class_field()
        expected_value = PageData.ACTIVE_FIELD
        assert expected_value in actually_value
