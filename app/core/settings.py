"""
Django settings for core project.
"""

from datetime import timedelta
from pathlib import Path

import environ
from corsheaders.defaults import default_headers

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Security Settings
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# CORS Settings
CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS", default=True)
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_HEADERS = list(default_headers) + [
    "ngrok-skip-browser-warning",
]

# Environment
ENVIRONMENT_NAME = env.str("ENVIRONMENT_NAME")
ENVIRONMENT_COLOR = env.str("ENVIRONMENT_COLOR")

# Apps
INSTALLED_APPS = [
    # Django
    "django_admin_env_notice",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Packages
    "storages",
    "django_filters",
    "django_extensions",
    "corsheaders",
    "rest_framework",
    "rest_polymorphic",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    # Project
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Urls
ROOT_URLCONF = "core.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django_admin_env_notice.context_processors.from_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
DATABASES = {"default": env.db("DATABASE_URL")}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Rest Framework Settings
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "base.pagination.AppPagination",
    "PAGE_SIZE": 50,
    # Date Time Formats
    "DATE_FORMAT": "%d/%m/%Y",
    "DATE_INPUT_FORMATS": ["iso-8601", "%d/%m/%Y", "%d-%m-%Y"],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=21),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Internationalization settings
LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="es-mx")
TIME_ZONE = env.str("TIME_ZONE", default="America/Mexico_City")
USE_I18N = env.bool("USE_I18N", default=True)
USE_L10N = env.bool("USE_L10N", default=True)
USE_TZ = env.bool("USE_TZ", default=True)

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"
MEDIA_ROOT = "/vol/web/media"
STATIC_ROOT = "/vol/web/static"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Storage
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS Config
AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL")
AWS_BUCKET_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False

# Banner data
ENVIRONMENT_FLOAT = True
