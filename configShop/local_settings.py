STRIPE_PUB_KEY = 'pk_test_51IaGrcHeqmgb1QiuG622WhjRNTSICaqPuSAmr8xHf2NU7s61CWqWofWjxD6lJEeJUDUED9Vv9FFvFihrGTOINZNq00IlAF4Bcm'
STRIPE_SECRET_KEY ='sk_test_51IaGrcHeqmgb1QiuAPQVtpvRrfNXDhOYHrpREKSjKf7MbVEgVhSNpZXVHeOD2ojNVDWuSs23tbsSeU6RZr0Lk78500pdAirsRO'

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