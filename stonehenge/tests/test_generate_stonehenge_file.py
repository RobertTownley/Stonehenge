from unittest import TestCase

from stonehenge.new_project import generate_stonehenge_file


class GenerateStonehengeFileTestCase(TestCase):

    def test_file_is_generated(self):
        generate_stonehenge_file()
