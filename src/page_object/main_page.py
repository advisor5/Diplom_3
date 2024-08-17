import allure
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from src.locators.main_page_locators import LocatorsMain

class MainPage:

    title_collect_burger = (LocatorsMain.TITLE_COLLECT_BURGER)
    title_tape_orders = (LocatorsMain.TITLE_TAPE_ORDERS)
    button_account = (LocatorsMain.BUTTON_PERSONAL_AC)
    button_constructor = (LocatorsMain.BUTTON_CONSTRUCTOR)
    button_tape_orders = (LocatorsMain.BUTTON_TAPE_ORDERS)
    bun_r2_d3 = (LocatorsMain.IMG_BUN_R2_D3)
    modal_ingr = (LocatorsMain.MODAL_INGR)
    modal_title_detail_ingr = (LocatorsMain.MODAL_TITLE_DETAIL_INGR)
    button_cross = (LocatorsMain.BUTTON_CROSS_MODAL)
    section_main = (LocatorsMain.SECTION_MAIN)
    constructor_burger = (LocatorsMain.CONSTRUCTOR_BURGER)
    counter_bun_r2_d3 = (LocatorsMain.COUNTER_BUN_R2_D3)
    button_place_order = (LocatorsMain.BUTTON_PLACE_ORDER)
    order_modal = (LocatorsMain.MODAL_ORDER)
    order_number = (LocatorsMain.ORDER_NUMBER)
    modal_order_opened = (LocatorsMain.MODAL_ORDER_OPENED)
    load_number = (LocatorsMain.LOAD_NUMBER)

    def __init__(self,  driver: Chrome | Firefox):
        self.driver = driver

    @allure.step("Клик по кнопке 'Личных кабинет' на главной странице")
    def click_on_the_account_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.button_account)).click()

    @allure.step("Клик по кнопке 'Конструктор' на главной странице")
    def click_on_the_constructor(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_constructor)).click()
    
    @allure.step("Клик по кнопке 'Лента заказов' на главной странице")
    def click_on_the_tape_orders(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_tape_orders)).click()
        
    @allure.step("Ожидаем отображения заголовка - 'Собери бургер'")
    def wait_title_collect_burger(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.title_collect_burger))
    
    @allure.step("Ожидаем отображения заголовка - 'Лента заказов'")
    def wait_title_tape_orders(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.title_tape_orders))
        
    @allure.step("Кликаем по ингредиенту 'Флюоресцентная булка R2-D3'")
    def click_bun_r2_d3(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.bun_r2_d3)).click()
    
    @allure.step("Ожидаем загрузку модального окна 'Детали ингредиента'")
    def wait_load_modal_ingr_window(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.modal_ingr))

    @allure.step("Получает текст заголовка поля 'Детали ингредиента'")
    def get_text_modal_title(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.modal_title_detail_ingr)).text
    
    @allure.step("Кликаем кнопке - 'Закрыть' модального окна")
    def click_button_cross_in_modal_ingr(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_cross)).click()

    @allure.step("Получает значение атрибута 'class' области с ингредиентами на главной странице")
    def get_class_section_main(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.section_main)).get_attribute("class")
    
    @allure.step("Перетащить ингредиент - 'Флюоресцентная булка'")
    def drag_and_drop_bun_r2_d3_to_constructor(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.bun_r2_d3))
        target = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.constructor_burger))
        ActionChains(self.driver).drag_and_drop(element, target).perform()
    
    @allure.step("Проверяем значение каунтера ингредиент - 'Флюоресцентная булка'")
    def get_text_counter_bun(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.counter_bun_r2_d3)).text

    @allure.step("Кликаем кнопке - 'Оформить заказ' модального окна")
    def click_order_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_place_order)).click()
        
    @allure.step("Ожидаем загрузку модального окна 'Идентификатор заказа'")
    def wait_load_order_modal_window(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.order_modal))

    @allure.step("Получаем номером заказа")
    def get_order_number(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.order_number)).text

    @allure.step("Кликаем кнопке - 'крестик' модального окна заказа")
    def click_button_cross_in_modal_order(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.button_cross)).click()

    @allure.step("Ожидаем окончательную загрузку")
    def wait_load_modal_order(self): 
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.modal_order_opened))
    
    @allure.step("Ожидаем отобразения номера заказа")
    def wait_return_order_number_in_modal(self): 
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.load_number))
