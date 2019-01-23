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

# WORKS
# Listing schemas
# payload = nexus.schemas.list('bbp', 'example')
# nexus.tools.pretty_print(payload)


# WORKS
# Create a schema (NO id provided)
# my_schema = """{
#   "shapes": [
#     {
#       "@id": "this:MyShape",
#       "@type": "sh:NodeShape",
#       "nodeKind": "sh:BlankNodeOrIRI",
#       "targetClass": "ex:Custom",
#       "property": [
#         {
#           "path": "ex:name",
#           "datatype": "xsd:string",
#           "minCount": 1
#         },
#         {
#           "path": "ex:number",
#           "datatype": "xsd:integer",
#           "minCount": 1
#         },
#         {
#           "path": "ex:bool",
#           "datatype": "xsd:boolean",
#           "minCount": 1
#         }
#       ]
#     }
#   ]
# }"""
# payload = nexus.schemas.create('bbp', 'example', my_schema)
# nexus.tools.pretty_print(payload)


# Create a schema (id provided)
my_schema = """{
  "shapes": [
    {
      "@id": "this:MyShape",
      "@type": "sh:NodeShape",
      "nodeKind": "sh:BlankNodeOrIRI",
      "targetClass": "ex:Custom",
      "property": [
        {
          "path": "ex:name",
          "datatype": "xsd:string",
          "minCount": 1
        },
        {
          "path": "ex:number",
          "datatype": "xsd:integer",
          "minCount": 1
        },
        {
          "path": "ex:bool",
          "datatype": "xsd:boolean",
          "minCount": 1
        }
      ]
    }
  ]
}"""
payload = nexus.schemas.create('bbp', 'example', my_schema, schema_id="the_id2")
nexus.tools.pretty_print(payload)


# WORKS
# Fetching a schema
# payload = nexus.schemas.fetch('bbp', 'example', "http://example.com/981c24c9-25b3-411a-a0b8-93a08da523df", rev=4)
# nexus.tools.pretty_print(payload)


# WORKS
# Updating a schema
# payload["shapes"][0]["property"][0]["minCount"] = 10
# payload = nexus.schemas.update(payload)
# nexus.tools.pretty_print(payload)

# Deprecate a schema
# payload = nexus.schemas.deprecate(payload)
# nexus.tools.pretty_print(payload)


# Tag a schema
# payload = nexus.schemas.tag(payload, "big_tag", 4)
# nexus.tools.pretty_print(payload)
