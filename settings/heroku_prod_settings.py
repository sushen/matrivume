try:
    from settings.base_settings import *
    import django_heroku
except ImportError as exc:
    raise ImportError(
        "Couldn't import development settings from settings_module."
    ) from exc

DEBUG = False
WSGI_APPLICATION = 'matrivume.heroku_wsgi.application'

django_heroku.settings(locals())
