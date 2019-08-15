"""
This module provides a Python interface for operations on Access Control Lists.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-acls-api.html
"""

from typing import Dict, List, Optional

from nexussdk.utils.http import Http


class Acls:
    segment = "acls"
    
    def __init__(self, http: Http):
        self._http = http
    
    
    # Read functions.
    
    def fetch(this, subpath: str, rev: int = None, self: bool = True) -> Dict:
        """Fetch the ACLs on a subpath.
    
        :param subpath: Subpath on which fetching the ACLs.
        :param rev: (optional) Revision number of the ACLs.
        :param self: (optional) If 'True', only the ACLs containing the identities
            found in the authentication token are returned. If 'False', all the
            ACLs on the current subpath are returned.
        :return: A Nexus results list with the Nexus payloads of the ACLs.
        """
        return this._http.get([Acls.segment, subpath], rev=rev, self=self)
    
    
    def fetch_(this, path: str, rev: int = None, self: bool = True) -> Dict:
        """Fetch the ACLs on a full path.
    
        :param path: Full path on which fetching the ACLs.
        :param rev: (optional) Revision number of the ACLs.
        :param self: (optional) If 'True', only the ACLs containing the identities
            found in the authentication token are returned. If 'False', all the
            ACLs on the current subpath are returned.
        :return: A Nexus results list with the Nexus payloads of the ACLs.
        """
        return this._http.get(path, rev=rev, self=self)
    
    
    def list(this, subpath: str, ancestors: bool = False, self: bool = True) -> Dict:
        """List ACLs on a subpath.
    
        :param subpath: Subpath on which listing the ACLs.
        :param ancestors: (optional) If 'True', the ACLs on the parent path of the
            subpath are returned. If 'False', only the ACLs on the current subpath
            are returned.
        :param self: (optional) If 'True', only the ACLs containing the identities
            found in the authentication token are returned. If 'False', all the
            ACLs on the current subpath are returned.
        :return: A Nexus results list with the Nexus payloads of the ACLs.
        """
        return this._http.get([Acls.segment, subpath], ancestors=ancestors, self=self)
    
    
    def list_(this, path: str, ancestors: bool = False, self: bool = True) -> Dict:
        """List ACLs on a full path.
    
        :param path: Full path on which listing the ACLs.
        :param ancestors: (optional) If 'True', the ACLs on the parent path of the
            subpath are returned. If 'False', only the ACLs on the current subpath
            are returned.
        :param self: (optional) If 'True', only the ACLs containing the identities
            found in the authentication token are returned. If 'False', all the
            ACLs on the current subpath are returned.
        :return: A Nexus results list with the Nexus payloads of the ACLs.
        """
        return this._http.get(path, ancestors=ancestors, self=self)
    
    
    # Update functions.
    
    def replace(self, subpath: str, permissions: List[List[str]], identities: List[Dict], rev: int) -> Dict:
        """Replace ACLs on a subpath.
    
        ``permissions`` and ``identities`` have the same order.
    
        :param subpath: Subpath on which replacing the ACLs.
        :param permissions: List of list of permissions.
        :param identities: List of identities for which to replace permissions.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        payload = self._payload(permissions, identities)
        return self._http.put([Acls.segment, subpath], payload, rev=rev)
    
    
    def replace_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Replace ACLs on a full path.
    
        :param path: Full path on which replacing the ACLs.
        :param payload: Payload of the ACLs.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        return self._http.put(path, payload, rev=rev)
    
    
    def append(self, subpath: str, permissions: List[List[str]], identities: List[Dict], rev: int) -> Dict:
        """Append ACLs on a subpath.
    
        ``permissions`` and ``identities`` have the same order.
    
        :param subpath: Subpath on which appending ACLs.
        :param permissions: List of list of permissions.
        :param identities: List of identities for which to append the permissions.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        payload = self._payload(permissions, identities, "Append")
        return self._http.patch([Acls.segment, subpath], payload, rev=rev)
    
    
    def append_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Append ACLs on a full path.
    
        :param path: Full path on which appending ACLs.
        :param payload: Payload of the ACLs to append.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        return self._http.patch(path, payload, rev=rev)
    
    
    def subtract(self, subpath: str, permissions: List[List[str]], identities: List[Dict], rev: int) -> Dict:
        """Subtract ACLs on a subpath.
    
        `permissions`` and ``identities`` have the same order.
    
        :param subpath: Subpath on which subtracting ACLs.
        :param permissions: List of list of permissions.
        :param identities: List of identities for which to remove the permissions.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        payload = self._payload(permissions, identities, "Subtract")
        return self._http.patch([Acls.segment, subpath], payload, rev=rev)
    
    
    def subtract_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Subtract ACLs on a full path.
    
        :param path: Full path on which subtracting ACLs.
        :param payload: Payload of the ACLs to subtract.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        return self._http.patch(path, payload, rev=rev)
    
    
    # Delete functions.
    
    def delete(self, subpath: str, rev: int) -> Dict:
        """Delete ACLs on a subpath.
    
        :param subpath: Subpath on which deleting ACLs.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        return self._http.delete([Acls.segment, subpath], rev=rev)
    
    
    def delete_(self, path: str, rev: int) -> Dict:
        """Delete ACLs on a full path.
    
        :param path: Full path on which deleting ACLs.
        :param rev: Last revision of the ACLs.
        :return: The Nexus metadata of the ACLs.
        """
        return self._http.delete(path, rev=rev)
    
    
    # Internal helpers
    
    def _payload(self, permissions: List[List[str]], identities: List[Dict], operation: str = None) -> Dict:
        """Create an ACLs payload.
    
        ``permissions`` and ``identities`` have the same order.
    
        :param permissions: List of list of permissions.
        :param identities: List of identities to which the permissions apply.
        :param operation: (optional) Corresponding operation: "Append" or "Subtract".
        :return: Payload of the ACLs.
        """
        payload = {
            "acl": [
                {
                    "permissions": x,
                    "identity": y,
                } for x, y in zip(permissions, identities)
            ]
        }
        if operation is not None:
            payload["@type"] = operation
        return payload
    
    
    def events(self, last_id: Optional[str] = None):
        """
        Fetches ACL related events.
    
        :param last_id: ID of the last processed event, if provided, only events after
                the event with the provided ID will be returned.
        :return: iterator of ACL events
        """
        return self._http.sse_request("/acls/events", last_id)
