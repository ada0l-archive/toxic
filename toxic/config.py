from os import environ


def env(key, default=None):
    return environ[key] or default


TELEGRAM_BOT_API_TOKEN = env("TELEGRAM_BOT_API_TOKEN", "")
