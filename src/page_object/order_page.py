import allure
from src.locators.order_page_locator import LocatorsOrderPage
from src.page_object.base_page import BasePage


class OrderPage(BasePage):

    modal_order_detail = (LocatorsOrderPage.MODAL_ORDER_DETAIL)
    first_above = (LocatorsOrderPage.ORDER_FIRST_ABOVE)
    section_order_detail = (LocatorsOrderPage.SECTION_ORDER_DETAIL)
    section_order_list = (LocatorsOrderPage.SECTION_ORDER_LIST)
    total_order_all_time = (LocatorsOrderPage.TOTAL_ORDER_ALL_TIME)
    total_order_today = (LocatorsOrderPage.TOTAL_ORDER_TODAY)
    order_in_work = (LocatorsOrderPage.ORDER_IN_WORK)
    list_orders = (LocatorsOrderPage.LIST_ORDERS)

    @allure.step("Ожидаем загрузку модального окна с деталями заказа")
    def wait_modal_order_detail(self):
        self.def_visibility_of_element_located(self.modal_order_detail)
        
    @allure.step("Кликаем по первому заказу сверху")
    def click_order_first_above(self):
        self.def_visibility_of_element_located(self.first_above).click()
        
    @allure.step("Получает значение атрибута 'class' области с деталями заказа")
    def get_class_section_order_detail(self):
        return self.def_visibility_of_element_located(
            self.section_order_detail).get_attribute("class")
    
    @allure.step("Ожидаем загрузку списка с заказами")
    def wait_order_list(self):
        self.def_visibility_of_element_located(self.section_order_list)

    @allure.step("Проверяем наличие номера заказа в списке")
    def find_number_order(self, number):
        return self.def_text_to_be_present_in_element(self.list_orders, number)
    
    @allure.step("Получаем количество заказов за все время")
    def get_total_order_all_time(self):
        return self.def_visibility_of_element_located(self.total_order_all_time).text

    @allure.step("Получаем количество заказов за сегодня")
    def get_total_order_today(self):
        return self.def_visibility_of_element_located(self.total_order_today).text

    @allure.step("Получаем заказы в работе")
    def get_order_in_work(self):
        return self.def_visibility_of_element_located(self.order_in_work).text
