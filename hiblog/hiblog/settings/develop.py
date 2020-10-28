from .base import *  # NOQA


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hiblog',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'qwer789456',
        'PORT': '3306'
    }
}
