# Приложение TronWallet

**TronWallet** - для сбора активности кошелька в сети tron

### 🚀 Особенности
- Регистрация и авторизация пользователей.
- (POST) Запись информации в базу данных  о запрашиваемом колешьке
- (GET) Вывод всех записей c учетом пагинации
- Поддержка асинхронных операций.
- Docker для удобного развертывания.

### 🛠 Используемые технологии:
 - **Python 3.12**
 - **FastAPI**
 - **SQLAlchemy**
 - **Alembic**
 - **PostgreSQL**
 - **Docker / Docker Compose**
 - **asyncpg**
 - **Pytest**

### Пользователи
- Администратор может создавать и просматривать записи.

## Установка и настройка

### Предварительные шаги

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/ваш-аккаунт/tron-wallet.git
cd tron-wallet
```
2. **Создайте файл .env в соответствии с шаблоном .env.example:**
```
APP_TITLE=TronWallet - активность кошелька в сети tron
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=wallet_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# Создание суперюзера
FIRST_SUPERUSER_EMAIL=Mikhail@mail.ru
FIRST_SUPERUSER_PASSWORD=qwerty
SECRET=supersecrert
```
3. **Запустите Docker Compose:**

```bash
docker-compose -f docker-compose_prod.yaml up --force-recreate -d
```


### Документация

http://localhost:8000/docs/

http://localhost:8000/redoc/
