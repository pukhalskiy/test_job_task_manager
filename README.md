# Task Manager

## Технологии

- Python 3.10
- Django 
- Django REST framework 
- Celery
- RabbitMQ
- Flower
- Elasticsearch
- Docker
- Postgres


### Для развертывания проекта выполните следующие действия:

- Клонируйте проект по SSH:

```text
git@github.com:pukhalskiy/test_job_task_manager.git
```

- Перейдите в директорию проекта и переименуйте файл .emv.example в .env:

- Заполните .env:

```text
POSTGRES_USER=<django_user>
POSTGRES_PASSWORD=<mysecretpassword>
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<secret_key>
DEBUG='False'
HOSTS=<hosts>
TESTING='False'
```

- Запустите docker compose из директории:

```text
docker compose up --build -d
```

- Создайте миграции:
```text
docker exec test_job_task_manager-backend-1 python manage.py makemigrations 
```

- Сделайте миграции:
```text
docker exec test_job_task_manager-backend-1 python manage.py migrate  
```

## Использование API

- Для создание задачи отправьте POST запрос на эндойнт: http://0.0.0.0:8000/api/tasks/

![](https://i.imgur.com/X01dfry.png)

- Для удаления задачи отправьте DELETE запрос на эндпойнт: http://0.0.0.0:8000/api/tasks/id/

![](https://i.imgur.com/wOSE7PU.png)

- Для обновления задачи отправьте PATCH запрос на эндпойнт: http://0.0.0.0:8000/api/tasks/id/

![](https://i.imgur.com/6w6YmZX.png)

- Для получения списка всех задач отправьте GET запрос на эндпоинт: http://0.0.0.0:8000/api/tasks/all_tasks/

![](https://i.imgur.com/0PR8jLH.png)

- Для получения конкретной задачи отправьте GET запрос на эндпоинт: http://0.0.0.0:8000/api/tasks/id/

![](https://i.imgur.com/VzV0JI4.png)

- Так же можно осущиствить поиск задачи при помощи Elasticsearch. Отправьте GET запрос на эндпоинт: http://0.0.0.0:8000/api/search?search=пример_поиска

![](https://i.imgur.com/PY66cm8.png)

- Выполнение задач проходит в асинхронном режиме. Посмотреть статус можно при помощи Flower: http://localhost:5555/

![](https://i.imgur.com/Vpt1Rmr.png)
