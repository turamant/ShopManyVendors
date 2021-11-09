

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'viktoraskvart@yandex.ru'
EMAIL_HOST_PASSWORD = 'KkXkJHPJQ7g3L5e'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = 'ShopManyVendors <noreply@viktoraskvart@yandex.ru>'

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