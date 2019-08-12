"""
Files are a particular kind of resource that contain binary data. In addition, like any other resource, they are bound
to a project (and thus, an organization) and can be described with their metadata.
"""

import os
from typing import Dict, Optional
from urllib.parse import quote_plus as url_encode

import puremagic

from nexussdk.utils.http import http_delete
from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_put

SEGMENT = "files"
DEFAULT_MIME = "application/octet-stream"


def fetch(org_label: str, project_label: str, file_id: str, rev: Optional[int] = None, tag: Optional[str] = None,
          out_filepath: Optional[str] = None) -> Dict:
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

    # the elements composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    file_id = url_encode(file_id)

    path = [SEGMENT, org_label, project_label, file_id]

    response_metadata = http_get(path, rev=rev, tag=tag)
    response_binary = http_get(path, get_raw_response=True, accept="all", stream=True, rev=rev, tag=tag)

    if out_filepath is not None:
        if os.path.isdir(out_filepath):
            out_filepath = os.path.join(out_filepath, response_metadata["_filename"])

        # we write the result of the request into a file
        with open(out_filepath, "wb") as f:
            for chunk in response_binary.iter_content(chunk_size=4096):
                f.write(chunk)

    return response_metadata


def create(org_label: str, project_label: str, filepath: str, storage_id: Optional[str] = None,
           file_id: Optional[str] = None, filename: Optional[str] = None, content_type: Optional[str] = None) -> Dict:
    """
        Creates a file resource from a binary attachment using the POST method when the user does not provide
        a file ID, PUT otherwise.

        :param org_label: The label of the organization that the file belongs to
        :param project_label: The label of the project that the file belongs to
        :param filepath: path of the file to upload
        :param storage_id: OPTIONAL The id of the storage backend where the file will be stored.
                           If not provided, the project's default storage is used.
        :param file_id: OPTIONAL Will use this id to identify the file if provided.
                        If not provided, an ID will be generated.
        :param filename: OPTIONAL Overrides the automatically detected filename
        :param content_type: OPTIONAL Override the automatically detected content type
        :return: A payload containing only the Nexus metadata for this updated file.
    """

    # the elements composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = [SEGMENT, org_label, project_label]

    if filename is None:
        filename = filepath.split("/")[-1]

    file_obj = {
        "file": (filename, open(filepath, "rb"), _content_type(filepath, content_type))
    }

    if file_id is None:
        return http_post(path, body=file_obj, data_type="file", storage=storage_id)
    else:
        path.append(url_encode(file_id))
        return http_put(path, body=file_obj, data_type="file", storage=storage_id)


def create_link(org_label: str, project_label: str, filename: str, filepath: str, media_type: str,
                storage_id: Optional[str] = None, file_id: Optional[str] = None) -> Dict:
    """
        Creates a file resource from a link to an existing binary using the POST method when the user does not provide
        a file ID, PUT otherwise.

        :param org_label: The label of the organization that the file belongs to
        :param project_label: The label of the project that the file belongs to
        :param filename: The filename that will be exposed in the resource metadata
        :param filepath: The path (relative to its storage root) of the file to link
        :param media_type: The media type of the linked file
        :param storage_id: OPTIONAL The id of the storage backend where the file is located.
                           If not provided, the project's default storage is used.
        :param file_id: OPTIONAL The id of the created resource if provided.
                        If not, an ID will be generated
        :return: A payload containing only the Nexus metadata for this linked file.
    """

    # the elements composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    payload = {
        "filename": filename,
        "path": filepath,
        "mediaType": media_type
    }

    request_path = [SEGMENT, org_label, project_label]

    if file_id is not None:
        request_path.append(url_encode(file_id))

    if file_id is None:
        return http_post(request_path, body=payload, storage=storage_id)
    else:
        return http_put(request_path, body=payload, storage=storage_id)


