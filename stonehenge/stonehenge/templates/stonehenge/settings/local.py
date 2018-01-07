from .base import *
from .SECRETS import SECRETS

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': SECRETS['DB_NAME'],
        'USER': SECRETS['DB_USER'],
        'PASSWORD': SECRETS['DB_PASSWORD'],
        'HOST': SECRETS['DB_HOST'],
        'PORT': SECRETS['DB_PORT'],
    },
}

STATICFILES_DIRS = [
    os.path.join(
        os.path.dirname(os.path.dirname(BASE_DIR)),
        "node_modules",
    ),
]
