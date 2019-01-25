"""
Organizations can represent a lab, a company or even a team of collaborators. They are used to store projects.
"""

from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_delete
from urllib.parse import quote_plus as url_encode


def fetch(org_label, rev=None):
    """
    Fetch an organization.

    :param org_label: The label of the organization
    :param rev: OPTIONAL The specific revision of the wanted organization. If not provided, will get the last
    :return: All the details of this organization, as a dictionary
    """
    org_label = url_encode(org_label)
    path = "/orgs/" + org_label

    if rev is not None:
        path = path + "?rev=" + str(rev)

    return http_get(path, use_base=True)


def create(org_label, description=None):
    """
    Create a new organization.

    :param org_label: The label of the organization. Does not allow spaces or special characters
    :param description: OPTIONAL The description of the organization
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = url_encode(org_label)
    path = "/orgs/" + org_label

    data = {}

    if "description" is not None:
        data["description"] = description
    else:
        data["description"] = ""

    return http_put(path, use_base=True, body=data)


def update(org, rev=None):
    """
    Update an organization. Only the field "name" can be updated (and "description" in the future).

    :param org: Organization payload as a dictionary. This is most likely the returned value of `organisation.get(...)`
    :param rev: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
        this organization. If not provided, the `_rev` number from the `org` argument will be used.
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = url_encode(org["_label"])

    if rev is None:
        rev = org["_rev"]

    path = "/orgs/" + org_label + "?rev=" + str(rev)

    return http_put(path, org, use_base=True)


def list(pagination_from=0, pagination_size=20):
    """
    NOT WORKING
    List all the organizations.

    :param pagination_from: OPTIONAL Index of the list to start from (default: 0)
    :param pagination_size: OPTIONAL Size of the list (default: 20)
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """

    path = "/orgs?from=" + str(pagination_from) + "&size=" + str(pagination_size)

    return http_get(path, use_base=True)


def deprecate(org_label, rev):
    """
    Deprecate an organization. Nexus does not allow deleting organizations so deprecating is the way to flag them as
    not usable anymore.
    A deprecated organization can not be modified/updated.

    :param org_label: The label of the organization to deprecate
    :param rev: The previous revision number. To be provided to make sure the user is well aware of the details
        of the last revision of this organisation.
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = url_encode(org_label)
    path = "/orgs/" + org_label + "?rev=" + str(rev)

    return http_delete(path, use_base=True)
