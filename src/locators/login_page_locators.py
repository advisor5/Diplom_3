from selenium.webdriver.common.by import By


class LocatorsLogin:

    TITLE_LOGIN = (By.XPATH, "//h2[text()='Вход']") # Заголовок "Вход" на странице входа
    RECOVERY_LINK = (By.LINK_TEXT, 'Восстановить пароль') # Ссылка на восстановление пароля
    FIELD_EMAIL = (By.XPATH, "//input[@name='name']") # Поле "Email" в форме входа
    FIELD_PASSWORD = (By.NAME, 'Пароль') # Поле "Пароль" в форме входа
    BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" в форме входа
