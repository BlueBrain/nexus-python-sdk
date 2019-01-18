import nexussdk as nexus


# STAGING
# token = open('token.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('https://bbp-nexus.epfl.ch/staging/v1')

# DEV with Github token
token = open('token-gh.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')


# listing organizations
# NOT WORKING due to API
payload = nexus.organization.list(pagination_size=100)
nexus.tools.pretty_print(payload)

# getting a specific organization
# WORKS
# payload = nexus.organization.fetch("jojorg")
# nexus.tools.pretty_print(payload)


# Updating values of an organization
# WORKS
# payload["description"] = "an updated description v2"
# payload = nexus.organization.update(payload)
# nexus.tools.pretty_print(payload)


# payload = nexus.organization.fetch("jojorg")
# nexus.tools.pretty_print(payload)

# Create an Organization
# WORKS
# payload = nexus.organization.create("jojorg", name="The Jojo Organization", description="The description of the Jojo Organization")
# nexus.tools.pretty_print(payload)

# Deprecate an Organization
# WORKS
# payload = nexus.organization.deprecate("somefancyorg6", 1)
# nexus.tools.pretty_print(payload)
