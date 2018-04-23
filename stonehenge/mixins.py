

class DjangoMixin(object):
    '''Mixin for creating the initial Django project'''

    def create_django_project(self):
        command = 'django-admin startproject {0} .'
        self.run(command.format(self.PROJECT_SLUG))
