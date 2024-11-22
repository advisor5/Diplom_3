from selenium.webdriver.common.by import By


class LocatorsAccount:

    TITLE_PROFILE = (By.XPATH, "//a[text()='Профиль']") # Название "Профиль" в личном кабинете
    FIELD_LOGIN = (By.XPATH, "//input[contains(@value,'@')]") # Поле, содержащее email в личном кабинете
    HISTORY_ORDER = (By.LINK_TEXT, "История заказов") # пункт "История заказов"
    BUTTON_EXIT = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выйти" в личном кабинете
    LAST_ORDER_IN_LIST = (
        By.CSS_SELECTOR, "li:nth-last-child(1) a:nth-child(1) div:nth-child(1) p:nth-child(1)"
    ) # Последний элемент в списке заказов
