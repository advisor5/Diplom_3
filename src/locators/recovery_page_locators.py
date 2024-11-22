from selenium.webdriver.common.by import By


class LocatorsRecovery:

    TITLE_RECOVERY = (By.LINK_TEXT, 'Восстановление пароля') # Ссылка на восстановление пароля
    FIELD_EMAIL = (By.XPATH, "//input[@name='name']") # Поле для ввода почты
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']") # Кнопка Восстановить
    