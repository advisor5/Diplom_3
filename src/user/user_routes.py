import allure
import requests
from src.data.constants import Url, UserAPI, Parameters


class ApiRegister:

    @allure.step("POST запрос на ручку 'api/auth/register' - регистрация пользователя")
    def reg_user(self, data):
        return requests.post(f"{Url.HOST}{UserAPI.AUTH_REG}", data)

class ApiUser:

    @allure.step("DELETE запрос на ручку 'api/auth/user' - удаление пользователя")    
    def delete_user(self, access_token):
        headers = Parameters.HEADERS
        headers["authorization"] = access_token
        return requests.delete(f"{Url.HOST}{UserAPI.AUTH_USER}", headers=headers)

    @allure.step("GET запрос на ручку 'api/auth/user' - получение данных пользователя")    
    def get_user(self, access_token):
        headers = Parameters.HEADERS
        headers["authorization"] = access_token
        return requests.get(f"{Url.HOST}{UserAPI.AUTH_USER}", headers=headers)
