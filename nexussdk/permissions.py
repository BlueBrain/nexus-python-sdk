"""
This module provides a Python interface for operations on Permissions.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-permissions-api.html
"""

from typing import Dict, List, Optional

from nexussdk.utils.http import Http


class Permissions:
    segment = "permissions"

    def __init__(self, http: Http):
        self._http = http

    # Read functions.

    def fetch(self, rev: int = None) -> Dict:
        """Fetch the permissions.
    
        :param rev: (optional) Revision number of the permissions.
        :return: A Nexus payload with the permissions.
        """
        return self._http.get([Permissions.segment], rev=rev)

    def fetch_(self, endpoint: str, rev: int = None) -> Dict:
        """Fetch the permissions (full path version).
    
        :param endpoint: Endpoint for permissions.
        :param rev: (optional) Revision number of the permissions.
        :return: A Nexus payload with the permissions.
        """
        return self._http.get(endpoint, rev=rev)

    # Update functions.

    def replace(self, permissions: List[str], rev: int) -> Dict:
        """Replace the user-defined permissions.
    
        :param permissions: List of user-defined permissions.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        payload = self._payload(permissions)
        return self._http.put([Permissions.segment], payload, rev=rev)

    def replace_(self, endpoint: str, payload: Dict, rev: int) -> Dict:
        """Replace the user-defined permissions (full path version).
    
        :param endpoint: Endpoint for permissions.
        :param payload: Payload of user-defined permissions.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        return self._http.put(endpoint, payload, rev=rev)

    def append(self, permissions: List[str], rev: int) -> Dict:
        """Append user-defined permissions.
    
        :param permissions: List of user-defined permissions.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        payload = self._payload(permissions, "Append")
        return self._http.patch([Permissions.segment], payload, rev=rev)

    def append_(self, endpoint: str, payload: Dict, rev: int) -> Dict:
        """Append user-defined permissions (full path version).
    
        :param endpoint: Endpoint for permissions.
        :param payload: Payload of user-defined permissions to append.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        return self._http.patch(endpoint, payload, rev=rev)

    def subtract(self, permissions: List[str], rev: int) -> Dict:
        """Subtract user-defined permissions.
    
        :param permissions: List of user-defined permissions.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        payload = self._payload(permissions, "Subtract")
        return self._http.patch([Permissions.segment], payload, rev=rev)

    def subtract_(self, endpoint: str, payload: Dict, rev: int) -> Dict:
        """Subtract user-defined permissions (full path version).
    
        :param endpoint: Endpoint for permissions.
        :param payload: Payload of user-defined permissions to subtract.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        return self._http.patch(endpoint, payload, rev=rev)

    # Delete functions.

    def delete(self, rev: int) -> Dict:
        """Delete user-defined permissions.
    
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        return self._http.delete([Permissions.segment], rev=rev)

    def delete_(self, endpoint: str, rev: int) -> Dict:
        """Delete user-defined permissions (full path version).
    
        :param endpoint: Endpoint for permissions.
        :param rev: Last revision of the permissions.
        :return: The Nexus metadata of the permissions.
        """
        return self._http.delete(endpoint, rev=rev)

    # Internal helpers

    def _payload(self, permissions: List[str], operation: str = None) -> Dict:
        """Create a user-defined permissions payload.
    
        :param permissions: List of user-defined permissions.
        :param operation: (optional) Corresponding operation: "Append" or "Subtract".
        :return: Payload of user-defined permissions.
        """
        payload = {
            "permissions": permissions,
        }
        if operation is not None:
            payload["@type"] = operation
        return payload

    def events(self, last_id: Optional[str] = None):
        """
        Fetches permissions related events.
    
        :param last_id: ID of the last processed event, if provided, only events after
                the event with the provided ID will be returned.
        :return: iterator of permission events
        """
        return self._http.sse_request("/permissions/events", last_id)
