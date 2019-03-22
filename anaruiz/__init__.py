from __future__ import absolute_import, unicode_literals

# Esto sirve para q la aplicacion de Celery se cree siempre
# q Django se inicie
from .celery import app as celery_app

__all__ = ('celery_app',)