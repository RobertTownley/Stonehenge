"""
WSGI config for stonehenge_sample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import socket
import sys

from django.core.wsgi import get_wsgi_application

SETTINGS_MODULE = "{{ PROJECT_SLUG }}.settings"
SOCKET_NAME = socket.gethostname()
if "prod" in SOCKET_NAME:
    SETTINGS_MODULE += ".production"
elif "test" in sys.argv:
    SETTINGS_MODULE += ".test"
else:
    SETTINGS_MODULE += ".local"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

application = get_wsgi_application()