def update(org_label: str, project_label: str, filepath: str, file_id: str, rev: int, storage_id: Optional[str] = None,
           filename: Optional[str] = None, content_type: Optional[str] = None) -> Dict:
    """
        Updates an existing file resource with a new binary attachment.

        :param org_label: The label of the organization that the file belongs to
        :param project_label: The label of the project that the file belongs to
        :param filepath: The path of the file to upload
        :param file_id: The id of the file resource to update.
        :param rev: The revision to update from.
        :param storage_id: OPTIONAL The id of the storage backend where the file will be stored.
                           If not provided, the project's default storage is used.
        :param filename: OPTIONAL Overrides the automatically detected filename
        :param content_type: OPTIONAL Overrides the automatically detected content type
        :return: A payload containing only the Nexus metadata for this updated file.
    """

    # the elements composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = [SEGMENT, org_label, project_label, url_encode(file_id)]

    if filename is None:
        filename = filepath.split("/")[-1]

    file_obj = {
        "file": (filename, open(filepath, "rb"), _content_type(filepath, content_type))
    }

    return http_put(path, body=file_obj, data_type="file", rev=rev, storage=storage_id)


def update_(file: Dict, filepath: str, rev: Optional[int] = None, storage_id: Optional[str] = None,
            content_type: Optional[str] = None) -> Dict:
    """
        Update a file, from an existing file resource payload, for instance the value returned
        by nexus.file.fetch(), where some fields where modified, added or removed.
        Note that the returned payload only contains the Nexus metadata and not the
        complete file.

        :param file: Payload of a previously fetched file.
        :param rev: OPTIONAL The previous revision you want to update from.
                    If not provided, the rev from the file argument will be used.
        :param storage_id: OPTIONAL The id of the storage backend where the file will be stored.
                           If not provided, the project's default storage is used.
        :param content_type: OPTIONAL Overrides the automatically detected content type
        :return: A payload containing only the Nexus metadata for this updated file.
    """

    if rev is None:
        rev = file["_rev"]

    path = file["_self"]

    file_obj = {"file": (file["_filename"], open(filepath, "rb"), _content_type(filepath, content_type))}

    return http_put(path, body=file_obj, data_type="file", rev=rev, storage=storage_id)


def update_link(org_label: str, project_label: str, filename: str, filepath: str, media_type: str, rev: int,
                file_id: str, storage_id: Optional[str] = None) -> Dict:
    """
        Update a file (of any kind, not necessarily a link) with a link.

        :param org_label: The label of the organization that the file belongs to
        :param project_label: The label of the project that the file belongs to
        :param filename: The filename that will be exposed in the resource metadata
        :param filepath: The path (relative to its storage root) of the file to link
        :param media_type: The linked file's media type
        :param rev: The previous file revision
        :param file_id: The previous file resource id
        :param storage_id: OPTIONAL The id of the storage backend where the file is located.
                           If not provided, the project's default storage is used.
        :return: A payload containing only the Nexus metadata for this linked file.
    """

    # the elements composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    payload = {
        "filename": filename,
        "path": filepath,
        "mediaType": media_type
    }

    request_path = [SEGMENT, org_label, project_label, url_encode(file_id)]

    return http_put(request_path, body=payload, rev=rev, storage=storage_id)


def update_link_(file: Dict, filename: str, filepath: str, media_type: str,
                 rev: Optional[int] = None, storage_id: Optional[str] = None) -> Dict:
    """
        Update a file (of any kind, not necessarily a link) with a link
        from an existing file resource payload, for instance the value returned
        by nexus.file.fetch(), where some fields where modified, added or removed.

        :param file: Payload of a previously fetched file.
        :param filename: The filename that will be exposed in the resource metadata
        :param filepath: The path (relative to its storage root) of the file to link
        :param media_type: The linked file's media type
        :param rev: The previous file revision
        :param file_id: The previous file resource id
        :param storage_id: OPTIONAL The id of the storage backend where the file is located.
                           If not provided, the project's default storage is used.
        :return: A payload containing only the Nexus metadata for this linked file.
    """

    if rev is None:
        rev = file["_rev"]

    path = file["_self"]

    payload = {
        "filename": filename,
        "path": filepath,
        "mediaType": media_type
    }

    return http_put(path, body=payload, rev=rev, storage=storage_id)


