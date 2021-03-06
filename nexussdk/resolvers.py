"""
This module provides a Python interface for operations on Resolvers.
It is part of the Knowledge Graph API of Blue Brain Nexus v1.
https://bluebrainnexus.io/docs/api/1.1/kg/kg-resolvers-api.html
"""

from typing import Dict, List, Optional
from urllib.parse import quote_plus as encode_url

from nexussdk.utils.http import Http


class Resolvers:
    segment = "resolvers"

    def __init__(self, http: Http):
        self._http = http

    # Create functions.

    def create(self, org_label: str, project_label: str, projects: List[str], identities: List[Dict],
               priority: int, id: str = None, resource_types: List[str] = None) -> Dict:
        """Create a cross-project resolver.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param projects: List of target projects, given with format ``organization/project``.
        :param identities: List of identities the creator of the resolver has and
            which have the permission ``resources/read`` on the target projects.
        :param priority: Resolution priority.
        :param id: (optional) User-defined ID of the resolver, given as an IRI
            which is not URL encoded.
        :param resource_types: (optional) List of types of the resources to resolve,
            given as IRIs.
        :return: The Nexus metadata of the created resolver.
        """
        payload = self._payload(projects, identities, priority, id, resource_types)
        return self._http.post([self.segment, org_label, project_label], payload)

    def create_(self, path: str, payload: Dict, id: str = None) -> Dict:
        """Create a resolver (path version).
    
        :param path: Full path of the project the resolver belongs to, URL encoded.
        :param payload: Payload of the resolver.
        :param id: (optional) User-defined ID of the resolver, given as an IRI
            which is not URL encoded.
        :return: The Nexus metadata of the created resolver.
        """
        if id is None:
            return self._http.post(path, payload)
        else:
            encoded_id = encode_url(id)
            p = "{}/{}".format(path, encoded_id)
            return self._http.put(p, payload)

    # Read functions.

    def fetch(self, org_label: str, project_label: str, id: str, tag: str = None, rev: int = None) -> Dict:
        """Fetch a resolver.
    
        Raise an ``Exception`` if ``rev`` and ``tag`` are used together.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param id: ID of the resolver, given as an IRI which is not URL encoded.
        :param tag: (optional) Tag of the resolver.
        :param rev: (optional) Revision number of the resolver.
        :return: The Nexus payload of the fetched resolver.
        """
        self._check(rev, tag)
        encoded_id = encode_url(id)
        return self._http.get([self.segment, org_label, project_label, encoded_id], rev=rev, tag=tag)

    def fetch_(self, path: str, tag: str = None, rev: int = None) -> Dict:
        """Fetch a resolver (full path version).
    
        Raise an ``Exception`` if ``rev`` and ``tag`` are used together.
    
        :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
        :param tag: (optional) Tag of the resolver.
        :param rev: (optional) Revision number of the resolver.
        :return: The Nexus payload of the fetched resolver.
        """
        self._check(rev, tag)
        return self._http.get(path, rev=rev, tag=tag)

    def list(self, org_label: str, project_label: str, pagination_from: int = None,
             pagination_size: int = None, deprecated: bool = None, type: str = None,
             created_by: str = None, updated_by: str = None, rev: int = None) -> Dict:
        """List resolvers corresponding to some criteria.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param pagination_from: (optional) Pagination index to start from.
            Default: ``0``.
        :param pagination_size: (optional) Number of results to return per page.
            Default: ``20``.
        :param deprecated: (optional) Deprecation status of the resolvers to keep.
        :param type: (optional) Type of the resolvers to keep, given as an IRI.
        :param created_by: (optional) Identity ID of the creator of the resolvers
            to keep, given as an IRI.
        :param updated_by: (optional) Identity ID of the last identity which has
            updated the resolvers to keep, given as en IRI.
        :param rev: (optional) Revision number of the resolvers to keep.
        :return: A Nexus results list with the Nexus metadata of the matching resolvers.
        """
        params = self._params(pagination_from, pagination_size, deprecated, type, created_by, updated_by, rev)
        return self._http.get([self.segment, org_label, project_label], params=params)

    def list_(self, path: str, pagination_from: int = None, pagination_size: int = None,
              deprecated: bool = None, type: str = None, created_by: str = None,
              updated_by: str = None, rev: int = None) -> Dict:
        """List resolvers corresponding to some criteria (path version).
    
        :param path: Full path of the project the resolver belongs to, URL encoded.
        :param pagination_from: (optional) Pagination index to start from.
            Default: ``0``.
        :param pagination_size: (optional) Number of results to return per page.
            Default: ``20``.
        :param deprecated: (optional) Deprecation status of the resolvers to keep.
        :param type: (optional) Type of the resolvers to keep, given as an IRI.
        :param created_by: (optional) Identity ID of the creator of the resolvers
            to keep, given as an IRI.
        :param updated_by: (optional) Identity ID of the last identity which has
            updated the resolvers to keep, given as en IRI.
        :param rev: (optional) Revision number of the resolvers to keep.
        :return: A Nexus results list with the Nexus metadata of the matching resolvers.
        """
        params = self._params(pagination_from, pagination_size, deprecated, type, created_by, updated_by, rev)
        return self._http.get(path, params=params)

    # Update functions.

    def update(self, org_label: str, project_label: str, id: str, projects: List[str],
               identities: List[Dict], priority: int, rev: int, resource_types: List[str] = None) -> Dict:
        """Update a resolver.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param id: ID of the resolver, given as an IRI which is not URL encoded.
        :param projects: List of target projects, given with format ``organization/project``.
        :param identities: List of identities the creator of the resolver has and
            which have the permission ``resources/read`` on the target projects.
        :param priority: Resolution priority.
        :param rev: Last revision of the resolver.
        :param resource_types: (optional) List of types of the resources to resolve,
            given as IRIs.
        :return: The Nexus metadata of the updated resolver.
        """
        encoded_id = encode_url(id)
        payload = self._payload(projects, identities, priority, id, resource_types)
        return self._http.put([self.segment, org_label, project_label, encoded_id], payload, rev=rev)

    def update_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Update a resolver (full path version).
    
        :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
        :param payload: Payload of the resolver.
        :param rev: Last revision of the resolver.
        :return: The Nexus metadata of the updated resolver.
        """
        return self._http.put(path, payload, rev=rev)

    def tag(self, org_label: str, project_label: str, id: str, tag: str, rev_to_tag: str, rev: int) -> Dict:
        """Tag a revision of a resolver.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param id: ID of the resolver, given as an IRI which is not URL encoded.
        :param tag: Tag to set.
        :param rev_to_tag: Revision number to tag.
        :param rev: Last revision of the resolver.
        :return: The Nexus metadata of the tagged resolver.
        """
        encoded_id = encode_url(id)
        payload = {
            "tag": tag,
            "rev": rev_to_tag,
        }
        return self._http.post([self.segment, org_label, project_label, encoded_id, "tags"], payload, rev=rev)

    def tag_(self, path: str, payload: Dict, rev: int) -> Dict:
        """Tag a revision of a resolver (full path version).
    
        :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
        :param payload: Payload of the tag.
        :param rev: Last revision of the resolver.
        :return: The Nexus metadata of the tagged resolver.
        """
        p = "{}/tags".format(path)
        return self._http.post(p, payload, rev=rev)

    # Delete functions.

    def deprecate(self, org_label: str, project_label: str, id: str, rev: int) -> Dict:
        """Deprecate a resolver.
    
        :param org_label: Label of the organization the resolver belongs to.
        :param project_label: Label of the project the resolver belongs to.
        :param id: ID of the resolver, given as an IRI which is not URL encoded.
        :param rev: Last revision of the resolver.
        :return: The Nexus metadata of the deprecated resolver.
        """
        encoded_id = encode_url(id)
        return self._http.delete([self.segment, org_label, project_label, encoded_id], rev=rev)

    def deprecate_(self, path: str, rev: int) -> Dict:
        """Deprecate a resolver (full path version).
    
        :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
        :param rev: Last revision of the resolver.
        :return: The Nexus metadata of the deprecated resolver.
        """
        return self._http.delete(path, rev=rev)

    # Internal helpers

    def _payload(self, projects: List[str], identities: List[Dict], priority: int,
                 id: Optional[str], resource_types: Optional[List[str]]) -> Dict:
        """Create a cross-project resolver payload.
    
        :param projects: List of target projects, given with format ``organization/project``.
        :param identities: List of identities the creator of the resolver has and
            which have the permission ``resources/read`` on the target projects.
        :param priority: Resolution priority.
        :param id: ID of the resolver, given as an IRI which is not URL encoded.
        :param resource_types: List of types of the resources to resolve,
            given as IRIs.
        :return: Payload of the cross-project resolver.
        """
        payload = {
            "@type": "CrossProject",
            "projects": projects,
            "identities": identities,
            "priority": priority,
        }
        if id is not None:
            payload["@id"] = id
        if resource_types is not None:
            payload["resourceTypes"] = resource_types
        return payload

    def _check(self, rev: Optional[int], tag: Optional[str]) -> None:
        """Check that ``rev`` and ``tag`` are not both specified.
    
        :param rev: Revision number of the resolver.
        :param tag: Tag of the resolver.
        :return: None. Raise an exception if ``rev`` and ``tag`` are both specified.
        """
        if rev is not None and tag is not None:
            raise Exception("'rev' and 'tag' cannot be specified together.")

    def _params(self, pagination_from: Optional[int], pagination_size: Optional[int],
                deprecated: Optional[bool], type: Optional[str], created_by: Optional[str],
                updated_by: Optional[str], rev: Optional[int]):
        """Create a dictionary of the parameters configuring listings.
    
        Some parameter names are using Python reserved ones. They cannot therefore
        be directly passed to ``requests`` as ``kwargs``.
    
        :param pagination_from: Pagination index to start from.
        :param pagination_size: Number of results to return per page.
        :param deprecated: Deprecation status of the resolvers to keep.
        :param type: Type of the resolvers to keep, given as an IRI.
        :param created_by: Identity ID of the creator of the resolvers
            to keep, given as an IRI.
        :param updated_by: Identity ID of the last identity which has
            updated the resolvers to keep, given as en IRI.
        :param rev: Revision number of the resolvers to keep.
        :return: Dictionary of the parameters configuring listings.
         """
        return {
            "from": pagination_from,
            "size": pagination_size,
            "deprecated": deprecated,
            "type": type,
            "createdBy": created_by,
            "updatedBy": updated_by,
            "rev": rev,
        }
