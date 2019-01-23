# acls
## List
(no documentation provided)


## append
Append ACLs on a subpath.

- *argument* **subpath**: Subpath on which appending ACLs.
- *argument* **permissions**: List of permissions.
- *argument* **identity**: Payload of the identity for which to append the permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## delete
Delete ACLs on a subpath.

- *argument* **subpath**: Subpath on which deleting ACLs.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## fetch
Fetch the ACLs on a subpath.

- *argument* **subpath**: Subpath on which fetching the ACLs.
- *argument* **rev**: (optional) Revision number of the ACLs.
- *argument* **self**: (optional) If 'True', only the ACLs containing the identities
found in the authentication token are returned. If 'False', all the ACLs
on the current subpath are returned.
- *returned*: A Nexus results list with the Nexus payloads of the ACLs.


## list
List ACLs on a subpath.

- *argument* **subpath**: Subpath on which listing the ACLs.
- *argument* **ancestors**: (optional) If 'True', the ACLs on the parent path of the
subpath are returned. If 'False', only the ACLs on the current subpath are
returned.
- *argument* **self**: (optional) If 'True', only the ACLs containing the identities
found in the authentication token are returned. If 'False', all the ACLs
on the current subpath are returned.
- *returned*: A Nexus results list with the Nexus payloads of the ACLs.


## replace
Replace ACLs on a subpath.

- *argument* **subpath**: Subpath on which replacing the ACLs.
- *argument* **permissions**: List of permissions.
- *argument* **identity**: Payload of the identity for which to replace permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


## subtract
Subtract ACLs on a subpath.

- *argument* **subpath**: Subpath on which subtracting ACLs.
- *argument* **permissions**: List of permissions.
- *argument* **identity**: Payload of the identity for which to remove the permissions.
- *argument* **rev**: Last revision of the ACLs.
- *returned*: The Nexus metadata of the ACLs.


# config
## remove_token
(no documentation provided)


## set_environment
(no documentation provided)


## set_token
(no documentation provided)


# files
## create
This is the POST method, when the user does not provide a file ID.

- *argument* **org_label**: The label of the organization that the file belongs to
- *argument* **project_label**: The label of the project that the file belongs to
- *argument* **filepath**: path of the file to upload
- *argument* **file_id**: OPTIONAL Will use this id to identify the file if provided. If not provided, an ID will be generated
- *returned*: A payload containing only the Nexus metadata for this updated file.


## deprecate
Flag a file as deprecated. files cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **file**: payload of a previously fetched file
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated file.


## fetch
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


## list
List the files available for a given organization and project.

- *argument* **org_label**: The label of the organization that the file belongs to
- *argument* **project_label**: The label of the project that the file belongs to
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated file if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated file.
- *argument* **full_text_search_query**: A string to look for as a full text query
- *returned*: The raw payload as a dictionary


## tag
Add a tag to a a specific revision of the file. Note that a new revision (untagged) will be created

- *argument* **file**: payload of a previously fetched file
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided file payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this file.


## tags
List all the tags added to this file, along with their version numbers

- *argument* **file**: payload of a previously fetched file
- *returned*: payload containing the list of tags and versions


## update
Update a file. The file object is most likely the returned value of a
nexus.file.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete file.

- *argument* **file**: payload of a previously fetched file, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the file argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated file.


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


# identities
## fetch
Fetch the identities.

- *returned*: A list with the Nexus payloads of the identities.


# organizations
## create
Create a new organization.

- *argument* **org_label**: The label of the organization. Does not allow spaces or special characters
- *argument* **name**: OPTIONAL Name of the organization. If not provided, the `org_label` will be used
- *argument* **description**: NOT USED YET - OPTIONAL The description of the organization
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## deprecate
Deprecate an organization. Nexus does not allow deleting organizations so deprecating is the way to flag them as
not usable anymore.
A deprecated organization can not be modified/updated.

- *argument* **org_label**: The label of the organization to deprecate
- *argument* **rev**: The previous revision number. To be provided to make sure the user is well aware of the details
of the last revision of this organisation.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## fetch
Fetch an organization.

