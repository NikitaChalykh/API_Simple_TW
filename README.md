Тестовое задание на вакансию "разработчик на Django"
=====

Описание проекта
----------
Данный проект предствавляет собой тестовое задание на проектирование REST API.

Для аутентификации в проекте примненяется JWT-токен.

Дополнительно настроены модели для админки и подключена автодокументация API.

Эндпоинт создания пользователя - ```http://127.0.0.1:8000/api/auth/users/```

Эндпоинт получения JWT токена - ```http://127.0.0.1:8000/api/auth/jwt/create/```

Системные требования
----------
* Python 3.8+
* Works on Linux, Windows, macOS, BSD

Стек технологий
----------
* Python 3.8
* Django 2.2
* SQLite3
* Django Rest Framework
* djoser

Установка проекта из репозитория (Linux и macOS)
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:NikitaChalykh/API_Simple_TW.git

cd API_Simple_TW
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv env

source env/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```
4. Выполнить миграции:
```bash
cd simple_api

python manage.py migrate
```
5. Запустить проект (в режиме тестового сервера Django):
```bash
python manage.py runserver
```

Документация к проекту
----------
Документация для API после установки доступна по адресу ```http://127.0.0.1:8000/redoc/```.
