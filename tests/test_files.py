import filecmp
import time
import unittest

from nexussdk.utils.tools import pretty_print
from . import *


class TestResources(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestResources, self).__init__(*args, **kwargs)
        self.nexus = new_client()
        self.org = random_string()
        self.prj = random_string()
        self.nexus.organizations.create(self.org)
        self.nexus.projects.create(self.org, self.prj)
        self.data = {
            "firstname": "Johnny",
            "lastname": "Bravo"
        }

    # Create a resource (NOT providing an ID)
    def _post(self):
        payload = self.nexus.files.create(self.org, self.prj, "tests/an_attachment.txt")
        pretty_print(payload)
        self.nexus.files.fetch(self.org, self.prj, payload["@id"], out_filepath="/tmp/")
        self.assertTrue(filecmp.cmp("tests/an_attachment.txt", "/tmp/an_attachment.txt"))

    # Create a resource (providing an ID)
    def _put(self, id=random_string()):
        payload = self.nexus.files.create(self.org, self.prj, "tests/an_attachment_image.jpg", file_id=id)
        pretty_print(payload)
        self.nexus.files.fetch(self.org, self.prj, id, out_filepath="/tmp/")
        self.assertTrue(filecmp.cmp("tests/an_attachment_image.jpg", "/tmp/an_attachment_image.jpg"))

    def test_list(self):
        self._post()
        self._put()
        time.sleep(10)
        payload = self.nexus.files.list(self.org, self.prj)
        pretty_print(payload)
        self.assertGreater(len(payload["_results"]), 0)
