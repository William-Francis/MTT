"""
Django settings for mtt project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from mtt import is_true, split_with_comma

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
INSECURE_KEY = "1e57a452a094728c291bc42bf2bc7eb8d9fd8844d1369da2bf728588b46c4e75"
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", INSECURE_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_true(os.getenv("DJANGO_DEBUG", "true"))

ALLOWED_HOSTS = split_with_comma(
    os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost")
)


INTERNAL_IPS = ["127.0.0.1"]

if DEBUG:
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_vite",
    "rest_framework",
    "django_filters",
    "core.apps.CoreConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mtt.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mtt.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        # "NAME": Path(os.environ["DJANGO_SQLITE_DIR"]) / "db.sqlite3",
    }
}
if "POSTGRES_DB" in os.environ:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "mtt",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "en-us")

TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "Africa/Johannesburg")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = os.environ["DJANGO_MEDIA_ROOT"]
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", "/var/www/media")

# URL that handles the media served from MEDIA_ROOT.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = os.getenv("DJANGO_MEDIA_URL", "media/")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

# STATIC_ROOT = os.environ["DJANGO_STATIC_ROOT"]
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT", "/var/www/static")

DJANGO_VITE_DEV_MODE = DEBUG

DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static" / "dist"

STATICFILES_DIRS = [DJANGO_VITE_ASSETS_PATH]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Sessions
SESSION_COOKIE_SECURE = is_true(os.getenv("DJANGO_SESSION_COOKIE_SECURE"))

# Settings for CSRF cookie.
CSRF_COOKIE_SECURE = is_true(os.getenv("DJANGO_CSRF_COOKIE_SECURE"))
CSRF_TRUSTED_ORIGINS = split_with_comma(os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", ""))

# Security Middleware (manage.py check --deploy)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 2  # 2 weeks, default - 0
SECURE_SSL_REDIRECT = is_true(os.getenv("DJANGO_SECURE_SSL_REDIRECT"))
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Email settings
EMAIL_HOST = os.getenv("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.getenv("DJANGO_EMAIL_PORT", 25))
EMAIL_HOST_USER = os.getenv("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("DJANGO_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = is_true(os.getenv("DJANGO_EMAIL_USE_TLS"))

# Email address that error messages come from.
SERVER_EMAIL = os.getenv("DJANGO_SERVER_EMAIL", "root@localhost")

# Default email address to use for various automated correspondence from the site managers.
DEFAULT_FROM_EMAIL = os.getenv("DJANGO_DEFAULT_FROM_EMAIL", "webmaster@localhost")

# People who get code error notifications. In the format
# [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMIN_NAME = os.getenv("DJANGO_ADMIN_NAME", "")
ADMIN_EMAIL = os.getenv("DJANGO_ADMIN_EMAIL")
if ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]


# Log settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            # https://docs.python.org/3/library/logging.html#logrecord-attributes
            "format": "{levelname} [{asctime}] -- {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins", "console"] if not DEBUG else ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

try:
    from .local_settings import *
except ImportError:
    pass
