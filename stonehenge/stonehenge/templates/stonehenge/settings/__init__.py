import socket
import sys

from .base import *
if socket.gethostname() == "{{ ENVIRONMENTS.PRODUCTION.HOSTNAME }}":
    from .production import *
elif socket.gethostname() == "{{ ENVIRONmENTS.STAGING.HOSTNAME }}":
    from .staging import *
elif "test" in sys.argv:
    from .testing import *
else:
    from .local import *
