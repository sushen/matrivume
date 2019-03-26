FROM python:3.7

ENV PYTHONUNBUFFERED 1

ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt \
    && mkdir /code/

WORKDIR /code/
ADD . /code/

ENV DJANGO_SETTINGS_MODULE=settings.docker_settings
