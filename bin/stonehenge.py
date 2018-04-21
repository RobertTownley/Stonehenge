#!/usr/bin/env python
import os
import sys

from stonehenge.messages import INTRO_MESSAGE
from stonehenge.cli_utils import create_new_project_file


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print(INTRO_MESSAGE)
        return

    if command.lower() == "new":
        create_new_project_file()
    else:
        msg = "ERROR: Invalid parameter supplied: {0}\n\n"
        print(msg.format(sys.argv[1]))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stonehenge.settings")
    main()
