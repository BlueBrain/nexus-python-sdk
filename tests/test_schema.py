import time
import unittest

from nexussdk.utils.tools import pretty_print
from . import *


class TestSchemas(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSchemas, self).__init__(*args, **kwargs)
        self.nexus = new_client()
        self.org = random_string()
        self.prj = random_string()
        self.nexus.organizations.create(self.org)
        self.nexus.projects.create(self.org, self.prj)

    # Create a schema (NO id provided)
    def _post(self):
        my_schema = """{
          "shapes": [
            {
              "@id": "this:MyShape",
              "@type": "sh:NodeShape",
              "nodeKind": "sh:BlankNodeOrIRI",
              "targetClass": "ex:Custom",
              "property": [
                {
                  "path": "ex:name",
                  "datatype": "xsd:string",
                  "minCount": 1
                },
                {
                  "path": "ex:number",
                  "datatype": "xsd:integer",
                  "minCount": 1
                },
                {
                  "path": "ex:bool",
                  "datatype": "xsd:boolean",
                  "minCount": 1
                }
              ]
            }
          ]
        }"""
        payload = self.nexus.schemas.create(self.org, self.prj, my_schema)
        pretty_print(payload)
        id = payload["@id"]
        payload = self.nexus.schemas.fetch(self.org, self.prj, id)
        self.assertEqual(len(payload["shapes"]), 1)

    # Create a schema (id provided)
    def _put(self, id=random_string()):
        my_schema = """{
          "shapes": [
            {
              "@id": "this:MyShape",
              "@type": "sh:NodeShape",
              "nodeKind": "sh:BlankNodeOrIRI",
              "targetClass": "ex:Custom",
              "property": [
                {
                  "path": "ex:name",
                  "datatype": "xsd:string",
                  "minCount": 1
                },
                {
                  "path": "ex:number",
                  "datatype": "xsd:integer",
                  "minCount": 1
                },
                {
                  "path": "ex:bool",
                  "datatype": "xsd:boolean",
                  "minCount": 1
                }
              ]
            }
          ]
        }"""
        payload = self.nexus.schemas.create(self.org, self.prj, my_schema, schema_id=id)
        pretty_print(payload)
        payload = self.nexus.schemas.fetch(self.org, self.prj, id)
        self.assertEqual(len(payload["shapes"]), 1)

    def test_update(self):
        id = random_string()
        self._put(id)
        payload = self.nexus.schemas.fetch(self.org, self.prj, id)
        payload["shapes"][0]["property"][0]["minCount"] = 10
        payload = self.nexus.schemas.update(payload)
        self.assertEqual(payload["_rev"], 2)
        pretty_print(payload)

    # Deprecate
    def test_deprecate(self):
        id = random_string()
        self._put(id)
        payload = self.nexus.schemas.fetch(self.org, self.prj, id)
        payload = self.nexus.schemas.deprecate(payload)
        pretty_print(payload)
        self.assertEqual(payload["_deprecated"], True)

    def test_tag(self):
        id = random_string()
        self._put(id)
        payload = self.nexus.schemas.fetch(self.org, self.prj, id)
        payload = self.nexus.resources.tag(payload, "mytag")
        tags = self.nexus.resources.tags(payload)
        pretty_print(tags)
        self.assertEqual(tags["tags"][0]["tag"], "mytag")

    # Listing schemas
    def test_list(self):
        self._post()
        self._put()
        time.sleep(10)
        payload = self.nexus.schemas.list(self.org, self.prj)
        self.assertGreater(len(payload["_results"]), 0)
