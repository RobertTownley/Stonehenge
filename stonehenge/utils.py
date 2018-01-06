import django

from django.conf import settings
from django.template import Context, Template

from stonehenge.stonehenge import settings as stonehenge_settings


def create_new_config_file():
    '''Create a new stonehenge_config.py file'''
    settings.configure(stonehenge_settings)
    django.setup()
    template = Template("stonehenge/sample_config.py")
    context = Context({'foo': 'bar'})
    file_content = template.render(context)
    with open("stonehenge_config.py", "w+") as config_file:
        config_file.write(file_content)


def configure_new_project():
    '''Read in the stonehenge_config.py and configure project'''
    print("This would configure the project based on config.py")
