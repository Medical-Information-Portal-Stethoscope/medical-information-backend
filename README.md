# medical-information-backend

## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Развертывание в режиме разработчика
### Клонировать репозиторий
```
git clone git@github.com:Medical-Information/medical-information-backend.git
```
### Создать виртуальное окружение
```
python3.11 -n venv venv
```
### Активировать виртуальное окружение
```
. ./venv/bin/activate
```
### Обновить установщик пакетов pip
```
pip install --upgrade pip
```
### Установить зависимости
```
pip install -r ./stethoscope/requirements/dev.txt
```
### В директории stethoscope скопировать файл `.env.example` в `.env` и задать значения переменным

| Переменная | Значение по умолчанию | Описание |
| --- | --- | --- |
| DEBUG | False | Режим отладки |
| SECRET_KEY | None | `from django.core.management.utils import get_random_secret_key; get_random_secret_key()` |
| ALLOWED_HOSTS | * | Список разрешенных хостов, указанных через пробел |
| USE_SQLITE | True | Использовать SQLite вместо PostgreSQL |
| POSTGRES_DB | postgres | Имя базы данных |
| POSTGRES_USER | postgres | Имя пользователя (владельца) базы данных |
| POSTGRES_PASSWORD | postgres | Пароль пользователя (владельца) базы данных |
| POSTGRES_HOST | 127.0.0.1 | ip-адрес хоста, на котором находится база данных |
| POSTGRES_PORT | 5432 | порт, который слушает база данных |
| EMAIL_HOST | *** | адрес smtp-сервера
| EMAIL_HOST_USER | *** | адрес электронной почты
| EMAIL_HOST_PASSWORD | *** | пароль к электронной почте
| EMAIL_PORT | *** | порт smtp-сервера |
### Применить миграции
```
python manage.py migrate
```
### Создать суперпользователя
```
python manage.py createsuperuser
```
### Запустить сервер
```
python manage.py runserver
```
## Полезности
### Ссылки
- Открыть панель администратора [localhost:8000/admin/](http://localhost:8000/admin/)
- Открыть главную страницу [localhost:8000/](http://localhost:8000/)
- Открыть страницу документации API [localhost:8000/api/v1/swagger/](http://localhost:8000/api/v1/swagger/)
### Установка pre-commit хуков
```
pre-commit install
```

### Запросы к API
- Получить список всех пользователей/регистрация пользователя [localhost:8000/api/v1/users/](http://localhost:8000/api/v1/users/)
- Получить (изменить, удалить) информацию о себе [localhost:8000/api/v1/users/me/](http://localhost:8000/api/v1/users/me/)
- Изменения пароля пользователя [localhost:8000/api/v1/users/set_password/](http://localhost:8000/api/v1/users/set_password/)
- Сброс пароля [localhost:8000/api/v1/users/reset_password/](http://localhost:8000/api/v1/users/reset_password/)
- Подтверждение сброса пароля [localhost:8000/api/v1/users/reset_password_confirm/](http://localhost:8000/api/v1/users/reset_password_confirm/)
- Получить токен авторизации [localhost:8000/api/v1/auth/token/login/](http://localhost:8000/api/v1/auth/token/login/)
- Удалить токен авторизации [localhost:8000/api/v1/auth/token/logout/](http://localhost:8000/api/v1/auth/token/logout/)
