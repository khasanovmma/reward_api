from config.settings import env

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", [])
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "content-type",
    "Accept-Language",
]
