from stonehenge.projects import DefaultProject


class StonehengeProject(DefaultProject):
    '''Initial project configuration file, created by Stonehenge

    Customize this object to your project's preferred settings.
    Once you're done, execute this file by running python stonehenge.py
    to create, initialize, and deploy your new project.
    '''

    # Your project name
    PROJECT_NAME = "Stonehenge Sample"

    # Project Description, used in Meta attributes of default pages
    PROJECT_DESCRIPTION = "A modern, clean website"

    # Absolute filepath of desired project location on your local filesystem
    PROJECT_ROOT = '/home/robert/Laboratory/SampleStonehenge/'

    # Project Creator, used in HTML meta tags
    PROJECT_AUTHOR = "My Organization"

    # Default language for templates
    PROJECT_LANGUAGE = "en"

    # Local Database Settings
    LOCAL_DATABASE = {
        'HOST': 'localhost',
        'NAME': 'stonehengedb',
        'USER': 'stonehenge',
        'PASSWORD': 'stonehengepassword',
        'POSTGRES_USER_PASSWORD': 'postgres',
    }

    # Virtual Environment and python version to use
    PYTHON_PATH = "/usr/bin/python3"
    VIRTUAL_ENVIRONMENT_NAME = "venv"

    # Version Control
    REMOTE_REPOSITORY = 'git@github.com:RobertTownley/TestStonehenge.git'
    REMOTE_NAME = 'origin'

    # Social Authentication Settings
    # Great guide for social authentication setup:
    # simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
    USE_SOCIAL_AUTHENTICATION = True
    SOCIAL_AUTH_FACEBOOK_KEY = '451821651x33143'
    SOCIAL_AUTH_FACEBOOK_SECRET = '524fada3c3ca5adgb279da535da1d863'

    def validate_system(self):
        '''TODO: Add validation steps'''
        pass

    def validate_project(self):
        '''TODO: Add validation steps'''
        pass

    def build(self):
        self.validate_system()
        self.validate_project()
        self.create_project_root()
        self.create_local_database()
        self.create_virtual_environment()
        self.initialize_git_repository()
        self.install_python_dependencies()
        self.install_frontend_build()
        self.create_django_project()


project = StonehengeProject()
project.build()
