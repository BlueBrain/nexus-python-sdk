import nexussdk as nexus

# # STAGING
# token = open('token.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('https://bbp-nexus.epfl.ch/staging/v1')

# # DEV with Github token
token = open('token-gh.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')


# listing projects
# payload = nexus.projects.list()
# nexus.tools.pretty_print(payload)

# getting a specific organization
# WORKS
# payload = nexus.projects.fetch("jojorg", "first_project")
# nexus.tools.pretty_print(payload)


# Updating values of an organization
# WORKS
# payload["apiMappings"] = ["not", "sure", "what", "to", "put", "there"]
# payload = nexus.projects.update(payload)
# nexus.tools.pretty_print(payload)

# Create an Project
# WORKS
data = {
    "name": "The First Project",
    "description": "The description of the first project"
}
payload = nexus.projects.create("my_org", "first_project")
nexus.tools.pretty_print(payload)


# Deprecate an project
# WORKS
# payload = nexus.projects.deprecate(payload)
# nexus.tools.pretty_print(payload)
