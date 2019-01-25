Documentation of Nexus Python SDK
# Table of content
- [acls](#acls)
	- [acls: append](#acls-append)
	- [acls: delete](#acls-delete)
	- [acls: fetch](#acls-fetch)
	- [acls: list](#acls-list)
	- [acls: replace](#acls-replace)
	- [acls: subtract](#acls-subtract)
- [config](#config)
	- [config: remove_token](#config-remove_token)
	- [config: set_environment](#config-set_environment)
	- [config: set_token](#config-set_token)
- [files](#files)
	- [files: create](#files-create)
	- [files: deprecate](#files-deprecate)
	- [files: fetch](#files-fetch)
	- [files: list](#files-list)
	- [files: tag](#files-tag)
	- [files: tags](#files-tags)
	- [files: update](#files-update)
- [identities](#identities)
	- [identities: fetch](#identities-fetch)
- [organizations](#organizations)
	- [organizations: create](#organizations-create)
	- [organizations: deprecate](#organizations-deprecate)
	- [organizations: fetch](#organizations-fetch)
	- [organizations: list](#organizations-list)
	- [organizations: update](#organizations-update)
- [permissions](#permissions)
	- [permissions: append](#permissions-append)
	- [permissions: delete](#permissions-delete)
	- [permissions: fetch](#permissions-fetch)
	- [permissions: replace](#permissions-replace)
	- [permissions: subtract](#permissions-subtract)
- [projects](#projects)
	- [projects: create](#projects-create)
	- [projects: deprecate](#projects-deprecate)
	- [projects: fetch](#projects-fetch)
	- [projects: list](#projects-list)
	- [projects: update](#projects-update)
- [realms](#realms)
	- [realms: create](#realms-create)
	- [realms: deprecate](#realms-deprecate)
	- [realms: fetch](#realms-fetch)
	- [realms: list](#realms-list)
	- [realms: replace](#realms-replace)
- [resources](#resources)
	- [resources: create](#resources-create)
	- [resources: deprecate](#resources-deprecate)
	- [resources: fetch](#resources-fetch)
	- [resources: list](#resources-list)
	- [resources: tag](#resources-tag)
	- [resources: tags](#resources-tags)
	- [resources: update](#resources-update)
- [schemas](#schemas)
	- [schemas: create](#schemas-create)
	- [schemas: deprecate](#schemas-deprecate)
	- [schemas: fetch](#schemas-fetch)
	- [schemas: list](#schemas-list)
	- [schemas: tag](#schemas-tag)
	- [schemas: update](#schemas-update)
- [tools](#tools)
	- [tools: pretty_print](#tools-pretty_print)
- [views](#views)
	- [views: aggregate_es](#views-aggregate_es)
	- [views: create_es](#views-create_es)
	- [views: deprecate_es](#views-deprecate_es)
	- [views: fetch](#views-fetch)
	- [views: list](#views-list)
	- [views: list_keep_only_es](#views-list_keep_only_es)
	- [views: list_keep_only_sparql](#views-list_keep_only_sparql)
	- [views: query_es](#views-query_es)
	- [views: query_sparql](#views-query_sparql)
	- [views: tag_es](#views-tag_es)
	- [views: update_es](#views-update_es)


# acls
This module provides a Python interface for operations on Access Control Lists.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-acls-api.html
## acls: append
Append ACLs on a subpath. ``permissions`` and ``identities`` have the same order.

- *argument* **subpath**: Subpath on which appending ACLs.
- *argument* **permissions**: List of list of permissions.
- *argument* **identities**: List of identities for which to append the permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## acls: delete
Delete ACLs on a subpath.

- *argument* **subpath**: Subpath on which deleting ACLs.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## acls: fetch
Fetch the ACLs on a subpath.

- *argument* **subpath**: Subpath on which fetching the ACLs.
- *argument* **rev**: (optional) Revision number of the ACLs.
- *argument* **self**: (optional) If 'True', only the ACLs containing the identities
found in the authentication token are returned. If 'False', all the
ACLs on the current subpath are returned.
- *returned*: A Nexus results list with the Nexus payloads of the ACLs.


## acls: list
List ACLs on a subpath.

- *argument* **subpath**: Subpath on which listing the ACLs.
- *argument* **ancestors**: (optional) If 'True', the ACLs on the parent path of the
subpath are returned. If 'False', only the ACLs on the current subpath
are returned.
- *argument* **self**: (optional) If 'True', only the ACLs containing the identities
found in the authentication token are returned. If 'False', all the
ACLs on the current subpath are returned.
- *returned*: A Nexus results list with the Nexus payloads of the ACLs.


## acls: replace
Replace ACLs on a subpath. ``permissions`` and ``identities`` have the same order.

- *argument* **subpath**: Subpath on which replacing the ACLs.
- *argument* **permissions**: List of list of permissions.
- *argument* **identities**: List of identities for which to replace permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## acls: subtract
Subtract ACLs on a subpath. ``permissions`` and ``identities`` have the same order.

- *argument* **subpath**: Subpath on which subtracting ACLs.
- *argument* **permissions**: List of list of permissions.
- *argument* **identities**: List of identities for which to remove the permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


# config
The config provides an easy way to handle the Nexus environment and token.
## config: remove_token
Remove the token. Then Nexus will no longer be able to perform any operations.


## config: set_environment
Define the base URL of the Nexus environment. This URL should be of the form `https://my-nexus-env.com/v1`
Note that it should not finish with a slash.
- *argument* **env**: The base URL for the environment


## config: set_token
Set the token for the Nexus environment.

- *argument* **token**: The token is a string given by Nexus or a connected service.


# files
Files are a particular kind of resource that contain binary data. In addition, like any other resource, they are bound
to a project (and thus, an organization) and can be described with their metadata.
## files: create
This is the POST method, when the user does not provide a file ID.

- *argument* **org_label**: The label of the organization that the file belongs to
- *argument* **project_label**: The label of the project that the file belongs to
- *argument* **filepath**: path of the file to upload
- *argument* **file_id**: OPTIONAL Will use this id to identify the file if provided. If not provided, an ID will be generated
- *returned*: A payload containing only the Nexus metadata for this updated file.


## files: deprecate
Flag a file as deprecated. files cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **file**: payload of a previously fetched file
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated file.


## files: fetch
Fetches a distant file and returns the metadata of this file. In addition, if the argument `out_filepath` can
be of three forms:
- out_filepath=None (default): the binary is not fetched
- out_filepath="./some/folder/" the binary is fetched and written in this dir with it's original filename
- out_filepath="./somefile.jpg" the binary is fetched and written under this exact filename

In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the file belongs to
- *argument* **project_label**: The label of the project that the file belongs to
- *argument* **file_id**: id of the file
- *argument* **rev**: OPTIONAL fetches a specific revision of a file (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the file version that has a specific tag (default: None)
- *argument* **out_filepath**: OPTIONAL the filename to write (default: None)
- *returned*: Payload of the whole file as a dictionary


## files: list
List the files available for a given organization and project.

- *argument* **org_label**: The label of the organization that the file belongs to
- *argument* **project_label**: The label of the project that the file belongs to
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated file if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated file.
- *argument* **type**: OPTIONAL Lists only the file for a given type (default: None)
- *argument* **rev**: OPTIONAL List only the resource with this particular revision
- *argument* **schema**: OPTIONAL list only the views with a certain schema
- *argument* **created_by**: OPTIONAL List only the file created by a certain user
- *argument* **updated_by**: OPTIONAL List only the file that were updated by a certain user
- *argument* **file_id**: OPTIONAL List only the file with this id. Relevant only when combined with other args
- *returned*: The raw list payload as a dictionary


## files: tag
Add a tag to a a specific revision of the file. Note that a new revision (untagged) will be created

- *argument* **file**: payload of a previously fetched file
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided file payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this file.


## files: tags
List all the tags added to this file, along with their version numbers

- *argument* **file**: payload of a previously fetched file
- *returned*: payload containing the list of tags and versions


## files: update
Update a file. The file object is most likely the returned value of a
nexus.file.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete file.

- *argument* **file**: payload of a previously fetched file, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated file.


# identities
This module provides a Python interface for operations on Identities.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
## identities: fetch
Fetch the identities.

- *returned*: A list with the Nexus payloads of the identities.


# organizations
Organizations can represent a lab, a company or even a team of collaborators. They are used to store projects.
## organizations: create
Create a new organization.

- *argument* **org_label**: The label of the organization. Does not allow spaces or special characters
- *argument* **description**: OPTIONAL The description of the organization
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## organizations: deprecate
Deprecate an organization. Nexus does not allow deleting organizations so deprecating is the way to flag them as
not usable anymore.
A deprecated organization can not be modified/updated.

- *argument* **org_label**: The label of the organization to deprecate
- *argument* **rev**: The previous revision number. To be provided to make sure the user is well aware of the details
of the last revision of this organisation.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## organizations: fetch
Fetch an organization.

- *argument* **org_label**: The label of the organization
- *argument* **rev**: OPTIONAL The specific revision of the wanted organization. If not provided, will get the last
- *returned*: All the details of this organization, as a dictionary


## organizations: list
NOT WORKING
List all the organizations.

- *argument* **pagination_from**: OPTIONAL Index of the list to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL Size of the list (default: 20)
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## organizations: update
Update an organization. Only the field "name" can be updated (and "description" in the future).

- *argument* **org**: Organization payload as a dictionary. This is most likely the returned value of `organisation.get(...)`
- *argument* **rev**: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
this organization. If not provided, the `_rev` number from the `org` argument will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


# permissions
This module provides a Python interface for operations on Permissions.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-permissions-api.html
## permissions: append
Append user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## permissions: delete
Delete user-defined permissions.

- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## permissions: fetch
Fetch the permissions.

- *argument* **rev**: (optional) Revision number of the permissions.
- *returned*: A Nexus payload with the permissions.


## permissions: replace
Replace the user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## permissions: subtract
Subtract user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


# projects
A project is a place to store data (files, resources, schemas, etc.). It belongs to an organization.
## projects: create
Create a new project under an organization.

- *argument* **org_label**: The label of the organization to create the project in
- *argument* **project_label**: The label of the project to add
- *argument* **description**: OPTIONAL a description for this project
- *argument* **api_mappings**: OPTIONAL apiMappings
see https://bluebrain.github.io/nexus/docs/api/admin/admin-projects-api.html#api-mappings
- *argument* **vocab**: OPTIONAL vocab as a string
- *argument* **base**: OPTIONAL base for the project
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


## projects: deprecate
Deprecate a project. Nexus does not allow deleting projects so deprecating is the way to flag them as
not usable anymore.
A deprecated project cannot be modified/updated.

- *argument* **project**: The project payload, most likely retrieved with fetch()
- *argument* **rev**: OPTIONAL provide the last version of the project to make sure the user has full knowledge of
the version being deprecated. If not provided, the revision number from the project payload will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


## projects: fetch
Fetch a project and all its details.
Note: This does not give the list of resources. To get that, use the `resource` package.

- *argument* **org_label**: The label of the organization that contains the project to be fetched
- *argument* **project_label**: label of a the project to fetch
- *argument* **rev**: OPTIONAL The specific revision of the wanted project. If not provided, will get the last.
- *returned*: All the details of this project, as a dictionary


## projects: list
List all the projects. If the arguments org_label is provided, this will list only the projects of this given
organization. If not provided, all the projects from all organizations will be listed.

- *argument* **org_label**: OPTIONAL get only the list of project for this given organization
- *argument* **pagination_from**: OPTIONAL Index of the list to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL Size of the list (default: 20)
- *argument* **deprecated**: OPTIONAL Lists only the deprecated if True,
lists only the non-deprecated if False,
lists everything if not provided or None (default: None)
- *argument* **full_text_search_query**: OPTIONAL List only the projects that match this query
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata and the list of projects


## projects: update
Update a project. The data to update on a project are mostly related to the api mapping. To do so, you must
get the project information as a payload, most likely using `project.fetch(...)`, then, modify this payload
according to the update to perform, and finally, use this modified payload as the `project` argument of this method.

- *argument* **project**: Project payload as a dictionary. This is most likely the returned value of `project.fetch(...)`
- *argument* **rev**: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
this project. If not provided, the `_rev` number from the `project` argument will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


# realms
This module provides a Python interface for operations on Realms.
It is part of the Identity & Access Management API of Blue Brain Nexus v1.
https://bluebrain.github.io/nexus/docs/api/iam/iam-realms-api.html
## realms: create
Create a realm.

- *argument* **subpath**: Subpath of the realm.
- *argument* **name**: Name of the realm.
- *argument* **openid_config**: URL of the OpenID configuration.
- *argument* **logo**: (optional) URL of a logo.
- *returned*: The Nexus metadata of the created realm.


## realms: deprecate
Deprecate a realm.

- *argument* **subpath**: Subpath of the realm.
- *argument* **rev**: Last revision of the realm.
- *returned*: The Nexus metadata of the deprecated realm.


## realms: fetch
Fetch a realm.

- *argument* **subpath**: Subpath of the realm.
- *argument* **rev**: (optional) Revision number of the realm.
- *returned*: The Nexus payload of the fetched realm.


## realms: list
List realms.

- *returned*: A Nexus results list with the Nexus payloads of the realms.


## realms: replace
Replace a realm.

- *argument* **subpath**: Subpath of the realm.
- *argument* **name**: Name of the realm.
- *argument* **openid_config**: Updated URL of the OpenID configuration.
- *argument* **rev**: Last revision of the realm.
- *argument* **logo**: (optional) Updated URL of a logo.
- *returned*: The Nexus metadata of the realm.


# resources
A resource represents a set of organized data represented with JSON. Hence, a resource can handle data such as numbers,
strings, arrays, boolean and complex objects made of those primitive types. In addition, Nexus adds some metadata.
Resources belong to projects and their access rights are defined at the project level.
## resources: create
Create a resource. If resource_id is provided, this given ID will be used. If resource_id not provided,
an ID will be automatically generated for this new resource.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema_id**: OPTIONAL The schema to constrain the data. Can be None for non constrained data (default: "resource)
- *argument* **data**: dictionary containing the data to store in this new resource
- *argument* **resource_id**: OPTIONAL force the use of a specific id when creating the new resource
- *returned*: A payload containing only the Nexus metadata for this updated resource.

If the data does not have a "@context" value, a default one is automatically added.


## resources: deprecate
Flag a resource as deprecated. Resources cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **resource**: payload of a previously fetched resource
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated resource.


## resources: fetch
Fetches a distant resource and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **resource_id**: id of the resource
- *argument* **schema_id**: OPTIONAL id of the schema (default: "_" means whatever)
- *argument* **rev**: OPTIONAL fetches a specific revision of a resource (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the resource version that has a specific tag (default: None)
- *returned*: Payload of the whole resource as a dictionary


## resources: list
List the resources available for a given organization and project.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema**: OPTIONAL Lists only the resource for a given schema (default: None)
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated resource if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated resource.
- *argument* **type**: OPTIONAL Lists only the resource for a given type (default: None)
- *argument* **rev**: OPTIONAL List only the resource with this particular revision
- *argument* **created_by**: OPTIONAL List only the resources created by a certain user
- *argument* **updated_by**: OPTIONAL List only the resources that were updated by a certain user
- *argument* **resource_id**: OPTIONAL List only the resources with this id. Relevant only when combined with other args
- *returned*: The raw payload as a dictionary


## resources: tag
Add a tag to a a specific revision of the resource. Note that a new revision (untagged) will be created

- *argument* **resource**: payload of a previously fetched resource
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided resource payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this resource.


## resources: tags
List all the tags added to this resource, along with their version numbers

- *argument* **resource**: payload of a previously fetched resource
- *returned*: payload containing the list of tags and versions


## resources: update
Update a resource. The resource object is most likely the returned value of a
nexus.resource.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete resource.

- *argument* **resource**: payload of a previously fetched resource, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated resource.


# schemas
Using schemas is a way to ensure your data to follow a set of rules.
## schemas: create
Create a new schema

- *argument* **org_label**: Label of the organization in which to create the schema
- *argument* **project_label**: label of the project in which to create a schema
- *argument* **schema_obj**: Schema, can be a dictionary or a JSON string
- *argument* **schema_id**: OPTIONAL The view will be created with this specific internal id, if provided.
Otherwise, an id will be generated by Nexus.
- *returned*: payload of the schema as a Python dictionary. This payload is partial and contains only Nexus metadata.
To get the full schema payload, use the fetch() method.


## schemas: deprecate
Flag a schema as deprecated. Schema cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **schema**: payload of a previously fetched resource
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated schema.


## schemas: fetch
Fetches a distant schema and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema_id**: id of the schema
- *argument* **rev**: OPTIONAL fetches a specific revision of a schema (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the schema version that has a specific tag (default: None)
- *returned*: Payload of the whole schema as a dictionary


## schemas: list
List all the schemas available

- *argument* **org_label**: Label of the organization to which listing the schema
- *argument* **project_label**: Label of the project to which listing the schema
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated resource if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated resource.
- *argument* **full_text_search_query**: A string to look for as a full text query
- *returned*: The raw payload as a dictionary
- *returned*: List of schema and some Nexus metadata


## schemas: tag
Add a tag to a a specific revision of the schema. Note that a new revision (untagged) will be created

- *argument* **schema**: payload of a previously fetched schema
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided schema payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this schema.


## schemas: update
Update a schema. The schema object is most likely the returned value of a
nexus.schema.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete resource.

- *argument* **schema**: payload of a previously fetched resource, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated schema.


# tools
(no documentation provided)
## tools: pretty_print
This helper function display a Python dict in a nice way, using the JSON syntax and an indentation of 2.
- *argument* **payload**: A Python dict


# views
A view is a way to access Nexus data and to perform queries. A view belongs to a specific project.
By default, an ElasticSearch view and a SparQL view are provided.
More ElasticSearch views can be created manually, hence providing a custom indexing and custom research capabilities.
## views: aggregate_es
Creates an aggregated view for ElasticSearch.

- *argument* **org_label**: Label of the organization the view wil belong to
- *argument* **project_label**: label of the project the view will belong too
- *argument* **esviews**: list of ElasticSearch view payloads, most likely got with .fetch()
- *argument* **id**: id to give to this aggregation id ElasticSearch views
- *returned*: A payload containing only the Nexus metadata for this aggregated view.


## views: create_es
Creates an ElasticSearch view

- *argument* **org_label**: Label of the organization the view wil belong to
- *argument* **project_label**: label of the project the view will belong too
- *argument* **view_data**: Mapping data required for ElasticSearch indexing
- *argument* **view_id**: OPTIONAL if provided, the view will be created with the given id.
Otherwise, an autogenerated one will be given by Nexus
- *returned*: The payload representing the view. This payload only contains the Nexus metadata


## views: deprecate_es
Update a ElasticSearch view. The esview object is most likely the returned value of a
nexus.views.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete view.

- *argument* **esview**: payload of a previously fetched view, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the view argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated view.


## views: fetch
Fetches a distant view and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the view belongs to
- *argument* **project_label**: The label of the project that the view belongs to
- *argument* **view_id**: id of the view
- *argument* **rev**: OPTIONAL fetches a specific revision of a view (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the view version that has a specific tag (default: None)
- *returned*: Payload of the whole view as a dictionary


## views: list
List the views available for a given organization and project. All views, of all kinds.

- *argument* **org_label**: The label of the organization that the view belongs to
- *argument* **project_label**: The label of the project that the view belongs to
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated view if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated view.
- *argument* **type**: OPTIONAL The view type
- *argument* **rev**: OPTIONAL Revision to list
- *argument* **schema**: OPTIONAL list only the views with a certain schema
- *argument* **created_by**: OPTIONAL List only the views created by a certain user
- *argument* **updated_by**: OPTIONAL List only the views that were updated by a certain user
- *argument* **view_id**: OPTIONAL List only the view with this id. Relevant only when combined with other args
- *returned*: The raw payload as a dictionary


## views: list_keep_only_es
Helper function to keep only the ElasticSearch views metadata from the result of a .list() call
- *argument* **viewlist**: the payload returned by .list()
- *returned*: the list of ElasticSearch view metadata (beware: not complete payloads like if it was the result of .fetch() calls)


## views: list_keep_only_sparql
Helper function to keep only the SparQL views metadata from the result of a .list() call
- *argument* **viewlist**: the payload returned by .list()
- *returned*: the list of SparQL view metadata (beware: not complete payloads like if it was the result of .fetch() calls)


## views: query_es
Perform a ElasticSearch query

- *argument* **org_label**: Label of the organization to perform the query on
- *argument* **project_label**: Label of the project to perform the query on
- *argument* **view_id**: id of an ElasticSearch view
- *argument* **query**: ElasticSearch query as a JSON string or a dictionary
- *returned*: the result of the query as a dictionary


## views: query_sparql
Perform a SparQL query.

- *argument* **org_label**: Label of the organization to perform the query on
- *argument* **project_label**: Label of the project to perform the query on
- *argument* **query**: Query as a string
- *returned*: result of the query as a dictionary


## views: tag_es
Add a tag to a a specific revision of an ElasticSearch view. Note that a new revision (untagged) will be created

- *argument* **esview**: payload of a previously fetched view (ElasticSearch)
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided resource payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this view.


## views: update_es
Update a ElasticSearch view. The esview object is most likely the returned value of a
nexus.views.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete view.

- *argument* **esview**: payload of a previously fetched view, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the view argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated view.



