import nexussdk as nexus

prod = "https://bbp.epfl.ch/nexus/v1/"
staging = 'https://bbp-nexus.epfl.ch/staging/v1'
dev = 'http://dev.nexus.ocp.bbp.epfl.ch/v1'

# token = open('token.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment(staging)

# DEV with Github token
token = open('token-gh.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment(dev)

# payload = nexus.files.list("my_org", "first_project")
# nexus.tools.pretty_print(payload)

# WORKS
# Uploading a file (providing an ID)
# payload = nexus.files.create("my_org", "first_project", "./an_attachment.txt", "some_file_id")
# nexus.tools.pretty_print(payload)

# WORKS
# Uploading a file (NOT providing an ID)
# payload = nexus.files.create("my_org", "first_project", "./an_attachment_image.jpg")
# nexus.tools.pretty_print(payload)

# WORKS
# Fetch a file
# payload = nexus.files.fetch("my_org", "first_project", "a8074a47-19f6-405e-83bc-f9b203b9dc91", out_filepath="./out/", tag="THE_TAG")
# nexus.tools.pretty_print(payload)

# Tag a file
# payload = nexus.files.fetch("my_org", "first_project", "a8074a47-19f6-405e-83bc-f9b203b9dc91")
# payload = nexus.files.tag(payload, tag_value="THE_TAG")
# nexus.tools.pretty_print(payload)

# Update a file
# # payload = nexus.files.fetch("my_org", "first_project", "a8074a47-19f6-405e-83bc-f9b203b9dc91")
# payload = nexus.files.update(payload, filepath="./other_image.png")
# nexus.tools.pretty_print(payload)


# Get the tags of a given file
payload = nexus.files.fetch("my_org", "first_project", "a8074a47-19f6-405e-83bc-f9b203b9dc91")
payload = nexus.files.tags(payload)
nexus.tools.pretty_print(payload)
