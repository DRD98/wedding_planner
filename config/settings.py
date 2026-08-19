"""Django local settings for wedding-planner project."""

# from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

import environ

from .base import *  # noqa: F405 F401 F403

# Read from environment variables file
env = environ.Env()
env.read_env(BASE_DIR / '.env')

ALLOWED_HOSTS = env.list(
    "LOCAL_ALLOWED_HOSTS",
    default=[""],
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
    }
}

SECRET_KEY = env(
    "LOCAL_DJANGO_SECRET_KEY",
    default="!!!INSECURE_LOCAL_SECRET!!!",
)

