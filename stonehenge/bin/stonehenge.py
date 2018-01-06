#!/usr/bin/env python
import os
import sys

from stonehenge.cli_utils import print_help
from stonehenge.utils import create_new_config_file, configure_new_project

COMMANDS = {
    'new': create_new_config_file,
    'build': configure_new_project,
}


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print_help()
        return

    if command in COMMANDS:
        COMMANDS[command]()
    else:
        msg = "ERROR: Invalid parameter supplied: {0}\n\n".format(
            sys.argv[1],
        )
        print_help(msg=msg)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stonehenge.settings")
    main()
