FROM python:3.6

WORKDIR /app

ARG requirements=requirements/development.txt

ENV DJANGO_SETTINGS_MODULE=anaruiz.settings.development

COPY anaruiz anaruiz
COPY manage.py /app/
COPY requirements/ /app/requirements/ 

RUN pip install -r $requirements && \
  python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]