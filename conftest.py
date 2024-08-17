import pytest
import random
import string
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options


from src.data.constants import Url
from src.user.user_routes import ApiRegister, ApiUser
from src.page_object.main_page import MainPage
from src.page_object.login_page import LoginPage
from src.page_object.reset_page import ResetPage
from src.page_object.order_page import OrderPage
from src.page_object.account_page import AccountPage
from src.page_object.recovery_page import RecoveryPage


# @pytest.fixture(params=["chrome","firefox"])
# def driver(request):
#     chrome_opt = ChromeOptions()
#     chrome_opt.add_argument("--start-maximized")
#     if request.param == 'chrome':
#         driver = webdriver.Chrome(options=chrome_opt)
#     elif request.param == 'firefox':
#         driver = webdriver.Firefox()
#         driver.maximize_window()
#     else:
#         raise ValueError(f"Unknown browaer: {request.param}")
#     driver.get(Url.HOST)
#     yield driver
#     driver.quit()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(Url.HOST)
    yield driver
    driver.quit()

@pytest.fixture
def generate_random_string():
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(10))
        return random_string

@pytest.fixture
def register_rand_user(generate_random_string):

    email = f"{generate_random_string}@yandex.ru"
    password = "123456!"
    name = generate_random_string
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    
    response = ApiRegister().reg_user(payload)
    access_token = response.json()["accessToken"]

    data_user = []
    data_user.append(email)
    data_user.append(password)
    data_user.append(name)
    
    data_login = {
    "email": data_user[0],
    "password": data_user[1]
    }
    
    yield data_user, data_login, response, access_token 
    ApiUser().delete_user(access_token)

@pytest.fixture
def login(
        driver, 
        register_rand_user,
        main_page: MainPage, 
        login_page: LoginPage
    ):
    data_user = register_rand_user[0]
    email = data_user[0]
    password = data_user[1]

    main_page.click_on_the_account_button()
    login_page.input_email(email)
    login_page.input_password(password)
    login_page.click_input_button()
    yield driver, email

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def recovery_page(driver):
    recovery_page = RecoveryPage(driver)
    return recovery_page

@pytest.fixture
def reset_page(driver):
    reset_page = ResetPage(driver)
    return reset_page

@pytest.fixture
def account_page(driver):
    account_page = AccountPage(driver)
    return account_page

@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
