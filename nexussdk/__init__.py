# Settings
from . import config

# Main entry points
from . import organization
from . import project
from . import resource

# Views
#from . import elasticsearchview
#from . import sparqlview


from . utils import tools

# Expose this error so that a user of the nexus sdk can refer to it as nexussdk.HTTPError
# and does not have to figure out from what lib it comes from
from requests.exceptions import HTTPError