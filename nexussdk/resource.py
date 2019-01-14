import json
from . utils.http import http_get
from . utils.http import is_response_valid
from . utils.http import http_put
from . utils.http import http_post
from . utils.http import http_delete
from . utils.tools import copy_this_into_that
import urllib.parse

url_encode = urllib.parse.quote_plus

# This context is the default one when none is provided at the creation of a resource
DEFAULT_CONTEXT = {
    "@context": {
        "@base": "http://example.com/",
        "@vocab": "http://schema.org/"
    }
}


def fetch(org_label, project_label, schema_id, resource_id):
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
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    schema_id = url_encode(schema_id)
    resource_id = url_encode(resource_id)

    path = "/resources/" + org_label + "/" + project_label + "/" + schema_id + "/" + resource_id
    response_raw = http_get(path)
    return json.loads(response_raw.text)



def update(resource, previous_rev=None):
    """
        Update a resource. The resource object is most likely the returned value of a
        nexus.resource.get(), where some fields where modified, added or removed.
        Note that the returned payload only contains the Nexus metadata and not the
        complete resource.

        :param resource: payload of a previously fetched resource, with the modification to be updated
        :param previous_rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
        :return: A payload containing only the Nexus metadata for this updated resource.
    """

    if previous_rev is None:
        previous_rev = resource["_rev"]

    path = resource["_self"] + "?rev=" + str(previous_rev)

    response_raw = http_put(path, resource, use_base=False)
    return json.loads(response_raw.text)


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
    if schema_id is None:
        schema_id = 'resource'

    # the element composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    schema_id = url_encode(schema_id)

    path = "/resources/" + org_label + "/" + project_label + "/" + schema_id

    # If the data does not have a '@context' field, we should had a default one
    if "@context" not in data:
        copy_this_into_that(DEFAULT_CONTEXT, data)

    response_raw = http_post(path, data)
    return json.loads(response_raw.text)


def list(org_label, project_label, schema=None, pagination_from=0, pagination_size=20,
         deprecated=None, full_text_search_query=None):
    """
        List the resources available for a given organization and project.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema: OPTIONAL Lists only the resource for a given schema (default: None)
        :param pagination_from: OPTIONAL The pagination index to start from (default: 0)
        :param pagination_size: OPTIONAL The maximum number of elements to returns at once (default: 20)
        :param deprecated: OPTIONAL Get only deprecated resource if True and get only non-deprecated results if False.
        If not specified (default), return both deprecated and not deprecated resource.
        :param full_text_search_query: A string to look for as a full text query
        :return: The raw payload as a dictionary
    """

    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/resources/" + org_label + "/" + project_label

    if schema:
        schema = url_encode(schema)
        path = path + "/" + schema

    path = path + "?from=" + str(pagination_from) + "&size=" + str(pagination_size)

    if deprecated is not None:
        deprecated = "true" if deprecated else "false"
        path = path + "&deprecated=" + deprecated

    if full_text_search_query:
        full_text_search_query = url_encode(full_text_search_query)
        path = path + "&q=" + full_text_search_query

    response_raw = http_get(path)
    return json.loads(response_raw.text)


def deprecate(resource, previous_rev=None):
    """
       Flag a resource as deprecated. Resources cannot be deleted in Nexus, once one is deprecated, it is no longer
       possible to update it.

       :param resource: payload of a previouslsy fetched resource, with the modification to be updated
       :param previous_rev: OPTIONAL The previous revision you want to update from.
       If not provided, the rev from the resource argument will be used.
       :return: A payload containing only the Nexus metadata for this deprecated resource.
    """

    if previous_rev is None:
        previous_rev = resource["_rev"]

    path = resource["_self"] + "?rev=" + str(previous_rev)

    response_raw = http_delete(path, use_base=False)
    return json.loads(response_raw.text)
