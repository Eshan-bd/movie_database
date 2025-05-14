import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_database.settings")
app = Celery("movie_database")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.event_serializer = 'pickle'# this event_serializer is optional. somehow i missed this when writing this solution and it still worked without.
app.conf.task_serializer = 'pickle'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['application/json', 'application/x-python-serialize']

