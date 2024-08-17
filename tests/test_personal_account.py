import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox

from src.data.constants import Url
from src.page_object.main_page import MainPage
from src.page_object.login_page import LoginPage
from src.page_object.account_page import AccountPage


class TestAccount:

    @allure.title("Тест авторизации в личном кабинете")
    @allure.description("Проверяем переход по клику на 'Личный кабинет'")
    def test_click_to_personal_account_transfer_to_account(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage, 
        account_page: AccountPage
    ):  
        main_page.click_on_the_account_button()

        actually_value = account_page.get_login_field_text()
        email = login[1]
        expected_value = email
        assert actually_value == expected_value

    @allure.title("Тест переход в раздел «История заказов»")
    @allure.description("Проверяем, что по выбору пункта 'История заказов' открывается странциа")
    def test_click_to_history_order_transfer_to_history_order(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage, 
        account_page: AccountPage
    ):

        main_page.click_on_the_account_button()
        account_page.click_history_order()

        actually_value = login[0].current_url
        expected_value = Url.URL_ORDER_HISTORY
        assert actually_value == expected_value

    allure.title("Тест выхода из аккаунта")
    @allure.description("Проверяем, что по клику по пункту 'Ввыход', выходим из аккаунта")
    def test_click_to_exit_transfer_to_login_page(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage, 
        login_page: LoginPage,
        account_page: AccountPage
    ):

        main_page.click_on_the_account_button()
        account_page.click_button_exit()
        login_page.wait_title_login()

        actually_value = login[0].current_url
        expected_value = Url.URL_LOGIN
        assert actually_value == expected_value
  