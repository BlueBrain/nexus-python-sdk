import nexussdk as nexus

# STAGING
token = open('token.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment('https://bbp-nexus.epfl.ch/staging/v1')

# # DEV with Github token
# token = open('token-gh.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')


# listing projects
payload = nexus.project.list("bbp")
nexus.tools.pretty_print(payload)

# getting a specific organization
# WORKS
# payload = nexus.project.fetch("jojo", "second_project")
# nexus.tools.pretty_print(payload)


# Updating values of an organization
# WORKS
# payload["apiMappings"] = ["not", "sure", "what", "to", "put", "there"]
# payload = nexus.project.update(payload)
# nexus.tools.pretty_print(payload)

# Create an Project
# WORKS
# data = {
#     "name": "The Second Project",
#     "description": "The description of the second project"
# }
# payload = nexus.project.create("jojo", "second_project")
# nexus.tools.pretty_print(payload)


# Deprecate an Organization
# WORKS
# payload = nexus.project.deprecate("jojo", "second_project", 4)
# nexus.tools.pretty_print(payload)