- *argument* **org_label**: The label of the organization
- *argument* **rev**: OPTIONAL The specific revision of the wanted organization. If not provided, will get the last
- *returned*: All the details of this organization, as a dictionary


## list
NOT WORKING
List all the organizations.

- *argument* **pagination_from**: OPTIONAL Index of the list to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL Size of the list (default: 20)
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## update
Update an organization. Only the field "name" can be updated (and "description" in the future).

- *argument* **org**: Organization payload as a dictionary. This is most likely the returned value of `organisation.get(...)`
- *argument* **rev**: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
this organization. If not provided, the `_rev` number from the `org` argument will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the organization


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


# permissions
## List
(no documentation provided)


## append
Append user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## delete
Delete user-defined permissions.

- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## fetch
Fetch the permissions.

- *argument* **rev**: (optional) Revision number of the permissions.
- *returned*: A Nexus payload with the permissions.


## replace
Replace the user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


## subtract
Subtract user-defined permissions.

- *argument* **permissions**: List of user-defined permissions.
- *argument* **rev**: Last revision of the permissions.
- *returned*: The Nexus metadata of the permissions.


# projects
## create
Create a new project under an organization.

- *argument* **org_label**: The label of the organization to create the project in
- *argument* **project_label**: The label of the project to add
- *argument* **description**: OPTIONAL a description for this project
- *argument* **api_mappings**: OPTIONAL apiMappings
see https://bluebrain.github.io/nexus/docs/api/admin/admin-projects-api.html#api-mappings
- *argument* **vocab**: OPTIONAL vocab as a string
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


## deprecate
Deprecate a project. Nexus does not allow deleting projects so deprecating is the way to flag them as
not usable anymore.
A deprecated project cannot be modified/updated.

- *argument* **project**: The project payload, most likely retrieved with fetch()
- *argument* **rev**: OPTIONAL provide the last version of the project to make sure the user has full knowledge of
the version being deprecated. If not provided, the revision number from the project payload will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


## fetch
Fetch a project and all its details.
Note: This does not give the list of resources. To get that, use the `resource` package.

- *argument* **org_label**: The label of the organization that contains the project to be fetched
- *argument* **project_label**: label of a the project to fetch
- *argument* **rev**: OPTIONAL The specific revision of the wanted project. If not provided, will get the last.
- *returned*: All the details of this project, as a dictionary


## list
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


## update
Update a project. The data to update on a project are mostly related to the api mapping. To do so, you must
get the project information as a payload, most likely using `project.fetch(...)`, then, modify this payload
according to the update to perform, and finally, use this modified payload as the `project` argument of this method.

- *argument* **project**: Project payload as a dictionary. This is most likely the returned value of `project.fetch(...)`
- *argument* **rev**: OPTIONAL The last revision number, to make sure the developer is aware of the latest status of
this project. If not provided, the `_rev` number from the `project` argument will be used.
- *returned*: The payload from the Nexus API as a dictionary. This contains the Nexus metadata of the project


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


# realms
## create
Create a realm.

- *argument* **name**: Name of the realm.
- *argument* **description**: Description of the realm.
- *argument* **openid_config**: URL of the OpenID configuration.
- *returned*: The Nexus metadata of the created realm.


## deprecate
Deprecate a realm.

- *argument* **name**: Name of the realm.
- *argument* **rev**: Last revision of the realm.
- *returned*: The Nexus metadata of the deprecated realm.


## fetch
Fetch a realm.

- *argument* **name**: Name of the realm.
- *argument* **rev**: (optional) Revision number of the realm.
- *returned*: The Nexus payload of the fetched realm.


## list
List realms.

- *returned*: A Nexus results list with the Nexus payloads of the realms.


## update
Update a realm.

- *argument* **name**: Name of the realm.
- *argument* **description**: Updated description of the realm.
- *argument* **openid_config**: Updated URL of the OpenID configuration.
- *argument* **rev**: Last revision of the realm.
- *returned*: The Nexus metadata of the updated realm.


# resources
## add_attachement
DEPRECATED

Attach a file to an existing resource. A new revision is created.

