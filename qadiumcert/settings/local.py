from .base import *  # noqa


ADMINS = (
    ('Edgar', 'edgar@qadium.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'qadiumcert',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/qadiumcert_test.db',
        }
    }
