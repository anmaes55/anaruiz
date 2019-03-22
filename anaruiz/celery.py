from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer las opciones de Django para la aplicacion de celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anaruiz.settings')

# Crear la aplicacion de Celery
app = Celery('anaruiz')

# Especificamos q las vbles de config de Celery se encuentran
# en el fichero settings.py de Django.
# El parametro namespace es para decir q las vbles de config
# de Celery en el fichero settings empiezan por el prefijo *CELERY_*
app.config_from_object('django.conf:settings', namespace='CELERY')

# Este metodo auto-registra las tareas para el broker.
# Busca tareas dentro de todos los archivos tasks.py q hay en las apps
# y las envia a RabbitMQ automaticamente
app.autodiscover_tasks()