import unittest

from nexussdk.utils.tools import pretty_print
from . import *


class TestOrgs(unittest.TestCase):

    def test_orgs(self):
        nexus = new_client()
        org = random_string()

        # listing organizations
        payload = nexus.organizations.list(pagination_size=100)
        pretty_print(payload)

        # getting a specific organization
        nexus.organizations.create(org)
        payload = nexus.organizations.fetch(org)
        pretty_print(payload)
        self.assertEqual(payload["_rev"], 1)

        # Updating values of an organization
        payload["description"] = "an updated description v2"
        payload = nexus.organizations.update(payload)
        pretty_print(payload)
        self.assertEqual(payload["_rev"], 2)

        # Deprecate an Organization
        payload = nexus.organizations.deprecate(org, 2)
        pretty_print(payload)
        self.assertEqual(payload["_rev"], 3)
