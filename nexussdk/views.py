import json
from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_delete
from urllib.parse import quote_plus as url_encode


def create(org_label, project_label, view_data, type="ElasticView"):
    """
        Generic interface to create a view for different engines.

        :param org_label: Label of the organization the view wil belong to
        :param project_label: label of the project the view will belong too
        :param view_data: Mapping data required for ElasticSearch indexing
        :param type: OPTIONAL For the moment, only "ElasticView" is supported
        :return: The payload representing the view. This payload only contains the Nexus metadata
    """
    if type == "ElasticView":
        return create_es(org_label, project_label, view_data)


def create_es(org_label, project_label, view_data):
    """
        Creates an ElasticSearch view

        :param org_label: Label of the organization the view wil belong to
        :param project_label: label of the project the view will belong too
        :param view_data: Mapping data required for ElasticSearch indexing
        :return: The payload representing the view. This payload only contains the Nexus metadata
    """

    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/view/" + org_label + "/" + project_label

    # we give the possibility to use a JSON string instead of a dict
    if (not isinstance(view_data, dict)) and isinstance(view_data, str):
        view_data = json.loads(view_data)

    if "@type" not in view_data:
        view_data["@type"] = ["ElasticView"]

    return http_post(path, body=view_data)


def update():
    None


def

def deprecate():
    None


def fetch():
    None


def list():
    None

def query_es():
    None


def query_sq():
    None