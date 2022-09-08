from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['autofrenorio.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ddg0rhklfbriob',
        'USER': 'ioiwndhycktmsx',
        'PASSWORD': '1d3d5ed1e6f25ec9e2c2a152ac113b7bf14e6aae675854551f5227b0756158cf',
        'HOST': 'ec2-54-204-241-136.compute-1.amazonaws.com',
        'PORT': 5432
    }
}
