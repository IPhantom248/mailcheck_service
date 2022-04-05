from celery import Celery
from celery.schedules import crontab
from decouple import config

BROKER_URL = config("BROKER_URL", default="redis://localhost:6379")

app = Celery("main", include=["main.tasks"])
app.conf.broker_url = BROKER_URL
app.conf.result_backend = BROKER_URL

app.conf.beat_schedule = {
    "refresh-every-day": {
        "task": "run_refresh_domains",
        "schedule": crontab(hour="*/24"),
    },
}
