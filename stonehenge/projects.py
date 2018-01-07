import django
import os
import psycopg2
import shutil
import subprocess

from distutils.dir_util import copy_tree
from django.conf import settings
from django.template.loader import get_template

from stonehenge.file_validators import validate_config
from stonehenge.stonehenge import settings as stonehenge_settings


def build_new_project():
    '''Read in the stonehenge_config.py and configure project'''
    config_file = os.path.join(os.getcwd(), "stonehenge_config.py")
    CONFIG = validate_config(config_file)
    project = StonehengeProject(CONFIG)
    project.build()


class StonehengeProject(object):
    '''Object representation of a new project'''

    def __init__(self, CONFIG, *args, **kwargs):
        self.config = CONFIG
        settings.configure(stonehenge_settings)
        django.setup()
        self.BASE_DIR = os.path.join(
            os.getcwd(),
            self.config['DJANGO_SETTINGS']['PROJECT_NAME']
        )
        self.STONEHENGE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.STONEHENGE_TEMPLATES_DIR = os.path.join(
            self.STONEHENGE_DIR,
            'stonehenge/templates',
        )

    def run_command(self, command):
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
        )
        process.communicate()

    def run_management_command(self, command):
        command = "{0}/bin/python {1} {2}".format(
            self.config['VIRTUAL_ENVIRONMENT_NAME'],
            os.path.join(os.getcwd(), self.config['DJANGO_SETTINGS']['PROJECT_NAME'], 'manage.py'),
            command,
        )
        self.run_command(command)

    def build(self):
        # self.create_local_database()
        # self.initialize_git_repository()
        # self.create_virtual_environment()
        # self.create_node_modules()
        # self.install_pip_modules()
        self.create_django_project()

    def create_local_database(self):
        print("-- Creating database")
        db = self.config['DATABASES']['local']

        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            user='postgres',
            dbname='postgres',
            host=db['HOST'],
            password=self.config['LOCAL_POSTGRES_PASSWORD'],
        )
        connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        # Delete database if it currently exists
        command = "SELECT datname from pg_database WHERE datname='{0}';".format(db['NAME'])
        cursor.execute(command)
        if cursor.fetchone():
            cursor.execute("DROP DATABASE {0}".format(db['NAME']))

        # Delete the user if they currently exist
        command = "SELECT 1 FROM pg_roles WHERE rolname='{0}';".format(db['USER'])
        cursor.execute(command)
        if cursor.fetchone():
            cursor.execute("DROP USER {0}".format(db['USER']))

        # Create the database and user
        cursor.execute("CREATE DATABASE {0};".format(db['NAME']))
        cursor.execute("CREATE USER {0};".format(db['USER']))
        cursor.execute("ALTER USER {0} WITH PASSWORD '{1}';".format(
            db['USER'],
            db['PASSWORD'],
        ))
        cursor.execute("GRANT ALL PRIVILEGES ON DATABASE {0} TO {1}".format(
            db['NAME'],
            db['USER'],
        ))

    def initialize_git_repository(self):
        print("-- Building git repository")
        git_location = os.path.join(os.getcwd(), ".git")
        if os.path.isdir(git_location):
            shutil.rmtree(git_location)
        other_files = ['README.md', '.gitignore']
        for other_file in other_files:
            file_location = os.path.join(os.getcwd(), other_file)
            if os.path.isfile(file_location):
                os.remove(file_location)

        # Create new git repo
        self.run_command("git init")
        repo = self.config['GITHUB_REPOSITORY']
        self.run_command("git remote add origin {0}".format(repo))
        self.run_command("git pull --quiet origin master")

    def create_virtual_environment(self):
        print("-- Creating virtual environment")
        env_name = self.config['VIRTUAL_ENVIRONMENT_NAME']
        env_location = os.path.join(os.getcwd(), env_name)
        if os.path.isdir(env_location):
            # Delete existing virtual environment
            shutil.rmtree(env_location)

        self.run_command('python3 -m venv {0}'.format(env_name))

    def create_node_modules(self):
        template = get_template("stonehenge/sample_package.json")
        context = self.config
        file_content = template.render(context)
        with open('package.json', 'w+') as package_file:
            package_file.write(file_content)

        self.run_command("npm install bootstrap jquery")
        print("-- Creating node modules")

    def install_pip_modules(self):
        print("-- Installing pip modules")
        for module in self.config['PIP_MODULES']:
            command = "{0}/bin/pip install {1}".format(
                self.config['VIRTUAL_ENVIRONMENT_NAME'],
                module,
            )
            self.run_command(command)

    def create_django_project(self):
        print("-- Creating django project")
        django_conf = self.config['DJANGO_SETTINGS']
        django_project_dir = os.path.join(os.getcwd(), django_conf['PROJECT_NAME'])
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

        # self.run_management_command("makemigrations")
        # self.run_management_command("migrate")

    def create_public_app(self):
        PUBLIC_DIR = os.path.join(self.BASE_DIR, 'public')
        STONEHENGE_DIR = os.path.join(
            self.STONEHENGE_DIR,
            'stonehenge/templates/stonehenge/public',
        )
        os.mkdir(PUBLIC_DIR)
        copy_tree(STONEHENGE_DIR, PUBLIC_DIR)

    def customize_settings_files(self):
        self.SETTINGS_DIR = os.path.join(
            self.BASE_DIR,
            self.config['DJANGO_SETTINGS']['PROJECT_NAME'],
            "settings",
        )
        os.mkdir(self.SETTINGS_DIR)

        # Move existing settings.py into settings/base.py
        os.rename(self.SETTINGS_DIR + ".py", self.SETTINGS_DIR + "/base.py")

        # Modifications to settings/base.py
        with open("{0}/base.py".format(self.SETTINGS_DIR), "a") as settings_file:
            content = "\nAUTH_USER_MODEL = 'public.User'\n"
            settings_file.write(content)

        # Create files for local, staging, test, and production
        STONEHENGE_SETTINGS_DIR = os.path.join(
            self.STONEHENGE_TEMPLATES_DIR,
            'stonehenge/settings',
        )

        for settings_filename in os.listdir(STONEHENGE_SETTINGS_DIR):
            settings_filepath = os.path.join(STONEHENGE_SETTINGS_DIR, settings_filename)
            template_name = settings_filepath.replace(
                self.STONEHENGE_TEMPLATES_DIR + "/",
                '',
            )
            template = get_template(template_name)
            file_content = template.render(self.config)
            destination_filepath = os.path.join(self.SETTINGS_DIR, settings_filename)
            with open(destination_filepath, "w+") as destination_file:
                destination_file.write(file_content)
