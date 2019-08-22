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
        payload = self.nexus.resources.create(self.org, self.prj, self.data)
        payload = self.nexus.resources.fetch(self.org, self.prj, payload["@id"])
        pretty_print(payload)
        self.assertEqual(payload["_rev"], 1)

    # Create a resource (providing an ID)
    def _put(self, id=random_string()):
        self.nexus.resources.create(self.org, self.prj, self.data, resource_id=id)
        payload = self.nexus.resources.fetch(self.org, self.prj, id)
        pretty_print(payload)
        self.assertEqual(payload["_rev"], 1)

    # Update a resource
    def test_update(self):
        id = random_string()
        payload = self._put(id)
        data = self.data
        data["birthdate"] = 1566380674
        data["_rev"] = 1
        data["@id"] = payload["@id"]
        data["_self"] = payload["_self"]
        self.nexus.resources.update(data)
        update = self.nexus.resources.fetch(self.org, self.prj, id)
        self.assertEqual(update["birthdate"], 1566380674)

    def test_deprecate(self):
        id = random_string()
        payload = self.nexus.resources.create(self.org, self.prj, self.data, resource_id=id)
        deprecated = self.nexus.resources.deprecate(payload)
        pretty_print(deprecated)
        self.assertEqual(deprecated["_deprecated"], True)

    def test_tag(self):
        id = random_string()
        payload = self.nexus.resources.create(self.org, self.prj, self.data, resource_id=id)
        self.nexus.resources.tag(payload, "mytag")
        tags = self.nexus.resources.tags(payload)
        pretty_print(tags)
        self.assertEqual(tags["tags"][0]["tag"], "mytag")

    def test_attach(self):
        # Attach a file to an existing resource
        id = random_string()
        self._put(id)
        payload = self.nexus.resources.fetch(self.org, self.prj, resource_id=id)
        f = "./an_attachment.txt"
        payload = self.nexus.resources.add_attachement(payload, f)
        f = "./an_attachment_image.jpg"
        payload = self.nexus.resources.add_attachement(payload, f)
        pretty_print(payload)

    def test_list(self):
        self._post()
        self._put()
        time.sleep(10)
        payload = self.nexus.resources.list(self.org, self.prj)
        pretty_print(payload)
        self.assertGreater(len(payload["_results"]), 0)

        payload = self.nexus.resources.list(self.org, self.prj, schema="context")
        self.assertEqual(len(payload["_results"]), 0)
