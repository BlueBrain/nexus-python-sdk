"""
This module provides a Python interface for operations on Resolvers.
It is part of the Knowledge Graph API of Blue Brain Nexus v1.
https://bluebrainnexus.io/docs/api/kg/kg-resolvers-api.html
"""

from typing import Dict, List, Optional
from urllib.parse import quote_plus as encode_url

from nexussdk.utils.http import (http_delete, http_get, http_post, http_put)

SEGMENT = "resolvers"


# Create functions.

def create(org_label: str, project_label: str, projects: List[str], identities: List[Dict],
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
    payload = _payload(projects, identities, priority, id, resource_types)
    return http_post([SEGMENT, org_label, project_label], payload)


def create_(path: str, payload: Dict) -> Dict:
    """Create a resolver (path version).

    :param path: Full path of the project the resolver belongs to, URL encoded.
    :param payload: Payload of the resolver.
    :return: The Nexus metadata of the created resolver.
    """
    return http_post(path, payload)


# Read functions.

def fetch(org_label: str, project_label: str, id: str, tag: str = None, rev: int = None) -> Dict:
    """Fetch a resolver.

    Raise an ``Exception`` if ``rev`` and ``tag`` are used together.

    :param org_label: Label of the organization the resolver belongs to.
    :param project_label: Label of the project the resolver belongs to.
    :param id: ID of the resolver, given as an IRI which is not URL encoded.
    :param tag: (optional) Tag of the resolver.
    :param rev: (optional) Revision number of the resolver.
    :return: The Nexus payload of the fetched resolver.
    """
    _check(rev, tag)
    encoded_id = encode_url(id)
    return http_get([SEGMENT, org_label, project_label, encoded_id], rev=rev, tag=tag)


def fetch_(path: str, tag: str = None, rev: int = None) -> Dict:
    """Fetch a resolver (full path version).

    Raise an ``Exception`` if ``rev`` and ``tag`` are used together.

    :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
    :param tag: (optional) Tag of the resolver.
    :param rev: (optional) Revision number of the resolver.
    :return: The Nexus payload of the fetched resolver.
    """
    _check(rev, tag)
    return http_get(path, rev=rev, tag=tag)


def list(org_label: str, project_label: str, pagination_from: int = None,
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
    params = _params(pagination_from, pagination_size, deprecated, type, created_by, updated_by, rev)
    return http_get([SEGMENT, org_label, project_label], params=params)


def list_(path: str, pagination_from: int = None, pagination_size: int = None,
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
    params = _params(pagination_from, pagination_size, deprecated, type, created_by, updated_by, rev)
    return http_get(path, params=params)


# Update functions.

def update(org_label: str, project_label: str, id: str, projects: List[str],
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
    payload = _payload(projects, identities, priority, id, resource_types)
    return http_put([SEGMENT, org_label, project_label, encoded_id], payload, rev=rev)


def update_(path: str, payload: Dict, rev: int) -> Dict:
    """Update a resolver (full path version).

    :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
    :param payload: Payload of the resolver.
    :param rev: Last revision of the resolver.
    :return: The Nexus metadata of the updated resolver.
    """
    return http_put(path, payload, rev=rev)


def tag(org_label: str, project_label: str, id: str, tag: str, rev_to_tag: str, rev: int) -> Dict:
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
    return http_post([SEGMENT, org_label, project_label, encoded_id, "tags"], payload, rev=rev)


def tag_(path: str, payload: Dict, rev: int) -> Dict:
    """Tag a revision of a resolver (full path version).

    :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
    :param payload: Payload of the tag.
    :param rev: Last revision of the resolver.
    :return: The Nexus metadata of the tagged resolver.
    """
    p = "{}/tags".format(path)
    return http_post(p, payload, rev=rev)


# Delete functions.

def deprecate(org_label: str, project_label: str, id: str, rev: int) -> Dict:
    """Deprecate a resolver.

    :param org_label: Label of the organization the resolver belongs to.
    :param project_label: Label of the project the resolver belongs to.
    :param id: ID of the resolver, given as an IRI which is not URL encoded.
    :param rev: Last revision of the resolver.
    :return: The Nexus metadata of the deprecated resolver.
    """
    encoded_id = encode_url(id)
    return http_delete([SEGMENT, org_label, project_label, encoded_id], rev=rev)


def deprecate_(path: str, rev: int) -> Dict:
    """Deprecate a resolver (full path version).

    :param path: Full path of the resolver (i.e. includes its ID), URL encoded.
    :param rev: Last revision of the resolver.
    :return: The Nexus metadata of the deprecated resolver.
    """
    return http_delete(path, rev=rev)


# Internal helpers

def _payload(projects: List[str], identities: List[Dict], priority: int,
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


def _check(rev: Optional[int], tag: Optional[str]) -> None:
    """Check that ``rev`` and ``tag`` are not both specified.

    :param rev: Revision number of the resolver.
    :param tag: Tag of the resolver.
    :return: None. Raise an exception if ``rev`` and ``tag`` are both specified.
    """
    if rev is not None and tag is not None:
        raise Exception("'rev' and 'tag' cannot be specified together.")


def _params(pagination_from: Optional[int], pagination_size: Optional[int],
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
