"""
Django settings for svc project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u*uem4%tq7b+8u$z_r)ibd62u!!ino@un+mp4xknmmk74n8t4='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'sslserver',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    'social_django',

    'phonenumber_field',
    'crispy_forms',

    'clients',
    'accounts',
    'professional',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'svc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
]


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '489488048195-rqb0k714dkc3kuj45q0cgvd9f5ksl8ee.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HKfwK7VvZfmlIgpXpXrHSvgW'
HOST = 'https://localhost:5000'
SOCIAL_AUTH_FACEBOOK_KEY = '116954303618847'
SOCIAL_AUTH_FACEBOOK_SECRET = '3fb07848389c705bf5bbec4773d2c69f'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
WSGI_APPLICATION = 'svc.wsgi.application'
ASGI_APPLICATION = 'svc.asgi.application'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
    'ENGINE': 'sql_server.pyodbc',
        'NAME': 'baghiService',
        'HOST': 'DESKTOP-IUNO0HB',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            # 'isolation_level': 'READ UNCOMMITTED',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
# SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = "/social/logging"
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/social/logedin/'
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/social/register/'


AUTH_USER_MODEL = 'accounts.UserList'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
