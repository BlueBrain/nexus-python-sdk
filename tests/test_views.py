import nexussdk as nexus


prod = "https://bbp.epfl.ch/nexus/v1/"
staging = 'https://bbp-nexus.epfl.ch/staging/v1'

token = open('token.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment(staging)

# DEV with Github token
# token = open('token-gh.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')

# DEV with Github token
# token = open('token-gh.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')


# WORKS
# Fetch a view
# payload = nexus.views.fetch("bbp", "example", "http://example.comthe_id_of_this")
# payload = nexus.views.fetch("bbp", "example", "http://example.comthe_id_of_this", tag="some_tag")
# nexus.tools.pretty_print(payload)

# WORKS
# Create a ES view
# view_data = """
# {
#   "mapping": {
#     "dynamic": false,
#     "properties": {
#       "@id": {
#         "type": "keyword"
#       },
#       "@type": {
#         "type": "keyword"
#       },
#       "firstname": {
#         "type": "keyword"
#       },
#       "lastname": {
#         "type": "keyword"
#       }
#     }
#   },
#   "includeMetadata": false,
#   "sourceAsText": false,
#   "resourceSchemas": "nxs:myschema"
# }
# """
# payload = nexus.views.create_es("bbp", "example", view_data, id="name_view")
# nexus.tools.pretty_print(payload)


# WORKS
# List the views (all kinds)
# payload = nexus.views.list("bbp", "example")
# nexus.tools.pretty_print(payload)

# Listing but keeping only the ElasticSearch view from the list
# list_of_es_views = nexus.views.list_keep_only_es( nexus.views.list("bbp", "example") )
# nexus.tools.pretty_print(list_of_es_views)

# WORKS
# Update a view
# payload["mapping"]["dynamic"] = True
# payload = nexus.views.update_es(payload)
# nexus.tools.pretty_print(payload)

# WORKS
# Deprecate a view
# payload = nexus.views.deprecate_es(payload)
# nexus.tools.pretty_print(payload)


# Tag a view
# payload = nexus.views.tag_es(payload, "some_tag")
# nexus.tools.pretty_print(payload)



# # Aggregate some views
# # 1- make a list of their ids
# view_ids_to_aggregate = [
#     "http://example.comthe_id_of_this",
#     "nxv:myview1"
# ]
# # 2- gotta fetch'em all!
# views_to_aggregate = []
# for id in view_ids_to_aggregate:
#     views_to_aggregate.append( nexus.views.fetch("bbp", "example", id) )
#
# # 3- make the call to Aggregate them
# payload = nexus.views.aggregate_es("bbp", "example", views_to_aggregate, id="some_fancy_aggregation")
# nexus.tools.pretty_print(payload)


# # # Perform a ES query
# query = """
# {
#   "query": {
#     "term": {
#       "firstname": "Johnny6"
#     }
#   }
# }
# """
# payload_view = nexus.views.fetch("bbp", "example", "name_view")
# payload = nexus.views.query_es(payload_view, query)
# nexus.tools.pretty_print(payload)


# SparQL query
query = "SELECT ?s where {?s ?p ?o} LIMIT 2"
payload = nexus.views.query_sparql("bbp", "example", query)
nexus.tools.pretty_print(payload)
