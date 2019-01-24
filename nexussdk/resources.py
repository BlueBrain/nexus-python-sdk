"""
A resource represents a set of organized data represented with JSON. Hence, a resource can handle data such as numbers,
strings, arrays, boolean and complex objects made of those primitive types. In addition, Nexus adds some metadata.
Resources belong to projects and their access rights are defined at the project level.
"""

import os
from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_delete
from nexussdk.utils.tools import copy_this_into_that
from urllib.parse import quote_plus as url_encode

# This context is the default one when none is provided at the creation of a resource
DEFAULT_CONTEXT = {
    "@context": {
        "@base": "http://example.com/",
        "@vocab": "http://schema.org/"
    }
}


def fetch(org_label, project_label, schema_id, resource_id, rev=None, tag=None):
    """
        Fetches a distant resource and returns the payload as a dictionary.
        In case of error, an exception is thrown.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema_id: id of the schema
        :param resource_id: id of the resource
        :param rev: OPTIONAL fetches a specific revision of a resource (default: None, fetches the last)
        :param tag: OPTIONAL fetches the resource version that has a specific tag (default: None)
        :return: Payload of the whole resource as a dictionary
    """

    if rev is not None and tag is not None:
        raise Exception("The arguments rev and tag are mutually exclusive. One or the other must be chosen.")

    # the element composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    schema_id = url_encode(schema_id)
    resource_id = url_encode(resource_id)
    path = "/resources/" + org_label + "/" + project_label + "/" + schema_id + "/" + resource_id

    if rev is not None:
        path = path + "?rev=" + str(rev)

    if tag is not None:
        path = path + "?tag=" + str(tag)

    return http_get(path, use_base=True)


def update(resource, rev=None):
    """
        Update a resource. The resource object is most likely the returned value of a
        nexus.resource.fetch(), where some fields where modified, added or removed.
        Note that the returned payload only contains the Nexus metadata and not the
        complete resource.

        :param resource: payload of a previously fetched resource, with the modification to be updated
        :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
        :return: A payload containing only the Nexus metadata for this updated resource.
    """

    if rev is None:
        rev = resource["_rev"]

    path = resource["_self"] + "?rev=" + str(rev)

    return http_put(path, resource, use_base=False)


def create(org_label, project_label, data, schema_id='_', resource_id=None):
    """
        Create a resource. If resource_id is provided, this given ID will be used. If resource_id not provided,
        an ID will be automatically generated for this new resource.

        :param org_label: The label of the organization that the resource belongs to
        :param project_label: The label of the project that the resource belongs to
        :param schema_id: OPTIONAL The schema to constrain the data. Can be None for non constrained data (default: 'resource')
        :param data: dictionary containing the data to store in this new resource
        :param resource_id: OPTIONAL force the use of a specific id when creating the new resource
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

    if resource_id is None:
        return http_post(path, data, use_base=True)
    else:
        resource_id = url_encode(resource_id)
        path = path + "/" + resource_id
        return http_put(path, data, use_base=True)


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

    return http_get(path, use_base=True)


def deprecate(resource, rev=None):
    """
       Flag a resource as deprecated. Resources cannot be deleted in Nexus, once one is deprecated, it is no longer
       possible to update it.

       :param resource: payload of a previously fetched resource
       :param rev: OPTIONAL The previous revision you want to update from.
       If not provided, the rev from the resource argument will be used.
       :return: A payload containing only the Nexus metadata for this deprecated resource.
    """

    if rev is None:
        rev = resource["_rev"]

    path = resource["_self"] + "?rev=" + str(rev)

    return http_delete(path, use_base=False)


def tag(resource, tag_value, rev_to_tag=None, rev=None):
    """
        Add a tag to a a specific revision of the resource. Note that a new revision (untagged) will be created

        :param resource: payload of a previously fetched resource
        :param tag_value: The value (or name) of a tag
        :param rev_to_tag: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
        from the provided resource payload.
        :param rev: OPTIONAL The previous revision you want to update from.
       If not provided, the rev from the resource argument will be used.
        :return: A payload containing only the Nexus metadata for this resource.
    """

    if rev is None:
        rev = resource["_rev"]

    if rev_to_tag is None:
        rev_to_tag = resource["_rev"]

    path = resource["_self"] + "/tags?rev=" + str(rev)

    data = {
        "tag": tag_value,
        "rev": rev_to_tag
    }

    return http_post(path, body=data, use_base=False)


def tags(resource):
    """
        List all the tags added to this resource, along with their version numbers

        :param resource: payload of a previously fetched resource
        :return: payload containing the list of tags and versions
    """

    path = resource["_self"] + "/tags"
    return http_get(path, use_base=False)


def add_attachement(resource, filepath, rev=None):
    """
        DEPRECATED

        Attach a file to an existing resource. A new revision is created.

        :param resource: payload of a previously fetched resource
        :param filepath: Path of the file to upload
        :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
        :return: A payload containing only the Nexus metadata for this resource.
    """

    if rev is None:
        rev = resource["_rev"]

    file_basename = url_encode(os.path.basename(filepath))
    path = resource["_self"] + "/attachments/" + file_basename + "?rev=" + str(rev)
    file_obj = {'file': open(filepath, "rb")}
    return http_put(path, use_base=False, body=file_obj, data_type='file')


def delete_attachment(resource, basename, rev=None):
    """
        DEPRECATED

        Delete the attachment of a resource. This creates a new revision.

        :param resource: payload of a previously fetched resource
        :param basename: The attachment basename (filename with extension but without full path)
        :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
        :return: A payload containing only the Nexus metadata for this resource.
    """

    if rev is None:
        rev = resource["_rev"]

    path = resource["_self"] + "/attachments/" + basename + "?rev=" + str(rev)
    return http_delete(path, use_base=False)


def fetch_attachment(resource, name, rev=None, tag=None, out_filename=None):
    """
        DEPRECATED

        Fetch the attachment of a a resource. Two ways are possible: by specifying an output filepath (out_filename),
        then the distant file will be downloaded under this name. Or, if out_filename is not specified,
        the binary buffer of the distant file is returned by this function.

        If the distant file is large, it is advised to write it directly as a file because streaming is handled. Keeping
        a large file into memory may not be a good idea.

    :param resource: payload of a previously fetched resource
    :param name: ID of the resource's attachment
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
        Note that this cannot be given along tag
    :param tag: OPTIONAL tag of a resource. Note that this cannot be given along rev
    :param out_filename: OPTIONAL file path to which write the fetched file.
    :return: If out_filename is provided None is returned.
        If out_filename is not provided, the binary buffer is returned as a byte_arr
    """

    if (rev is not None) and (tag is not None):
        raise Exception("The arguments rev and tag are mutually exclusive and should not be used together.")

    path = resource["_self"] + "/attachments/" + name

    if rev is not None:
        path = path + "?rev=" + str(rev)

    if tag is not None:
        path = path + "?tag=" + str(tag)

    response = http_get(path, use_base=False, get_raw_response=True, stream=True)

    if out_filename is not None:
        # we write the result of the request into a file
        with open(out_filename, 'wb') as f:
            for chunk in response.iter_content():
                f.write(chunk)
        return None

    else:
        # we concat all the chunks to make a larger bytearray containing the response
        byte_arr = bytearray(0)

        for chunk in response.iter_content():
            byte_arr = byte_arr + chunk

        return byte_arr
