from selenium.webdriver.common.by import By

class LocatorsReset:

    FIELD_INPUT_PASS = (By.XPATH, "//input[@type='password']") # Поле ввода нового пароля
    BUTTON_EYE= (By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]") #кнопка 'Глаз'
    FIELD_NEW_PASS = (By.XPATH, "//fieldset[1]/div/div") # Поле нового пароля
