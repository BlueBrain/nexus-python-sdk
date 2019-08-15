from nexussdk import client

# Expose this error so that a user of the nexus sdk can refer to it as nexussdk.HTTPError
# and does not have to figure out from what lib it comes from
from requests.exceptions import HTTPError
