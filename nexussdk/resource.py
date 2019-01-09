import json
from . utils.http import httpGet
from . utils.http import isResponseValid
from . utils.http import httpPut
from . utils.http import httpPost
from . utils.tools import copyThisIntoThat
import urllib.parse

# This context is the default one when none is provided at the creation of a resource
DEFAULT_CONTEXT = {
    "@context": {
        "@base": "http://example.com/",
        "@vocab": "http://schema.org/"
    }
}


def get(org_label, project_label, schema_id, resource_id):
    """
        Fetches a distant resource and returns the payload as a dictionary.
        In case of error, an exception is thrown.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema_id: id of the schema
        :param resource_id: id of the resource
        :return: Payload of the whole resource as a dictionary
    """
    # the element composing the query URL need to be URL-encoded
    org_label = urllib.parse.quote_plus(org_label)
    project_label = urllib.parse.quote_plus(project_label)
    schema_id = urllib.parse.quote_plus(schema_id)
    resource_id = urllib.parse.quote_plus(resource_id)

    url = "/resources/" + org_label + "/" + project_label + "/" + schema_id + "/" + resource_id
    response_raw = httpGet(url)

    if not isResponseValid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url + " (Status " + str(response_raw.status_code) + ")")

    response_obj = json.loads(response_raw.text)
    return response_obj


def update(org_label, project_label, resource):
    """
        Update a resource. The resource object is mostl likely the returned value of a
        nexus.resource.get(), where some fields where modified, added or removed.
        Note that the returned payload only contains the Nexus metadata and not the
        complete resource.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param resource: payload of a previoulsy fetched resource, with the modification to be updated
        :return: A payload containing only the Nexus metadata for this updated resource.
    """

    # the element composing the query URL need to be URL-encoded
    org_label = urllib.parse.quote_plus(org_label)
    project_label = urllib.parse.quote_plus(project_label)
    schema_id = urllib.parse.quote_plus(resource["_constrainedBy"])
    resource_id = urllib.parse.quote_plus(resource["@id"])
    previous_rev = resource["_rev"]

    # url = "/resources/" + org_label + "/" + project_label + "/" + schema_id + "/" + resource_id + "?rev=" + str(previous_rev)
    url = resource["_self"] + "?rev=" + str(previous_rev)

    response_raw = httpPut(url, resource, use_base=False)

    if not isResponseValid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url + " (Status " + str(response_raw.status_code) + ")")

    response_obj = json.loads(response_raw.text)
    return response_obj


def create(org_label, project_label, data, schema_id='resource', resource_id=None):
    """
        This is the POST method, when the user does not provide a resource ID.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema_id: OPTIONAL The schema to constrain the data. Can be None for non contrained data (default: 'resource')
        :param data: dictionary containing the data to store in this new resource
        :param resource_id: OPTIONAL - NOT UESED YET
        :return: A payload containing only the Nexus metadata for this updated resource.

        If the data does not have a '@context' value, a default one is automatically added.
    """

    # if no schema is provided, we can create a resource with a non-constraining
    # default schema called 'resource'
    if schema_id == None:
        schema_id = 'resource'

    # the element composing the query URL need to be URL-encoded
    org_label = urllib.parse.quote_plus(org_label)
    project_label = urllib.parse.quote_plus(project_label)
    schema_id = urllib.parse.quote_plus(schema_id)

    url = "/resources/" + org_label + "/" + project_label + "/" + schema_id

    # If the data does not have a '@context' field, we should had a default one
    if "@context" not in data:
        copyThisIntoThat(DEFAULT_CONTEXT, data)

    response_raw = httpPost(url, data)

    if not isResponseValid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url + " (Status " + str(response_raw.status_code) + ")")

    response_obj = json.loads(response_raw.text)
    return response_obj



def list(org_label, project_label, schema=None, pagination_from=0, pagination_size=20, deprecated=None, full_text_search_query=None):
    """
        List the resources available for a given organization and project.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema: OPTIONAL Lists only the resource for a given schema (default: None)
        :param pagination_from: OPTIONAL The pagination index to start from (default: 0)
        :param pagination_size: OPTIONAL The maximum number of elements to returns at once (default: 20)
        :param deprecated: OPTIONAL Get only deprecated resource if True and get only non-deprecated results if False. If not specified (default), return both deprecated and not deprecated resource.
        :return: The raw payload as a dictionary
    """

    org_label = urllib.parse.quote_plus(org_label)
    project_label = urllib.parse.quote_plus(project_label)

    url = "/resources/" + org_label + "/" + project_label

    if schema:
        schema = urllib.parse.quote_plus(schema)
        url = url + "/" "schema"

    url = url + "?from=" + str(pagination_from) + "&size=" + str(pagination_size)


    if deprecated is not None:
        deprecated = "true" if deprecated else "false"
        url = url + "&deprecated=" + deprecated

    if full_text_search_query:
        full_text_search_query = urllib.parse.quote_plus(full_text_search_query)
        url = url + "&q=" + full_text_search_query

    response_raw = httpGet(url)

    if not isResponseValid(response_raw):
        raise Exception("Invalid http request for " + response_raw.url + " (Status " + str(response_raw.status_code) + ")")

    response_obj = json.loads(response_raw.text)
    return response_obj
