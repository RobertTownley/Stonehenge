import os
import psycopg2
import shutil

from stonehenge.file_validators import validate_config
from stonehenge.utils import run_command


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

    def build(self):
        self.create_local_database()
        self.initialize_git_repository()
        # self.create_virtual_environment()
        # self.create_node_modules()
        # self.create_django_project()

    def create_local_database(self):
        db = self.config['DATABASE']['local']

        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            user='postgres',
            dbname='postgres',
            host=db['HOST'],
            password=db['POSTGRES_PASSWORD'],
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
        print("-- Database created")

    def initialize_git_repository(self):
        # Delete existing .git folder
        git_location = os.path.join(os.getcwd(), ".git")
        if os.path.isdir(git_location):
            shutil.rmtree(git_location)
        other_files = ['README.md', '.gitignore']
        for other_file in other_files:
            file_location = os.path.join(os.getcwd(), other_file)
            if os.path.isfile(file_location):
                os.remove(file_location)

        # Create new git repo
        run_command("git init")
        run_command("git remote add origin {0}".format(self.config['GITHUB_REPOSITORY']))
        run_command("git pull --quiet origin master")
        print("-- Git repository built")

    def create_virtual_environment(self):
        print("Creating virtual environment")

    def create_node_modules(self):
        print("Creating node modules")

    def create_django_project(self):
        print("Creating django project")
