import os
from pathlib import Path

import environ
from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

env = environ.Env(DEFAULT=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


include(
    "components/apps.py",
    "components/db.py",
    "components/i18n.py",
    "components/media.py",
    "components/security.py",
    optional("local.py"),
)
