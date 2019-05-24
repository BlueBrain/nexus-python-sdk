"""
A view is a way to access Nexus data and to perform queries. A view belongs to a specific project.
By default, an ElasticSearch view and a SPARQL view are provided.
More ElasticSearch and SPARQL views can be created manually, hence providing a custom indexing and custom research capabilities.
For more details see `Nexus KG views documentation <https://bluebrainnexus.io/docs/api/kg/kg-views-api.html>`_.
"""

import json
from typing import Dict, List, Optional, Set, Union

from nexussdk.utils.http import http_get
from nexussdk.utils.http import http_put
from nexussdk.utils.http import http_post
from nexussdk.utils.http import http_delete
from urllib.parse import quote_plus as url_encode

ELASTIC_TYPE = "ElasticSearchView"
SPARQL_TYPE = "SparqlView"


def create_(org_label: str, project_label: str, payload: Dict, view_id: Optional[str]):
    """Create a view from a given payload.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param payload: JSON payload oft he view
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :return: The Nexus metadata of the created view.
    """
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/views/" + org_label + "/" + project_label
    if view_id is not None:
        payload["@id"] = view_id

    return http_post(path, body=payload, use_base=True)


def create_es(org_label: str, project_label: str, mapping: Dict, view_id: Optional[str] = None,
              resource_schemas: Optional[Set[str]] = None,
              resource_types: Optional[Set[str]] = None,
              tag: Optional[str] = None,
              source_as_text: Optional[bool] = None,
              include_metadata: bool = False,
              include_deprecated: bool = False
              ) -> Dict:
    """ Create an ElasticSearch view.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param mapping: ElasticSearch mapping
        (see https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html for more details).
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :param resource_schemas: (optional) IDs of the schemas which will be used to filter the resources
        indexed in the view.
    :param resource_types: (optional) IDs of the types which will be used to filter the resources
        indexed in the view.
    :param tag: (optional) tag to use for filtering the resources which will be indexed in the view.
    :param source_as_text: (optional) whether to include original JSON source of the resources in the view. If True,
        the resource’s payload will be stored in the ElasticSearch document
        as a single escaped string value of the key _original_source.
    :param include_metadata: whether to include Nexus metadata in the index
    :param include_deprecated: whether to include deprecated resources in the index
    :return: The Nexus metadata of the created view.
    """
    payload = {
        "@type": ["View", ELASTIC_TYPE],
        "mapping": mapping,
        "includeMetadata": include_metadata,
        "includeDeprecated": include_deprecated
    }

    if resource_schemas:
        payload["resourceSchemas"] = resource_schemas
    if resource_types:
        payload["resourceTypes"] = resource_types
    if tag is not None:
        payload["resourceTag"] = tag
    if source_as_text is not None:
        payload["sourceAsText"] = source_as_text
    return create_(org_label, project_label, payload, view_id)


def update_es(esview, rev=None):
    """
    Update a ElasticSearch view. The esview object is most likely the returned value of a
    nexus.views.fetch(), where some fields where modified, added or removed.
    Note that the returned payload only contains the Nexus metadata and not the
    complete view.

    :param esview: payload of a previously fetched view, with the modification to be updated
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the view argument will be used.
    :return: A payload containing only the Nexus metadata for this updated view.
    """

    if rev is None:
        rev = esview["_rev"]

    path = esview["_self"] + "?rev=" + str(rev)

    return http_put(path, esview, use_base=False)


def deprecate_es(esview, rev=None):
    """
    Update a ElasticSearch view. The esview object is most likely the returned value of a
    nexus.views.fetch(), where some fields where modified, added or removed.
    Note that the returned payload only contains the Nexus metadata and not the
    complete view.

    :param esview: payload of a previously fetched view, with the modification to be updated
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the view argument will be used.
    :return: A payload containing only the Nexus metadata for this updated view.
    """

    if rev is None:
        rev = esview["_rev"]

    path = esview["_self"] + "?rev=" + str(rev)

    return http_delete(path, esview, use_base=False)


