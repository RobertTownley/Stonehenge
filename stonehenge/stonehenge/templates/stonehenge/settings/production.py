from .base import *
from .SECRETS import SECRETS

ALLOWED_HOSTS = {{ ENVIRONMENTS.PRODUCTION.ALLOWED_HOSTS|safe }}
DEBUG = FALSE
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
SECRET_KEY = SECRETS['SECRET_KEY']

STATICFILES_DIRS = [ 
    os.path.join(
        os.path.dirname(BASE_DIR),
        "node_modules",
    ),  
]
