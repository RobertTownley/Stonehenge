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


def add_to_string(filedata, content, delimiter, before=False):
    '''Adds the "content" attribute to a string after the delimiter

    The command will error out if the delimiter occurs more than once in a
    string, as this would insert the content unpredictably.

    Usage:
        filedata = 'this is some string'
        content = 'really awesome'
        delimiter = 'some '
        result = add_to_string_after_delimiter(filedata, content, delimiter)
        print(result)  # 'this is some really awesome string'
    '''
    if filedata.count(delimiter) > 1:
        raise Exception("{0} occurs in string more than once".format(delimiter))

    parts = filedata.split(delimiter, 1)
    if before:
        result = "".join([parts[0], content, delimiter, parts[1]])
    else:
        result = "".join([parts[0], delimiter, content, parts[1]])
    return result


def customize_base_settings_data(filedata, config={}):
    '''Takes content of a user's settings/base.py and returns customized data

    '''
    # Installing public before auth to accommodate AUTH_USER_MODEL
    app_content = "'public',\n    "
    delimiter = "'django.contrib.admin'"
    filedata = add_to_string(filedata, app_content, delimiter, before=True)

    # Placing other apps at the bottom of INSTALLED_APPS
    additional_apps = [
        'django_extensions',
    ]
    app_content = "\n" + "\n".join(["    '{0}',".format(app) for app in additional_apps])
    delimiter = "'django.contrib.staticfiles',"  # Last app in the list as of 2.0.1
    filedata = add_to_string(filedata, app_content, delimiter)

    # Adding a custom AUTH_USER_MODEL (the one in public/models.py)
    delimiter = "\nAUTH_PASSWORD_VALIDATORS"
    user_model_content = "\nAUTH_USER_MODEL = 'public.User'\n"
    filedata = add_to_string(filedata, user_model_content, delimiter, before=True)
    return filedata


def get_gitignore_content(config={}):
    '''Generate content that will be appended to the new project's .gitignore'''
    ignored_files = [
        '\n# Project-specific ignores',
        '*SECRETS.py',
    ]
    return "\n".join([ignored_file for ignored_file in ignored_files])


def customize_url_file_content(filedata, config={}):
    '''Generate content that will replace the project's app/urls.py'''
    # Importing public views
    import_content = "\n\nfrom public.views import HomepageView"
    delimiter = "from django.urls import path"
    filedata = add_to_string(filedata, import_content, delimiter)

    # Adding views to urlpatterns
    pattern_content = "\n\n    path('', HomepageView.as_view(), name='homepage'),"
    delimiter = "path('admin/', admin.site.urls),"
    filedata = add_to_string(filedata, pattern_content, delimiter)
    return filedata
