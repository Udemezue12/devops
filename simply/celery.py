import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','simply.settings.dev')

celery = Celery('simply')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
celery.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
celery.autodiscover_tasks()
