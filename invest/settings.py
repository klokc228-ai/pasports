from pathlib import Path
import os

# ----------------------------------------------------
# BASE
# ----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: в проде задашь через переменную окружения
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "dev-insecure-key-change-me"  # на проде ЭТО НЕ ИСПОЛЬЗОВАТЬ
)

# DEBUG: локально True, на хостинге поставишь DJANGO_DEBUG=False
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "False"

# ALLOWED_HOSTS: список доменов, через запятую в переменной
# пример: DJANGO_ALLOWED_HOSTS=drivedocs.site,127.0.0.1,localhost
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# ----------------------------------------------------
# APPS
# ----------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "main",   # твоё приложение
]


# ----------------------------------------------------
# MIDDLEWARE
# ----------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise — раздача статики в проде
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "invest.urls"


# ----------------------------------------------------
# TEMPLATES
# ----------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # шаблоны лежат в main/templates/main — APP_DIRS=True их найдёт
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "invest.wsgi.application"


# ----------------------------------------------------
# DATABASE
# ----------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ----------------------------------------------------
# PASSWORDS
# ----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ----------------------------------------------------
# I18N / TIMEZONE
# ----------------------------------------------------
LANGUAGE_CODE = "ru"
TIME_ZONE = "Europe/Kiev"
USE_I18N = True
USE_TZ = True


# ----------------------------------------------------
# STATIC FILES (CSS, JS, IMG)
# ----------------------------------------------------
# URL, по которому статика отдаётся
STATIC_URL = "/static/"

# Папка с исходной статикой в проекте (у тебя: main/static/main/...)
STATICFILES_DIRS = [
    BASE_DIR / "main" / "static",
]

# Куда collectstatic будет собирать все файлы (для прод-сервера)
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise сторедж — чтобы нормально кэшировалось в проде
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ----------------------------------------------------
# DEFAULT AUTO FIELD
# ----------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
