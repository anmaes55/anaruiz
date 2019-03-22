from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

# El decorador shared_task sirve para crear tareas independientes a la app.
# La tarea solo es una simulacion.
# Pero se puede usar cualquier libreria y clase aqui. Incluido el ORM para acceder a la BD
@shared_task
def simulate_send_emails(num_emails):
    for i in range(1,num_emails):
        print('Sending email %d' % i)
        # esperamos un segundo
        sleep(1)
    return 'Emails sent'
