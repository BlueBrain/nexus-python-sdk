"""
A project is a place to store data (files, resources, schemas, etc.). It belongs to an organization.
"""

from typing import Optional
from urllib.parse import quote_plus as url_encode

from nexussdk.utils.http import Http


class Projects:
    def __init__(self, http: Http):
        self._http = http

    def fetch(self, org_label, project_label, rev=None):
        """
        Fetch a project and all its details.
        Note: This does not give the list of resources. To get that, use the `resource` package.
    
        :param org_label: The label of the organization that contains the project to be fetched
        :param project_label: label of a the project to fetch
        :param rev: OPTIONAL The specific revision of the wanted project. If not provided, will get the last.
        :return: All the details of this project, as a dictionary
        """

        org_label = url_encode(org_label)
        project_label = url_encode(project_label)
        path = "/projects/" + org_label + "/" + project_label

        if rev is not None:
            path = path + "?rev=" + str(rev)

        return self._http.get(path, use_base=True)

    def create(self, org_label, project_label, description=None, api_mappings=None, vocab=None, base=None):
        """
        Create a new project under an organization.
    
        :param org_label: The label of the organization to create the project in
        :param project_label: The label of the project to add
        :param description: OPTIONAL a description for this project
        :param api_mappings: OPTIONAL apiMappings
            see https://bluebrain.github.io/nexus/docs/api/admin/admin-projects-api.html#api-mappings
        :param vocab: OPTIONAL vocab as a string
        :param base: OPTIONAL base for the project
        :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project
        """

        org_label = url_encode(org_label)
        project_label = url_encode(project_label)
        path = "/projects/" + org_label + "/" + project_label

        config = {}

        if description is not None:
            config["description"] = description

        if api_mappings is not None:
            config["apiMappings"] = api_mappings

        if vocab is not None:
            config["vocab"] = vocab

        if base is not None:
            config["base"] = base

        return self._http.put(path, use_base=True, body=config)

    def update(self, project, rev=None):
        """
        Update a project. The data to update on a project are mostly related to the api mapping. To do so, you must
        get the project information as a payload, most likely using `project.fetch(...)`, then, modify this payload
        according to the update to perform, and finally, use this modified payload as the `project` argument of this method.
    
        :param project: Project payload as a dictionary. This is most likely the returned value of `project.fetch(...)`
        :param rev: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
            this project. If not provided, the `_rev` number from the `project` argument will be used.
        :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project
        """

        if rev is None:
            rev = project["_rev"]

        org_label = url_encode(project["_organizationLabel"])
        project_label = url_encode(project["_label"])

        path = "/projects/" + org_label + "/" + project_label + "?rev=" + str(rev)

        return self._http.put(path, project, use_base=True)

    def list(self, org_label=None, pagination_from=0, pagination_size=20, deprecated=None, full_text_search_query=None):
        """
        List all the projects. If the arguments org_label is provided, this will list only the projects of this given
        organization. If not provided, all the projects from all organizations will be listed.
    
        :param org_label: OPTIONAL get only the list of project for this given organization
        :param pagination_from: OPTIONAL Index of the list to start from (default: 0)
        :param pagination_size: OPTIONAL Size of the list (default: 20)
        :param deprecated: OPTIONAL Lists only the deprecated if True,
            lists only the non-deprecated if False,
            lists everything if not provided or None (default: None)
        :param full_text_search_query: OPTIONAL List only the projects that match this query
        :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata and the list of projects
        """

        path = "/projects"

        if org_label is not None:
            org_label = url_encode(org_label)
            path = path + "/" + org_label

        path = path + "?from=" + str(pagination_from) + "&size=" + str(pagination_size)

        if deprecated is not None:
            deprecated = "true" if deprecated else "false"
            path = path + "&deprecated=" + deprecated

        if full_text_search_query is not None:
            full_text_search_query = url_encode(full_text_search_query)
            path = path + "&q=" + full_text_search_query

        return self._http.get(path, use_base=True)

    def deprecate_2(self, org_label, project_label, rev):
        """
        Deprecate a project. Nexus does not allow deleting projects so deprecating is the way to flag them as
        not usable anymore.
        A deprecated project cannot be modified/updated.
    
        :param org_label: The label of the organization the project to deprecate belongs to
        :param project_label: The label of the project to deprecate
        :param rev: The previous revision number. Provided to make sure the user is well aware of the details
            of the last revision of this project.
        :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project
        """

        org_label = url_encode(org_label)
        project_label = url_encode(project_label)

        path = "/projects/" + org_label + "/" + project_label + "?rev=" + str(rev)

        return self._http.delete(path, use_base=True)

    def deprecate(self, project, rev=None):
        """
        Deprecate a project. Nexus does not allow deleting projects so deprecating is the way to flag them as
        not usable anymore.
        A deprecated project cannot be modified/updated.
    
        :param project: The project payload, most likely retrieved with fetch()
        :param rev: OPTIONAL provide the last version of the project to make sure the user has full knowledge of
            the version being deprecated. If not provided, the revision number from the project payload will be used.
        :return: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project
        """

        org_label = url_encode(project["_organizationLabel"])
        project_label = url_encode(project["_label"])

        if rev is None:
            rev = project["_rev"]

        path = "/projects/" + org_label + "/" + project_label + "?rev=" + str(rev)

        return self._http.delete(path, use_base=True)

    def events(self, last_id: Optional[str] = None):
        """
        Fetches project related events.
    
        :param last_id: ID of the last processed event, if provided, only events after
                the event with the provided ID will be returned.
        :return: iterator of project events
        """
        return self._http.sse_request("/projects/events", last_id)
