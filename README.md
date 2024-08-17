Дипломный проект. Задание 3: веб-приложение
Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers
Реализованные сценарии

Структура проекта

    в папке allure_results/ - хранятся отчеты о тестировании
    
    в файле src/data/constants.py - константы
    в папке src/locators/ - описаны локаторы
    в папке src/page_object/ - хранятся файлы с классами страниц
    в файле src/user/user_routes.py - API методы
    
    в папке tests/ - хранятся файлы с тестами
    в файле - .gitignore - игнорирование
    в файле - conftest.py - фикстуры
    в файле - requirements.txt - необходимые зависимости
    
Запуск автотестов

Установка зависимостей

    $ pip install -r requirements.txt

Запуск автотестов и создание HTML-отчета

    $ pytest -v -s tests/ --alluredir=allure_results
    