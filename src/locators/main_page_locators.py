from selenium.webdriver.common.by import By


class LocatorsMain:

    BUTTON_PERSONAL_AC = (By.XPATH, "//header/nav/a") # Кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор") # Кнопка "Конструктор"
    BUTTON_TAPE_ORDERS = (By.XPATH, "//header/nav//li[2]/a") # Кнопка "Лента Заказов"
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")# Заголовок "Собери бургер"
    TITLE_TAPE_ORDERS = (By.XPATH, "//h1[text()='Лента заказов']")# Заголовок "Лента заказов"
    IMG_BUN_R2_D3 = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']") # Ингредиент "Флюоресцентная булка"
    COUNTER_BUN_R2_D3 = (By.XPATH ,"(//div[contains(@class,'counter')])[1]/p") # Счетчик ингредиента Флюоресцентная булка
    CONSTRUCTOR_BURGER = (By.XPATH, "//section[2]/ul") # Конструктор бургера
    MODAL_INGR = (By.XPATH, "//section[contains(@class,'modal_opened')]") # Модально окно открыто
    MODAL_TITLE_DETAIL_INGR = (By.XPATH, "//h2[contains(@class,'modal__title_modified')]") # Модальное окно "Детали ингредиента"
    BUTTON_CROSS_MODAL = (By.XPATH, "//section[contains(@class,'modal_opened')]//button") #кнопка показать пароль
    SECTION_MAIN = (By.XPATH, "//section[contains(@class,'Modal')][1]") # Область с игредиентами на главной странице
    BUTTON_PLACE_ORDER =(By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    
    # Модальное окно оформленного заказа
    MODAL_ORDER = (By.XPATH, "//div[contains(@class,'modal__container')]") # Модальное окно оформленного заказа
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class,'modal__container')]//h2") # Заголовок с номером заказа 
    MODAL_ORDER_OPENED = (By.XPATH, "//section[contains(@class,'modal_opened')]") # Открытое модельное заказа 
    LOAD_NUMBER = (By.XPATH, "//div/div[contains(@class,'modal_opened')]") # Загрузился номер
