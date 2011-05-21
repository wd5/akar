# -*- coding: utf-8 -*-

import os, sys

def rel(*args):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *args)

DEBUG = True

# start django-registration settings
ACCOUNT_ACTIVATION_DAYS = 2 # кол-во дней для хранения кода активации
# для отправки кода активации
AUTH_USER_EMAIL_UNIQUE = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@akarinvest.ru'
# end django-registration settings

ADMINS = (
    ('Yunin Ivan', 'yu7@yu7.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('sqlite_mysite_db2'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

FIRST_DAY_OF_WEEK = 1

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = rel('media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bbi2o_ossr*(7*r1vri)ug)+yyh1=0(9-ham#u13gihda6iv@f'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    rel('templates'),
)

INSTALLED_APPS = (
    # base
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'django.contrib.comments',

    # dependencies
    #'google_analytics',    # git://github.com/clintecker/django-google-analytics.git/
    #'registration',        # http://bitbucket.org/ubernostrum/django-registration/

    # applications
    'blog',
    'gallery',
    'news',
    'realty',
    'registration',
)


