import os
import psycopg2

from stonehenge.file_validators import validate_config


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
        self.create_virtual_environment()
        self.create_node_modules()
        self.create_django_project()

    def create_local_database(self):
        print("Building database")
        db = self.config['DATABASE']
        connection = psycopg2.connect(
            user='postgres',
            dbname='postgres',
            host=db['HOST'],
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE {0}".format(db['NAME']))

    def initialize_git_repository(self):
        print("Building Git Repo")

    def create_virtual_environment(self):
        print("Creating virtual environment")

    def create_node_modules(self):
        print("Creating node modules")

    def create_django_project(self):
        print("Creating django project")
