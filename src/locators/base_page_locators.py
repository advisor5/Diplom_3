from selenium.webdriver.common.by import By


class LocatorsBase:
    BUTTON_PERSONAL_AC = (By.XPATH, "//header/nav/a") # Кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор") # Кнопка "Конструктор"
    BUTTON_TAPE_ORDERS = (By.XPATH, "//header/nav//li[2]/a") # Кнопка "Лента Заказов"
