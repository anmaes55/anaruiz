# anaruiz/settings/production.py
from os import environ
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = environ["SECRET_KEY"],

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

# To send emails using SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ADMINS = (('Juan Ruiz', 'juan@quitiweb.com'),)
EMAIL_HOST = 'smtp.dreamhost.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'info@anaruizromero.es'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
