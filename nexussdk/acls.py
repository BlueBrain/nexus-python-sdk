from typing import Dict, List

from nexussdk.utils import iam

SEGMENT = "acls"


# Read functions.

def fetch(subpath: str, rev: int = None, self: bool = True) -> Dict:
    return iam.get([SEGMENT, subpath], rev=rev, self=self)


def fetch_(path: str, rev: int = None, self: bool = True) -> Dict:
    return iam.get(path, rev=rev, self=self)


def list(subpath: str, ancestors: bool = False, self: bool = True) -> Dict:
    return iam.get([SEGMENT, subpath], ancestors=ancestors, self=self)


def list_(path: str, ancestors: bool = False, self: bool = True) -> Dict:
    return iam.get(path, ancestors=ancestors, self=self)


# Update functions.

def replace(subpath: str, permissions: List[str], identity: Dict, rev: int) -> Dict:
    payload = _payload(permissions, identity)
    return iam.put([SEGMENT, subpath], payload, rev=rev)


def replace_(path: str, payload: Dict, rev: int) -> Dict:
    return iam.put(path, payload, rev=rev)


def append(subpath: str, permissions: List[str], identity: Dict, rev: int) -> Dict:
    payload = _payload(permissions, identity, "Append")
    return iam.patch([SEGMENT, subpath], payload, rev=rev)


def append_(path: str, payload: Dict, rev: int) -> Dict:
    return iam.patch(path, payload, rev=rev)


def subtract(subpath: str, permissions: List[str], identity: Dict, rev: int) -> Dict:
    payload = _payload(permissions, identity, "Subtract")
    return iam.patch([SEGMENT, subpath], payload, rev=rev)


def subtract_(path: str, payload: Dict, rev: int) -> Dict:
    return iam.patch(path, payload, rev=rev)


# Delete functions.

def delete(subpath: str, rev: int) -> Dict:
    return iam.delete([SEGMENT, subpath], rev=rev)


def delete_(path: str, rev: int) -> Dict:
    return iam.delete(path, rev=rev)


# Internal helpers

def _payload(permissions: List[str], identity: Dict, operation: str = None) -> Dict:
    payload = {
        "acl": [
            {
                "permissions": permissions,
                "identity": identity,
            },
        ]
    }
    if operation is not None:
        payload["@type"] = operation
    return payload
