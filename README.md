# API обмена валют

## Используемые технологии
- FastAPI для создания API с автоматической документацией.
- Pydantic для валидации данных.
- Библиотека fastapi-users для регистрации и авторизации.
- Внешний API для получения обменных курсов с помощью requests.
- Модульное тестирование с использованием pytest.
- Конфигурация переменных окружения с использованием environs.
- HTML страницы с CSS и JavaScript для отображения данных.
- Jinja для шаблонизации HTML страниц.
- Запуск приложения с использованием uvicorn.

## Установка 🔧

### 1. Настройка проекта
- Создайте виртуальное окружение и активируйте его.
- Установите зависимости из файла `requirements.txt`.
  ```shell
  pip install -r requirements.txt
  ```

### 2. Конфигурация среды
- Заполните env.dev необходимыми данными:
    ```
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASS=
    
    CURRENCY_API_KEY=your_api_key
    SECRET_KEY=your_secret_key
    ```

### 3. Запуск приложения
- Приложение будет доступно по адресу `http://127.0.0.1:8000`.
  ```shell
  uvicorn main:app --reload
  ```

## Тестирование
- Запустите тесты папки `tests` с помощью команды `pytest`.

## Примеры запросов API

- **Вход пользователя и получение JWT-токена:**
    ```shell
    curl -X POST 'http://127.0.0.1:8000/auth/jwt/login/' --header 'content-type: application/x-www-form-urlencoded' --form 'username="user"' --form 'password="pass"''
    ```

- **Получение списка поддерживаемых валют и их кодов (валидный JWT-токен):**
    ```shell
    curl -X GET 'http://127.0.0.1:8000/currency/get_list/' --header 'Cookie: access_token="Bearer your_jwt_token"'  
    ```

- **Обмен валюты (валидный JWT-токен):**
    ```shell
    curl -X GET 'http://127.0.0.1:8000/currency/exchange/?base=usd&quote=rub&amount=1000' --header 'Cookie: access_token="Bearer your_jwt_token"'  
    ```

## Примеры ответов API

- **Список поддерживаемых валют:**
    ```json
    {
        "AED": "United Arab Emirates Dirham",
        "AFN": "Afghan Afghani",
        "ALL": "Albanian Lek",
        ...
    }
    ```
- **Успешный обмен валюты:**
    ```json
    {
        "success": true,
        "query": {
            "from": "USD",
            "to": "RUB",
            "amount": 1000
        },
        "info": {
            "timestamp": 1700419983,
            "quote": 89.350433
        },
        "result": 89350.433
    }
    ```

## HTML страницы для удобства выполнения запросов

![pic1](https://github.com/egorzhmaev/FastAPIcurrency/blob/master/2024-04-09_23-27-42.png)
