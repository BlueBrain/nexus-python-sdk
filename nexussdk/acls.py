from typing import Dict

from nexussdk.utils import iam


# Create functions.

def create(path: str, acls: Dict, rev: int) -> Dict:
    return iam.put(path, acls, rev=rev)


# Read functions.

def fetch(path: str, rev: int = None, self: bool = True) -> Dict:
    return iam.get(path, rev=rev, self=self)


def list_(path: str, ancestors: bool = False, self: bool = True) -> Dict:
    return iam.get(path, ancestors=ancestors, self=self)


# Update functions.

def replace(path: str, acls: Dict, rev: int) -> Dict:
    return iam.put(path, acls, rev=rev)


def append(path: str, acls: Dict, rev: int) -> Dict:
    return iam.patch(path, acls, rev=rev)


def subtract(path: str, acls: Dict, rev: int) -> Dict:
    return iam.patch(path, acls, rev=rev)


# Delete functions.

def delete(path: str, rev: int) -> Dict:
    return iam.delete(path, rev=rev)
