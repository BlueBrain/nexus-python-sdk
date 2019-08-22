import time
import unittest

from nexussdk.utils.tools import pretty_print
from . import *


class TestViews(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestViews, self).__init__(*args, **kwargs)
        self.nexus = new_client()
        self.org = random_string()
        self.prj = random_string()
        self.nexus.organizations.create(self.org)
        self.nexus.projects.create(self.org, self.prj)
        self.mapping = {
            "dynamic": False,
            "properties": {
                "@id": {
                    "type": "keyword"
                },
                "@type": {
                    "type": "keyword"
                },
                "firstname": {
                    "type": "keyword"
                },
                "lastname": {
                    "type": "keyword"
                }
            }
        }

    # Create a ES view
    def _put(self, id=f"nxv:{random_string()}"):
        payload = self.nexus.views.create_es(self.org, self.prj, self.mapping, view_id=id)
        pretty_print(payload)

    def test_list(self):
        self._put()
        time.sleep(10)
        payload = self.nexus.views.list(self.org, self.prj)
        pretty_print(payload)
        self.assertGreater(len(payload["_results"]), 0)
        es = self.nexus.views.list_keep_only_es(payload)
        self.assertNotEqual(payload, es)

    def test_es_query(self):
        resource = self.nexus.resources.create(self.org, self.prj, {"firstname": "Johnny", "lastname": "Bravo"})
        resource = self.nexus.resources.fetch(self.org, self.prj, resource["@id"])
        self.assertEqual(resource["_rev"], 1)
        query = """
        {
          "query": {
            "term": {
              "firstname": "Johnny"
            }
          }
        }
        """
        id = f"nxv:{random_string()}"
        self._put(id)
        time.sleep(10)
        payload_view = self.nexus.views.fetch(self.org, self.prj, id)
        pretty_print(payload_view)
        payload = self.nexus.views.query_es(self.org, self.prj, query, id)
        pretty_print(payload)
        self.assertGreater(len(payload["hits"]["hits"]), 0)

    def test_sparql_query(self):
        resource = self.nexus.resources.create(self.org, self.prj, {"firstname": "Johnny", "lastname": "Bravo"})
        resource = self.nexus.resources.fetch(self.org, self.prj, resource["@id"])
        self.assertEqual(resource["_rev"], 1)
        time.sleep(10)
        query = 'SELECT ?s where {?s ?p "Bravo"} LIMIT 10'
        payload = self.nexus.views.query_sparql(self.org, self.prj, query)
        pretty_print(payload)
        self.assertGreater(len(payload["results"]["bindings"]), 0)
