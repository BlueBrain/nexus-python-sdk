import random
import string

from nexussdk.client import NexusClient

_ENV_ = "https://dev.nexus.ocp.bbp.epfl.ch/v1"
_TOKEN_ = None


def random_string(length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def new_client():
    return NexusClient(_ENV_, _TOKEN_)
