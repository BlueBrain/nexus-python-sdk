"""
This module provides a Python interface for operations on Realms.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-realms-api.html
"""

from typing import Dict

from nexussdk.utils.http import http_delete, http_get, http_put

SEGMENT = "realms"


# Create functions.

def create(subpath: str, name: str, openid_config: str, logo: str = None) -> Dict:
    """Create a realm.

    :param subpath: Subpath of the realm.
    :param name: Name of the realm.
    :param openid_config: URL of the OpenID configuration.
    :param logo: (optional) URL of a logo.
    :return: The Nexus metadata of the created realm.
    """
    payload = _payload(name, openid_config, logo)
    return http_put([SEGMENT, subpath], payload)


def create_(path: str, payload: Dict) -> Dict:
    """Create a realm (full path version).

    :param path: Full path of the realm.
    :param payload: Payload of the realm.
    :return: The Nexus metadata of the created realm.
    """
    return http_put(path, payload)


# Read functions.

def fetch(subpath: str, rev: int = None) -> Dict:
    """Fetch a realm.

    :param subpath: Subpath of the realm.
    :param rev: (optional) Revision number of the realm.
    :return: The Nexus payload of the fetched realm.
    """
    return http_get([SEGMENT, subpath], rev=rev)


def fetch_(path: str, rev: int = None) -> Dict:
    """Fetch a realm (full path version).

    :param path: Full path of the realm.
    :param rev: (optional) Revision number of the realm.
    :return: The Nexus payload of the fetched realm.
    """
    return http_get(path, rev=rev)


def list() -> Dict:
    """List realms.

    :return: A Nexus results list with the Nexus payloads of the realms.
    """
    return http_get([SEGMENT])


def list_(endpoint: str) -> Dict:
    """List realms (full path version).

    :param endpoint: Endpoint for realms.
    :return: A Nexus results list with the Nexus payloads of the realms.
    """
    return http_get(endpoint)


# Update functions.

def replace(subpath: str, name: str, openid_config: str, rev: int, logo: str = None) -> Dict:
    """Replace a realm.

    :param subpath: Subpath of the realm.
    :param name: Name of the realm.
    :param openid_config: Updated URL of the OpenID configuration.
    :param rev: Last revision of the realm.
    :param logo: (optional) Updated URL of a logo.
    :return: The Nexus metadata of the realm.
    """
    payload = _payload(name, openid_config, logo)
    return http_put([SEGMENT, subpath], payload, rev=rev)


def replace_(path: str, payload: Dict, rev: int) -> Dict:
    """Replace a realm (full path version).

    :param path: Full path of the realm.
    :param payload: Updated payload of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the realm.
    """
    return http_put(path, payload, rev=rev)


# Delete functions.

def deprecate(subpath: str, rev: int) -> Dict:
    """Deprecate a realm.

    :param subpath: Subpath of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the deprecated realm.
    """
    return http_delete([SEGMENT, subpath], rev=rev)


def deprecate_(path: str, rev: int) -> Dict:
    """Deprecate a realm (full path version).

    :param path: Full path of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the deprecated realm.
    """
    return http_delete(path, rev=rev)


# Internal helpers

def _payload(name: str, openid_config: str, logo: str = None) -> Dict:
    """Create a realm payload.

    :param name: Name of the realm.
    :param openid_config: URL of the OpenID configuration.
    :param logo: (optional) URL of a logo.
    :return: Payload of the realm.
    """
    payload = {
        "name": name,
        "openIdConfig": openid_config,
    }
    if logo is not None:
        payload["logo"] = logo
    return payload
