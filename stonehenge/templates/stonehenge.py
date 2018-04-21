from stonehenge.projects import DefaultProject


class StonehengeProject(DefaultProject):
    '''Initial project configuration file, created by Stonehenge

    Customize this object to your project's preferred settings.
    Once you're done, execute this file by running python stonehenge.py
    to create, initialize, and deploy your new project.
    '''

    # Your project name
    name = "Stonehenge Sample"

    # Absolute filepath of desired project location on your local filesystem
    PROJECT_ROOT = '/home/rtownley/Laboratory/SampleStonehenge/'

    # Local Database Settings
    LOCAL_DATABASE = {
        'HOST': 'localhost',
        'NAME': 'stonehengedb',
        'USER': 'stonehenge',
        'PASSWORD': 'stonehengepassword',
        'POSTGRES_USER_PASSWORD': 'postgres',
    }

    # Virtual Environment and python version to use
    PYTHON_PATH = "/usr/local/bin/python3"
    VIRTUAL_ENVIRONMENT_NAME = "venv"

    # Version Control
    REMOTE_REPOSITORY = 'git@github.com:RobertTownley/TestStonehenge.git'
    REMOTE_NAME = 'origin'

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
        print("I'm getting built!")


project = StonehengeProject()
project.build()
