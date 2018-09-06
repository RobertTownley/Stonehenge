import os
import psycopg2
import shutil

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from subprocess import call

from stonehenge.utils import copy_from_template
from stonehenge.utils import copy_dir_from_template
from stonehenge.utils import generate_password
from stonehenge.utils import config
from stonehenge.utils import PROJECT_DIR
from stonehenge.utils import TEMPLATES_DIR
from stonehenge.utils import git_commit


def install_python_dependencies(project):
    '''Installs Python requirements for a project'''
    copy_from_template(project, 'requirements.txt')
    call(['pip', 'install', '-r', 'requirements.txt'])


def configure_database(project):
    '''Configures the PostgreSQL database for the project'''
    if not project.DATABASE_NAME:
        project.DATABASE_NAME = project.slug + "db"
    if not project.DATABASE_USER:
        project.DATABASE_USER = project.slug + "dbuser"
    if not project.DATABASE_PASSWORD:
        project.DATABASE_PASSWORD = generate_password()

    postgres_password = getattr(config, 'POSTGRES_USER_PASSWORD', None)
    if not postgres_password:
        postgres_password = input("PostgreSQL user password: ")
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password=postgres_password,
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Create database user
    try:
        cursor.execute("CREATE USER {0};".format(project.DATABASE_USER))
    except psycopg2.ProgrammingError:
        try:
            cursor.execute("DROP USER {0};".format(project.DATABASE_USER))
            cursor.execute("CREATE USER {0};".format(project.DATABASE_USER))
        except psycopg2.InternalError:
            cursor.execute("DROP DATABASE {0};".format(project.DATABASE_NAME))
            cursor.execute("DROP USER {0};".format(project.DATABASE_USER))
            cursor.execute("CREATE USER {0};".format(project.DATABASE_USER))

    # Set User Password
    cursor.execute("ALTER USER {0} WITH PASSWORD '{1}';".format(
        project.DATABASE_USER,
        project.DATABASE_PASSWORD,
    ))

    # Create Database
    try:
        cursor.execute("CREATE DATABASE {0} OWNER {1};".format(
            project.DATABASE_NAME,
            project.DATABASE_USER,
        ))
    except psycopg2.ProgrammingError:
        cursor.execute("DROP DATABASE {0};".format(project.DATABASE_NAME))
        cursor.execute("CREATE DATABASE {0} OWNER {1};".format(
            project.DATABASE_NAME,
            project.DATABASE_USER,
        ))


def setup_version_control(project):
    '''Configures version control for the project'''
    if os.path.isdir(os.path.join(PROJECT_DIR, '.git')):
        shutil.rmtree(os.path.join(PROJECT_DIR, '.git'))
    if os.path.isfile(os.path.join(PROJECT_DIR, '.gitignore')):
        os.remove(os.path.join(PROJECT_DIR, '.gitignore'))

    call(['git', 'init'])
    call(['git', 'remote', 'add', 'origin', project.GIT_REPOSITORY])
    copy_from_template(project, '.gitignore')


def build_backend(project):
    '''Build the backend project out

    Called after building frontend to accommodate create-react-app
    '''
    # Build the initial project
    call(['django-admin', 'startproject', project.slug, '.'])
    call('python manage.py startapp public'.split(' '))

    # Configure settings
    os.remove(os.path.join(PROJECT_DIR, project.slug, 'settings.py'))
    os.makedirs(os.path.join(PROJECT_DIR, project.slug, 'settings'))
    for settings_file in os.listdir(os.path.join(TEMPLATES_DIR, 'settings')):
        source = os.path.join('settings', settings_file)
        destination = os.path.join(PROJECT_DIR, project.slug, 'settings', settings_file)
        copy_from_template(project, source, dest=destination)

    # Set up URLs
    destination = os.path.join(PROJECT_DIR, project.slug, 'urls.py')
    copy_from_template(project, 'urls.py', dest=destination)

    # Create a template directory for exported webpack bundles
    os.makedirs(os.path.join(PROJECT_DIR, 'templates'))
    destination = os.path.join(PROJECT_DIR, 'templates', 'index.html')
    copy_dir_from_template(project, 'public')
    call('python manage.py migrate'.split(' '))


def build_frontend(project):
    '''Build out the frontend'''
    call(['npx', 'create-react-app', 'frontend'])
    for filename in os.listdir(os.path.join(PROJECT_DIR, 'frontend')):
        if filename != project.slug:
            shutil.move(
                os.path.join(PROJECT_DIR, 'frontend', filename),
                os.path.join(PROJECT_DIR, filename),
            )
    shutil.rmtree(os.path.join(PROJECT_DIR, 'frontend'))
    git_commit("Pre create-react-app ejection commit")
    call(['npm', 'run', 'eject'])  # TODO: Find a way to have this not require user input

    # Install node dependencies
    FRONTEND_DEV_DEPENDENCIES = [
        'style-loader',
        'css-loader',
        'sass-loader',
        'node-sass',
    ]
    for dep in FRONTEND_DEV_DEPENDENCIES:
        call('npm install {0} --save-dev'.format(dep).split(' '))

    # Build out webpack configuration to allow it to talk to Django
    call('npm install webpack-bundle-tracker --save-dev'.split(' '))
    copy_from_template(project, 'config/paths.js')
    copy_from_template(project, 'config/webpack.config.dev.js')
    copy_from_template(project, 'config/webpackDevServer.config.js')
    call('mkdir -p assets/bundles'.split(' '))

    # Create initial React components
    call('npm install --save react-router-dom'.split(' '))
    call('mkdir -p src/components/'.split(' '))
    copy_from_template(project, 'src/App.js')
    components_dir = os.path.join(TEMPLATES_DIR, 'src/components')
    components = os.listdir(components_dir)
    for filepath in components:
        source = os.path.join('src/components', filepath)
        copy_from_template(project, source)
