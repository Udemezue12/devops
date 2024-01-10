release: python manage.py makemigrations --no-input && python manage.py migrate --no-input


web: waitress-serve --port=$PORT simply.wsgi:application


worker: celery -A simply worker -l info