def list(org_label: str, project_label: str, pagination_from: int = 0, pagination_size: int = 20,
         deprecated: Optional[bool] = None, type: Optional[str] = None, rev: Optional[int] = None,
         schema: Optional[str] = None, created_by: Optional[str] = None, updated_by: Optional[str] = None,
         file_id: Optional[str] = None) -> Dict:
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

    path = [SEGMENT, org_label, project_label]

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

    return http_get(path, params=params)


def deprecate(org_label: str, project_label: str, file_id: str, rev: int) -> Dict:
    """
        Deprecate a file.
        Files cannot be deleted in Nexus, once one is deprecated, it is no longer possible to update it.

        :param org_label: The label of the organization that the file belongs to.
        :param project_label: The label of the project that the file belongs to.
        :param file_id: The identifier of the file to deprecate.
        :param rev: The last revision of the file.
        :return: A payload containing only the Nexus metadata for this deprecated file.
    """
    path = [SEGMENT, org_label, project_label, url_encode(file_id)]
    return http_delete(path, rev=rev)


def deprecate_(file: Dict, rev: Optional[int] = None) -> Dict:
    """
        Deprecate a file from an existing file resource payload, for instance the value returned
        by nexus.file.fetch(), where some fields where modified, added or removed.
        Files cannot be deleted in Nexus, once one is deprecated, it is no longer possible to update it.

        :param file: Payload of a previously fetched file.
        :param rev: OPTIONAL The last revision of the file. If not provided, the rev from the file argument will be used.
        :return: A payload containing only the Nexus metadata for this deprecated file.
    """

    if rev is None:
        rev = file["_rev"]

    path = file["_self"]

    return http_delete(path, rev=rev)


def tag(org_label: str, project_label: str, file_id: str, rev_to_tag: int, tag_value: str, rev: int) -> Dict:
    """
        Tag a specific revision of the file. Note that a new revision (untagged) will be created

        :param org_label: The label of the organization that the file belongs to.
        :param project_label: The label of the project that the file belongs to.
        :param file_id: The identifier of the file to tag.

        :param rev: The last revision of the file.
        :return: A payload containing only the Nexus metadata for this file.
    """
    path = [SEGMENT, org_label, project_label, url_encode(file_id), "tags"]

    payload = {
        "tag": tag_value,
        "rev": rev_to_tag
    }

    return http_post(path, payload, rev=rev)


def tag_(file: Dict, tag_value: str, rev_to_tag: Optional[int] = None, rev: Optional[int] = None) -> Dict:
    """
        Tag a specific revision of the file. Note that a new revision (untagged) will be created

        :param file: Payload of a previously fetched file.
        :param tag_value: The value (or name) of a tag
        :param rev_to_tag: OPTIONAL Number of the revision to tag.
            If not provided, the revision from the file argument will be used.
        :param rev: OPTIONAL The previous revision you want to update from.
            If not provided, the revision from the file argument will be used.
        :return: A payload containing only the Nexus metadata for this file.
    """

    if rev is None:
        rev = file["_rev"]

    if rev_to_tag is None:
        rev_to_tag = file["_rev"]

    path = file["_self"] + "/tags"

    payload = {
        "tag": tag_value,
        "rev": rev_to_tag
    }

    return http_post(path, body=payload, rev=rev)


def tags(file: Dict) -> Dict:
    """
        List all the tags added to this file, along with their version numbers

        :param file: Payload of a previously fetched file.
        :return: payload containing the list of tags and versions
    """

    path = file["_self"] + "/tags"
    return http_get(path)


def _content_type(filepath: str, content_type: Optional[str]) -> str:
    if content_type is None:
        try:
            guessed_content_type = puremagic.from_file(filepath, True)
        except puremagic.main.PureError as e:
            print(e)
            print("using the default content type instead:", DEFAULT_MIME)
            guessed_content_type = DEFAULT_MIME
        return guessed_content_type
    else:
        return content_type
