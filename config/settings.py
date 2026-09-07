from pathlib import Path
import environ

from .base import *

env = environ.Env()
env.read_env(BASE_DIR / '.env')

ALLOWED_HOSTS = env.list(
    "LOCAL_ALLOWED_HOSTS",
    default=[""],
)

if "RENDER_EXTERNAL_HOSTNAME" in os.environ:
    ALLOWED_HOSTS.append(os.environ["RENDER_EXTERNAL_HOSTNAME"])

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = env(
    "LOCAL_DJANGO_SECRET_KEY",
    default="!!!INSECURE_LOCAL_SECRET!!!",
)

