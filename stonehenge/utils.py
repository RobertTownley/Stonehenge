import importlib.util
import os
import random
import string

from pathlib import Path
from subprocess import call

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


try:
    config = get_stonehenge_config()
except FileNotFoundError:
    msg = """To use Stonehenge, you'll need to create a file called .stonehenge in
    your user's home directory.

    For more information, visit the Stonehenge documentation at
    https://github.com/RobertTownley/Stonehenge
    """
    raise FileNotFoundError(msg)


def get_user_project_from_filepath(filepath):
    spec = importlib.util.spec_from_file_location('customized_project', filepath)
    customized_project = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(customized_project)
    project = customized_project.Project()
    return project


def copy_from_template(project, template_file, dest=None):
    '''Copies a file from a stonehenge template into the new project'''
    filepath = os.path.join(TEMPLATES_DIR, template_file)
    if template_file.endswith('.swp'):
        return None

    if not dest:
        dest = os.path.join(PROJECT_DIR, template_file)

    with open(filepath, 'r') as read_file:
        contents = read_file.read()

    while "??? " in contents:
        variable = contents.split("??? ")[1].split(" !!!")[0]
        try:
            contents = contents.replace("??? {0} !!!".format(variable), getattr(project, variable))
        except TypeError as e:
            msg = "Attribute '{0}' not defined in project. Error encountered while building {1}."
            raise TypeError(msg.format(variable, template_file))

    with open(dest or os.path.join(PROJECT_DIR, template_file), 'w') as write_file:
        write_file.write(contents)


def generate_password():
    '''Create a pseudo-random password.

    If more security is needed, implement a different password or change the
    password after the project has been generated.
    '''
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))


def git_commit(msg):
    '''Commit the current working code to GitHub'''
    call(['git', 'add', '--all', ':/'])
    call(['git', 'commit', '-m', msg])
