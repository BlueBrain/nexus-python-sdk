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


# # # WORKS but the API does not list everything
payload = nexus.resources.list('bbp', 'example', schema=None)
nexus.tools.pretty_print(payload)
#
# exit()

# # WORKS but the API does not list everything
# payload = nexus.resources.list('bbp', 'example', schema="resource")
# nexus.tools.pretty_print(payload)


# WORKS
# payload = None
# try:
#     payload = nexus.resources.fetch('bbp', 'example', 'resource', "http://example.com/77cba9c7-437d-42dc-8721-55f0cb491345")
#     # nexus.tools.pretty_print(payload)
# except nexus.HTTPError as e:
#     print(e.response.text)
# #
# #
# print('===========================================================')
#
# exit()

# Create a resource (NOT providing an ID)
# data = {
#     "firstname": "Johnny6",
#     "lastname": "Bravo6"
# }
# payload = nexus.resources.create('jojo', 'first_project', data)
# payload = nexus.resources.create('bbp', 'example', data)
# nexus.tools.pretty_print(payload)


# Create a resource (providing an ID)
# data = {
#     "firstname": "Johnny7",
#     "lastname": "Bravo7"
# }
# # payload = nexus.resources.create('jojo', 'first_project', data, )
# payload = nexus.resources.create('bbp', 'example', data, id="00000000-1111-2222-3333-444444444444")
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
# payload = nexus.resources.tag(payload, "some_tag", 4)
