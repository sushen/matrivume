import django_heroku
from settings.base_settings import *

DEBUG = False
WSGI_APPLICATION = 'matrivume.heroku_wsgi.application'

django_heroku.settings(locals())
