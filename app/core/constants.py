HEADERS = {
    'accept': 'application/json',
    'content-type': 'application/json'
}
"""
HEADERS — Словарь с HTTP-заголовками для API-запросов.
- accept: JSON-ответ.
- content-type: отправляем JSON-данные.
"""
URL_GET_ACCOUNT = 'https://api.shasta.trongrid.io/wallet/getaccount'
"""
Урл для получения баланса кошелька.
"""
URL_GET_ACCOUNT_RESOURCE = (
    'https://api.shasta.trongrid.io/wallet/getaccountresource'
)
"""
Урл для получения energy и bandwidth кошелька.
"""
URL_VALIDATE_ADDRESS = 'https://api.shasta.trongrid.io/wallet/validateaddress'
"""
Урл для валидации адреса кошелька.
"""
URL_DATABASE_DEV = (
    'postgresql+asyncpg://postgres:postgres@localhost:5432/wallet_db'
)
"""
Урл для подключения к тестовой базе данных.
"""
URL_APP_DEV = 'http://localhost:8000'
"""
Урл на котором ращвернуто приложение в Docker Compose.
"""
DATA_FOR_TESTS = {
    'username': 'Mikhail@mail.ru',
    'password': 'qwerty',
}
"""
Тестовый суперпользователь.
"""
VALID_ADDRESS = 'TZCEajSZ67YTmdphnz638zqU1MLxAaJfXz'
"""
Валидный адресс кошелька.
"""
INVALID_ADDRESS = 'TZCEajSZ67YTmdphnz638zqU1MLxAaJfX'
"""
Невалидный адрес кошелька.
"""
URL_LOGIN = '/auth/jwt/login'
"""
Урл для авторизации.
"""
DATABASE_URL_FRO_TEST = (
    'postgresql+asyncpg://postgres:postgres@localhost:5432/wallet_db'
)
