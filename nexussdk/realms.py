from typing import Dict

from nexussdk.utils import iam


# Create functions.

def create(path: str, config: Dict, rev: int) -> Dict:
    return iam.put(path, config, rev=rev)


# Read functions.

def fetch(path: str, rev: int = None) -> Dict:
    return iam.get(path, rev=rev)


def list_(path: str) -> Dict:
    return iam.get(path)


# Update functions.

def update(path: str, config: Dict, rev: int) -> Dict:
    return iam.put(path, config, rev=rev)


# Delete functions.

def delete(path: str, rev: int) -> Dict:
    return iam.delete(path, rev=rev)
