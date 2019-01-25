"""
Files are a particular kind of resource that contain binary data. In addition, like any other resource, they are bound
to a project (and thus, an organization) and can be described with their metadata.
"""

import os
from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_delete
from urllib.parse import quote_plus as url_encode


def fetch(org_label, project_label, file_id, rev=None, tag=None, out_filepath=None):
    """
    Fetches a distant file and returns the metadata of this file. In addition, if the argument `out_filepath` can
    be of three forms:
    - out_filepath=None (default): the binary is not fetched
    - out_filepath="./some/folder/" the binary is fetched and written in this dir with it's original filename
    - out_filepath="./somefile.jpg" the binary is fetched and written under this exact filename

    In case of error, an exception is thrown.

    :param org_label: The label of the organization that the file belongs to
    :param project_label: The label of the project that the file belongs to
    :param file_id: id of the file
    :param rev: OPTIONAL fetches a specific revision of a file (default: None, fetches the last)
    :param tag: OPTIONAL fetches the file version that has a specific tag (default: None)
    :param out_filepath: OPTIONAL the filename to write (default: None)
    :return: Payload of the whole file as a dictionary
    """

    if rev is not None and tag is not None:
        raise Exception("The arguments rev and tag are mutually exclusive. One or the other must be chosen.")

    # the element composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    file_id = url_encode(file_id)

    path = "/files/" + org_label + "/" + project_label + "/" + file_id

    if rev is not None:
        path = path + "?rev=" + str(rev)

    if tag is not None:
        path = path + "?tag=" + str(tag)

    response_metadata = http_get(path, use_base=True, data_type="json", accept="json", get_raw_response=False, stream=False)
    response_binary = http_get(path, use_base=True, get_raw_response=True, accept="all", stream=True)

    if out_filepath is not None:
        if os.path.isdir(out_filepath):
            out_filepath = os.path.join(out_filepath, response_metadata["_filename"])

        # we write the result of the request into a file
        with open(out_filepath, "wb") as f:
            for chunk in response_binary.iter_content():
                f.write(chunk)

    return response_metadata


def update(file, filepath, rev=None):
    """
    Update a file. The file object is most likely the returned value of a
    nexus.file.fetch(), where some fields where modified, added or removed.
    Note that the returned payload only contains the Nexus metadata and not the
    complete file.

    :param file: payload of a previously fetched file, with the modification to be updated
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the file argument will be used.
    :return: A payload containing only the Nexus metadata for this updated file.
    """

    if rev is None:
        rev = file["_rev"]

    path = file["_self"] + "?rev=" + str(rev)

    file_obj = {"file": open(filepath, "rb")}

    return http_put(path, body=file_obj, use_base=False, data_type="file")


def create(org_label, project_label, filepath, file_id=None):
    """
    This is the POST method, when the user does not provide a file ID.

    :param org_label: The label of the organization that the file belongs to
    :param project_label: The label of the project that the file belongs to
    :param filepath: path of the file to upload
    :param file_id: OPTIONAL Will use this id to identify the file if provided. If not provided, an ID will be generated
    :return: A payload containing only the Nexus metadata for this updated file.
    """

    # the element composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/files/" + org_label + "/" + project_label

    file_obj = {"file": open(filepath, "rb")}

    if file_id is None:
        return http_post(path, body=file_obj, data_type="file", use_base=True)
    else:
        file_id = url_encode(file_id)
        path = path + "/" + file_id
        return http_put(path, use_base=True, body=file_obj, data_type="file")


def list(org_label, project_label, pagination_from=0, pagination_size=20,
         deprecated=None, type=None, rev=None, schema=None, created_by=None, updated_by=None, file_id=None):
    """
    List the files available for a given organization and project.

    :param org_label: The label of the organization that the file belongs to
    :param project_label: The label of the project that the file belongs to
    :param pagination_from: OPTIONAL The pagination index to start from (default: 0)
    :param pagination_size: OPTIONAL The maximum number of elements to returns at once (default: 20)
    :param deprecated: OPTIONAL Get only deprecated file if True and get only non-deprecated results if False.
        If not specified (default), return both deprecated and not deprecated file.
    :param type: OPTIONAL Lists only the file for a given type (default: None)
    :param rev: OPTIONAL List only the resource with this particular revision
    :param schema: OPTIONAL list only the views with a certain schema
    :param created_by: OPTIONAL List only the file created by a certain user
    :param updated_by: OPTIONAL List only the file that were updated by a certain user
    :param file_id: OPTIONAL List only the file with this id. Relevant only when combined with other args
    :return: The raw list payload as a dictionary
    """

    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/files/" + org_label + "/" + project_label

    params = {
        "from": pagination_from,
        "size": pagination_size,
        "type": type,
        "deprecated": deprecated,
        "rev": rev,
        "schema": schema,
        "created_by": created_by,
        "updated_by": updated_by,
        "id": file_id
    }

    return http_get(path, use_base=True, params=params)


def deprecate(file, rev=None):
    """
    Flag a file as deprecated. files cannot be deleted in Nexus, once one is deprecated, it is no longer
    possible to update it.

    :param file: payload of a previously fetched file
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the file argument will be used.
    :return: A payload containing only the Nexus metadata for this deprecated file.
    """

    if rev is None:
        rev = file["_rev"]

    path = file["_self"] + "?rev=" + str(rev)

    return http_delete(path, use_base=False)


def tag(file, tag_value, rev_to_tag=None, rev=None):
    """
    Add a tag to a a specific revision of the file. Note that a new revision (untagged) will be created

    :param file: payload of a previously fetched file
    :param tag_value: The value (or name) of a tag
    :param rev_to_tag: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
        from the provided file payload.
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the file argument will be used.
    :return: A payload containing only the Nexus metadata for this file.
    """

    if rev is None:
        rev = file["_rev"]

    if rev_to_tag is None:
        rev_to_tag = file["_rev"]

    path = file["_self"] + "/tags?rev=" + str(rev)

    data = {
        "tag": tag_value,
        "rev": rev_to_tag
    }

    return http_post(path, body=data, use_base=False)


def tags(file):
    """
    List all the tags added to this file, along with their version numbers

    :param file: payload of a previously fetched file
    :return: payload containing the list of tags and versions
    """

    path = file["_self"] + "/tags"
    return http_get(path, use_base=False)
