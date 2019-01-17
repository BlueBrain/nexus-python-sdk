from typing import Dict

from nexussdk.utils.http import http_delete, http_get, http_put

SEGMENT = "realms"


# Create functions.

def create(name: str, description: str, open_id_config: str) -> Dict:
    payload = _payload(description, open_id_config)
    return http_put([SEGMENT, name], payload)


def create_(path: str, payload: Dict) -> Dict:
    return http_put(path, payload)


# Read functions.

def fetch(name: str, rev: int = None) -> Dict:
    return http_get([SEGMENT, name], rev=rev)


def fetch_(path: str, rev: int = None) -> Dict:
    return http_get(path, rev=rev)


def list() -> Dict:
    return http_get([SEGMENT])


def list_(endpoint: str) -> Dict:
    return http_get(endpoint)


# Update functions.

def update(name: str, description: str, open_id_config: str, rev: int) -> Dict:
    payload = _payload(description, open_id_config)
    return http_put([SEGMENT, name], payload, rev=rev)


def update_(path: str, payload: Dict, rev: int) -> Dict:
    return http_put(path, payload, rev=rev)


# Delete functions.

def deprecate(name: str, rev: int) -> Dict:
    return http_delete([SEGMENT, name], rev=rev)


def deprecate_(path: str, rev: int) -> Dict:
    return http_delete(path, rev=rev)


# Internal helpers

def _payload(description: str, open_id_config: str) -> Dict:
    return {
        "name": description,
        "openIdConfig": open_id_config,
    }
