from .base import *

ALLOWED_HOSTS += ['blog.jesusfloressanjose.com']
WSGI_APPLICATION = 'blog.wsgi-prod.application'
DEBUG = True
