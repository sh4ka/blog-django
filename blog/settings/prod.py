from .base import *

ALLOWED_HOSTS += ['blog.jesusfloressanjose.com']

WSGI_APPLICATION = 'blog.wsgi-prod.application'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/www/blog-django/db.sqlite3',
    }
}
