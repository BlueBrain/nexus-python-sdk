"""
This module provides a Python interface for operations on Identities.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-identities.html
"""

from typing import Dict

from nexussdk.utils.http import Http


class Identities:
    segment = "identities"

    def __init__(self, http: Http):
        self._http = http

    # Read functions.

    def fetch(self) -> Dict:
        """Fetch the identities.

        :return: A list with the Nexus payloads of the identities.
        """
        return self._http.get([Identities.segment])

    def fetch_(self, endpoint: str) -> Dict:
        """Fetch the identities (full path version).

        :return: A list with the Nexus payloads of the identities.
        """
        return self._http.get(endpoint)
