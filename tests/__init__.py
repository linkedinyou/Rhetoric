import unittest
import os


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.testapp.testapp.settings")