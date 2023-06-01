import time

from celery import Celery

celery = Celery("tasks", broker="redis://redis:6379")


@celery.task()
def some_long_task():
    time.sleep(10)
    return "Done"


celery.autodiscover_tasks()
