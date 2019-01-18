import nexussdk as nexus


prod = "https://bbp.epfl.ch/nexus/v1"
staging = 'https://bbp-nexus.epfl.ch/staging/v1'

token = open('token.txt', 'r').read().strip()
nexus.config.set_token(token)
nexus.config.set_environment(staging)


payload = nexus.project.list()
nexus.tools.pretty_print(payload)

proj = "https://bbp.epfl.ch/nexus/v1/projects/test/proj2"
exit()

data = {
    "firstname": "Johnny",
    "lastname": "Bravo"
}
payload = nexus.resource.create('test', 'proj1', data)
nexus.tools.pretty_print(payload)



exit()

# WORKS
payload = None
try:
    payload = nexus.resource.fetch('bbp', 'example', 'resource', "http://example.com/2db592a9-3852-4304-9578-634b65ae29bd")
    #nexus.tools.pretty_print(payload)
except nexus.HTTPError as e:
    print(e.response.text)


# data = {
#     "firstname": "Johnny",
#     "lastname": "Bravo"
# }
# payload = nexus.resource.create('jojo', 'first_project', data)
# # payload = nexus.resource.create('bbp', 'example', data)
# nexus.tools.pretty_print(payload)

# # WORKS
# payload["birthdate"] = "Some day, a long time ago"
# response = nexus.resource.update(payload)
# nexus.tools.pretty_print(response)


# payload = nexus.resource.deprecate(payload)
# nexus.tools.pretty_print(payload)


# Attach a file to an existing resource
f = "./an_attachment.txt"
#f = "./an_attachment_image.jpg"
payload = nexus.resource.add_attachement(payload, f)
nexus.tools.pretty_print(payload)
