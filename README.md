# 🏆 Reward API

**Reward API** — backend-приложение на Django, позволяющее управлять пользователями, начислять награды и обрабатывать отложенные задачи через Celery.

---

## 🚀 Стек технологий

- Django 4.2
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- JWT (SimpleJWT)
- drf-spectacular (Swagger)
- Docker / Docker Compose

---

## 📦 Установка и запуск

### 🐳 Запуск через Docker

1. Клонируй проект:

```bash
git clone https://github.com/yourusername/reward-api.git
cd reward-api
```

2. Запуск:

```bash
docker-compose up -d --build
```

3. Применение миграций:

```bash
docker-compose exec web python manage.py migrate
```

4. Создание суперпользователя (по желанию):

```bash
docker-compose exec web python manage.py createsuperuser
```

---

### 💻 Запуск вручную (без Docker)

1. Перейди в папку:

```bash
cd deployment/environment/
```

2. Скопируй `.env.example`:

```bash
cp .env.example .env
```

3. Отредактируй `.env` при необходимости (например, `SECRET_KEY`, `DB` и т.д.)

4. Установи зависимости:

```bash
pip install -r requirements.txt
```

5. Применение миграций:

```bash
python manage.py migrate
```

6. Запусти Redis (если не через Docker):

```bash
docker run -d --name reward_api_redis -p 6379:6379 redis:7
```

7. Запусти Celery:

```bash
celery -A core worker -l info
```

8. Запусти Django-сервер:

```bash
python manage.py runserver
```

---

## 🔑 Аутентификация

JWT-эндпоинты:

| Метод | URL | Назначение |
|-------|-----|------------|
| POST | `/api/token/` | Получить access/refresh токены |
| POST | `/api/token/refresh/` | Обновить токен |
| POST | `/api/token/verify/` | Проверить токен |

---

## 🔧 Основные эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| `GET` | `/api/profile/` | Профиль текущего пользователя |
| `GET` | `/api/rewards/` | Список наград пользователя |
| `POST` | `/api/rewards/request/` | Запрос награды (1 раз в день, выполняется через 5 минут) |

---

## ⏳ Celery & Отложенные задачи

Модель `ScheduledReward` используется для создания отложенной награды, которая:

- Выполняется в заданное `execute_at`
- Начисляет пользователю `coins`
- Логирует награду в `RewardLog`

Celery использует Redis как брокер.

---

## 📘 Swagger

Автогенерация API-документации доступна по адресу:

```
/api/schema/swagger/
```

---

## ✅ Тесты

```bash
python manage.py test
```

Тестируются:

- Аутентификация (получение токена)
- Профиль пользователя
- Ограничение на получение награды раз в день

---

## 📄 Переменные окружения

### 🔄 Использование `.env`

#### 📁 Для Docker:

Используется файл:
```
deployment/environment/.env
```

#### 💻 Для ручного запуска:

1. Скопируй `.env.example`:
```bash
cp deployment/environment/.env.example deployment/environment/.env
```

2. Заполни значения (если нужно):
```env
POSTGRES_DB=rewarddb
POSTGRES_USER=rewarduser
POSTGRES_PASSWORD=rewardpass
SECRET_KEY=your_secret_key
DEBUG=True
```

---

## 🛠 Полезные команды

```bash
docker-compose up --build       # Запустить проект
docker-compose exec web sh      # Зайти внутрь контейнера
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.
