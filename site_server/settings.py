from pathlib import Path
import os
# import django_heroku
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Initialise environment variables
env = environ.Env()
environ.Env.read_env(
    DEBUG=(bool, False),
    EMAIL_USE_TLS=(bool, True),
    SECURE=(bool, True)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

# ALLOWED_HOSTS = ["vicsites.herokuapp.com", "http://siteserver-env.eba-f5mm2bqz.us-east-1.elasticbeanstalk.com"]
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["vicsites.herokuapp.com"]


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
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    "cloudinary_storage",
    "cloudinary",
    "ckeditor",
    # Local Apps
    "accounts.apps.AccountsConfig",
    "transactions.apps.TransactionsConfig",
    "investments.apps.InvestmentsConfig",
    "contents.apps.ContentsConfig",
]

AUTH_USER_MODEL = "accounts.CustomUser"

# EMAIL CONFIG
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.avaloqsassets.com"
EMAIL_HOST = "server87.web-hosting.com"
EMAIL_PORT = 465
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = env("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = env("EMAIL_HOST_USER")

SITE_ID = 1

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
# ]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "/accounts/auth/users/reset_password_confirm/{uid}/{token}",
    # "PASSWORD_RESET_CONFIRM_URL": "email/reset/confirm/{uid}2efetg34t/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    'EMAIL': {
        "password_reset": "djoser.email.PasswordResetEmail",
        "password_changed_confirmation": "djoser.email.PasswordChangedConfirmationEmail",
    },
    "SERIALIZERS": {
        "user_create": "accounts.serializers.UserCreateSerializer",  # custom serializer
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "user_delete": "djoser.serializers.UserSerializer",
        "password_reset": "djoser.serializers.SendEmailResetSerializer",
        "password_reset_confirm": "djoser.serializers.PasswordResetConfirmSerializer",
    },
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

# CORS_ORIGIN_ALLOW_ALL = False

CORS_ALLOW_CREDENTIALS: True

CORS_ALLOWED_ORIGINS = [
    "https://crypto-bank-dashboard.vercel.app",
    "https://vicsites.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://crypto-bank-dashboard.vercel.app",
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8000",
    "http://localhost:3000",
    "https://crypto-bank-dashboard.vercel.app",
    #   'https://crypto-bank-dashboard.vercel.app/'
)

ROOT_URLCONF = "site_server.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "site_server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
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
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# django_heroku.settings(locals())

# CLOUDINARY_URL= env("CLOUDINARY_URL")
cloudinary.config(
  cloud_name = "dilshekwz",
  api_key = "732985572112147",
  api_secret = "sEoMHN05aeJllHFmf6X3pF5WPLs",
  secure = True
)
