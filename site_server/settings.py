from pathlib import Path
from decouple import config as cgf
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import environ

# env = environ.cgf(
#     # set casting, default value
#     DEBUG=(bool, False)
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cgf("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "False"

ALLOWED_HOSTS = ['avaloqsassets.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd Party
    "corsheaders",
    "cloudinary",
    "ckeditor",
    # "rest_framework",
    # Local Apps
    "accounts.apps.AccountsConfig",
    "transactions.apps.TransactionsConfig",
    "investments.apps.InvestmentsConfig",
    "contents.apps.ContentsConfig",
    "fronts.apps.FrontsConfig",
]

AUTH_USER_MODEL = "accounts.CustomUser"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True

# EMAIL CONFIG

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "django_mailjet.backends.MailjetBackend"
MAILJET_API_KEY = cgf("API_KEY")
MAILJET_API_SECRET = cgf("API_SECRET")
# EMAIL_HOST = "in-v3.mailjet.com"
# EMAIL_PORT = 465
# EMAIL_HOST_USER = cgf("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = cgf("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True

SITE_ID = 1

#############

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "site_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "site_server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": cgf("POSTGRES_DB"),
        "USER": cgf("POSTGRES_USER"),
        "PASSWORD": cgf("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        "PORT": "",
    }

    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

cloudinary.config(
    cloud_name=cgf("cloud_name"),
    api_key=cgf("api_key"),
    api_secret=cgf("api_secret"),
    secure=True,
)

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"
