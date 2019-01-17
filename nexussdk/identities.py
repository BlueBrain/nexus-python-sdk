from typing import Dict

from nexussdk.utils import iam

SEGMENT = "identities"


# Read functions.

def fetch():
    return iam.get([SEGMENT])


def fetch_(endpoint: str) -> Dict:
    return iam.get(endpoint)
