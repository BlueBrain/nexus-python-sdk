import json
from . utils.http import http_get
from . utils.http import is_response_valid
from . utils.http import http_put
from . utils.http import http_delete
import urllib.parse


def fetch(org_label, rev=None):
    """
    Fetch an organization.

    :param org_label: The label of the organization
    :param rev: OPTIONAL The specific revision of the wanted organization. If not provided, will get the last
    :return: All the details of this organization, as a dictionary
    """
    org_label = urllib.parse.quote_plus(org_label)
    url = "/orgs/" + org_label

    if rev is not None:
        url = url + "?rev=" + str(rev)

    response_raw = http_get(url)

    if not is_response_valid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url +
                        " (Status " + str(response_raw.status_code) + ")" + "\n" +
                        response_raw.text)

    response_obj = json.loads(response_raw.text)
    return response_obj


def create(org_label, name=None, description=None):
    """
    Create a new organization.

    :param org_label: The label of the organization. Does not allow spaces or special characters
    :param name: OPTIONAL Name of the organization. If not provided, the `org_label` will be used
    :param description: NOT USED YET - OPTIONAL The description of the organization
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = urllib.parse.quote_plus(org_label)
    url = "/orgs/" + org_label

    data = {}

    # this field is mandatory
    if "name" is not None:
        data["name"] = name
    else:
        data["name"] = org_label

    # this field will probably become mandatory
    if "description" is not None:
        data["description"] = description
    else:
        data["description"] = ""

    response_raw = http_put(url, body=data)


    if not is_response_valid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url +
                        " (Status " + str(response_raw.status_code) + ")" + "\n" +
                        response_raw.text)

    response_obj = json.loads(response_raw.text)
    return response_obj


def update(org, previous_rev=None):
    """
    Update an organization. Only the field "name" can be updated (and "description" in the future).

    :param org: Organization payload as a dictionary. This is most likely the returned value of `organisation.get(...)`
    :param previous_rev: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
    this organization. If not provided, the `_rev` number from the `org` argument will be used.
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = urllib.parse.quote_plus(org["label"])

    if previous_rev is None:
        previous_rev = org["_rev"]

    url = "/orgs/" + org_label + "?rev=" + str(previous_rev)

    response_raw = http_put(url, org)

    raise Exception("Invalid http request for " + response_raw.url +
                    " (Status " + str(response_raw.status_code) + ")" + "\n" +
                    response_raw.text)

    response_obj = json.loads(response_raw.text)
    return response_obj


def list(pagination_from=0, pagination_size=20, deprecated=None, full_text_search_query=None):
    """
    NOT WORKING
    List all the organizations.

    :param pagination_from: OPTIONAL Index of the list to start from (default: 0)
    :param pagination_size: OPTIONAL Size of the list (default: 20)
    :param deprecated: OPTIONAL Lists only the deprecated if True,
    lists only the non-deprecated if False,
    lists everything if not provided or None (default: None)
    :param full_text_search_query: OPTIONAL List only the orgs that match this query
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """

    url = "/orgs?from=" + str(pagination_from) + "&size=" + str(pagination_size)

    if deprecated is not None:
        deprecated = "true" if deprecated else "false"
        url = url + "&deprecated=" + deprecated

    if full_text_search_query is not None:
        full_text_search_query = urllib.parse.quote_plus(full_text_search_query)
        url = url + "&q=" + full_text_search_query

    response_raw = http_get(url)

    if not is_response_valid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url +
                        " (Status " + str(response_raw.status_code) + ")" + "\n" +
                        response_raw.text)

    response_obj = json.loads(response_raw.text)
    return response_obj


def deprecate(org_label, previous_rev):
    """
    Deprecate an organization. Nexus does not allow deleting organizations so deprecating is the way to flag them as
    not usable anymore.
    A deprecated organization can not be modified/updated.

    :param org_label: The label of the organization to deprecate
    :param previous_rev: The previous revision number. To be provided to make sure the user is well aware of the details
    of the last revision of this organisation.
    :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization
    """
    org_label = urllib.parse.quote_plus(org_label)
    url = "/orgs/" + org_label + "?rev=" + str(previous_rev)

    response_raw = http_delete(url)

    if not is_response_valid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url +
                        " (Status " + str(response_raw.status_code) + ")" + "\n" +
                        response_raw.text)

    response_obj = json.loads(response_raw.text)
    return response_obj



