"""
This module provides a Python interface for operations on Permissions.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-permissions-api.html
"""

from typing import Dict, List

from nexussdk.utils.http import http_delete, http_get, http_patch, http_put

SEGMENT = "permissions"


# Read functions.

def fetch(rev: int = None) -> Dict:
    """Fetch the permissions.

    :param rev: (optional) Revision number of the permissions.
    :return: A Nexus payload with the permissions.
    """
    return http_get([SEGMENT], rev=rev)


def fetch_(endpoint: str, rev: int = None) -> Dict:
    """Fetch the permissions (full path version).

    :param endpoint: Endpoint for permissions.
    :param rev: (optional) Revision number of the permissions.
    :return: A Nexus payload with the permissions.
    """
    return http_get(endpoint, rev=rev)


# Update functions.

def replace(permissions: List[str], rev: int) -> Dict:
    """Replace the user-defined permissions.

    :param permissions: List of user-defined permissions.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    payload = _payload(permissions)
    return http_put([SEGMENT], payload, rev=rev)


def replace_(endpoint: str, payload: Dict, rev: int) -> Dict:
    """Replace the user-defined permissions (full path version).

    :param endpoint: Endpoint for permissions.
    :param payload: Payload of user-defined permissions.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    return http_put(endpoint, payload, rev=rev)


def append(permissions: List[str], rev: int) -> Dict:
    """Append user-defined permissions.

    :param permissions: List of user-defined permissions.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    payload = _payload(permissions, "Append")
    return http_patch([SEGMENT], payload, rev=rev)


def append_(endpoint: str, payload: Dict, rev: int) -> Dict:
    """Append user-defined permissions (full path version).

    :param endpoint: Endpoint for permissions.
    :param payload: Payload of user-defined permissions to append.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    return http_patch(endpoint, payload, rev=rev)


def subtract(permissions: List[str], rev: int) -> Dict:
    """Subtract user-defined permissions.

    :param permissions: List of user-defined permissions.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    payload = _payload(permissions, "Subtract")
    return http_patch([SEGMENT], payload, rev=rev)


def subtract_(endpoint: str, payload: Dict, rev: int) -> Dict:
    """Subtract user-defined permissions (full path version).

    :param endpoint: Endpoint for permissions.
    :param payload: Payload of user-defined permissions to subtract.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    return http_patch(endpoint, payload, rev=rev)


# Delete functions.

def delete(rev: int) -> Dict:
    """Delete user-defined permissions.

    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    return http_delete([SEGMENT], rev=rev)


def delete_(endpoint: str, rev: int) -> Dict:
    """Delete user-defined permissions (full path version).

    :param endpoint: Endpoint for permissions.
    :param rev: Last revision of the permissions.
    :return: The Nexus metadata of the permissions.
    """
    return http_delete(endpoint, rev=rev)


# Internal helpers

def _payload(permissions: List[str], operation: str = None) -> Dict:
    """Create a user-defined permissions payload.

    :param permissions: List of user-defined permissions.
    :param operation: (optional) Corresponding operation: "Append" or "Subtract".
    :return: Payload of user-defined permissions.
    """
    payload = {
        "permissions": permissions,
    }
    if operation is not None:
        payload["@type"] = operation
    return payload
