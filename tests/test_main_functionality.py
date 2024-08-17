import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox

from src.data.constants import Url, PageData
from src.page_object.main_page import MainPage
from src.page_object.account_page import AccountPage


class TestFunctionality:
  
    @allure.title("Тест перехода в 'Конструктор'")
    @allure.description(
        "Проверка: по клику на «Конструктор», находявь в личном кабинете, выполняется преход")
    def test_click_to_constructor_transfer_to_completed(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage, 
        account_page: AccountPage
    ):  
        main_page.click_on_the_account_button()
        account_page.wait_title_profile()
        main_page.click_on_the_constructor()
        main_page.wait_title_collect_burger()

        actually_value = login[0].current_url
        expected_value = Url.HOST
        assert actually_value == expected_value

    @allure.title("Тест перехода по клику в 'Ленту заказов'")
    @allure.description(
        "Проверка: по клику на 'Лента заказов', находявь в личном кабинете, выполняется преход")
    def test_click_to_tape_orders_transfer_to_completed(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage, 
        account_page: AccountPage
    ):  
        main_page.click_on_the_account_button()
        account_page.wait_title_profile()
        main_page.click_on_the_tape_orders()
        main_page.wait_title_tape_orders()

        actually_value = login[0].current_url
        expected_value = Url.URL_TAPE_ORDERS
        assert actually_value == expected_value

    @allure.title("Тест отображения всплывающего окна с деталями")
    @allure.description(
        "Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_to_bun_r2_d3_open_modal(self, main_page: MainPage):  

        main_page.click_bun_r2_d3()
        main_page.wait_load_modal_ingr_window()

        actually_value = main_page.get_text_modal_title()
        expected_value = PageData.TITLE_DETAIL
        assert actually_value == expected_value

    @allure.title("Тест закрытия всплывающего окна")
    @allure.description(
        "Проверка: всплывающее окно закрывается кликом по крестику")
    def test_click_to_cross_closed_modal_ingr(self, main_page: MainPage):  

        main_page.click_bun_r2_d3()
        main_page.wait_load_modal_ingr_window()
        main_page.click_button_cross_in_modal_ingr()

        actually_value = main_page.get_class_section_main()
        expected_value = PageData.MODAL_CLOSED
        assert  expected_value not in actually_value

    @allure.title("Тест добавления ингредиента в заказ")
    @allure.description(
        "Проверка: при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_add_bun_r2_d3_to_order_return_counter_two(self, main_page: MainPage):  

        main_page.wait_title_collect_burger()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()

        actually_value = main_page.get_text_counter_bun()
        expected_value = PageData.COUNTER_VALUE_2
        assert  actually_value == expected_value

    @allure.title("Тест оформления заказа пользователем")
    @allure.description(
        "Проверка: авторизованный пользователь может оформить заказ")
    def test_making_an_order(
            self,
            login: Chrome | Firefox,
            main_page: MainPage
        ):  

        main_page.wait_title_collect_burger()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()
        main_page.click_order_button()
        main_page.wait_load_modal_order()
        main_page.wait_return_order_number_in_modal()

        actually_value = main_page.get_order_number()
        print(actually_value) #УДАЛИТЬ
        expected_value = PageData.EMPTY
        assert not actually_value == expected_value
