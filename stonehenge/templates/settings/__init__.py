import socket
import sys

if "prod" in socket.gethostname():
    from .production import *
elif "stage" in socket.gethostname():
    from .staging import *
elif "test" in sys.argv and "raven" not in sys.argv:
    from .testing import *
else:
    from .local import *
