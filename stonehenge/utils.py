import django
import os

from django.conf import settings
from django.template.loader import get_template

from stonehenge.stonehenge import settings as stonehenge_settings


def existing_config_file():
    if os.path.isfile('stonehenge_config.py'):
        msg = "ERROR: stonehenge_config.py already exists. Delete file? (y/N)"
        delete_file = input(msg)
        if delete_file in ['y', 'yes']:
            # File will be overwritten by the config file command
            print("Config file will be overwritten")
            return False
        else:
            return True
    return False


def create_new_config_file():
    '''Create a new stonehenge_config.py file'''
    if existing_config_file():
        # User has an existing stonehenge_config.py
        print("Config file detected. Exiting.")
        return
    settings.configure(stonehenge_settings)
    django.setup()
    template = get_template("stonehenge/sample_config.py")
    context = {'foo': 'bar'}
    file_content = template.render(context)
    with open("stonehenge_config.py", "w+") as config_file:
        config_file.write(file_content)
