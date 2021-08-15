from os import environ


def env(key, default=None):
    if key not in environ:
        return default

    return environ[key]


TELEGRAM_BOT_API_TOKEN = env("TELEGRAM_BOT_API_TOKEN", "")
