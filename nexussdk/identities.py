"""
This module provides a Python interface for operations on Identities.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-identities.html
"""

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
