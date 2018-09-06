from django.utils.text import slugify

from stonehenge.build_project.steps import install_python_dependencies
from stonehenge.build_project.steps import configure_database
from stonehenge.build_project.steps import setup_version_control
from stonehenge.build_project.steps import build_backend
from stonehenge.build_project.steps import build_frontend


class StonehengeProject:

    def __init__(self, *args, **kwargs):
        super(StonehengeProject, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Stonehenge Project: {0}".format(self.NAME)

    def build(self):
        '''Build the actual project'''
        install_python_dependencies(self)
        configure_database(self)
        setup_version_control(self)
        build_backend(self)
        build_frontend(self)

    @property
    def slug(self):
        slug = self.SLUG or slugify(self.NAME)
        return slug.replace("-", "_")
