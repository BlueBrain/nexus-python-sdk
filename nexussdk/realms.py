from typing import Dict

from nexussdk.utils.http import http_delete, http_get, http_put

SEGMENT = "realms"


# Create functions.

def create(name: str, description: str, openid_config: str) -> Dict:
    """Create a realm.

    :param name: Name of the realm.
    :param description: Description of the realm.
    :param openid_config: URL of the OpenID configuration.
    :return: The Nexus metadata of the created realm.
    """
    payload = _payload(description, openid_config)
    return http_put([SEGMENT, name], payload)


def create_(path: str, payload: Dict) -> Dict:
    """Create a realm (full path version).

    :param path: Full path of the realm.
    :param payload: Payload of the realm.
    :return: The Nexus metadata of the created realm.
    """
    return http_put(path, payload)


# Read functions.

def fetch(name: str, rev: int = None) -> Dict:
    """Fetch a realm.

    :param name: Name of the realm.
    :param rev: (optional) Revision number of the realm.
    :return: The Nexus payload of the fetched realm.
    """
    return http_get([SEGMENT, name], rev=rev)


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

def update(name: str, description: str, openid_config: str, rev: int) -> Dict:
    """Update a realm.
    
    :param name: Name of the realm.
    :param description: Updated description of the realm.
    :param openid_config: Updated URL of the OpenID configuration.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the updated realm.
    """
    payload = _payload(description, openid_config)
    return http_put([SEGMENT, name], payload, rev=rev)


def update_(path: str, payload: Dict, rev: int) -> Dict:
    """Update a realm (full path version).
    
    :param path: Full path of the realm.
    :param payload: Updated payload of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the updated realm.
    """
    return http_put(path, payload, rev=rev)


# Delete functions.

def deprecate(name: str, rev: int) -> Dict:
    """Deprecate a realm.
    
    :param name: Name of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the deprecated realm.
    """
    return http_delete([SEGMENT, name], rev=rev)


def deprecate_(path: str, rev: int) -> Dict:
    """Deprecate a realm (full path version).
    
    :param path: Full path of the realm.
    :param rev: Last revision of the realm.
    :return: The Nexus metadata of the deprecated realm.
    """
    return http_delete(path, rev=rev)


# Internal helpers

def _payload(description: str, openid_config: str) -> Dict:
    """Create a realm payload.
    
    :param description: Description of the realm.
    :param openid_config: URL of the OpenID configuration.
    :return: Payload of the realm.
    """
    return {
        "name": description,
        "openIdConfig": openid_config,
    }