- *argument* **resource**: payload of a previously fetched resource
- *argument* **filepath**: Path of the file to upload
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this resource.


## create
Create a resource. If resource_id is provided, this given ID will be used. If resource_id not provided,
an ID will be automatically generated for this new resource.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema_id**: OPTIONAL The schema to constrain the data. Can be None for non constrained data (default: 'resource')
- *argument* **data**: dictionary containing the data to store in this new resource
- *argument* **resource_id**: OPTIONAL force the use of a specific id when creating the new resource
- *returned*: A payload containing only the Nexus metadata for this updated resource.

If the data does not have a '@context' value, a default one is automatically added.


## delete_attachment
DEPRECATED

Delete the attachment of a resource. This creates a new revision.

- *argument* **resource**: payload of a previously fetched resource
- *argument* **basename**: The attachment basename (filename with extension but without full path)
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this resource.


## deprecate
Flag a resource as deprecated. Resources cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **resource**: payload of a previously fetched resource
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated resource.


## fetch
Fetches a distant resource and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema_id**: id of the schema
- *argument* **resource_id**: id of the resource
- *argument* **rev**: OPTIONAL fetches a specific revision of a resource (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the resource version that has a specific tag (default: None)
- *returned*: Payload of the whole resource as a dictionary


## fetch_attachment
DEPRECATED

Fetch the attachment of a a resource. Two ways are possible: by specifying an output filepath (out_filename),
then the distant file will be downloaded under this name. Or, if out_filename is not specified,
the binary buffer of the distant file is returned by this function.

If the distant file is large, it is advised to write it directly as a file because streaming is handled. Keeping
a large file into memory may not be a good idea.

- *argument* **resource**: payload of a previously fetched resource
- *argument* **name**: ID of the resource's attachment
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
Note that this cannot be given along tag
- *argument* **tag**: OPTIONAL tag of a resource. Note that this cannot be given along rev
- *argument* **out_filename**: OPTIONAL file path to which write the fetched file.
- *returned*: If out_filename is provided None is returned.
If out_filename is not provided, the binary buffer is returned as a byte_arr


## list
List the resources available for a given organization and project.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema**: OPTIONAL Lists only the resource for a given schema (default: None)
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated resource if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated resource.
- *argument* **full_text_search_query**: A string to look for as a full text query
- *returned*: The raw payload as a dictionary


## tag
Add a tag to a a specific revision of the resource. Note that a new revision (untagged) will be created

- *argument* **resource**: payload of a previously fetched resource
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided resource payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this resource.


## tags
List all the tags added to this resource, along with their version numbers

- *argument* **resource**: payload of a previously fetched resource
- *returned*: payload containing the list of tags and versions


## update
Update a resource. The resource object is most likely the returned value of a
nexus.resource.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete resource.

- *argument* **resource**: payload of a previously fetched resource, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated resource.


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


# schemas
## create
Create a new schema

- *argument* **org_label**: Label of the organization in which to create the schema
- *argument* **project_label**: label of the project in which to create a schema
- *argument* **schema_obj**: Schema, can be a dictionary or a JSON string
- *returned*: payload of the schema as a Python dictionary. This payload is partial and contains only Nexus metadata.
To get the full schema payload, use the fetch() method.


## deprecate
Flag a schema as deprecated. Schema cannot be deleted in Nexus, once one is deprecated, it is no longer
possible to update it.

- *argument* **schema**: payload of a previously fetched resource
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this deprecated schema.


## fetch
Fetches a distant schema and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the resource belongs to
- *argument* **project_label**: The label of the project that the resource belongs to
- *argument* **schema_id**: id of the schema
- *returned*: Payload of the whole schema as a dictionary


## list
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


## tag
Add a tag to a a specific revision of the schema. Note that a new revision (untagged) will be created

- *argument* **schema**: payload of a previously fetched schema
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided schema payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this schema.


## update
Update a schema. The schema object is most likely the returned value of a
nexus.schema.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete resource.

- *argument* **schema**: payload of a previously fetched resource, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the schema argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated schema.


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


# tools
## pretty_print
(no documentation provided)


# utils
# views
## aggregate_es
Creates an aggregated view for ElasticSearch.

- *argument* **org_label**: Label of the organization the view wil belong to
- *argument* **project_label**: label of the project the view will belong too
- *argument* **esviews**: list of ElasticSearch view payloads, most likely got with .fetch()
- *argument* **id**: id to give to this aggregation id ElasticSearch views
- *returned*: A payload containing only the Nexus metadata for this aggregated view.


## create_es
Creates an ElasticSearch view

- *argument* **org_label**: Label of the organization the view wil belong to
- *argument* **project_label**: label of the project the view will belong too
- *argument* **view_data**: Mapping data required for ElasticSearch indexing
- *returned*: The payload representing the view. This payload only contains the Nexus metadata


## deprecate_es
Update a ElasticSearch view. The esview object is most likely the returned value of a
nexus.views.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete view.

- *argument* **esview**: payload of a previously fetched view, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the view argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated view.


## fetch
Fetches a distant view and returns the payload as a dictionary.
In case of error, an exception is thrown.

- *argument* **org_label**: The label of the organization that the view belongs to
- *argument* **project_label**: The label of the project that the view belongs to
- *argument* **view_id**: id of the view
- *argument* **rev**: OPTIONAL fetches a specific revision of a view (default: None, fetches the last)
- *argument* **tag**: OPTIONAL fetches the view version that has a specific tag (default: None)
- *returned*: Payload of the whole view as a dictionary


## list
List the views available for a given organization and project. All views, of all kinds.

- *argument* **org_label**: The label of the organization that the view belongs to
- *argument* **project_label**: The label of the project that the view belongs to
- *argument* **pagination_from**: OPTIONAL The pagination index to start from (default: 0)
- *argument* **pagination_size**: OPTIONAL The maximum number of elements to returns at once (default: 20)
- *argument* **deprecated**: OPTIONAL Get only deprecated view if True and get only non-deprecated results if False.
If not specified (default), return both deprecated and not deprecated view.
- *argument* **full_text_search_query**: A string to look for as a full text query
- *returned*: The raw payload as a dictionary


## list_keep_only_es
Helper function to keep only the ElasticSearch views metadata from the result of a .list() call
- *argument* **viewlist**: the payload returned by .list()
- *returned*: the list of ElasticSearch view metadata (beware: not complete payloads like if it was the result of .fetch() calls)


## list_keep_only_sparql
Helper function to keep only the SparQL views metadata from the result of a .list() call
- *argument* **viewlist**: the payload returned by .list()
- *returned*: the list of SparQL view metadata (beware: not complete payloads like if it was the result of .fetch() calls)


## query_es
Perform a ElasticSearch query

- *argument* **esview**: Payload of an ElasticSearch view, most likely got with the .fetch() function
- *argument* **query**: ElasticSearch query as a JSON string or a dictionary
- *returned*: the result of the query as a dictionary


## query_sparql
Perform a SparQL query.

- *argument* **org_label**: Label of the oragnization to perform the query on
- *argument* **project_label**: Label of the project to perform the query on
- *argument* **query**: Query as a string
- *returned*: result of the query as a dictionary


## tag_es
Add a tag to a a specific revision of an ElasticSearch view. Note that a new revision (untagged) will be created

- *argument* **esview**: payload of a previously fetched view (ElasticSearch)
- *argument* **tag_value**: The value (or name) of a tag
- *argument* **rev_to_tag**: OPTIONAL Number of the revision to tag. If not provided, this will take the revision number
from the provided resource payload.
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the resource argument will be used.
- *returned*: A payload containing only the Nexus metadata for this view.


## update_es
Update a ElasticSearch view. The esview object is most likely the returned value of a
nexus.views.fetch(), where some fields where modified, added or removed.
Note that the returned payload only contains the Nexus metadata and not the
complete view.

- *argument* **esview**: payload of a previously fetched view, with the modification to be updated
- *argument* **rev**: OPTIONAL The previous revision you want to update from.
If not provided, the rev from the view argument will be used.
- *returned*: A payload containing only the Nexus metadata for this updated view.


## quote_plus
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.


