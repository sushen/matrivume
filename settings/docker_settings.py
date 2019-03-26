try:
    from settings.base_settings import *
except ImportError as exc:
    raise ImportError(
        "Couldn't import development settings from settings_module."
    ) from exc

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': 'my_db',
        'PORT': '',
    }
}
