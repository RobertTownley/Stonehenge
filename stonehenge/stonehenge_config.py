'''Sample configuration file generated by the "stonehenge new" command

When the command 'stonehenge build' is run in the same directory as this file,
settings from this file will be used to create a new project. Set project
parameters here.

This script will be interpreted as python, so feel free to use imports and
modules to generate values. For example, the following code would result in
a project name of "Stonehenge Example 2018" (or whatever year it is):
import datetime
year = datetime.datetime.now().year
PROJECT_NAME = "Stonehenge Example {0}".format(year)
'''
import random
import string

# General Details
PROJECT_NAME = ''

# Version Control
GITHUB_REPOSITORY = ''

'''Database settings

At minimum, the "local" key needs to be given values. This database will be
created locally.

By default, a reasonably-secure password will be randomly generated.
For more security, use a password generated by PerfectPassword at GRC:
    https://www.grc.com/passwords.htm
'''
# Database Settings
DATABASE_PASSWORD = ''.join(
    random.choice(string.ascii_uppercase + string.digits) for _ in range(32)
)

DATABASE = {
    'local': {
        'USER': '',
        'NAME': '',
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
    }
}

# Wrapping all of the above into project configuration
# You probably don't need to edit anything below this line unless you're doing
# more involved customization.
PROJECT_CONFIGURATION = {
    'PROJECT_NAME': PROJECT_NAME,
    'GITHUB_REPOSITORY': GITHUB_REPOSITORY,
    'DATABASE': DATABASE,
}
