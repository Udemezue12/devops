release: python manage.py migrate

web: waitress-serve --port=$PORT simply.wsgi:application


worker: celery -A simply worker -l info
