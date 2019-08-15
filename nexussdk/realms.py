"""
This module provides a Python interface for operations on Realms.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-realms-api.html
"""

from typing import Dict, Optional

from nexussdk.utils.http import Http


class Realms:
    segment = "realms"

    def __init__(self, http: Http):
        self._http = http

    # Create functions.

    def create(self, subpath: str, name: str, openid_config: str, logo: str = None) -> Dict:
        """Create a realm.
    
        :param subpath: Subpath of the realm.
        :param name: Name of the realm.
        :param openid_config: URL of the OpenID configuration.
        :param logo: (optional) URL of a logo.
        :return: The Nexus metadata of the created realm.
        """
        payload = self._payload(name, openid_config, logo)
        return self._http.put([Realms.segment, subpath], payload)

    def create_(self, path: str, payload: Dict) -> Dict:
        """Create a realm (full path version).
    
        :param path: Full path of the realm.
        :param payload: Payload of the realm.
        :return: The Nexus metadata of the created realm.
        """
        return self._http.put(path, payload)

    # Read functions.

    def fetch(self, subpath: str, rev: int = None) -> Dict:
        """Fetch a realm.
    
        :param subpath: Subpath of the realm.
        :param rev: (optional) Revision number of the realm.
        :return: The Nexus payload of the fetched realm.
        """
        return self._http.get([Realms.segment, subpath], rev=rev)

    def fetch_(self, path: str, rev: int = None) -> Dict:
        """Fetch a realm (full path version).
    
        :param path: Full path of the realm.
        :param rev: (optional) Revision number of the realm.
        :return: The Nexus payload of the fetched realm.
        """
        return self._http.get(path, rev=rev)

    def list(self, ) -> Dict:
        """List realms.
    
        :return: A Nexus results list with the Nexus payloads of the realms.
        """
        return self._http.get([Realms.segment])

    def list_(self, endpoint: str) -> Dict:
        """List realms (full path version).
    
        :param endpoint: Endpoint for realms.
        :return: A Nexus results list with the Nexus payloads of the realms.
        """
        return self._http.get(endpoint)

    # Update functions.

    def replace(self, subpath: str, name: str, openid_config: str, rev: int, logo: str = None) -> Dict:
        """Replace a realm.
    
        :param subpath: Subpath of the realm.
        :param name: Name of the realm.
        :param openid_config: Updated URL of the OpenID configuration.
        :param rev: Last revision of the realm.
        :param logo: (optional) Updated URL of a logo.
        :return: The Nexus metadata of the realm.
        """
        payload = self._payload(name, openid_config, logo)
        return self._http.put([Realms.segment, subpath], payload, rev=rev)

    def replace_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Replace a realm (full path version).
    
        :param path: Full path of the realm.
        :param payload: Updated payload of the realm.
        :param rev: Last revision of the realm.
        :return: The Nexus metadata of the realm.
        """
        return self._http.put(path, payload, rev=rev)

    # Delete functions.

    def deprecate(self, subpath: str, rev: int) -> Dict:
        """Deprecate a realm.
    
        :param subpath: Subpath of the realm.
        :param rev: Last revision of the realm.
        :return: The Nexus metadata of the deprecated realm.
        """
        return self._http.delete([Realms.segment, subpath], rev=rev)

    def deprecate_(self, path: str, rev: int) -> Dict:
        """Deprecate a realm (full path version).
    
        :param path: Full path of the realm.
        :param rev: Last revision of the realm.
        :return: The Nexus metadata of the deprecated realm.
        """
        return self._http.delete(path, rev=rev)

    # Internal helpers

    def _payload(self, name: str, openid_config: str, logo: str = None) -> Dict:
        """Create a realm payload.
    
        :param name: Name of the realm.
        :param openid_config: URL of the OpenID configuration.
        :param logo: (optional) URL of a logo.
        :return: Payload of the realm.
        """
        payload = {
            "name": name,
            "openIdConfig": openid_config,
        }
        if logo is not None:
            payload["logo"] = logo
        return payload

    def events(self, last_id: Optional[str] = None):
        """
        Fetches realm related events.
    
        :param last_id: ID of the last processed event, if provided, only events after
                the event with the provided ID will be returned.
        :return: iterator of realm events
        """
        return sse_request("/projects/events", last_id)
