import importlib.util
import os
import random
import string

from pathlib import Path

BASE_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


def get_stonehenge_config():
    '''Returns system-wide settings that a user has placed into ~/.stonehenge'''
    USER_HOME_DIRECTORY = str(Path.home())
    filepath = os.path.join(USER_HOME_DIRECTORY, '.stonehenge.py')
    spec = importlib.util.spec_from_file_location('settings', filepath)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)
    return settings


config = get_stonehenge_config()


def get_user_project_from_filepath(filepath):
    spec = importlib.util.spec_from_file_location('customized_project', filepath)
    customized_project = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(customized_project)
    project = customized_project.Project()
    return project


def copy_from_template(template_file, dest=None):
    '''Copies a file from a stonehenge template into the new project'''
    with open(os.path.join(TEMPLATES_DIR, template_file), 'r') as read_file:
        contents = read_file.read()
    with open(os.path.join(PROJECT_DIR, dest or template_file), 'w') as write_file:
        write_file.write(contents)


def generate_password():
    '''Create a pseudo-random password.

    If more security is needed, implement a different password or change the
    password after the project has been generated.
    '''
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
