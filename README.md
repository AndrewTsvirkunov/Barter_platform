# Платформа обмена вещами

Веб-приложение на Django, которое позволяет пользователям обмениваться вещами.
<br>Оно включает создание, редактирование и удаление объявлений, а также отправку и получение предложений обмена.

## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/AndrewTsvirkunov/Barter_platform.git

2. Создайте и активируйте виртуальное окружение:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
    (для Windows)
    ```
    python -m venv venv
    source venv/bin/activate
    ```
    (для MacOS/Linux)

3.  Установите зависимости:
    ```
    pip install -r requirements.txt

4.  Создайте базу данных и примените миграции:
    ```
    python manage.py makemigrations
    python manage.py migrate
   
5.  Создайте суперпользователя:
    ```
    python manage.py createsuperuser

## Запуск

1. Запустите сервер разработки:
    ```
    python manage.py runserver
   
2. Откройте браузер и перейдите по адресу:
    ```
    http://127.0.0.1:8000/
   
## Интерфейс

1. Откроется главная страница с размещенными объявлениями c возможностью перемещения между страницами, 
   <br>поиска по заголовкам и словам в описании, а также возможностью создания, 
   редактирования и удаления объявлений.

2. Перейдя по адресу:
    ```
    http://127.0.0.1:8000/api/proposals/
    ```
    откроется интерфейс Django REST Framework со списком предложений на обмен.

3. Админ-панель с подробной информацией об объявлениях и предложениях на обмен, 
   датой публикации и статусом находится по адресу:
    ```
    http://127.0.0.1:8000/admin

## Тестирование

1. Для запуска тестов выполните команду:
    ```
    python manage.py test ads
