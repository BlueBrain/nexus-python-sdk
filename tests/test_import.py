import nexussdk as nexus

# STAGING
# token = open('token.txt', 'r').read().strip()
# nexus.config.set_token(token)
# nexus.config.set_environment('https://bbp-nexus.epfl.ch/staging/v1')

nexus.tools.pretty_print({"foo":"bar"})
