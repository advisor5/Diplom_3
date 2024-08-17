from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    SECTION_ORDER_DETAIL = (By.XPATH, "//section[2]") # Секция для модального окна с деталями заказа 
    MODAL_ORDER_DETAIL = (By.XPATH, "//section[contains(@class,'modal_opened')]") # Открытое модальное окно с деталями
    ORDER_FIRST_ABOVE = (By.XPATH, "(//li[contains(@class,'OrderHistory')]/a)[1]") # Первый заказ сверху
    SECTION_ORDER_LIST = (By.XPATH, "(//ul[contains(@class,'OrderFeed')])[1]") # Секция со списком заказов
    TOTAL_ORDER_ALL_TIME = (By.XPATH, "//div[2]//p[contains(@class,'OrderFeed_number')]") # Всего заказов за все время
    TOTAL_ORDER_TODAY = (By.XPATH, "//div[3]//p[contains(@class,'OrderFeed_number')]") # Всего заказов за все время
    ORDER_IN_WORK = (
        By.XPATH,
        "//ul[contains(@class,'orderListReady')]/li[contains(@class,'type_digits-default')]"
        ) # Заказы в работе
    LIST_ORDERS = (By.XPATH, "//li/a/div/p[1]") # Список с заказами 50 шт 