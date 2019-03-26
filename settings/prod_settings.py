try:
    from settings.base_settings import *
    import django_heroku
except ImportError as exc:
    raise ImportError(
        "Couldn't import development settings from settings_module."
    ) from exc

DEBUG = False

django_heroku.settings(locals())
