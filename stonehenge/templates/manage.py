#!/usr/bin/env python
import os
import socket
import sys

if __name__ == "__main__":
    SETTINGS_MODULE = "{{ PROJECT_SLUG }}.settings"
    SOCKET_NAME = socket.gethostname()
    if "prod" in SOCKET_NAME:
        SETTINGS_MODULE += ".production"
    elif "test" in sys.argv:
        SETTINGS_MODULE += ".test"
    else:
        SETTINGS_MODULE += ".local"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
