# Django settings for anaruiz project

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_APP_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(PROJECT_APP_ROOT))
HOST_ROOT = os.path.abspath(os.path.dirname(PROJECT_ROOT))
PUBLIC_ROOT = os.path.abspath(os.path.join(HOST_ROOT, 'public'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '++zp1aynsy_e@1sr)7n%or0%8e77^byh(7p8864739&xl(vgvc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.anaruizromero.es',
    '127.0.0.1',
    'localhost',
]


# Application definition
#sys.path.insert(1, os.path.join(sys.path[0], '..'))
#sys.path.append(BASE_DIR)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'anaruiz.apps.landing',
    'anaruiz.apps.blog',
    'anaruiz.apps.accounts',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'anaruiz.urls'
WSGI_APPLICATION = 'anaruiz.wsgi.application'


# Templates

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates'),'templates', 'anaruiz/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# STATIC_ROOT and STATIC_URL are for static files - files that are used by your web application and don't change by its users
# i.e. static images(you site logo, backgrounds, etc)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# If you are using files, that are uploaded by users, images or not, MEDIA_ROOT and MEDIA_URL are used.
# When you define upload_to it is concatenated with MEDIA_ROOT in your settings.

MEDIA_URL = '/media/'
# /home/rafrom3/anaruiz.club/public/media

#MEDIA_ROOT = '/home/rafrom3/anaruiz.club/public/media/'

# Login/logout redirects to homepage
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# url del broker al que conectamos celery
#CELERY_BROKER_URL = 'amqp://guest@127.0.0.1:5672//'

# PENDIENTE
# Sentry
#import sentry_sdk
#from sentry_sdk.integrations.django import DjangoIntegration

#sentry_sdk.init(
#    dsn="https://eb0f720fdc59403f960c0373bf4fb7a8@sentry.io/1331892",
#    integrations=[DjangoIntegration()])