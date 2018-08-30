import os

from stonehenge.utils import PROJECT_DIR
from stonehenge.utils import TEMPLATES_DIR


def generate_stonehenge_file():
    '''Create a new Stonehenge file in the current user directory'''
    template_filepath = os.path.join(TEMPLATES_DIR, 'stonehenge.py')
    with open(template_filepath, 'r') as template_file:
        contents = template_file.read()
    dest = os.path.join(PROJECT_DIR, 'stonehenge.py')
    with open(dest, 'w') as destination_file:
        destination_file.write(contents)
