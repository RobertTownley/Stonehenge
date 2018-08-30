import os

from stonehenge.utils import get_user_project_from_filepath
from stonehenge.utils import PROJECT_DIR


def validate_config_file():
    filepath = os.path.join(PROJECT_DIR, 'stonehenge.py')
    if not os.path.isfile(filepath):
        raise FileNotFoundError("File not found at {0}".format(filepath))
    project = get_user_project_from_filepath(filepath)

    # Determine if the project configuration is valid
    errors = []  # TODO Add in validation logic
    if errors:
        raise Exception(str(errors))
    return project
