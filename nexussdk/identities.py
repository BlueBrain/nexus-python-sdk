from typing import Dict

from nexussdk.utils.http import http_get

SEGMENT = "identities"


# Read functions.

def fetch():
    return http_get([SEGMENT])


def fetch_(endpoint: str) -> Dict:
    return http_get(endpoint)
