import os
import psycopg2
import shutil
import subprocess

from stonehenge.utils import PYTHON_DEPENDENCIES


class DefaultProject(object):
    '''Object representation of a new project'''

    def validate_system(self):
        # Confirm that the user has the correct PostgreSQL user password
        pass

    def validate_project(self):
        # Confirm that the project settings are valid
        pass

    def create_project_root(self):
        '''Clear out existing project root location if it exists'''
        command = "rm -rf {0}".format(self.PROJECT_ROOT)
        self.run_system_command(command, cwd=os.getcwd())
        command = "mkdir -p {0}".format(self.PROJECT_ROOT)
        self.run_system_command(command, cwd=os.getcwd())

    def create_local_database(self):
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            user='postgres',
            dbname='postgres',
            host=self.LOCAL_DATABASE['HOST'],
            password=self.LOCAL_DATABASE['POSTGRES_USER_PASSWORD'],
        )
        connection.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        )
        cursor = connection.cursor()

        # Delete database if it currently exists
        command = "SELECT datname from pg_database WHERE datname='{0}';"
        cursor.execute(command.format(self.LOCAL_DATABASE['NAME']))
        if cursor.fetchone():
            command = "DROP DATABASE {0}"
            cursor.execute(command.format(self.LOCAL_DATABASE['NAME']))

        # Delete the user if they currently exist
        command = "SELECT 1 FROM pg_roles WHERE rolname='{0}';"
        cursor.execute(command.format(self.LOCAL_DATABASE['USER']))
        if cursor.fetchone():
            command = "DROP USER {0}"
            cursor.execute(command.format(self.LOCAL_DATABASE['USER']))

        # Create the database and user
        commands = [
            "CREATE DATABASE {0}".format(self.LOCAL_DATABASE['NAME']),
            "CREATE USER {0}".format(self.LOCAL_DATABASE['USER']),
            "ALTER USER {0} WITH PASSWORD '{1}'".format(
                self.LOCAL_DATABASE['USER'],
                self.LOCAL_DATABASE['PASSWORD'],
            ),
            "GRANT ALL PRIVILEGES ON DATABASE {0} TO {1}".format(
                self.LOCAL_DATABASE['NAME'],
                self.LOCAL_DATABASE['USER'],
            ),
        ]
        for command in commands:
            cursor.execute(command)

    def create_virtual_environment(self):
        env_location = os.path.join(
            self.PROJECT_ROOT,
            self.VIRTUAL_ENVIRONMENT_NAME,
        )
        if os.path.isdir(env_location):
            # Delete existing virtual environment
            shutil.rmtree(env_location)

        virtualenv_path = os.path.join(
            self.PROJECT_ROOT,
            self.VIRTUAL_ENVIRONMENT_NAME,
        )
        command = "{0} -m venv {1}".format(
            self.PYTHON_PATH,
            virtualenv_path,
        )
        self.run_system_command(command)
        command = "chmod -R u+x {0}".format(env_location)
        self.run_system_command(command)

    def initialize_git_repository(self):
        git_location = os.path.join(self.PROJECT_ROOT, ".git")
        if os.path.isdir(git_location):
            shutil.rmtree(git_location)
        other_files = ['README.md', '.gitignore']
        for other_file in other_files:
            file_location = os.path.join(self.PROJECT_ROOT, other_file)
            if os.path.isfile(file_location):
                os.remove(file_location)

        # Create new git repo
        command = "git init {0}".format(self.PROJECT_ROOT)
        self.run_system_command(command)
        command = "git --git-dir {0} remote add {1} {2}".format(
            git_location,
            self.REMOTE_NAME,
            self.REMOTE_REPOSITORY,
        )
        self.run_system_command(command)

        # Create .gitignore
        filepath = os.path.join(
            self.STONEHENGE_DIR,
            "templates/.gitignore",
        )
        with open(filepath) as template:
            contents = template.read()

        destination = os.path.join(
            self.PROJECT_ROOT,
            ".gitignore",
        )
        with open(destination, 'w+') as gitignore_destination:
            gitignore_destination.write(contents)

        commands = [
            "git add --all :/",
            "git commit -m 'initialProjectCommit'",
            "git pull origin master",
        ]
        for command in commands:
            self.run_system_command(command)

    def install_python_dependencies(self):
        virtualenv_location = os.path.join(
            self.PROJECT_ROOT,
            self.VIRTUAL_ENVIRONMENT_NAME,
        )
        command = "{0}/bin/pip install --upgrade pip"
        self.run_system_command(command.format(virtualenv_location))
        for dependency in PYTHON_DEPENDENCIES:
            command = "{0}/bin/pip install {1}"
            self.run_system_command(command.format(
                virtualenv_location,
                dependency,
            ))

    def install_frontend_build(self):
        '''Initialize a react app'''
        command = "create-react-app stonehengefrontend"
        self.run_system_command(command)

    def run_system_command(self, command, cwd=None):
        if not cwd:
            cwd = self.PROJECT_ROOT
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            cwd=cwd,
        )
        process.communicate()

    def create_node_modules(self):
        pass

    '''
    def create_django_project(self):
        print("-- Creating django project")
        django_conf = self.config['DJANGO_SETTINGS']
        django_project_dir = os.path.join(
            os.getcwd(), django_conf['PROJECT_NAME']
        )
        if os.path.isdir(django_project_dir):
            shutil.rmtree(django_project_dir)

        command = "{0}/bin/django-admin startproject {1}".format(
            self.config['VIRTUAL_ENVIRONMENT_NAME'],
            django_conf['PROJECT_NAME'],
        )
        self.run_command(command)

        # Configure Django project
        self.create_public_app()
        self.customize_settings_files()
        self.customize_urls()

        self.run_management_command("makemigrations")
        self.run_management_command("migrate")

    def create_public_app(self):
        PUBLIC_DIR = os.path.join(self.BASE_DIR, 'public')
        STONEHENGE_DIR = os.path.join(
            self.STONEHENGE_DIR,
            'stonehenge/templates/stonehenge/public',
        )
        os.mkdir(PUBLIC_DIR)
        copy_tree(STONEHENGE_DIR, PUBLIC_DIR)
    '''

    @property
    def STONEHENGE_DIR(self):
        return os.path.dirname(os.path.abspath(__file__))
