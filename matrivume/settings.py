try:
    from settings.base_settings import *
except ImportError as exc:
    raise ImportError(
        "Couldn't import development settings from settings_module."
    ) from exc
