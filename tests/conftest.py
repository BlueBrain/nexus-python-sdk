from collections import namedtuple

from pytest import fixture

from . import *


@fixture
def env():
    nexus_client = new_client()
    org = random_string()
    prj = random_string()
    nexus_client.organizations.create(org)
    nexus_client.projects.create(org, prj)
    Environment = namedtuple('Environment', ['client', 'org', 'prj'])
    return Environment(nexus_client, org, prj)

