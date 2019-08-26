import unittest

from nexussdk.utils.tools import pretty_print
from . import *


class TestProjects(unittest.TestCase):

    def test_projects(self):
        nexus = new_client()
        org = random_string()
        prj = random_string()

        # listing projects
        payload = nexus.projects.list()
        pretty_print(payload)

        nexus.organizations.create(org, description="This is my org, there are many like it but this one is mine.")
        nexus.projects.create(org, prj, "This is my awesome project")

        # Getting a specific project
        project = nexus.projects.fetch(org, prj)
        pretty_print(project)

        # Updating a project
        project["apiMappings"] = ["not", "sure", "what", "to", "put", "there"]
        updated = nexus.projects.update(project)
        pretty_print(updated)
        rev = updated["_rev"]
        self.assertEqual(rev, 2)

        # Deprecate a project
        deprecated = nexus.projects.deprecate(project, rev)
        pretty_print(project)
        self.assertEqual(deprecated["_rev"], 3)
