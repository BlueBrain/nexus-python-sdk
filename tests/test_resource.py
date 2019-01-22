import nexussdk as nexus


prod = "https://bbp.epfl.ch/nexus/v1/"
staging = 'https://bbp-nexus.epfl.ch/staging/v1'

# token = open('token.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment(staging)

# DEV with Github token
token = open('token-gh.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')

# DEV with Github token
# token = open('token-gh.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('http://dev.nexus.ocp.bbp.epfl.ch/v1')


# # # WORKS but the API does not list everything
# payload = nexus.resources.list('my_org', 'first_project')
# nexus.tools.pretty_print(payload)
#
# exit()

# # WORKS but the API does not list everything
# payload = nexus.resources.list('my_org', 'first_project', schema="resource")
# nexus.tools.pretty_print(payload)


# WORKS
# payload = None

# payload = nexus.resources.fetch('my_org', 'first_project', 'resource', "13744e26-92a7-45fa-b9c5-7e5e4dd80110")
# nexus.tools.pretty_print(payload)
# #
# #
# print('===========================================================')
#
# exit()

# Create a resource (NOT providing an ID)
# data = {
#     "firstname": "Johnny2",
#     "lastname": "Bravo2"
# }
# payload = nexus.resources.create('my_org', 'first_project', data)
# # payload = nexus.resources.create('bbp', 'example', data)
# nexus.tools.pretty_print(payload)


# Create a resource (providing an ID)
# data = {
#     "firstname": "Johnny1",
#     "lastname": "Bravo1"
# }
# payload = nexus.resources.create('my_org', 'first_project', data )
# # payload = nexus.resources.create('jojorg', 'second_project', data, id="the-fancy-id-i-absolutely-need")
# nexus.tools.pretty_print(payload)


# WORKS
# payload["birthdate"] = "Some day, a long time ago"
# payload["alignment"] = "chaotic good"
# response = nexus.resources.update(payload)
# nexus.tools.pretty_print(response)
#
# exit()

# payload = nexus.resources.deprecate(payload)
# nexus.tools.pretty_print(payload)


# Attach a file to an existing resource
# f = "./an_attachment.txt"
# f = "./an_attachment_image.jpg"
# payload = nexus.resources.add_attachement(payload, f)
# nexus.tools.pretty_print(payload)


# Delete an attachment from a resource
# payload = nexus.resources.delete_attachment(payload, "an_attachment.txt")
# nexus.tools.pretty_print(payload)


# Fetch en attachment
#payload = nexus.resources.fetch_attachment(payload, "an_attachment.txt", out_filename="an_attachment_OUT.txt")
# payload = nexus.resources.fetch_attachment(payload, "an_attachment_image.jpg", out_filename="an_attachment_image_OUT.jpg")
# print(payload)


# Works
# Tag a resource
# payload = nexus.resources.fetch('my_org', 'first_project', 'resource', "http://dev.nexus.ocp.bbp.epfl.ch/v1/resources/my_org/first_project/_/13744e26-92a7-45fa-b9c5-7e5e4dd80110")
# payload = nexus.resources.tag(payload, "some_tag")
# nexus.tools.pretty_print(payload)

# Get all the tags for a resource
payload = nexus.resources.fetch('my_org', 'first_project', 'resource', "13744e26-92a7-45fa-b9c5-7e5e4dd80110")
payload = nexus.resources.tags(payload)
nexus.tools.pretty_print(payload)
