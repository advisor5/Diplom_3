class UserData:
    EMAIL = "sergei_kravchuk10111@yyy.ru"
    NAME = "Sergei"

class Url:
    HOST = "https://stellarburgers.nomoreparties.site/"
    URL_LOGIN = f"{HOST}login"
    URL_RECOVERY_PASS = f"{HOST}forgot-password"
    URL_RESSET_PASS = f"{HOST}reset-password"
    URL_ORDER_HISTORY = f"{HOST}account/order-history"
    URL_TAPE_ORDERS = f"{HOST}feed"
    
class PageData:
    ACTIVE_FIELD = "input_status_active"
    OPENED_MODAL_DETAIL = "modal_opened"
    TITLE_DETAIL = "Детали ингредиента"
    MODAL_CLOSED = "modal_opened"
    COUNTER_VALUE_2 = "2"
    EMPTY = ""

class UserAPI:
    AUTH_REG = "api/auth/register"
    AUTH_USER = "api/auth/user"

class Parameters:
    HEADERS = {"Content-type": "application/json"}