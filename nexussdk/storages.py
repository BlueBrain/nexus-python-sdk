"""
This module provides a Python interface for operations on Storages.
It is part of the Knowledge Graph API of Blue Brain Nexus v1.
https://bluebrainnexus.io/docs/api/1.1/kg/kg-storages-api.html
"""

from typing import Dict, Optional

from urllib.parse import quote_plus as url_encode
from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_delete
from nexussdk.utils.tools import listing_params

SEGMENT = "storages"


def create_(org_label: str, project_label: str, payload: Dict, storage_id: Optional[str]) -> Dict:
    """Create storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param payload: Payload of the storage
    :param storage_id: (optional) User-defined ID of the storage, given as an IRI which is not URL encoded.
    :return: The Nexus metadata of the created storage.
    """
    if storage_id is not None:
        payload["@id"] = storage_id

    return http_post([SEGMENT, org_label, project_label], body=payload)


def update_(org_label: str, project_label: str, payload: Dict, storage_id: str, rev: int) -> Dict:
    """Update storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param payload: Payload of the storage
    :param storage_id: (optional) User-defined ID of the storage, given as an IRI which is not URL encoded.
    :param rev: last known revision of the storage
    :return: The Nexus metadata of the updated storage.
    """
    return http_put([SEGMENT, org_label, project_label, url_encode(storage_id)], body=payload, rev=rev)


