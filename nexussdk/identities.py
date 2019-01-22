from typing import Dict

from nexussdk.utils.http import http_get

SEGMENT = "identities"


# Read functions.

def fetch() -> Dict:
    """Fetch the identities.

    :return: A list with the Nexus payloads of the identities.
    """
    return http_get([SEGMENT])


def fetch_(endpoint: str) -> Dict:
    """Fetch the identities (full path version).

    :return: A list with the Nexus payloads of the identities.
    """
    return http_get(endpoint)
