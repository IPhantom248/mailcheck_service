<h1>Шаблон приложения fastapi + django</h1>
В приложении есть примеры работы с апи, моделями, а также есть подключенная кафка, с возможностью отправить и получить сообщение кафки
<br>
<br>
Пример docker-compose.yml

    example_app:
        image: docreg.millionagents.com:5000/example_app
        command: >
            bash -c "gunicorn --workers=4 main.asgi:app --bind 0.0.0.0:8888 -k uvicorn.workers.UvicornWorker"
            bash -c "python3 /usr/src/app_name/main/kafka/consumer.py
        ports:
            - "192.168.31.132:8888:8888"
        volumes:
            - "/opt/example_app/settings.ini:/usr/src/example_app/settings.ini"

<br>
Модели:<br>
./api/models.py<br>
Схемы(для сериализациии моделей в апи):<br>
./api/schemas.py<br>
Вьюхи:<br>
./api/views.py<br>
Kafka producer:<br>
./main/kafka/producer.py<br>
Kafka consumer:<br>
./main/kafka/consumer.py<br>
