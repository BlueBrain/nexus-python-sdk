from typing import Dict, List

from nexussdk.utils import iam

SEGMENT = "permissions"


# Read functions.

def fetch(rev: int = None):
    return iam.get([SEGMENT], rev=rev)


def fetch_(endpoint: str, rev: int = None) -> Dict:
    return iam.get(endpoint, rev=rev)


# Update functions.

def replace(permissions: List[str], rev: int) -> Dict:
    payload = _payload(permissions)
    return iam.put([SEGMENT], payload, rev=rev)


def replace_(endpoint: str, payload: Dict, rev: int) -> Dict:
    return iam.put(endpoint, payload, rev=rev)


def append(permissions: List[str], rev: int) -> Dict:
    payload = _payload(permissions, "Append")
    return iam.patch([SEGMENT], payload, rev=rev)


def append_(endpoint: str, payload: Dict, rev: int) -> Dict:
    return iam.patch(endpoint, payload, rev=rev)


def subtract(permissions: List[str], rev: int) -> Dict:
    payload = _payload(permissions, "Subtract")
    return iam.patch([SEGMENT], payload, rev=rev)


def subtract_(endpoint: str, payload: Dict, rev: int) -> Dict:
    return iam.patch(endpoint, payload, rev=rev)


# Delete functions.

def delete(rev: int) -> Dict:
    return iam.delete([SEGMENT], rev=rev)


def delete_(endpoint: str, rev: int) -> Dict:
    return iam.delete(endpoint, rev=rev)


# Internal helpers

def _payload(permissions: List[str], operation: str = None):
    payload = {
        "permissions": permissions,
    }
    if operation is not None:
        payload["@type"] = operation
    return payload
