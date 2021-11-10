"""
Django settings for configShop project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

try:
    from .local_settings import *
except ImportError:
    pass


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = '#vgiuvihif9797f8fv89yv98fy9fvy9fyv988ydv98fyf98vy98fdyv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#login vendor
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

#cart
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'




STRIPE_PUB_KEY = 'pk_test_51IaGrcHeqmgb1QiuG622WhjRNTSICaqPuSAmr8xHf2NU7s61CWqWofWjxD6lJEeJUDUED9Vv9FFvFihrGTOINZNq00IlAF4Bcm'
STRIPE_SECRET_KEY ='sk_test_51IaGrcHeqmgb1QiuAPQVtpvRrfNXDhOYHrpREKSjKf7MbVEgVhSNpZXVHeOD2ojNVDWuSs23tbsSeU6RZr0Lk78500pdAirsRO'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'viktoraskvart@yandex.ru'
EMAIL_HOST_PASSWORD = 'KkXkJHPJQ7g3L5e'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = 'ShopManyVendors <noreply@viktoraskvart@yandex.ru>'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.cart',
    'apps.core',
    'apps.order',
    'apps.product',
    'apps.vendor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'configShop.urls'

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
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'configShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop_many_sellers',
        'USER': 'columb',
        'PASSWORD': 'olimp',
        'HOST': '127.0.0.1',
        'PORT': 5432,
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]




STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



import dj_database_url
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