def fetch(org_label, project_label, view_id, rev=None, tag=None):
    """
    Fetches a distant view and returns the payload as a dictionary.
    In case of error, an exception is thrown.

    :param org_label: The label of the organization that the view belongs to
    :param project_label: The label of the project that the view belongs to
    :param view_id: id of the view
    :param rev: OPTIONAL fetches a specific revision of a view (default: None, fetches the last)
    :param tag: OPTIONAL fetches the view version that has a specific tag (default: None)
    :return: Payload of the whole view as a dictionary
    """

    if rev is not None and tag is not None:
        raise Exception("The arguments rev and tag are mutually exclusive. One or the other must be chosen.")

    # the element composing the query URL need to be URL-encoded
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    view_id = url_encode(view_id)

    path = "/views/" + org_label + "/" + project_label + "/" + view_id

    if rev is not None:
        path = path + "?rev=" + str(rev)

    if tag is not None:
        path = path + "?tag=" + str(tag)

    return http_get(path, use_base=True)


def list(org_label, project_label, pagination_from=0, pagination_size=20,
         deprecated=None, type=None, rev=None, schema=None, created_by=None, updated_by=None, view_id=None):
    """
    List the views available for a given organization and project. All views, of all kinds.

    :param org_label: The label of the organization that the view belongs to
    :param project_label: The label of the project that the view belongs to
    :param pagination_from: OPTIONAL The pagination index to start from (default: 0)
    :param pagination_size: OPTIONAL The maximum number of elements to returns at once (default: 20)
    :param deprecated: OPTIONAL Get only deprecated view if True and get only non-deprecated results if False.
        If not specified (default), return both deprecated and not deprecated view.
    :param type: OPTIONAL The view type
    :param rev: OPTIONAL Revision to list
    :param schema: OPTIONAL list only the views with a certain schema
    :param created_by: OPTIONAL List only the views created by a certain user
    :param updated_by: OPTIONAL List only the views that were updated by a certain user
    :param view_id: OPTIONAL List only the view with this id. Relevant only when combined with other args
    :return: The raw payload as a dictionary
    """
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/views/" + org_label + "/" + project_label

    params = {
        "from": pagination_from,
        "size": pagination_size,
        "type": type,
        "deprecated": deprecated,
        "rev": rev,
        "schema": schema,
        "created_by": created_by,
        "updated_by": updated_by,
        "id": view_id
    }

    return http_get(path, use_base=True, params=params)


def tag_es(esview, tag_value, rev_to_tag=None, rev=None):
    """
    Add a tag to a a specific revision of an ElasticSearch view. Note that a new revision (untagged) will be created.

    :param esview: payload of a previously fetched view (ElasticSearch)
    :param tag_value: The value (or name) of a tag
    :param rev_to_tag: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
        from the provided resource payload.
    :param rev: OPTIONAL The previous revision you want to update from.
        If not provided, the rev from the resource argument will be used.
    :return: A payload containing only the Nexus metadata for this view.
    """

    if rev is None:
        rev = esview["_rev"]

    if rev_to_tag is None:
        rev_to_tag = esview["_rev"]

    path = esview["_self"] + "/tags?rev=" + str(rev)

    data = {
        "tag": tag_value,
        "rev": rev_to_tag
    }

    return http_put(path, body=data, use_base=False)


def create_es_aggregated(org_label: str, project_label: str, es_views: List[Dict], view_id: Optional[str]) -> Dict:
    """Create an aggregated ElasticSearch view.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param es_views: The views which will be included in the aggregate view.
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :return: The Nexus metadata of the created view.
    """
    views_data = []
    for v in es_views:
        v_data = {
            "project": "/".join(v["_project"].split("/")[-2:]),
            "viewId": v["@id"]
        }

        views_data.append(v_data)

    payload = {
        "@type": [
            "View",
            "AggregateElasticSearchView"
        ],
        "views": views_data
    }

    return create_(org_label, project_label, payload, view_id)


def list_keep_only_es(viewlist):
    """
    Helper function to keep only the ElasticSearch views metadata from the result of a .list() call.

    :param viewlist: the payload returned by .list()
    :return: the list of ElasticSearch view metadata (beware: not complete payloads like if it was the result of .fetch() calls)
    """
    return _filter_list_by_type(viewlist, ELASTIC_TYPE)


