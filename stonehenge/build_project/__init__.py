from stonehenge.validators import validate_config_file
from .steps import *


def build_project_from_stonehenge_file():
    '''Builds the project'''
    project = validate_config_file()
    project.build()
