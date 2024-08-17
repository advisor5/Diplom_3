import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox

from src.data.constants import PageData
from src.page_object.main_page import MainPage
from src.page_object.order_page import OrderPage
from src.page_object.account_page import AccountPage


class TestOrderFeed:
    
    @allure.title("Тест отображения окна с деталями заказа в ленте заказов")
    @allure.description(
        "Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_opened_details_modal(
        self, 
        main_page: MainPage,
        order_page: OrderPage
    ):  

        main_page.click_on_the_tape_orders()
        order_page.click_order_first_above()

        actually_value = order_page.get_class_section_order_detail()
        expected_value = PageData.OPENED_MODAL_DETAIL
        assert expected_value in actually_value

    @allure.title("Тест отображения заказов пользователя в Ленте заказов")
    @allure.description(
        "Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_displayed_orders_in_orders_list(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage,
        order_page: OrderPage,
        account_page: AccountPage
    ):  
        
        main_page.wait_title_collect_burger()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()
        main_page.click_order_button()
        main_page.wait_load_modal_order()
        main_page.wait_return_order_number_in_modal()
        main_page.click_button_cross_in_modal_order()
        
        main_page.click_on_the_account_button()
        account_page.click_history_order()
        last_order_number = account_page.get_last_order_in_list()
        main_page.click_on_the_tape_orders()
        order_page.wait_order_list()
        
        actually_value = order_page.find_number_order(last_order_number)
        expected_value = True
        assert actually_value == expected_value 

    @allure.title("Тест увеличения значения в счетчике 'Выполнено за все время'")
    @allure.description(
        "Проверка: при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_add_order_increase_total_all_time(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage,
        order_page: OrderPage,
    ):  
        
        main_page.click_on_the_tape_orders()
        total_all_time = int(order_page.get_total_order_all_time())
        main_page.click_on_the_constructor()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()
        main_page.click_order_button()
        main_page.wait_load_modal_order()
        main_page.wait_return_order_number_in_modal()
        main_page.click_button_cross_in_modal_order()
        main_page.click_on_the_tape_orders()
        
        actually_value = int(order_page.get_total_order_all_time())
        expected_value = total_all_time + 1
        assert actually_value == expected_value
    
    @allure.title("Тест увеличения значения в счетчике 'Выполнено за сегодня'")
    @allure.description(
        "Проверка: при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_add_order_increase_total_today(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage,
        order_page: OrderPage,
    ):  
        
        main_page.click_on_the_tape_orders()
        total_today = int(order_page.get_total_order_today())
        main_page.click_on_the_constructor()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()
        main_page.click_order_button()
        main_page.wait_load_modal_order()
        main_page.wait_return_order_number_in_modal()
        main_page.click_button_cross_in_modal_order()
        main_page.click_on_the_tape_orders()
        
        actually_value = int(order_page.get_total_order_today())
        expected_value = total_today + 1
        assert actually_value == expected_value

    @allure.title("Тест отображения созданного заказа в разделе 'В работе'")
    @allure.description(
        "Проверка: после оформления заказа его номер появляется в разделе В работе")
    def test_add_order_displayed_in_work(
        self, 
        login: Chrome | Firefox,
        main_page: MainPage,
        order_page: OrderPage,
    ):  
        
        main_page.click_on_the_constructor()
        main_page.drag_and_drop_bun_r2_d3_to_constructor()
        main_page.click_order_button()
        main_page.wait_load_modal_order()
        main_page.wait_return_order_number_in_modal()
        order_number = main_page.get_order_number()
        main_page.click_button_cross_in_modal_order()
        main_page.click_on_the_tape_orders()
        
        actually_value = order_page.get_order_in_work()
        expected_value = order_number
        assert expected_value in actually_value 
