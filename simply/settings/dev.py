from decouple import config 
from .common import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'PASSWORD': config('DB_PASSWORD'),
        'USER': config('DB_USER'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

CELERY_BROKER_URL = 'redis://localhost:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

EMAIL_PORT = config('EMAIL_PORT', default='', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')