def list_keep_only_sparql(viewlist):
    """
    Helper function to keep only the SparQL views metadata from the result of a .list() call.

    :param viewlist: the payload returned by .list()
    :return: the list of SparQL view metadata (beware: not complete payloads like if it was the result of .fetch() calls)
    """
    return _filter_list_by_type(viewlist, SPARQL_TYPE)


def _filter_list_by_type(list, type):
    new_list = []

    for el in list["_results"]:
        if type in el["@type"]:
            new_list.append(el)

    return new_list


def query_es(org_label: str, project_label: str, query: Union[str, Dict],
             view_id: str = "nxv:defaultElasticSearchIndex") -> Dict:
    """
    Perform a ElasticSearch query.

    :param org_label: Label of the organization to perform the query on
    :param project_label: Label of the project to perform the query on
    :param view_id: id of an ElasticSearch view
    :param query: ElasticSearch query as a JSON string or a dictionary
    :return: the result of the query as a dictionary
    """
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)
    view_id = url_encode(view_id)

    path = "/views/" + org_label + "/" + project_label + "/" + view_id + "/_search"

    if (not isinstance(query, dict)) and isinstance(query, str):
        query = json.loads(query)

    return http_post(path, body=query, use_base=True)


def create_sparql(org_label: str, project_label: str, view_id: Optional[str] = None,
                  resource_schemas: Optional[Set[str]] = None,
                  resource_types: Optional[Set[str]] = None,
                  tag: Optional[str] = None,
                  include_metadata=False,
                  include_deprecated=False
                  ) -> Dict:
    """Create a Sparql view.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :param resource_schemas: (optional) IDs of the schemas which will be used to filter the resources
        indexed in the view.
    :param resource_types: (optional) IDs of the types which will be used to filter the resources
        indexed in the view.
    :param tag: (optional) tag to use for filtering the resources which will be indexed in the view.
    :param include_metadata: whether to include Nexus metadata in the index
    :param include_deprecated: whether to include deprecated resources in the index
    :return: The Nexus metadata of the created view.
    """
    payload = {
        "@type": ["View", SPARQL_TYPE],
        "includeMetadata": include_metadata,
        "includeDeprecated": include_deprecated
    }
    if view_id is not None:
        payload["@id"] = view_id
    if resource_schemas:
        payload["resourceSchemas"] = resource_schemas
    if resource_types:
        payload["resourceTypes"] = resource_types
    if tag is not None:
        payload["resourceTag"] = tag

    return create_(org_label, project_label, payload, view_id)


def create_sparql_aggregated(org_label: str, project_label: str, sparql_views: [Set[Dict]],
                             view_id: Optional[str]) -> Dict:
    """Create aggregated Sparql view.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :param sparql_views: The views which will be included in the aggregate view.
    :param view_id: (optional) User-defined ID of the view, given as an IRI
        which is not URL encoded.
    :return: The Nexus metadata of the created view.
    """
    views_data = []

    for v in sparql_views:
        v_data = {
            "project": "/".join(v["_project"].split("/")[-2:]),
            "viewId": v["@id"]
        }

        views_data.append(v_data)

    payload = {
        "@type": [
            "View",
            "AggregateSparqlView"
        ],
        "views": views_data
    }
    return create_(org_label, project_label, payload, view_id)


def query_sparql(org_label: str, project_label: str, query: str, view_id: str = "nxv:defaultSparqlIndex") -> Dict:
    """
    Perform a SparQL query.

    :param org_label: Label of the organization to perform the query on
    :param project_label: Label of the project to perform the query on
    :param query: Sparql query
    :param view_id: id of a Sparql view
    :return: result of the query as a dictionary
    """
    org_label = url_encode(org_label)
    project_label = url_encode(project_label)

    path = "/views/" + org_label + "/" + project_label + "/" + url_encode(view_id) + "/sparql"

    return http_post(path, body=query, data_type="sparql", use_base=True)


def stats(org_label: str, project_label: str, view_id: str) -> Dict:
    """
    Fetch indexing statistics for a view.

    :param org_label: Label of the organization the view belongs to.
    :param project_label: Label of the project the view belongs to.
    :param view_id: ID of the view.
    :return: the view's indexing statistics.
    """
    return http_get(["views", org_label, project_label, url_encode(view_id), "statistics"])
