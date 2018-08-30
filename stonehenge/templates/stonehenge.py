from stonehenge.projects import StonehengeProject


class Project(StonehengeProject):
    NAME = 'Best Stonehenge Ever'
    SLUG = None  # Defaults to slugified project name

    # Database Info
    DATABASE_NAME = None  # Defaults to {PROJECT_SLUG}db
    DATABASE_USER = None  # Defaults to {PROJECT_SLUG}dbuser
    DATABASE_PASSWORD = None  # Defaults to a generated string
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = 5432  # Default port for PostgreSQL

    # Version Control
    GIT_REPOSITORY = 'git@github.com:RobertTownley/TestStonehenge.git'

    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
