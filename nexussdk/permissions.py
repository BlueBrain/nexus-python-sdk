from typing import Dict

from nexussdk.utils import iam


# Read functions.

def fetch(path: str, rev: int = None) -> Dict:
    return iam.get(path, rev=rev)


# Update functions.

def replace(path: str, permissions: Dict, rev: int) -> Dict:
    return iam.put(path, permissions, rev=rev)


def append(path: str, permissions: Dict, rev: int) -> Dict:
    return iam.patch(path, permissions, rev=rev)


def subtract(path: str, permissions: Dict, rev: int) -> Dict:
    return iam.patch(path, permissions, rev=rev)


# Delete functions.

def delete(path: str, rev: int) -> Dict:
    return iam.delete(path, rev=rev)
