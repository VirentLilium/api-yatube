# API Yatube

Учебный проект REST API для социальной платформы Yatube.

Проект реализован на Django REST Framework и позволяет работать с публикациями, группами и комментариями через API.

---

## Стек технологий

* Python
* Django
* Django REST Framework
* SQLite
* Token Authentication
* Pytest

---

## Возможности API

API позволяет:

* получать список публикаций;
* создавать публикации;
* получать отдельную публикацию;
* редактировать и удалять свои публикации;
* получать список групп;
* получать информацию об отдельной группе;
* получать комментарии к публикации;
* создавать комментарии;
* редактировать и удалять свои комментарии;
* получать токен авторизации.

---

## Права доступа

* Анонимные пользователи могут только читать данные.
* Авторизованные пользователи могут создавать публикации и комментарии.
* Изменять и удалять публикации или комментарии может только их автор.

---

## 📂 Структура проекта

```text
api-yatube/
├── .gitignore
├── LICENSE
├── README.md
├── pytest.ini
├── requirements.txt
├── setup.cfg
├── .postman/
├── postman/
├── postman_collection/
├── tests/
└── yatube_api/
    ├── manage.py
    ├── api/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── posts/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   └── migrations/
    │
    └── yatube_api/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

---

## ⚙️ Установка и запуск

Клонировать репозиторий:

```bash
git clone https://github.com/VirentLilium/api-yatube.git
```

Перейти в директорию проекта:

```bash
cd api-yatube
```

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать виртуальное окружение.

Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Перейти в директорию с `manage.py`:

```bash
cd yatube_api
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить сервер:

```bash
python manage.py runserver
```

---

## Получение токена

Для получения токена нужно отправить POST-запрос:

```http
POST /api/v1/api-token-auth/
```

Пример тела запроса:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Пример ответа:

```json
{
  "token": "your_token"
}
```

Для авторизованных запросов нужно передавать токен в заголовке:

```http
Authorization: Token your_token
```

---

## Основные эндпоинты

### Публикации

```http
GET /api/v1/posts/
POST /api/v1/posts/
GET /api/v1/posts/{post_id}/
PUT /api/v1/posts/{post_id}/
PATCH /api/v1/posts/{post_id}/
DELETE /api/v1/posts/{post_id}/
```

### Группы

```http
GET /api/v1/groups/
GET /api/v1/groups/{group_id}/
```

### Комментарии

```http
GET /api/v1/posts/{post_id}/comments/
POST /api/v1/posts/{post_id}/comments/
GET /api/v1/posts/{post_id}/comments/{comment_id}/
PUT /api/v1/posts/{post_id}/comments/{comment_id}/
PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
```

## Запуск тестов

Из корневой директории проекта:

```bash
pytest
```

---

## Postman

В проекте есть готовая коллекция Postman:

```text
postman_collection/CRUD_for_yatube.postman_collection.json
```

Её можно импортировать в Postman и использовать для проверки работы API.

---