from .base import *

DEBUG = False

ALLOWED_HOSTS = ['peopleontheroad.kr']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password'
    }
}