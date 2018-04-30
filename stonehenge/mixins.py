import os


class FileMixin(object):

    def copy(self, source, destination):
        '''Utility for copying files to and from the Stonehenge defaults

        Files containing certain uniquely-delimited strings will be copied over
        with their contents altered to match the specific project.
        '''
        if ".swp" in source:
            return None
        if os.path.isfile(source):
            # Single file copy
            with open(source, "r") as source_file:
                contents = source_file.read()
            customized_contents = self.get_customized_contents(contents)
            with open(destination, "w+") as destination_file:
                destination_file.write(customized_contents)
        elif os.path.isdir(source):
            # Recursive file copy
            if not os.path.exists(destination):
                os.makedirs(destination)
            for new_file in os.listdir(source):
                new_filepath = os.path.join(source, new_file)
                new_destination = os.path.join(destination, os.path.basename(new_filepath))
                self.copy(new_filepath, new_destination)
        else:
            raise Exception("Path {0} does not exist".format(source))

    def get_customized_contents(self, contents):
        '''Replace file contents with project-specific settings

        This is used, for example, to replace "~~~PROJECT_NAME~~~" with the
        name of the project.
        '''
        NAMESPACE = [
            'PROJECT_DESCRIPTION',
            'PROJECT_NAME',
            'PROJECT_SLUG',
        ]
        for item in NAMESPACE:
            escape_key = "{{ " + item + " }}"
            contents = contents.replace(escape_key, getattr(self, item, ''))
        return contents


class DjangoMixin(object):
    '''Mixin for creating the initial Django project'''

    def create_django_project(self):
        command = 'django-admin startproject {0} .'
        self.run(command.format(self.PROJECT_SLUG))
        self.create_public_app()
        self.setup_settings_directory()
        self.run_migrations()
        self.setup_urls()

    def create_public_app(self):
        '''Copy the public app from stonehenge templates into the new project

        The public app contains several expected project defaults, including:
            - A custom auth user model
            - Templates for common pages and their components
            - Authentication URLs for account creation, login, and logout
            - An admin for user management

        This command copies all of these templated resources into the
        destination project, customizing them as-needed.
        '''
        stonehenge_public_path = os.path.join(self.STONEHENGE_DIR, "templates/public")
        destination_public_path = os.path.join(self.PROJECT_ROOT, "public")
        self.copy(stonehenge_public_path, destination_public_path)

    def setup_settings_directory(self):
        '''Delete existing settings file and replace it with a directory

        Different settings should be used for different environments, such as
        local, staging, production, testing, and continuous integration. To
        accommodate this, different settings files should be used.

        Once these files are created, manage.py and wsgi.py are both updated
        with logic to decide which settings file to use.
        '''
        existing_settings_path = os.path.join(self.DJANGO_ROOT, "settings.py")
        os.remove(existing_settings_path)

        settings_path = os.path.join(self.STONEHENGE_DIR, "templates/settings")
        destination_path = os.path.join(self.DJANGO_ROOT, "settings")
        self.copy(settings_path, destination_path)

        # Edit manage.py and wsgi.py to be aware of these directories
        self.copy(
            os.path.join(self.STONEHENGE_DIR, "templates/manage.py"),
            os.path.join(self.PROJECT_ROOT, "manage.py"),
        )
        self.copy(
            os.path.join(self.STONEHENGE_DIR, "templates/wsgi.py"),
            os.path.join(self.DJANGO_ROOT, "wsgi.py"),
        )

    def run_migrations(self):
        '''Create and run migration files

        Should be done at least once during project creation to accommodate the
        custom user model in public/models.py
        '''
        self.run_management_command('makemigrations')
        self.run_management_command('migrate')

    def setup_urls(self):
        '''Change urls.py to point to the public views'''
        urls_path = os.path.join(self.STONEHENGE_DIR, "templates/urls.py")
        destination_path = os.path.join(self.DJANGO_ROOT, "urls.py")
        self.copy(urls_path, destination_path)