def create_disk_storage(org_label: str, project_label: str, volume: str,
                        storage_id: Optional[str] = None, read_permission: Optional[str] = None,
                        write_permission: Optional[str] = None, default: bool = False) -> Dict:
    """Create disk storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param volume: the volume on the local file system where the files are going to be stored
    :param storage_id: (optional) User-defined ID of the storage, given as an IRI which is not URL encoded.
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :return: The Nexus metadata of the created storage.
    """
    payload = {
        "@type": "nxv:DiskStorage",
        "volume": volume,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    return create_(org_label, project_label, payload, storage_id)


def create_s3_storage(org_label: str, project_label: str,
                      bucket: str,
                      storage_id: Optional[str] = None, read_permission: Optional[str] = None,
                      write_permission: Optional[str] = None, default: bool = False, endpoint: Optional[str] = None,
                      region: Optional[str] = None,
                      access_key: Optional[str] = None,
                      secret_key: Optional[str] = None) -> Dict:
    """Create S3 storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param bucket: the S3 bucket where the files are going to be stored
    :param storage_id: (optional) User-defined ID of the storage, given as an IRI which is not URL encoded.
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :param endpoint: (optional) S3 endpoint, either the domain or a full URL
    :param region: (optional) S3 region
    :param access_key: (optional) S3 access key
    :param secret_key: (optional) S3 secret key
    :return: The Nexus metadata of the created storage.
    """
    payload = {
        "@type": "nxv:S3Storage",
        "bucket": bucket,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    if endpoint is not None:
        payload["endpoint"] = endpoint

    if region is not None:
        payload["region"] = region

    if access_key is not None:
        payload["accessKey"] = access_key

    if secret_key is not None:
        payload["secretKey"] = secret_key

    return create_(org_label, project_label, payload, storage_id)


def create_external_disk_storage(org_label: str, project_label: str, endpoint: str, folder: str,
                                 storage_id: Optional[str] = None, read_permission: Optional[str] = None,
                                 write_permission: Optional[str] = None, default: bool = False,
                                 credentials: Optional[str] = None) -> Dict:
    """Create external disk storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param endpoint: endpoint to communicate with the external storage
    :param folder:  external storage folder (similar concept to bucket in the S3)
    :param storage_id: (optional) User-defined ID of the storage, given as an IRI which is not URL encoded.
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :param credentials: (optional) external storage optional Bearer Token
    :return: The Nexus metadata of the created storage.
    """
    payload = {
        "@type": "nxv:ExternalDiskStorage",
        "endpoint": endpoint,
        "folder": folder,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    if credentials is not None:
        payload["credentials"] = credentials

    return create_(org_label, project_label, payload, storage_id)


def update_disk_storage(org_label: str, project_label: str, volume: str,
                        storage_id: str, rev: int, read_permission: Optional[str] = None,
                        write_permission: Optional[str] = None, default: bool = False) -> Dict:
    """Update disk storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param volume: the volume on the local file system where the files are going to be stored
    :param storage_id: the storage ID
    :param rev: last known revision of the storage
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :return: The Nexus metadata of the updated storage.
    """
    payload = {
        "@id": storage_id,
        "@type": "nxv:DiskStorage",
        "volume": volume,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    return update_(org_label, project_label, payload, storage_id, rev)


def update_s3_storage(org_label: str, project_label: str,
                      bucket: str,
                      storage_id: str, rev: int, read_permission: Optional[str] = None,
                      write_permission: Optional[str] = None, default: bool = False, endpoint: Optional[str] = None,
                      region: Optional[str] = None,
                      access_key: Optional[str] = None,
                      secret_key: Optional[str] = None) -> Dict:
    """Update S3 storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param bucket: the S3 bucket where the files are going to be stored
    :param storage_id: the storage ID
    :param rev: last known revision of the storage
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :param endpoint: (optional) S3 endpoint, either the domain or a full URL
    :param region: (optional) S3 region
    :param access_key: (optional) S3 access key
    :param secret_key: (optional) S3 secret key
    :return: The Nexus metadata of the updated storage.
    """
    payload = {
        "@id": storage_id,
        "@type": "nxv:S3Storage",
        "bucket": bucket,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    if endpoint is not None:
        payload["endpoint"] = endpoint

    if region is not None:
        payload["region"] = region

    if access_key is not None:
        payload["accessKey"] = access_key

    if secret_key is not None:
        payload["secretKey"] = secret_key

    return update_(org_label, project_label, payload, storage_id, rev)


def update_external_disk_storage(org_label: str, project_label: str, endpoint: str, folder: str,
                                 storage_id: str, rev: int, read_permission: Optional[str] = None,
                                 write_permission: Optional[str] = None, default: bool = False,
                                 credentials: Optional[str] = None) -> Dict:
    """Update external disk storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param endpoint: endpoint to communicate with the external storage
    :param folder:  external storage folder (similar concept to bucket in the S3)
    :param storage_id: the storage ID
    :param rev: last known revision of the storage
    :param read_permission: (optional) the permission required in order to download a file from this storage
    :param write_permission: (optional) the permission required in order to upload a file to this storage
    :param default: (optional) whether the storage should be the default storage for the project, defaults to False
    :param credentials: (optional) external storage optional Bearer Token
    :return: The Nexus metadata of the updated storage.
    """
    payload = {
        "@type": "nxv:ExternalDiskStorage",
        "endpoint": endpoint,
        "folder": folder,
        "default": default
    }

    if storage_id is not None:
        payload["@id"] = storage_id

    if read_permission is not None:
        payload["readPermission"] = read_permission

    if write_permission is not None:
        payload["writePermission"] = write_permission

    if credentials is not None:
        payload["credentials"] = credentials

    return update_(org_label, project_label, payload, storage_id, rev)


def deprecate(org_label: str, project_label: str, storage_id: str, rev: int) -> Dict:
    """Deprecate storage

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param storage_id: the storage ID
    :param rev: last known revision of the storage
    :return: The Nexus metadata of the storage.
    """
    return http_delete([SEGMENT, org_label, project_label, url_encode(storage_id)], rev=rev)


def tag(org_label: str, project_label: str, storage_id: str, tag: str, rev_to_tag: str, rev: int) -> Dict:
    """Tag a storage

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param storage_id: the storage ID
    :param tag: tag label
    :param rev_to_tag: revision to tag
    :param rev: last known revision of the storage
    :return: The Nexus metadata of the updated storage.
    """
    payload = {
        "tag": tag,
        "rev": rev_to_tag,
    }
    return http_post([SEGMENT, org_label, project_label, url_encode(storage_id), "tags"], payload, rev=rev)


def tags(org_label: str, project_label: str, storage_id: str) -> Dict:
    """Fetch tags for storage.

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param storage_id: the storage ID
    :return: The tags for the storage.
    """
    return http_get([SEGMENT, org_label, project_label, url_encode(storage_id), "tags"])


def fetch(org_label: str, project_label: str, storage_id: str, tag: Optional[str] = None,
          rev: Optional[int] = None) -> Dict:
    """Fetch a storage

    :param org_label: Label of the organization the storage belongs to.
    :param project_label: Label of the project the storage belongs to.
    :param storage_id: the storage ID
    :param tag: tag to fetch
    :param rev: revision to fetch
    :return: storage payload
    """
    return http_get([SEGMENT, org_label, project_label, url_encode(storage_id)], rev=rev, tag=tag)


def list(org_label: str, project_label: str, pagination_from: Optional[int] = None,
         pagination_size: Optional[int] = None, deprecated: Optional[bool] = None, type: Optional[str] = None,
         created_by: Optional[str] = None, updated_by: Optional[str] = None, rev: Optional[int] = None) -> Dict:
    """List storages corresponding to some criteria.

    :param org_label: Label of the organization to list the storages for.
    :param project_label: Label of the project to list the storages for
    :param pagination_from: (optional) Pagination index to start from.
        Default: ``0``.
    :param pagination_size: (optional) Number of results to return per page.
        Default: ``20``.
    :param deprecated: (optional) Deprecation status of the storages to keep.
    :param type: (optional) Type of the storages to keep, given as an IRI.
    :param created_by: (optional) Identity ID of the creator of the storages
        to keep, given as an IRI.
    :param updated_by: (optional) Identity ID of the last identity which has
        updated the storages to keep, given as en IRI.
    :param rev: (optional) Revision number of the storages to keep.
    :return: A Nexus results list with the Nexus metadata of the matching storages.
    """
    return http_get([SEGMENT, org_label, project_label],
                    params=listing_params(pagination_from, pagination_size, deprecated, type, created_by, updated_by,
                                          rev))
